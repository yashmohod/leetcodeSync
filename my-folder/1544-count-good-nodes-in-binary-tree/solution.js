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
        if(next==null){
            return 0
        }
        let count=0
        if(next.val >= greatest){
            count=1
            greatest = next.val
        }
        let lCount = dive(next.left, greatest)
        let rCount = dive(next.right, greatest)
        return lCount+rCount+count
    }
    return dive(root, Number.NEGATIVE_INFINITY)
    
};
