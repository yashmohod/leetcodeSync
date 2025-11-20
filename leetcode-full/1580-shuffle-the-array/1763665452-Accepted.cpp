class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector<int> res = {};
        for(int x =0; x< n; x++){
            res.push_back(nums[x]);
            res.push_back(nums[x+n]);
        }
        return res;
    }
};
