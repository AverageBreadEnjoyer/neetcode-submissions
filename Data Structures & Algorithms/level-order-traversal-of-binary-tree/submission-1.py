# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        result = []

        if root:
            queue.append(root)

        level = 0

        while len(queue) > 0:
            inner = []

            for node in range(len(queue)):
                curr = queue.pop(0)
                #print(f"popped: {curr.val}")

                # Process the node, adding it to a list
                inner.append(curr.val)

                if curr.left:
                    #print(f"added: {curr.left.val}")
                    queue.append(curr.left)

                if curr.right:
                    #print(f"added: {curr.right.val}")
                    queue.append(curr.right)
            
            result.append(inner)
            level += 1
        
        return result
                




            
        