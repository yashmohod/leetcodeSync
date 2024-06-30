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
var longestZigZag = function(root) {
    if(root ==null  ){
        return 0
    }

    function traverse(curNode,isLeft,depth){
        if(curNode==null){
            return depth
        }
        if(isLeft){
            var leftleft = traverse(curNode.left, true, 0);
            var leftright = traverse(curNode.right, false, depth+1);
            if(leftleft> leftright){
                return leftleft;
            }else{
                return leftright
            }
        }else{
            var rightright = traverse(curNode.right, false, 0);
            var rightleft = traverse(curNode.left, true, depth+1);
            if(rightright> rightleft){
                return rightright;
            }else{
                return rightleft
            }

        }
    }

    var left = traverse(root.left, true, 0);
    var right = traverse(root.right, false, 0);
    if(left > right ){
        return left;
    }else{
        return right;
    }
    
};
