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
var goodNodes = function(root) {
    
    var dive = function(next,greatest){
        let rCount = 0
        let lCount = 0
        if(next.left!= null) {
            lCount = dive(next.left, (greatest>next.val?greatest:next.val))
        }
        if(next.right!= null) {
            rCount = dive(next.right, (greatest>next.val?greatest:next.val))
        }
        return (greatest>next.val? rCount+lCount:rCount+lCount+1 )
    }
    return dive(root, Number.NEGATIVE_INFINITY)
    
};
