
//Question no 121. Best Time to Buy and Sell Stock

#include<iostream>
using namespace std;

void maxprofit(int *prices,int n){
    int bestbuy[10000];
    bestbuy[0] = INT16_MAX;
    for(int i=1;i<n;i++){
        bestbuy[i] = min(bestbuy[i-1],prices[i-1]);
    }

    int maxprofit = 0;
    for(int i = 0;i<n;i++){
        int currProfit = prices[i] - bestbuy[i];
        maxprofit = max(maxprofit,currProfit);
    }
    cout<<"max Profit = "<<maxprofit<<endl;

}


int main(){
    int prices[6] = {7,1,5,3,10,4};
    maxprofit(prices,6);
}