from tree_sitter import Language,Parser
import sys
import tree_sitter_c

fname = sys.argv[1]

with open(fname) as f:
    code = f.read()

C_LANGUAGE = Language(tree_sitter_c.language())
parser = Parser(C_LANGUAGE)

tree = parser.parse(bytes(code,"utf8"))

root = tree.root_node

def get_text(node):
    return code[node.start_byte:node.end_byte]

def walk(node):
    if node.type == "function_definition":
        declarator = node.child_by_field_name("declarator")
        name = None

        if declarator:
            name_node = declarator.child_by_field_name("declarator")
            if name_node:
                name = get_text(name_node)
    
        print("function: ",name)
        print()
    
    for child in node.children:
        walk(child)

walk(root)


