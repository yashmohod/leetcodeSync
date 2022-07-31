class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] sol = new int[2];
        for(int x =0; x < nums.length; x++){
            for(int y = x+1; y<nums.length;y++){
                if(nums[x]+nums[y] == target){
                    sol[0]=x;
                    sol[1]=y;
                    return sol;
                }
            }
        }
        return sol;
    }
}
