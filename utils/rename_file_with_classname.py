import os
import re
import subprocess

for filename in os.listdir("."):
    if filename.endswith(".cs") and os.path.isfile(filename):
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                match = re.match(
                    # r"^\s*(public|internal|private|protected)?\s*(partial\s+)?interface\s+([A-Za-z0-9_]+)",
                    r"^\s*(public|internal|private|protected)?\s*(partial\s+)?(class|interface)\s+([A-Za-z0-9_]+)",
                    line,
                )
                if match:
                    class_name = match.group(3)
                    break
            else:
                class_name = None

        print(f"{filename} : {class_name}")
        if class_name:
            ext = filename.split(".")[-1]
            new_file = f"{class_name}.{ext}"
            if filename != new_file and not os.path.exists(new_file):
                print(f"Renaming: {filename} -> {new_file}")
                subprocess.run(["git", "mv", filename, new_file])
