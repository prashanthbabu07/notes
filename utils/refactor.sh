replace_field() {
    local file="$1"
    local field="$2"
    local param="$3"
    # remove last character if it's a semicolon in param
    param="${param%;}"
    # Escape special regex characters in field
    local esc_field
    esc_field=$(printf '%s\n' "$field" | sed 's/[][\.*^$(){}?+|/]/\\&/g')
    echo "Replacing '${esc_field}.' with '${param}.' in $file"
    # Only replace _fieldName. (optionally with spaces before dot) with paramName.
    # Do NOT replace if _fieldName is followed by a semicolon or anything other than a dot
    # This will NOT match _fieldName; or _fieldName = etc.
    perl -pi -e "s/(${esc_field})\s*\./${param}./g" "$file"
}

export -f replace_field

find . -type f -name "*.cs" | while read -r file; do
    awk '
    BEGIN { prev=""; }
    {
        if (prev != "") {
            if ($0 ~ /^[ \t]*[a-zA-Z0-9_]+;/) {
                split(prev, a, /[ \t=]+/);
                field=a[length(a)-1];
                param=$1;
                print field ":" param;
            }
            prev="";
        }
        if ($0 ~ /^ *private readonly .* = *$/) {
            prev=$0;
        }
        if ($0 ~ /^ *private readonly .* = [a-zA-Z0-9_]+;/) {
            split($0, a, /[ \t=;]+/);
            field=a[length(a)-2];
            param=a[length(a)-1];
            print field ":" param;
        }
    }
    ' "$file" | while IFS=: read -r field param; do
        if [[ -n "$field" && -n "$param" ]]; then
            echo "File: $file, Field: $field, Param: $param"
            replace_field "$file" "$field" "$param"
        fi
    done
done

echo "Done. All usages replaced, fields not deleted."
