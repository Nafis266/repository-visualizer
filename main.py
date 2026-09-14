from reposcan import scan_repository
from depend import extract_dependencies
from astcreator import extract_c_functions, extract_py_functions, extract_py_classes
import sys
from graph import create_graph
import json

repo = sys.argv[1]
repo_files = scan_repository(repo)

paths = [file["path"] for file in repo_files]

alldeps = {}
all_data = []

for file in paths:
    deps = extract_dependencies(file,paths)
    alldeps[file] = deps
    functions = [] 
    classes = []

    if file.endswith(".c"):
        functions = extract_c_functions(file)
    elif file.endswith(".py"):
        functions = extract_py_functions(file)
        classes = extract_py_classes(file)
    else:
        functions = []

    f_data = {
        "path": file,
        "dependencies": deps,
        "functions": functions,
        "classes": classes
    }

    all_data.append(f_data)

output = {
    "repository": repo,
    "files": all_data
}

with open("repo_data.json","w") as f:
    json.dump(output,f)

create_graph(alldeps)
