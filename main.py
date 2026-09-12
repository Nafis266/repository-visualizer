from reposcan import scan_repository
from depend import extract_dependencies
from astcreator import extract_c_functions, extract_py_functions

repo_files = scan_repository("./ex_repo")

paths = [file["path"] for file in repo_files]

for file in paths:
    deps = extract_dependencies(file,paths)
    print("\nFILE: ",file)
    print("depends on: ",deps if deps else "NULL")
    functions = [] 

    if file.endswith(".c"):
        functions = extract_c_functions(file)
    elif file.endswith(".py"):
        functions = extract_py_functions(file)
    else:
        functions = []
    
    if not functions:
        print("functions: NULL")
    else:
        print("functions: ")
        for fn in functions:
            name = fn['function_name']
            r_type = fn['return_type']
            p = fn['parameters']

            params = ", ".join(p)

            print(f"- {r_type if r_type is not None else ""} {name}({params})")


