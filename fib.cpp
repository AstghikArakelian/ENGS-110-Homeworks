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

void decTobin(int n)
{
	int binaryNum[16];
	int i = 0;
	while (n > 0) 
	{
		binaryNum[i] = n % 2;
		n = n / 2;
		i++;
	}
	while (i > 0)
	{
		i--;
		printf ("%d", binaryNum[i]);
	}
}

int main()
{
	int age = 19;
	int n = fib(age);
	printf ("The sum of all Fibonacci numbers less than %d is %d\n", age, fib(age));
	printf ("The binary representation of %d is ", fib(age));
       	decTobin(n);
	printf (".\n");
	return EXIT_SUCCESS;
}



