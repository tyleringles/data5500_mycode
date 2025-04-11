class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def search(root, value):
    if root is None:
        return False
    if root.value == value:
        return True
    elif value < root.value:
        return search(root.left, value)
    else:
        return search(root.right, value)


#I used sports cause I like them
root = TreeNode("Soccer")
root.left = TreeNode("Baseball")
root.right = TreeNode("Basketball")
root.left.left = TreeNode("Tennis")
root.left.right = TreeNode("Golf")
root.right.left = TreeNode("Football")
root.right.right = TreeNode("Rugby")

# Searchs for sports values:
print(search(root, "Football"))  
print(search(root, "Hockey"))    
