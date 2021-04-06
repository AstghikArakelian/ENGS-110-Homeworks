#include <iostream>
#include <cmath>

int main()
{
       	float a = 0;
	float b = 0;
	float c = 0;
	float D = 0;
	float x = 0;
	float x2 = 0;
	
	
	std::cout << "Enter the value of parameter a, for ax^2+bx+c=0  equation" << std::endl;
	std::cin >> a;
	if (std::cin.fail()) 
	{
		std::cout << "The enteredis not valid. Please enter a number" << std::endl;
		return EXIT_FAILURE;
	}
	std::cout << "Enter the value of parameter b, for ax^2+bx+c=0 equation" << std::endl;
	std::cin >> b;
	if (std::cin.fail()) 
	{
		std::cout << "The entered is not valid. Please enter a number" << std::endl;
		return EXIT_FAILURE;
	}
	std::cout << "Enter the value of parameter c, for ax^2+bx+c=0 equation" << std::endl;
	std::cin >> c;
	if (std::cin.fail()) 
	{
		std::cout << "The enteredis not valid. Please enter a number" << std::endl;
		return EXIT_FAILURE;
	}
	D = b*b - 4*a*c;
	if (D < 0)
	{
		std::cout << "The dicriminant is equall to " << D << " which is negative, hence there is no x for which " << a << "x^2+" << b << "x+" << c << "=0" <<  std::endl;
	}
	else if (D == 0)
	{ 
		x = (-b) / (2*a);
	std::cout << "The dicriminant is " << D << " so there is one solution x=" << x << std::endl;
	}
	else 
	{
		x = (-b + (sqrt(D))) / (2*a);
		x2 = (-b - (sqrt(D))) / (2*a);
		std::cout << "The dicriminant is " << D << " so there is two solutions x=" << x << " and x=" << x2 << std::endl;
	}


}
