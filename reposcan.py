import os

S_EXTENSIONS = (
    ".py",
    ".java",
    ".cpp",
    ".c",
    ".h",
)

def scan_repository(repo_path):
    files = []

    for root, dirs, filenames in os.walk(repo_path):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for filename in filenames:
            if filename.endswith(S_EXTENSIONS):
                file_path = os.path.join(root, filename)

                files.append({
                    "name": filename,
                    "path": file_path
                })
    return files

