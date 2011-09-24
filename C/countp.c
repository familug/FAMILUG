//Count char by FamiHug 05.01.2011 14:13:09
//Ver 1.0 chi nhap chu cai IN HOA VD: ABEAVDFSDEF
//Ver 2.0 Completed! 09.01.2011

#include <stdio.h>
#include <ctype.h>

int main()
{
	int i,temp;
	int cntr[26]={0};
	while((temp=getchar())!='\n')
	{
		if(isupper(temp))
			cntr[(temp-'A')]++;
		if(islower(temp))
			cntr[(temp-'a')]++;
	}
	for(i=0;i<26;i++)
		if(cntr[i]>0) printf("%c_%d\n",i+'A',cntr[i]);
	return 0;
}
