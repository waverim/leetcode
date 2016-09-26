#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    string fractionToDecimal(int numerator, int denominator) {
        string result;
        unordered_map<int, int> map;

        if (numerator == 0) {
            return "0";
        }

        if ((numerator ^ denominator) < 0) {
            result += "-";
        }

        long long int n = llabs(numerator), d = llabs(denominator);

        result += to_string(n / d);
        if (n % d == 0) {
            return result;
        }
        result += ".";

        long long int r = n % d;

        while (true) {
            if (map.count(r) > 0) {
                if (r == 0) {
                    result.pop_back();
                } else {
                    result.insert(map[r], 1, '(');
                    result += ")";
                }
                break;
            }

            map[r] = result.size();
            r *= 10;
            result += to_string(r / d);
            r %= d;
        }

        return result;
    }
};

int main () {
    Solution s;
    cout << s.fractionToDecimal(1, 7) << endl;
    cout << s.fractionToDecimal(1, 2) << endl;
    cout << s.fractionToDecimal(2, 1) << endl;
    cout << s.fractionToDecimal(2, 3) << endl;
    cout << s.fractionToDecimal(4, 9) << endl;
    cout << s.fractionToDecimal(4, 333) << endl;
    cout << s.fractionToDecimal(1, 6) << endl;
    cout << s.fractionToDecimal(-2147483648, -1) << endl;
    //cout << s.fractionToDecimal() << endl;
    return 0;
}
