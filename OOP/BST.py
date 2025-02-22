# # 5. Write a Python program to create a class representing a binary search tree. Include methods for inserting and searching for elements in the binary tree.


class Node: 
    def __init__(self,key):
        self.key = key 
        self.left = None
        self.right = None


class BST(Node): 
    def __init__(self):
        super().__init__(self)
        self.root = None
    
# Insert
    def insert(self,current):
        new_Node = Node(current)
        if self.root is None:
            self.root = current
        else:
            self.insertSearch(new_Node,current)

    def insertSearch(self,new_Node,key):
        while True:
            if key < self.root : 
                if new_Node.left is None : 
                    new_Node.left = key
                    print("Left Node Added !!!")
                else : 
                    self.root = new_Node.left
                    new_Node = Node(key)
                    self.insertSearch(new_Node,key)

            elif key > self.root :
                if new_Node.right is None : 
                    new_Node.right = key
                    print("Right Node Added !!!")
                else : 
                    self.root = new_Node.right
                    new_Node = Node(key);
                    self.insertSearch(new_Node,key)
            break

            
# Search 
    def search(self):
        pass


obj = BST()

obj.insert(12)
obj.insert(8)
