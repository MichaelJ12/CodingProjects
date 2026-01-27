
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)
    
class BinarySearchTree:
    def __init__(self):
        self.root = None


    def insert(self, new_value):
        if self.root is None:
            self.root = TreeNode(new_value)
            return
        self.root = self.insert_recursive(self.root, new_value)

    def search(self, current_node, value):

        if current_node is None:
            return False
        
        if value == current_node.val:
            return current_node
        
        if value < current_node.val:
            return self.search(current_node.left, value)   
           
        else:
            return self.search(current_node.right, value)   
            
    def delete(self, current_node, value):
        if current_node is None:
            return current_node
        
        if value < current_node.val:
            current_node.left = self.delete(current_node.left, value)   
           
        elif value > current_node.val:
            current_node.right = self.delete(current_node.right, value)
        
        else:
            if current_node.left is None and current_node.right is None:
                return None

            elif current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left

            else:
                min_node = self.find_min(current_node.right)

                current_node.val = min_node.val

                current_node.right = self.delete(current_node.right, min_node.val)

        return current_node  

    
    def find_min(self, node):
        if node.left is not None:
            return self.find_min(node.left)
        return node
        

        

    def insert_recursive(self, node, new_value):
            if node is None: 
                return TreeNode(new_value)
            
            if new_value < node.val:
                    node.left = self.insert_recursive(node.left, new_value)
                    return node
            else:
                node.right = self.insert_recursive(node.right, new_value)
                return node
            
    
    def in_order(self, node):
        if node is None:
            return  
        
        self.in_order(node.left)
       
        print(node.val)
        
        self.in_order(node.right)

    def print_in_order(self):
        self.in_order(self.root)
    
if __name__ == '__main__':
    #create a new BinarySearchTree isntance 
    tree = BinarySearchTree()

    values = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    for v in values:
        tree.insert(v)

    print(tree.search(tree.root, 11))

# newt step is implementing a search in the tree than deletion adn than we are done!



