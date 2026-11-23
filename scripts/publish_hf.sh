#!/usr/bin/env bash
set -euo pipefail

# One-command publisher for Hugging Face Dataset + Static Space.
# Requires HF_TOKEN or prior `hf auth login` / `huggingface-cli login`.

DATASET_REPO="${1:-stevevaius/KC_Meclis_Tutanak}"
SPACE_REPO="${2:-stevevaius/KC-Meclis-Tutanak-Arama}"

echo "==> 1/4 Building dataset & SQLite FTS5..."
python3 src/build_dataset.py

echo "==> 2/4 Optimizing Parquet for DuckDB-WASM & rebuilding static indices..."
python3 src/optimize_for_wasm.py
python3 src/analyze_topics.py

echo "==> 3/4 Uploading Parquet dataset -> https://huggingface.co/datasets/${DATASET_REPO}"
python3 src/upload_hf.py --repo-id "${DATASET_REPO}"

echo "==> 4/4 Deploying Static Space -> https://huggingface.co/spaces/${SPACE_REPO}"
python3 src/deploy_space.py --repo-id "${SPACE_REPO}" --with-indices --force

echo "Done!"
echo "  Dataset: https://huggingface.co/datasets/${DATASET_REPO}"
echo "  Space:   https://huggingface.co/spaces/${SPACE_REPO}"
