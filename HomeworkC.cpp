#include <iostream>

int main()
{
       	float a = 0;
	float b = 0;
	float x = 0;
	
	
	std::cout << "Enter the value of parameter a, for ax+b=0 equation" << std::endl;
	std::cin >> a;
	if (std::cin.fail()) 
	{
		std::cout << "The enteredis not valid. Please enter a number" << std::endl;
		return EXIT_FAILURE;
	}
	std::cout << "Enter the value of parameter b" << std::endl;
	std::cin >> b;
	if (std::cin.fail()) 
	{
		std::cout << "The entered is not valid. Please enter a number" << std::endl;
		return EXIT_FAILURE;
	}
	
	x = (-b)/a;
	std::cout << "For the equation " << a << "x+" << b << "=0  x=" << x <<std::endl;


}
