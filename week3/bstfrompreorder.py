def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        def build_local_tree(values):
            if not values:
                return None
            val = values.pop(0)
            tree = TreeNode(val)
            lower_values = [x for x in values if x < val]
            higher_values = [x for x in values if x > val]
            tree.left = build_local_tree(lower_values)
            tree.right = build_local_tree(higher_values)
            return tree
            
        return build_local_tree(preorder)
