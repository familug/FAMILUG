/* Chuong trinh su dung cin va cout de
 * Nhap vao mot day so nguyen
 * Sap xep day theo chieu tang dan
 */
#include <iostream>
using namespace std;

#define MAX 100

int main(void)
{
	int mang[MAX];
	int n;

	// Nhap du lieu cho mang
	cout<<"Nhap vao so phan tu cua mang:";
	cin>>n;

	if(n <= 0)
		return 1;

	cout<<"Nhap du lieu cho mang"<<endl;
	for(int i = 0; i < n; i++)
	{
		cout<<"Phan tu thu "<<i + 1<<":";
		cin>>mang[i];
	}

	cout<<"Mang vua nhap:";
	for(int i = 0; i < n; i++)
		cout<<mang[i]<<" ";
	cout<<endl;

	// Sap xep
	for(int i = 0; i < n; i++)
		for(int j = 0; j < i; j++)
		{
			int tmp;
			
			if(mang[i] < mang[j])
			{
				tmp = mang[i];
				mang[i] = mang[j];
				mang[j] = tmp;
			}
		}

	// Hien thi mang sau khi sap xep
	cout<<"Mang sap xep theo thu tu tang dan"<<endl;
	for(int i = 0; i < n; i++)
		cout<<mang[i]<<" ";
	cout<<endl;

	return 0;
}
