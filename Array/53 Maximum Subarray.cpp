//Kadane's Approach
#include <iostream>
using namespace std;

void maxsubarray(int *arr, int n){
    int maxsum = INT16_MIN;
    int curr_sum = 0;
    for(int i=0;i<n;i++){
        curr_sum += arr[i];
        maxsum = max(maxsum,curr_sum);
        if(curr_sum < 0){
            curr_sum = 0;
        }
    }
    cout<<"Max of subarray is: "<<maxsum<<endl;
}

int main(){
    int arr[5] = {1,2,3,4,5};
    maxsubarray(arr,5);

}