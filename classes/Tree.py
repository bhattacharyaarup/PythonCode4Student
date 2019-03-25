#Binary Tree

class Tree:
	
	def __init__(self):
		self.n=0
		self.left=None
		self.right=None
	def push(self,root,data):
		temp=Tree()
		temp.n=data
		
		if(root==None):
			root=temp
		else:
			ref=root
			prev=None
			while(ref!=None):
				prev=ref
				if(data>ref.n):
					ref=ref.right
				else:
					ref=ref.left
			if(data>prev.n):
				prev.right=temp
			else:
				prev.left=temp

		return root
	def inorder(self,root):
		if(root==None):
			return
		else:
			self.inorder(root.left)
			print("%d" %root.n)
			self.inorder(root.right)
			
obj=Tree()
root=Tree()
root=None
root=obj.push(root,10)
root=obj.push(root,5)
root=obj.push(root,20)
root=obj.push(root,15)
root=obj.push(root,2)
root=obj.push(root,7)
obj.inorder(root)