#include <iostream>
#include <cmath>
#include <cstdlib>

extern "C" float generator(float number);

using namespace std;

float randomFrom0to1() {
	return float(rand()) / float(RAND_MAX);
}

float randomFrom50to150() {
	return generator(randomFrom0to1());
}

int randomNumFrom1to4()
{
	float number = randomFrom0to1();
	if (number < 0.05)
	{
		return 1;
	}
	else if (number < 0.15 + 0.05)
	{
		return 2;
	}
	else if (number < 0.25 + 0.15 + 0.05)
	{
		return 3;
	}
	return 4;
}

int main() 
{
	int n = 100000;
	const int n_size = 10;
	int normalNumbers[n_size] = { 0 };

	for (int i = 0; i < n; i++)
	{
		float num = randomFrom50to150();
		num = (num - 50) / 10;

		int range = int(floor(num));
		if (range > n_size - 1)
		{
			range = n_size - 1;
		}
		normalNumbers[range] += 1;
	}


	for (int i = 0; i < n_size; i++)
	{
		cout << i + 1 << " " << normalNumbers[i] << endl;
	}

	const int inv_size = 4;
	int invNumbers[inv_size] = {0, 0, 0, 0};

	for (int i = 0; i < n; i++)
	{
		int num = randomNumFrom1to4();
		num -= 1;
		invNumbers[num]++;
	}

	cout << endl;
	for (int i = 0; i < inv_size; i++)
	{
		cout << i + 1 << " " << invNumbers[i] << endl;
	}
	return 0;
}