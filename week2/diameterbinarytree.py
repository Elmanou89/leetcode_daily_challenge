def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_path = 0
        def longest_path(root):
            global max_path
            lg_path_left = 0
            lg_path_right = 0
            if root.left is not None:
                lg_path_left += 1 + longest_path(root.left)
            if root.right is not None:
                lg_path_right += 1 + longest_path(root.right)
            if lg_path_left + lg_path_right > self.max_path:
                self.max_path = lg_path_left + lg_path_right
            return max(lg_path_left , lg_path_right)
        
        if root is None:
            return 0
        longest_path(root)
        return self.max_path
