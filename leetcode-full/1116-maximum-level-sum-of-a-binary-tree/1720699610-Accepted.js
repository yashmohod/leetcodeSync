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
var maxLevelSum = function(root) {
    let nums = []

    function bfs(node,lev){

        if(nums[lev] == undefined){
            nums.push(node.val)
        }else{
            nums[lev]+=node.val
        }
        if(node.left != null){
            bfs(node.left,lev+1)
        }
        if(node.right != null){
            bfs(node.right,lev+1)
        }
    }
    if(root == null){
        return 1
    }
    bfs(root,0)
    let lg = nums[0]
    let ind = 0
    for(let x =0; x<nums.length;x++ ){
        if(nums[x] > lg){
            ind = x
            lg = nums[x]
        }
    }
    return ind +1
};
