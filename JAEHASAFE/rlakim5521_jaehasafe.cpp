// JAEHASAFE
// Jaekyoung Kim(rlakim5521@naver.com)

#include <iostream>
#include <vector>
#include <string>
using namespace std;

int turnLeft(const string before, const string after) {
	int ret = 0;
	string doubleBefore = before + before;
	int compareIndex = 0;
	int len = after.length();
	while (after.compare(doubleBefore.substr(compareIndex, len))) {
		compareIndex += 1;
		ret += 1;
	}
	return ret;
}

int turnRight(const string before, const string after) {
	int ret = 0;
	string doubleBefore = before + before;
	int compareIndex = after.length();
	int len = after.length();
	while (after.compare(doubleBefore.substr(compareIndex, len))) {
		compareIndex -= 1;
		ret += 1;
	}
	return ret;
}

int main()
{
	int C;
	cin >> C;
	for (int c = 0; c < C; c++) {
		int N;
		string str_dial;
		vector<string> vec_dials;
		cin >> N;
		for (int n = 0; n <= N; n++) {
			cin >> str_dial;
			vec_dials.push_back(str_dial);
		}

		int output = 0;
		for (int n = 1; n <= N; n++) {
			if (n % 2 == 1) {
				output += turnRight(vec_dials[n - 1], vec_dials[n]);
			}
			else {
				output += turnLeft(vec_dials[n - 1], vec_dials[n]);
			}
		}

		cout << output << endl;
	}
}
