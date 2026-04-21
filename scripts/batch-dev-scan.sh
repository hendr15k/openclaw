#!/bin/bash
# GitHub Repo Development Script - Batch 1 (top-tier active repos)
set -e

WORKSPACE="/home/openclaw/.openclaw/workspace"
REPOS=(
  "bookish-waffle"
  "happyblue-elm327"
  "open-reader"
  "open-reader-v3"
  "spritpreise"
  "hendr15k.github.io"
  "sci-fi-app"
  "sci-fi-site"
  "sci-fi-empfehlungen"
  "sci-fi-reading-plans"
)

for repo in "${REPOS[@]}"; do
  dir="$WORKSPACE/$repo"
  [ ! -d "$dir/.git" ] && echo "SKIP $repo (no .git)" && continue
  echo "===== $repo ====="
  cd "$dir"
  
  # Check branch
  branch=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "none")
  echo "Branch: $branch"
  
  # Fetch latest
  git fetch origin 2>/dev/null && git pull --ff-only 2>/dev/null || echo "PULL: skipped/conflict"
  
  # Check for uncommitted changes
  status=$(git status --porcelain 2>/dev/null | wc -l)
  if [ "$status" -gt 0 ]; then
    echo "UNCLEAN: $status uncommitted files"
    git status --short | head -5
    continue
  fi
  
  echo "OK - clean"
  echo ""
done

echo "=== BATCH 1 SCAN COMPLETE ==="
