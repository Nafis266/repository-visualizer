#!/bin/bash

repo="$1"

python main.py $repo
dot -Tpng repo_graph.dot -o repo_graph.png

chafa repo_graph.png
