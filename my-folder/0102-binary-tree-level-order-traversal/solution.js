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
 * @return {number[][]}
 */
var levelOrder = function(root) {
    let nums = []

    function bfs(node,lev){

        if(nums[lev] == undefined){
            nums.push([node.val])
        }else{
            nums[lev].push(node.val)
        }
        if(node.left != null){
            bfs(node.left,lev+1)
        }
        if(node.right != null){
            bfs(node.right,lev+1)
        }
    }
    if(root == null){
        return []
    }
    bfs(root,0)
    return nums
};
