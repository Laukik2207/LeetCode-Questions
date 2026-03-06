// 28. Find the Index of the First Occurrence in a String

#include<iostream>
#include<string>
using namespace std;


int index(string haystack, string needle){
    int idx = haystack.find(needle);
        return idx;
}

int main(){
    string haystack = "sadbutsad";
    string needle = "sad";
    int idx = index(haystack, needle);
    cout << idx << endl;
}