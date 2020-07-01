"""
// Time Complexity : O(n)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No

// Your code here along with comments explaining your approach
Algorithm Explanation
Given below
"""
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
        """
        Idea is to do level order traversal such that we are capturing the nodes and appending to serialized string
        
        """
        if not root:
            return ""
        q = deque([root])
        # final_str = ["["]
        final_str = []
        final_str2 = ""
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr:
                    final_str.append(str(curr.val))
                    #final_str2+=str(curr.val)
                else:
                    #final_str2+=None
                    final_str.append("null")
                #final_str.append(",")
                if curr:
                    q.append(curr.left)
                    q.append(curr.right)
        
        #final_str = final_str[:-1]
        #final_str.append("]")
        #print(final_str)
        ser_str = ",".join(final_str)
        
        return ("[" + ser_str + "]")
        #return ",".join(final_str)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        
        Idea is to do use queue to keep track of the nodes being added based on the iterator moved along the serialized string
        
        
        """
        #edge case
        if data == "":
            return None
        
        data = data[1:-1]
        strs = data.split(",")
        print(strs)
        #get the root as the first element from the string
        root = TreeNode(int(strs[0]))
        #add the root to the queue
        q = deque([root])
        i = 1
        #iterate from next position until end of string and while q is not empty
        while q and i < len(strs):
            curr = q.popleft()
            if strs[i] != 'null':
                #update the left of the current root
                curr.left = TreeNode(int(strs[i]))
                q.append(curr.left)
            i+=1 #move one ptr ahead
            if strs[i] != 'null':
                #update the right of the current root
                curr.right = TreeNode(int(strs[i]))
                q.append(curr.right)
            i+=1 #move one ptr ahead
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))