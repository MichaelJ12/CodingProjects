from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "E", "F"],
    "D": ["B"],
    "E": ["C"],
    "F": ["C"]
}


target = "F"
queue = deque(["A"])
visited = set()
parent = {}

while queue:
    current = queue.popleft()
   
    
    if current == target:
        print("we are done here")
        break
    else:
        if current not in visited:
            visited.add(current)
            for child in graph[current]:
                if child not in visited:
                    queue.append(child)
                    parent[child] = current


                    print(f"current node:{current}")
                    print(f"parent child: {parent}")
                    print("_" * 50)

path = []
current_node = target

while current_node:
    path.append(current_node)
    current_node = parent.get(current_node)
print(f"{list(reversed(path))}")

