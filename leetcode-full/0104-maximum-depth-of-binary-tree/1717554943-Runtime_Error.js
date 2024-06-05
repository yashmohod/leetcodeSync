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
 * @return {number}
 */
var maxDepth = function(root) {
    
    var llen = 0
    var rlen = 0

    if (root.left != null){
        llen = maxDepth(root.left)
    }
    if (root.right != null){
        rlen = maxDepth(root.right)
    }
    if (root.right == null && root.left==null){
        return 1
    }

    if(rlen>llen){
        return rlen+1
    }else{
        return llen+1
    }


};
