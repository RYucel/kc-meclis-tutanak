"""Upload the generated Republic of Cyprus parliamentary Parquet dataset to Hugging Face Hub."""

from __future__ import annotations

import argparse
from pathlib import Path
from huggingface_hub import HfApi


def main() -> None:
    ap = argparse.ArgumentParser(description="Upload KC Meclis Tutanak dataset to Hugging Face Hub.")
    ap.add_argument("--repo-id", required=True, help="Target HF dataset repo, e.g. 'stevevaius/KC_Meclis_Tutanak'")
    ap.add_argument("--private", action="store_true")
    args = ap.parse_args()

    api = HfApi()
    user = api.whoami()
    print(f"Authenticated on Hugging Face as: {user.get('name') or user.get('fullname')}")

    hf_dir = Path("data/hf_dataset")
    if not (hf_dir / "data/speeches.parquet").exists():
        raise SystemExit("Run `python src/build_dataset.py` and `python src/optimize_for_wasm.py` first.")

    api.create_repo(repo_id=args.repo_id, repo_type="dataset", private=args.private, exist_ok=True)
    api.upload_folder(
        folder_path=str(hf_dir),
        repo_id=args.repo_id,
        repo_type="dataset",
        commit_message="Upload Republic of Cyprus House of Representatives Turkish-translated speaker-indexed dataset",
    )
    print(f"Uploaded dataset: https://huggingface.co/datasets/{args.repo_id}")


if __name__ == "__main__":
    main()
