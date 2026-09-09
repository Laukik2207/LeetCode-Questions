class Solution {
public:
    long long countCommas(long long n) {
        if(n < 1000){
            return 0;
        }
        int dg = 0;
        long long t = n;
        while(t>0){
            t/=10;
            dg++;
        }
        int m = 0;
        if(dg>=4 && dg<=6){
            m = 1;
        }else if(dg>=7 && dg <=9){
            m = 2;
        }else if(dg >= 10 && dg <= 12){
            m = 3;
        }else if(dg >= 13 && dg <= 15){
            m = 4;
        }
        else{
            m = 5;
        }

        long long st = 1000;
        long long ans = 0;
        int c = 1;

        while(c<=m){
            long long end = (st * 1000)-1;

            if(end > n){
                end = n;
            }
            ans += (end-st+1) * c;
            st *= 1000;
            c++;
        }

        return ans;
    }
};