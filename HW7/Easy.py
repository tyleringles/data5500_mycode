class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val  
        self.left = left  
        self.right = right  

def insert_into_bst(root, val):
    if root == None:
        return TreeNode(val)
    
    if val < root.val:
        
        if root.left == None:
            root.left = TreeNode(val)  
        else:
           
            insert_into_bst(root.left, val)  
    else:
        
        if root.right == None:
            root.right = TreeNode(val)  
        else:
            
            insert_into_bst(root.right, val)  
    
    return root 

