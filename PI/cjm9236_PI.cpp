// PI problem
// Author: JeongminCha (cjm9236@me.com)

#include <iostream>
#include <string>
#include <climits>
#include <cmath>
#include <cstring>

using namespace std;

int memo[10001];

// Returns True if all elements are same.
bool is_all_same(string str) {
    char ch = str.at(0);
    for(int index = 0; index < str.size(); index++) {
        if (ch != str.at(index)) {
        	return false;
        }
    }
    return true;
}

// Returns True if the input sequence is
// monotonically decreasing or increasing by 1
bool is_monotonic_by_one(string str) {
    int diff = str.at(1) - str.at(0);
    if (diff != 1 && diff != -1) {
        return false;
    }
    for(int index = 1; index < str.size(); index++) {
    	char prev = str.at(index-1);
    	char curr = str.at(index);
        if ((curr-prev) != diff) {
            return false;
        }
    }
    return true;
}

// Returns True if elements in input sequence are alternate.
bool is_alternate(string str) {
    for(int index = 2; index < str.size(); index++) {
        if (str.at(index) != str.at(index - 2)) {
            return false;
        }
    }
    return true;
}

// Returns True if the input sequence is an arithmetical progression.
bool is_ap(string str) {
	for (int index = 1; index < str.size()-1; index++) {
		char prev = str.at(index-1);
		char curr = str.at(index-0);
		char next = str.at(index+1);
		if ((next-curr) != (curr-prev)) {
			return false;
		}
	}
	return true;
}

int calc_cost(string target) {
    if (is_all_same(target)) {
    	return 1;
    } else if (is_monotonic_by_one(target)) {
    	return 2;	
    } else if (is_alternate(target)) {
    	return 4;
    } else if (is_ap(target)) {
    	return 5;
    } else {
    	return 10;
    }
}

int find_optimal_cost(string str) {
    int length = str.size();

    for(int unit = 3; unit <= 5; unit++) {
        memo[unit] = calc_cost(str.substr(0, unit));
    }

    for(int idx = 3; idx < length; idx += 3) {
        for(int unit = 3; unit <= 5; unit++) {
            int next_idx = idx + unit;
            if (next_idx > length) {
            	break;
            }
            for(int next_unit = 3; next_unit <= 5; next_unit++) {
            	int rest = next_idx - next_unit;
                if (rest >= 3) {
                    int cost = memo[rest] + calc_cost(str.substr(rest, next_unit));
                    if (memo[next_idx] == 0) {
                        memo[next_idx] = cost;
                    } else {
                        memo[next_idx] = min(cost, memo[next_idx]);
                    }
                }
            }
        }
    }
    return memo[length];
}

int main()
{
    int t;

    cin >> t;
    while(t--) {
        string input;
        cin >> input;
        cout << find_optimal_cost(input) << endl;
        memset(memo, 0, sizeof(memo));
    }

    return 0;
}