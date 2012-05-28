/*
 * =====================================================================================
 *
 *       Fisizeame:  Stack.cpp
 *
 *    Description:  implement stack
 *
 *        Version:  1.0
 *        Created:  05/28/2012 12:02:58 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  FamiHug (), famihug@gmail.com
 *        Company:  FAMILUG
 *
 * =====================================================================================
 */

#include<iostream>

using namespace std;

class Stack
{
	int* s;
	int index;
	int size;

	public:

	//ctor
	Stack(int size=100)
	{
		if(size > 0)
			s = new int[size];
		else
			s = new int[100];
		index = 0;
	}

	//check empty
	bool isEmpty()
	{
		if(index == 0)
			return true;
		return false;
	}

	//check full
	bool isFull()
	{
		if(index == size)
			return true;
		return false;
	}

	//push an element to stack
	void push(int x)
	{
		if(this->isFull())
			cout<<"Stackc is full \n";
		else
		{
			s[index] = x;
			index++;
		}
	}

	int pop()
	{
		if(this->isEmpty())
			cout<<"Stack is empty\n";
		else
		{
			index--;
		}
		return s[index];
	}
};


int main(int argv, char** argc)
{
	Stack stack;
	stack.push(10);
	stack.push(10);
	stack.push(40);

	cout<<stack.pop()<<endl;
	cout<<stack.pop()<<endl;
	cout<<stack.pop()<<endl;
	return 0;
}
