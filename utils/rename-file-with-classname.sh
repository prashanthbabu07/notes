find . -type f -name "*.cs" | while read -r file; do
    class_name=$(grep -E '^[[:space:]]*(public|internal|private|protected)?[[:space:]]*(partial[[:space:]]+)?class[[:space:]]+[A-Za-z0-9_]+' "$file" | head -n 1 | sed -E 's/.*class[[:space:]]+([A-Za-z0-9_]+).*/\1/')
    echo "$file : $class_name"
    if [ -n "$class_name" ]; then
        dir=$(dirname "$file")
        ext="${file##*.}"
        new_file="$dir/$class_name.$ext"
        if [ "$file" != "$new_file" ] && [ ! -e "$new_file" ]; then
            echo "Renaming: $file -> $new_file"
            git mv "$file" "$new_file"
        fi
    fi
done
