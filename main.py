from reposcan import scan_repository
from depend import extract_dependencies
from astcreator import extract_functions

repo_files = scan_repository("./ex_repo")

paths = [file["path"] for file in repo_files]

for file in paths:
    deps = extract_dependencies(file,paths)
    print("\nFILE: ",file)
    print("depends on: ","NULL" if not deps else deps)

    functions = extract_functions(file)
    print("functions: ",functions if functions else "NULL")
