#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    struct Node {
        char lc, rc;      // leftmost and rightmost char
        int pref, suff;   // longest prefix and suffix
        int best;         // longest repeating substring
        int len;          // segment length

        Node(char c=' ') {
            lc = rc = c;
            pref = suff = best = (c == ' ' ? 0 : 1);
            len = (c == ' ' ? 0 : 1);
        }
    };

    vector<Node> seg;
    string s;

    Node merge(Node a, Node b) {
        if (a.len == 0) return b;
        if (b.len == 0) return a;

        Node res;
        res.len = a.len + b.len;

        res.lc = a.lc;
        res.rc = b.rc;

        // prefix
        res.pref = a.pref;
        if (a.pref == a.len && a.rc == b.lc)
            res.pref = a.len + b.pref;

        // suffix
        res.suff = b.suff;
        if (b.suff == b.len && a.rc == b.lc)
            res.suff = b.len + a.suff;

        // best
        res.best = max(a.best, b.best);
        if (a.rc == b.lc)
            res.best = max(res.best, a.suff + b.pref);

        return res;
    }

    void build(int idx, int l, int r) {
        if (l == r) {
            seg[idx] = Node(s[l]);
            return;
        }

        int mid = (l + r) / 2;
        build(2*idx, l, mid);
        build(2*idx+1, mid+1, r);
        seg[idx] = merge(seg[2*idx], seg[2*idx+1]);
    }

    void update(int idx, int l, int r, int pos, char c) {
        if (l == r) {
            seg[idx] = Node(c);
            return;
        }

        int mid = (l + r) / 2;
        if (pos <= mid)
            update(2*idx, l, mid, pos, c);
        else
            update(2*idx+1, mid+1, r, pos, c);

        seg[idx] = merge(seg[2*idx], seg[2*idx+1]);
    }

    vector<int> longestRepeating(string s_, string queryCharacters, vector<int>& queryIndices) {
        s = s_;
        int n = s.size();
        seg.resize(4*n);

        build(1, 0, n-1);

        vector<int> ans;

        for (int i = 0; i < queryIndices.size(); i++) {
            int pos = queryIndices[i];
            char c = queryCharacters[i];

            update(1, 0, n-1, pos, c);
            ans.push_back(seg[1].best);
        }

        return ans;
    }
};