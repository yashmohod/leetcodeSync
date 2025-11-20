class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> newArray = {};

        for(int x = 0; x < nums.size()*2;x++){
            newArray.push_back(nums[x%nums.size()]);
        }

        return newArray;
    }
};
