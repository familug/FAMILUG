/*by FamiHug 
 * Fri Sep 23 00:25:31 ICT 2011
 */

//This program demonstrates increment operator
#include <stdio.h>

int main(int argc, char **argv)
{
	int a = 3;
	int b = a++; //posfix a = 3, b = a => b = 3, then a++, a = 4
	int c = ++b; //prefix b = 3, ++b, b = 4, c = b => c = 4

	printf("a = %d b = %d c = %d\n",a,b,c);

	return 0;
}//end main()

