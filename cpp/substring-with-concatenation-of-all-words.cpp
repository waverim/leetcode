#include <iostream>
#include <unordered_map>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        vector<int> result;
        unordered_map<string, int> map;
        int strLength = s.size();
        int wordListLength = words.size();
        int wordLength = words[0].size();
        
        for (string str : words) {
            map[str]++;
        }

        for (int i = 0; i < strLength - wordListLength * wordLength + 1; ++i) {
            unordered_map<string, int> freq;
            int j = 0;
            for (; j < wordListLength; j++) {
                string temp = s.substr(i + j * wordLength, wordLength);
                if (map.find(temp) != map.end()) {
                    freq[temp]++;
                    if (freq[temp] > map[temp]) {
                        break;
                    }
                } else {
                    break;
                }
            }
            if (j == wordListLength) {
                result.push_back(i);
            }
        }

        return result;
    }
};

int main () {
    /*string str = "barfoojjjjjfoobarkkkkk";
    vector<string> words = {"foo", "bar"};
    */
    string str = "wordgoodgoodgoodbestword";
    vector<string> words = {"word","good","best","good"};
    
    Solution s;
    for (int i : s.findSubstring(str, words)) {
        cout << i << " ";
    }
    cout << endl;

    return 0;
}
