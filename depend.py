import re
import os

def extract_dependencies(file_path, all_files):

    dependencies = []

    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            code = f.read()

        for other_file in all_files:

            if other_file == file_path:
                continue

            filename = os.path.basename(other_file)
            module_name = os.path.splitext(filename)[0]

            if re.search(r"\b" + module_name + r"\b", code):
                dependencies.append(other_file)

    except Exception:
        pass

    return dependencies
