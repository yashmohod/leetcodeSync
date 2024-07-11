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
 * @return {number[]}
 */
var rightSideView = function(root) {
    if(root == null){
        return []
    }else{
        let left = rightSideView(root.left)
        let right = rightSideView(root.right)

        if(left.length> right.length){
            for(let x =0; x<right.length;x++){
                left[x] = right[x]
            }
            left.unshift(root.val)
            return left
        }else{
            right.unshift(root.val)
            return right
        }
    }
};
