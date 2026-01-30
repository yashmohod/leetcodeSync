class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int largest = 0;
        for(int cur : candies){
            largest = (cur>largest)?cur:largest;
        }
        vector<bool> res(candies.size());
        for(int i=0; i < candies.size();i++){
           res[i] = ( candies[i]+extraCandies >= largest) ;
        }
        return res;
    }
};
