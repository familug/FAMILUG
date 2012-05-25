/* Chuong trinh minh hoa hoat dong cua stack chua so nguyen
 */
#include <iostream>
using namespace std;

#define MAX 100

// Khai bao bo nho su dung cho stack va con tro quan ly stack
int S[MAX], T = 0;

// Kiem tra stack co rong khong?
int is_empty()
{
	if(T <= 0)
		return 1;
	return 0;
}

// Kiem tra stack da day chua?
int is_full()
{
	if(T >= MAX)
		return 1;
	return 0;
}

// Day mot so nguyen vao stack
void push(int x)
{
	if(!is_full())
	{
		S[T] = x;
		T++;
	}
}

// Lay mot so nguyen khoi stack
int pop()
{
	if(!is_empty())
	{
		T--;
		return S[T];
	}

	return 0;
}

int main(void)
{
	// Day lien tiep 4 so nguyen 10, 20, 30, 40 vao stack
	push(10);
	push(20);
	push(30);
	push(40);

	// Lay lien tiep 3 so nguyen khoi stack va hien thi
	cout<<pop()<<endl;
	cout<<pop()<<endl;
	cout<<pop()<<endl;

	return 0;
}
