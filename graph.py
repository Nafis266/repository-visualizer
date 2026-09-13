
def create_graph(deps):
    with open("repo_graph.dot","w") as f:
        f.write("digraph repo {\n")

        for file,dep in deps.items():
            for d in dep:
                f.write(f'  "{file}" -> "{d}";\n')

        f.write("}\n")
