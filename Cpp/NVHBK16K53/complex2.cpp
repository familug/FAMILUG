/* Tao mot lop goi la Complex de thuc hien
 * cac thao tac so hoc voi so phuc.
 * Viet chuong trinh de kiem tra lop nay.
 * So phuc co dang: <phan thuc> + <phan ao>*i
 * Su dung cac bien thuc de bieu dien
 * cac thanh phan du lieu rieng cua lop.
 * Cung cap mot ham thiet lam de tao doi tuong.
 * Ham thiet lap su dung cac tham so co gia tri ngam dinh.
 * Ngoai ra con co cac toan tu sau:
 * + Cong, tru, nhan, chia 2 so phuc.
 * + Toan tu >, <, >=, <= de so sang modulo cua 2 so phuc.
 * + Toan tu ==, != de so sanh 2 so phuc.
 * + Ham hien thi so phuc ra man hinh.
 * + Viet cac tu do la ban cua lop Complex.
 */

using namespace std;

#include <iostream>

class Complex
{
	double re;
	double im;

	public:

	//Ham tao co cac tham so voi gia tri ngam dinh
	Complex(double re = 0, double im = 0)
	{
		this->re = re;
		this->im = im;
	}

	// Toan tu cong 2 so phuc
	Complex operator+(const Complex &c)
	{
		Complex res;

		res.re = re + c.re;
		res.im = im + c.im;

		return res;
	}

	// Toan tu tru 2 so phuc
	Complex operator-(const Complex &c)
	{
		Complex res;

		res.re = re - c.re;
		res.im = im - c.im;

		return res;
	}

	// Toan tu nhan 2 so phuc
	Complex operator*(const Complex &c)
	{
		Complex res;

		res.re = re*c.re - im*c.im;
		res.im = re*c.im + im*c.re;

		return res;
	}

	// Toan tu chia 2 so phuc
	Complex operator/(const Complex &c)
	{
		int d;
		Complex res;

		d = c.re*c.re - c.im*c.im;
		res.re = (re*c.re + im*c.im)/d;
		res.im = (im*c.re - re*c.im)/d;

		return res;
	}

	// Toan tu so sanh >
	int operator>(const Complex &c)
	{
		if(re*re + im*im > c.re*c.re + c.im*c.im)
			return 1;
		else
			return 0;
	}

	// Toan tu so sanh <
	int operator<(const Complex &c)
	{
		if(re*re + im*im < c.re*c.re + c.im*c.im)
			return 1;
		else
			return 0;
	}

	// Toan tu so sanh >=
	int operator>=(const Complex &c)
	{
		if(re*re + im*im >= c.re*c.re + c.im*c.im)
			return 1;
		else
			return 0;
	}
	
	// Toan tu so sanh <=
	int operator<=(const Complex &c)
	{
		if(re*re + im*im <= c.re*c.re + c.im*c.im)
			return 1;
		else
			return 0;
	}

	// Toan tu so sanh ==
	int operator==(const Complex &c)
	{
		if(re == c.re && im == c.im)
			return 1;
		else
			return 0;
	}
	
	// Toan tu so sanh !=
	int operator!=(const Complex &c)
	{
		if(re != c.re || im != c.im)
			return 1;
		else
			return 0;
	}

	// Hien thi so phuc dang a + b*i
	void display()
	{
		if(re == 0)
		{
			if(im == 0)
				cout<<"0";
			else
			{
				if(im == 1)
					cout<<"i";
				else if(im == -1)
					cout<<"-i";
				else
					cout<<im<<"*i";
			}
		}
		else
		{
			cout<<re;
			if(im < 0)
			{
				if(im == -1)
					cout<<"-i";
				else
					cout<<im<<"*i";
			}
			else if(im > 0)
			{
				if(im == 1)
					cout<<"+i";
				else
					cout<<"+"<<im<<"*i";
			}
		}
	}
};

// Cac ham tu do la ham ban cua lop Complex
Complex Add(Complex &c1, Complex &c2)
{
	return c1 + c2;
}

Complex Sub(Complex &c1, Complex &c2)
{
	return (c1 - c2);
}

Complex Mul(Complex &c1, Complex &c2)
{
	return (c1 * c2);
}

Complex Div(Complex &c1, Complex &c2)
{
	return (c1 / c2);
}

int main(void)
{
	Complex a(2,3), b(3,4), c;

	cout<<"So phuc thu nhat:";
	a.display();
	cout<<endl;

	cout<<"So phuc thu hai:";
	b.display();
	cout<<endl;

	cout<<"Tong hai so phuc la:";
	c = a + b;
	c.display();
	cout<<endl;

	cout<<"Hieu hai so phuc la:";
	c = a - b;
	c.display();
	cout<<endl;

	cout<<"Tich hai so phuc la:";
	c = a * b;
	c.display();
	cout<<endl;

	cout<<"Thuong hai so phuc la:";
	c = a / b;
	c.display();
	cout<<endl;

	if(a > b)
		cout<<"Modulo cua so thu nhat lon hon so thu hai"<<endl;
	else
		cout<<"Modulo cua so thu nhat khong lon hon so thu hai"<<endl;

	if(a < b)
		cout<<"Modulo cua so thu nhat nho hon so thu hai"<<endl;
	else
		cout<<"Modulo cua so thu nhat khong nho hon so thu hai"<<endl;

	if(a == b)
		cout<<"Hai so phuc bang nhau"<<endl;

	if(a != b)
		cout<<"Hai so phuc khac nhau"<<endl;

	return 0;
}
