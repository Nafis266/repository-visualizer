from reposcan import scan_repository
from depend import extract_dependencies
from astcreator import extract_functions

repo_files = scan_repository("./ex_repo")

paths = [file["path"] for file in repo_files]

for file in paths:
    deps = extract_dependencies(file,paths)
    print("\nFILE: ",file)
    print("depends on: ",deps if deps else "NULL")

    functions = extract_functions(file)
    
    if not functions:
        print("functions: NULL")
    else:
        print("functions: ")
        for fn in functions:
            print(f"    function: {fn['function_name']}")
            print(f"    return type: {fn['return_type']}")
            print(f"    parameters: {fn['parameters']}\n")
