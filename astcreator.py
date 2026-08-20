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

def walk(node):
    print(node.type)
    for child in node.children:
        walk(child)

walk(root)


