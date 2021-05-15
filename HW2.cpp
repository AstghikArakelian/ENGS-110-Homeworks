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
	fscanf(f, "%d", ps);
	while (fscanf(f, "%d", ps) != EOF)
	{
		sum = sum + *ps;
	}

	fclose(f);
	free(ps);

	f = fopen("result.txt", "w+");
	fprintf(f, "%d\n", sum);
	fclose(f);
	return EXIT_SUCCESS;
}


