#!/bin/bash
set -e

for d in ~/.??*; do
  dir=$(basename "$d")

  # Skip if not a directory or already a symlink
  [[ -d "$d" && ! -L "$d" ]] || continue

  plain_name="${dir#.}"
  src="$d"
  dst="/Volumes/Sandisk/SupportFiles/dotfiles/$plain_name"

  echo "Moving $src to $dst and creating symlink"
  mkdir -p "$(dirname "$dst")"
  mv "$src" "$dst" && \
  ln -s "$dst" "$src"
done

