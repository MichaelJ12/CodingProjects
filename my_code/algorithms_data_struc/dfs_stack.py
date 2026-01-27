graph: dict = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "E", "F"],
    "D": ["B"],
    "E": ["C"],
    "F": ["C"]
}
target: str = "F"



stack = ["A"]
visited = set()
parent = {}

while stack:
    current = stack.pop()
    

    if current == target:
        print("we Found it")
        break
    else:
        if current not in visited:
            visited.add(current)
            for child in reversed(graph[current]):
                if child not in visited:
                    stack.append(child)
                    parent[child] = current

                    
                    print(f"current node: {current}")
                    print(f"parent child: {parent}")
                    print("-" * 40)
         
path = []
current_node = target

while current_node:
    path.append(current_node)
    current_node = parent.get(current_node)
print(list(reversed(path)))