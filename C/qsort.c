/*
 * =====================================================================================
 *
 *       Filename:  qsort.c
 *
 *    Description:  try qsort
 *
 *        Version:  1.0
 *        Created:  06/15/2012 03:09:05 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  FamiHug (), famihug@gmail.com
 *        Company:  FAMILUG
 *
 * =====================================================================================
 */

#include <stdio.h>
#include <stdlib.h>

int compare (const void* a, const void * b)
{
	return (*(int*)a - *(int*)b );
}

int main()
{
	int values[] = { 40 , 100, 20 , 2 , 13};
	int n;
	// Mang can sxep, so phan tu cua mang, size cua moi phan tu, ham so sanh
	qsort(values, sizeof(values) / sizeof(int), sizeof(int), compare);

	for (n = 0; n < 5; n++)
		printf("%d ", values[n]);
	return 0;

}

