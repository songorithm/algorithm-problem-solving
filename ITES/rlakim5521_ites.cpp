// ITES
// Jaekyoung Kim(rlakim5521@naver.com)

#include <iostream>
#include <queue>
using namespace std;

unsigned int getNextA(unsigned int preA)
{
	return preA * 214013 + 2531011;
}

unsigned int getSignal(unsigned int currentA)
{
	return (currentA % 10000) + 1;
}

int main()
{
	unsigned int C;
	cin >> C;
	for (unsigned int c = 0; c < C; c++) {
		// Input
		unsigned int K, N;
		cin >> K >> N;

		// Solve
		unsigned int count = 0;
		unsigned int sectionSum = 0;
		unsigned int currentA = 1983;
		unsigned int currentSignal = getSignal(currentA);
		queue<unsigned int> section;

		for (unsigned int n = 0; n < N; n++) {
			section.push(currentSignal);
			sectionSum += currentSignal;
			while (sectionSum > K) {
				sectionSum -= section.front();
				section.pop();
			}
			if (sectionSum == K) {
				count++;
			}
			currentA = getNextA(currentA);
			currentSignal = getSignal(currentA);
		}

		// Output
		cout << count << endl;
	}
}
