// 344. Reverse String



#include<iostream>
#include<string>
using namespace std;

void reverseString(string &s) {
        int n = s.size();
        int st = 0;
        int end = n-1;
        while(st < end){
            swap(s[st++] , s[end--]);
        }
    }



int main(){
    string s = "Hello World";
    reverseString(s);
    cout << s << endl;
}