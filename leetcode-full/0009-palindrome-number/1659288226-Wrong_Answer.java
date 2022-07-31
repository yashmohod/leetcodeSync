class Solution {
    public boolean isPalindrome(int x) {
        if(x<0){
            return false;
        }
        String num = String.valueOf(x);
        int count = String.valueOf(x).length();
        if(count ==1){
            return true;
        }
        if(x%2 == 0){
            int test=0;
            int ct=0;
            while(ct<(count/2)){
                if(num.charAt(ct) == (num.charAt(count-ct-1))){
                    test++;
                }
                ct++;
            }
            if(test == count/2){
                return true;
            }else{
                return false;
            }
        }
        else{
            int test=0;
            int ct=0;
            while(ct<(count/2)){
                if(num.charAt(ct) == (num.charAt(count-ct-1))){
                    test++;
                }
                ct++;
            }
            if(test == (count/2)-1){
                return true;
            }else{
                return false;
            }
            
        }
        
    }
}
