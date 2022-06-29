#include <stdio.h>
#define ARRAY_SIZE(a)  sizeof(a)/sizeof(a[0])

int main()
{
	int tablica[] = {1, 2, 3, 4, 5, 6, 7 ,8, 9, 10};
	int i, max;
	const int N = ARRAY_SIZE(tablica);
	max = tablica[0];
	
	// funkcja
	for(i = 1; i < N; i++)
	{
		if(tablica[i] > max)
		{
			max = tablica[i];
		}	
	}
	printf("Najwieksza wartosc z tablicy %d", max);
	return 0;
}
