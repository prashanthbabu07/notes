import glob
import os
import re


def process_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    output = []
    i = 0
    while i < len(lines):
        line = lines[i]
        output.append(line)
        if line.strip() == "[TestMethod]":
            if i + 1 < len(lines):
                method_line = lines[i + 1]
                match = re.match(
                    r"(\s*public\s+async\s+Task\s+)(\w+)\((.*)", method_line
                )
                if match:
                    prefix, method_name, rest = match.groups()
                    new_method_name = (
                        method_name.split("_", 1)[-1]
                        if "_" in method_name
                        else method_name
                    )
                    new_line = f"{prefix}{new_method_name}({rest}\n"
                    output.append(new_line)
                    i += 1  # Skip the original method line
        i += 1

    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(output)


def process_pattern(pattern):
    for filename in glob.glob(pattern):
        if os.path.isfile(filename):
            process_file(filename)
            print(f"Processed {filename}")


# Usage example:
# In your shell: python3 rename_test_methods.py "*Query*Tests.cs"
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python3 rename_test_methods.py '<pattern>'")
    else:
        process_pattern(sys.argv[1])
