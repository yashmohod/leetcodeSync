/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {boolean}
 */
var leafSimilar = function(root1, root2) {
    var ends = function(root){
        if(root == null){
            return []
        }
        if(root.left == null && root.right ==null){
            return [root.val]
        }
        var comb = []
        var la = ends(root.left)
        var ra = ends(root.right)
        var rt = la.concat(ra)
        return rt
    }

    var r1 = ends(root1)
    var r2 = ends(root2)

    if (r1.length != r2.length){
        return false
    }else{
        for(var x =0; x< r1.length ;x++){
            if (r1[x] != r2[x]){
                return false
            }
        }
        return true
    }


};
