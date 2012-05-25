/* Chuong trinh tao class mo phong
 * hoat dong cua stack.
 */

using namespace std;

#include <iostream>

class stack
{
	int *S;
	int T;
	int len;

	public:

	// Ham thiet lap 1 tham so.
	stack(int len = 100)
	{
		if(len > 0)
			S = new int[len];
		else
			S = new int[100];
		T = 0;
	}

	// Stack co rong hay khong?
	int is_empty()
	{
		if(T == 0)
			return 1;
		return 0;
	}

	// Stack da day chua?
	int is_full()
	{
		if(T == len)
			return 1;
		return 0;
	}

	// Day du lieu vo stack
	void push(int x)
	{
		if(this->is_full() == 1)
			cout<<"Stack da day, khong the day them du lieu vao!"<<endl;
		else
		{
			S[T] = x;
			T++;
		}
	}

	// Lay du lieu ra khoi stack
	int pop()
	{
		if(this->is_empty() == 1)
			cout<<"Stack rong, khong lay duoc du lieu ra"<<endl;
		else
			T--;

		return S[T];
	}
};

int main(void)
{
	stack a;

	a.push(10);
	a.push(20);
	a.push(30);
	a.push(40);

	cout<<a.pop()<<endl;
	cout<<a.pop()<<endl;
	cout<<a.pop()<<endl;
	cout<<a.pop()<<endl;

	a.pop();

	return 0;
}
