/* Chuong trinh su dung toan tu new de
 * cap phat bo nho dong cho mang 2 chieu
 * minh hoa bang cac thao tac tren ma tran
 */
#include <iostream>
using namespace std;

int main(void)
{
	int n;
	float **matrix;

	cout<<"Nhap co cho ma tran vuong:";
	cin>>n;

	if(n <= 0)
		return 1;

	// Cap phat mang con tro kieu float gom n phan tu
	matrix = new float*[n];

	// Cap phat n mang kieu float, moi mang n phan tu
	for(int i = 0; i < n; i++)
		matrix[i] = new float[n];

	cout<<"Nhap du lieu cho ma tran"<<endl;
	for(int i = 0; i < n; i++)
		for(int j = 0; j < n; j++)
		{
			cout<<"Phan tu hang "<<i + 1<<" cot "<<j + 1<<" :";
			cin>>matrix[i][j];
		}

	// Hien thi ma tran vua nhap
	cout<<"Ma tran vua nhap la"<<endl;
	for(int i = 0; i < n; i++)
	{
		for(int j = 0; j < n; j++)
		{
			cout<<matrix[i][j]<<" ";
		}
		cout<<endl;
	}

	// Giai phong bo nho dong
	for(int i = 0; i < n; i++)
		delete[] matrix[i];
	delete[] matrix;

	return 0;
}
