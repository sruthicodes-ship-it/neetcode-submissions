# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        q = deque([root])
        while q:
            node = q.popleft()
            if not node:
                res.append('N')
            else:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        buildTree = data.split(",")
        if buildTree[0] == 'N':
            return None
        root = TreeNode(int(buildTree[0]))
        q = deque([root])
        index = 1
        while q and index < len(buildTree):
            node = q.popleft()
            if buildTree[index] != 'N':
                node.left = TreeNode(int(buildTree[index]))
                q.append(node.left)
            index += 1
            if index < len(buildTree) and buildTree[index] != 'N':
                node.right = TreeNode(int(buildTree[index]))
                q.append(node.right)
            index += 1
        
        return root
