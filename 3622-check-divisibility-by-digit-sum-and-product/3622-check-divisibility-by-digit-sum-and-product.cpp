class Solution {
public:
    bool checkDivisibility(int n) {
        int og = n;
        int sum = 0;
        int mul = 1;
        while(n!=0){
            int t = n%10;
            sum += t;
            mul *= t;
            n /= 10;
        }
        int t = sum+mul;
        cout<<sum;
        cout<<mul;
        if(og%t == 0 ){
            return true;
        }else{
            return false;
        }
    }
};