from tree_sitter import Language,Parser
import sys
import tree_sitter_c

def extract_functions(fname):

    with open(fname) as f:
        code = f.read()

    C_LANGUAGE = Language(tree_sitter_c.language())
    parser = Parser(C_LANGUAGE)

    tree = parser.parse(bytes(code,"utf8"))

    root = tree.root_node

    def get_text(node):
        return code[node.start_byte:node.end_byte]

    functions = []

    def walk(node):
        if node.type == "function_definition":
            declarator = node.child_by_field_name("declarator")
            return_type = get_text(node.child_by_field_name("type"))

            name = None
            parameters = []

            if declarator:
                name_node = declarator.child_by_field_name("declarator")
                params_node = declarator.child_by_field_name("parameters")

                if name_node:
                    name = get_text(name_node)

                if params_node:
                    for param in params_node.named_children:
                        parameters.append(get_text(param))
        
            functions.append({
                "function_name": name,
                "return_type": return_type,
                "parameters": parameters
            })
        
        for child in node.children:
            walk(child)

    walk(root)

    return functions


