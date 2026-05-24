# read files in the current directory and add the region to the using statements that are at the top of the file.
# We need to add #region and #end region with the name Usings to the using statements. This will help us to collapse the using statements.

import os


def add_region_to_usings(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Quick check: If the region already exists, skip to avoid duplicates
    file_content = "".join(lines)
    if "#region Usings" in file_content:
        return

    using_indices = []

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Track every line that starts with 'using '
        if stripped.startswith("using "):
            using_indices.append(i)
        # Allow blank lines or comments to exist between usings without breaking
        elif len(using_indices) > 0 and (stripped == "" or stripped.startswith("//")):
            continue
        # If we hit actual code (like a namespace or class) after finding usings, we can stop
        elif len(using_indices) > 0:
            break

    if using_indices:
        start_index = using_indices[0]
        # End index is the last detected 'using' statement
        end_index = using_indices[-1]

        # Insert from bottom to top so the indices don't shift unpredictably
        lines.insert(end_index + 1, "#endregion\n")
        lines.insert(start_index, "#region Usings\n")

        with open(file_path, "w", encoding="utf-8") as file:
            file.writelines(lines)
        print(file_path, "[UPDATED]")


if __name__ == "__main__":
    # Process only .cs files in the current directory
    for filename in os.listdir("."):
        if filename.endswith(".cs"):
            add_region_to_usings(filename)
