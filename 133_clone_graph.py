class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
        
class Solution(object):
    def __init__(self):
        self.my_dict = {}
        
    def cloneGraph(self, node):
        new_node = Node(node.val, node.neighbors[:]) # [:] needed for deep copy of list.      
        self.my_dict[node] = new_node #node passed into my dictionary is now equal to new node
        for idx, nxt in enumerate(new_node.neighbors):
            if nxt in self.my_dict:
                new_node.neighbors[idx] = self.my_dict[nxt]
            else:
                new_node.neighbors[idx] = self.cloneGraph(nxt)
        return new_node
    

# Or we can...
    def CloneGraph_2(self, node):
        if not node:
            return None 
        
        visited = {}
        def cloneGraph_(node):
            if node in visited:
                return visited[node]
            
            new_node = Node(node.val, [])
            visited[node] = new_node
            for neigh in node.neighbors:
                new_node.neighbors.append(cloneGraph_(neigh))
            return new_node
        return cloneGraph_(node)
    
    

    