#include <iostream>

int fib(int age)
{
	int F0 = 0;
	int F1 = 0;
	int F2 = 1;
	int sum = 0;
	while (F2 < age)
	{
		F0 = F2;
		sum = F2 + sum;
		F2 = F1 + F2;
		F1 = F0;
	}
	return sum;
}

long decTobin(int n)
{
	int place = 1;
	int rm = 0;
	long binarynum = 0;
	while(n != 0)
	{
		rm = n%2;
		n = n/2;
		binarynum = binarynum + place*rm;
		place = place*10;
	}
	return binarynum;
}

int main()
{
	int age = 19;
	int n = fib(age);
	printf ("The sum of all Fibonacci numbers less than %d is %d\n", age, fib(age));
	printf ("The binary representation of %d is %d.\n", fib(age), decTobin(n));

	return EXIT_SUCCESS;
}



