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
 * @param {number} val
 * @return {TreeNode}
 */
var searchBST = function(root, val) {
    let kue = []

    function traverse(node){
        if(node != null){
            kue.push(node)
            traverse(node.left)
            traverse(node.right)
        }
    }
    traverse(root)
    for(let x = 0; x< kue.length;x++){
        if(kue[x].val == val){
            return kue[x] 
        }
    }
    return null
};
