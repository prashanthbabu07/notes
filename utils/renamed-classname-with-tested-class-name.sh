find . -type f -name "*.cs" | while read -r file; do
    tested_class=$(grep -E 'private [^;=]+(Command|Query|Service)[[:space:]]+[A-Za-z0-9_]+[[:space:]]*=' "$file" | sed -E 's/.*private[[:space:]]+([A-Za-z0-9_]+(Command|Query|Service))[[:space:]]+[A-Za-z0-9_]+[[:space:]]*=.*/\1/' | head -n 1)
    if [ -n "$tested_class" ]; then
        sed -i '' -E "s/(public( sealed)? class )[A-Za-z0-9_]+Tests/\1${tested_class}Tests/" "$file"
        echo "Updated test class name in $file to ${tested_class}Tests"
    fi
done
