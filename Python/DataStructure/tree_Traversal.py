class Node:
  def __init__(self,info):
    self.info=info
    self.left=self.right=None
  def __str__(self):
    return str(self.info)

re=[]
class searchtree:
  def __init__(self):
    self.root=None
  def create(self,val):
    if self.root==None:
      self.root=Node(val)
    else:
      current=self.root
      while 1:
        if val < current.info:
          if current.left:
            current=current.left
          else:
            current.left=Node(val)
            break
        elif val>current.info:
           if current.right:
             current=current.right
           else:
             current.right=Node(val)
             break
        else:
         break
  def peek(stack):
    if len(stack)>0:
      return stack[-1]
    return None

  def in_order_non(self,node):
    current = node
    stack = [] 
  
     
    while True:
         
        if current is not None:
             
            stack.append(current)
         
            current = current.left
 
         
        elif(stack):
            current = stack.pop()
            print(current.info)
         
            current = current.right
 
        else:
            break
      
  def post_order_non(self,node):
    current=node
    hold=[]
    while True:
       while node:
         if node.right is not None:
           hold.append(node.right)
         hold.append(node)
         current=current.left
       current=hold.pop()
       if current.right is not None and peek(stack) ==current.right:
         hold.pop()
         hold.append(current)
         current=current.right
       else:
         re.append(current.info)
         current=None
       if len(stack)<=0:
         break
  def preorderIterative(self,root):
 
    if (root == None):
        return
 
    st = []
 
    
    curr = root
 
    
    while (len(st) or curr != None):
     
        
        while (curr != None):
         
            print(curr.info)
 
            if (curr.right != None):
                st.append(curr.right)
 
            curr = curr.left
         
       
        if (len(st) > 0):
            curr = st[-1]
            st.pop()
  def postorderIterative(self,root):
 
    if root is None:
        return
 
    stack = []
    stack.append(root)
 
    out = []
 
    while stack:
 
        curr = stack.pop()
        out.append(curr.info)
 
        # push the left and right child of the popped node into the stack
        if curr.left:
            stack.append(curr.left)
 
        if curr.right:
            stack.append(curr.right)
 
    # print postorder traversal
    while out:
        print(out.pop())
        
  

              

      

    

        
    
        
        

  def pre_order(self,node):
    if node is not None:
      print(node.info)
      self.pre_order(node.left)
      self.pre_order(node.right)
  def post_order(self,node):
    if node is not None:
      self.post_order(node.left)
      self.post_order(node.right)
      print(node.info)

  def inorder(self,node):
    if node is not None:
      self.inorder(node.left)
      print(node.info)
      self.inorder(node.right)

tree=searchtree()
arr=[8,3,1,6,4,7,10,14,13]
for i in arr:
  tree.create(i)
print("indoor traversel")
tree.inorder(tree.root)

print("Pre_order traversel")
tree.pre_order(tree.root)

print("Post_order traversel")
tree.post_order(tree.root)

print("Non_in_order traversel")
tree.in_order_non(tree.root)
print("post_non_order traversel")
tree.postorderIterative(tree.root)
print("pre_non_order traversel")
tree.preorderIterative(tree.root)
