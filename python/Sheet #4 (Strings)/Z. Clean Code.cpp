#https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/Z


#include <bits/stdc++.h>
using namespace std;

int main() {
    string line;
    bool inBlock = false;

    while (getline(cin, line)) {
        string result = "";
        for (int i = 0; i < line.size(); i++) {

            // If currently inside block comment
            if (inBlock) {
                if (i + 1 < line.size() && line[i] == '*' && line[i + 1] == '/') {
                    inBlock = false;
                    i++; // skip '/'
                }
            }
            else {
                // Start of block comment
                if (i + 1 < line.size() && line[i] == '/' && line[i + 1] == '*') {
                    inBlock = true;
                    i++; // skip '*'
                }
                // Single line comment
                else if (i + 1 < line.size() && line[i] == '/' && line[i + 1] == '/') {
                    break; // ignore rest of line
                }
                else {
                    result += line[i];
                }
            }
        }

        // Remove lines that are empty or only spaces
        bool isEmpty = true;
        for (char c : result) {
            if (!isspace(c)) {
                isEmpty = false;
                break;
            }
        }

        if (!isEmpty) {
            cout << result << endl;
        }
    }

    return 0;
}