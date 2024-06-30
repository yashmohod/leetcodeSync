/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} targetSum
 * @return {number}
 */
var pathSum = function(root, targetSum) {
    if (!root) {
        return 0;
    }
    
    let ans = 0;

    function traverse(node, sum) {
        if (!node) {
            return;
        }

        if (node.val === sum) {
            ans++;
        }
        
        sum -= node.val
        
        traverse(node.left, sum);
        traverse(node.right, sum);
    }
    
    traverse(root, targetSum);
    
    ans += pathSum(root.left, targetSum);
    ans += pathSum(root.right, targetSum);
    
    return ans;
};
