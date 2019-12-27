# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        queue = deque([root])
        bfs_order = []
        while queue:
            node = queue.popleft()
            bfs_order.append(str(node.val) if node else "#")
            if node:
                queue.append(node.left)
                queue.append(node.right)
        return " ".join(bfs_order)
    
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        
        if not data:
            return None
        bfs_order = [TreeNode(int(node)) if node != "#" else None for node in data.split()]
        root = bfs_order[0]
        fast_index = 1
        slow_index = 0
        nodes = [root]
        while slow_index < len(nodes):
            node = nodes[slow_index]
            slow_index += 1
            node.left = bfs_order[fast_index]
            node.right = bfs_order[fast_index + 1]
            fast_index += 2
            
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        
        return root
            
            
        
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))