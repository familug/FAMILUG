/* Tao mot lop goi la PS de thuc hien
 * cac thao tac so hoc voi phan so.
 * Viet chuong trinh kiem tra.
 * Su dung cac bien nguyen de bieu dien cac
 * thanh phan du lieu cua lop - tu so va mau so.
 * Viet dinh nghia ham thiet lap de tao doi
 * tuong sao cho mau so phai la so nguyen duong.
 * Ngoai ra con co cac ham thanh phan khac thuc
 * hien cac cong viec cu the:
 * + Cong 2 phan so. Ket qua phai duoc toi gian.
 * + Tru 2 phan so. Ket qua phai toi gian.
 * + Chia 2 phan so. Ket qua toi gian.
 * + Nhan 2 phan so. Ket qua toi gian.
 * + In ra man hinh phan so dang a/b trong do
 *   a la tu so con b la mau so.
 * + In phan so duoi dang so thap phan.
 */

using namespace std;

#include <iostream>

// Tim uoc chung lon nhat cua 2 so nguyen duong
int ucln(int a, int b)
{
	int tmp;

	if(a < 0)
		a = -a;
	if(b < 0)
		b = -b;

	if(a == 0 || b == 0)
		cout<<"Mot trong hai so bang 0"<<endl;

	do
	{
		tmp = a%b;
		a = b;
		b = tmp;
	}
	while(tmp > 0);

	return a;
}

class fraction
{
	int numerator;   // Tu so
	int denominator; // Mau so

	public:
	// Ham tao khong tham so
	fraction()
	{
		numerator = 0;
		denominator = 1;
	}

	// Ham tao 2 tham so a = tu so, b = mau so
	fraction(int a, int b)
	{	
		if(b == 0)
			cout<<"Math error!"<<endl;
		else if(b < 0)
		{
			numerator = -a;
			denominator = -b;
		}
		else
		{
			numerator = a;
			denominator = b;
		}
	}

	// Ham cong 2 phan so, tra ve ket qua toi gian
	fraction add(fraction x)
	{
		fraction res;
		int d;

		res.numerator = numerator*x.denominator + denominator*x.numerator;
		res.denominator = denominator*x.denominator;

		d = ucln(res.numerator, res.denominator);

		res.numerator /= d;
		res.denominator /= d;

		return res;
	}

	// Ham tru 2 phan so, tra ve ket qua toi gian
	fraction sub(fraction x)
	{
		fraction res;
		int d;

		res.numerator = numerator*x.denominator - denominator*x.numerator;
		res.denominator = denominator*x.denominator;

		d = ucln(res.numerator, res.denominator);

		res.numerator /= d;
		res.denominator /= d;

		return res;
	}

	// Ham nhan 2 phan so, tra ve ket qua toi gian
	fraction mul(fraction x)
	{
		fraction res;
		int d;

		res.numerator = numerator*x.numerator;
		res.denominator = denominator*x.denominator;

		d = ucln(res.numerator, res.denominator);

		res.numerator /= d;
		res.denominator /= d;

		return res;
	}

	// Ham chia 2 phan so, tra ve ket qua toi gian
	fraction div(fraction x)
	{
		fraction res;
		int d;

		res.numerator = numerator*x.denominator;
		res.denominator = denominator*x.numerator;

		d = ucln(res.numerator, res.denominator);

		res.numerator /= d;
		res.denominator /= d;

		return res;
	}

	// Ham hien thi phan so dang a/b
	void display1()
	{
		cout<<numerator<<"/"<<denominator;
	}

	// Ham hien thi phan so dan thap phan
	void display2()
	{
		cout<<(float)numerator/denominator;
	}
};

int main(void)
{
	fraction a(3,4), b(2,3), c;

	cout<<"Phan so thu nhat:";
	a.display1();
	cout<<endl;

	cout<<"Phan so thu hai:";
	b.display1();
	cout<<endl;

	c = a.add(b);
	cout<<"Tong 2 phan so:";
	c.display1();
	cout<<endl;

	c = a.sub(b);
	cout<<"Hieu 2 phan so:";
	c.display1();
	cout<<endl;

	c = a.mul(b);
	cout<<"Tich 2 phan so:";
	c.display1();
	cout<<endl;

	c = a.div(b);
	cout<<"Thuong 2 phan so:";
	c.display1();
	cout<<endl;

	cout<<"Dang thap phan cua phan so:";
	a.display2();
	cout<<" ";
	b.display2();
	cout<<endl;

	return 0;
}
