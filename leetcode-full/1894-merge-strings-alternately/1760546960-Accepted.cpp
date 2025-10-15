class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string result ="";
        bool first = true;
        int l = 0;
        int r = 0;
        for(int x=0 ; x<word1.length()+word2.length();x++){

            if(first){
                if(l<word1.length()){
                    result = result +word1[l];
                    l++;
                }else{
                    result = result +word2[r];
                    r++;
                }
                first= false;
            }else{
                if(r<word2.length()){
                    result = result +word2[r];
                    r++;
                }else{
                    result = result +word1[l];
                    l++;
                }
                first= true;
            }
        }
        return result;
    }
};
