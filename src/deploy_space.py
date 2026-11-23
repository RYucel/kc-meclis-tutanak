"""Deploy the Republic of Cyprus parliamentary search Static Space to Hugging Face Spaces."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from huggingface_hub import HfApi, hf_hub_download

INDEX_FILES = ("speakers_index.json", "terms_index.json", "topics_index.json", "speaker_topics.json")


def _stats(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8")).get("stats", {})


def local_is_stale(local: dict, live: dict) -> str | None:
    for key in ("latest_date", "synced_at"):
        if (local.get(key) or "") < (live.get(key) or ""):
            return f"local {key}={local.get(key)} is older than live {key}={live.get(key)}"
    if local.get("speeches", 0) < live.get("speeches", 0):
        return f"local index covers {local.get('speeches')} speeches, live covers {live.get('speeches')}"
    return None


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-id", required=True, help="Target HF Static Space, e.g. 'stevevaius/KC-Meclis-Tutanak-Arama'")
    ap.add_argument("--private", action="store_true")
    ap.add_argument("--with-indices", action="store_true")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    api = HfApi()
    space_dir = Path("space_static")
    assert (space_dir / "index.html").exists()

    api.create_repo(repo_id=args.repo_id, repo_type="space", space_sdk="static", private=args.private, exist_ok=True)
    patterns = ["index.html", "README.md"]
    if (space_dir / "mp_bios.json").exists():
        patterns.append("mp_bios.json")
    if args.with_indices:
        for fn in INDEX_FILES:
            assert (space_dir / fn).exists(), f"missing {space_dir / fn}"
        if not args.force:
            try:
                live = _stats(Path(hf_hub_download(args.repo_id, "speakers_index.json", repo_type="space", force_download=True)))
            except Exception:
                live = {}
            reason = local_is_stale(_stats(space_dir / "speakers_index.json"), live)
            if reason:
                raise SystemExit(f"Refusing to upload indices: {reason}. Pass --force to override.")
        patterns += list(INDEX_FILES)

    api.upload_folder(
        folder_path=str(space_dir),
        repo_id=args.repo_id,
        repo_type="space",
        allow_patterns=patterns,
        commit_message="Deploy serverless DuckDB-WASM Republic of Cyprus parliamentary search Static Space",
    )
    print(f"Space deployed: https://huggingface.co/spaces/{args.repo_id}")


if __name__ == "__main__":
    main()
