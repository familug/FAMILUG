/* Tao mot lop goi la Complex de thuc hien
 * cac thao tac so hoc voi cac so phuc.
 * Viet chuong trinh de kiem tra lop nay.
 * So phuc co dang: <phan thuc> + <phan ao>*i
 * Su dung cac bien thuc de bieu dien
 * cac thanh phan du lieu rieng cua lop.
 * Cung cap mot ham thiet lap de tao doi tuong.
 * Ham thiet lap su dung cac tham so co
 * gia tri ngam dinh.
 * Ngoai ra con co cac ham thanh phan public
 * de thuc hien cac cong viec sau
 * + Cong 2 so phuc
 * + Tru 2 so phuc
 * + In so phuc ra man hinh dang a+b*i
 */

#include <iostream>
using namespace std;

// Lop complex version 1
class Complex
{
	float re;
	float im;

	public:
	// Ham tao voi tham so ngam dinh
	Complex(float re = 0, float im = 0)
	{
		this->re = re;
		this->im = im;
	}

	// Ham cong 2 so phuc
	Complex add(Complex c)
	{
		Complex res;

		res.re = re + c.re;
		res.im = re + c.im;

		return res;
	}

	// Ham tru 2 so phuc
	Complex sub(Complex c)
	{
		Complex res;

		res.re = re - c.re;
		res.im = im - c.im;

		return res;
	}

	// Ham hien thi so phuc
	void display()
	{
		cout<<re;

		if(im < 0)
			cout<<"-"<<-im<<"*i";
		else if(im > 0)
			cout<<"+"<<im<<"*i";
	}
};

int main(void)
{
	Complex c1(3, 4), c2(5, 4), c3;

	cout<<"So phuc thu nhat: ";
	c1.display();
	cout<<endl;

	cout<<"So phuc thu hai: ";
	c2.display();
	cout<<endl;

	c3 = c1.add(c2);
	cout<<"Tong 2 so phuc: ";
	c3.display();
	cout<<endl;
	c3 = c1.sub(c2);
	cout<<"Hieu 2 so phuc: ";
	c3.display();
	cout<<endl;

	return 0;
}
