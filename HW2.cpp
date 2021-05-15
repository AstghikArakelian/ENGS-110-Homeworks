#include <stdio.h>
#include <stdlib.h>

int main()
{
	FILE* f = fopen("data.txt", "r");
	int *ps;
	int sum = 0;

	ps = (int *) malloc(20*sizeof(int));

	if(f == NULL)
	{
		printf("There has been an error!");
		exit(1);
	}

	while (fscanf(f, "%d", ps) != EOF)
	{
		sum = sum + *ps;
	}
	printf("%d\n", sum);

	fclose(f);
	free(ps);
	return EXIT_SUCCESS;
}


