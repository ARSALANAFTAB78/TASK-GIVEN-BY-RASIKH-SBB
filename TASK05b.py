class Node:
    """
    Represents a node in the binary tree.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_dfs(node, result):
    """
    Perform Inorder Traversal (Left, Root, Right).
    :param node: The current Node.
    :param result: List to store the traversal order.
    """
    if node:
        inorder_dfs(node.left, result) 
        result.append(node.value)       
        inorder_dfs(node.right, result) 

def preorder_dfs(node, result):
    """
    Perform Preorder Traversal (Root, Left, Right).
    :param node: The current Node.
    :param result: List to store the traversal order.
    """
    if node:
        result.append(node.value)  
        preorder_dfs(node.left, result) 
        preorder_dfs(node.right, result) 

def postorder_dfs(node, result):
    """
    Perform Postorder Traversal (Left, Right, Root).
    :param node: The current Node.
    :param result: List to store the traversal order.
    """
    if node:
        postorder_dfs(node.left, result) 
        postorder_dfs(node.right, result) 
        result.append(node.value)     

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    inorder_result = []
    preorder_result = []
    postorder_result = []

    inorder_dfs(root, inorder_result)
    preorder_dfs(root, preorder_result)
    postorder_dfs(root, postorder_result)

    print("Inorder Traversal:", inorder_result)    
    print("Preorder Traversal:", preorder_result)  
    print("Postorder Traversal:", postorder_result)