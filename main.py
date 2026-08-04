from reposcan import scan_repository
from depend import extract_dependencies

repo_files = scan_repository("./ex_repo")

paths = [file["path"] for file in repo_files]

for file in paths:
    deps = extract_dependencies(file,paths)
    print("\nFILE: ",file)
    print("depends on: ")
    for d in deps:
        print(d)
