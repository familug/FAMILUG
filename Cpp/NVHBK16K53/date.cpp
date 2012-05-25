/* Viet chuong trinh khai bao lop date
 * mo ta ngay, thang va nam: day, month, year.
 * Lop date co 2 thanh phan:
 * + Ham thiet lap 3 tham so co gia tri ngam dinh
 * + Ham print() hien thi thong tin ve ngay,
 *   thang va nam duoi dang quen thuoc dd-mm-yyyy
 * Viet chuong trinh kiem tra viec su dung phep
 * gan cho cac doi tuong thuoc lop date
 */

using namespace std;

#include <iostream>

class Date
{
	int d;
	int m;
	int y;

	public:

	// Ham thiet lap 3 tham so ngam dinh
	Date(int d = 10, int m = 10, int y = 1990)
	{
		if(d <= 0 || d > 31)
			this->d = 1;
		else
			this->d = d;
		if(m <= 0 || m > 12)
			this->m = 1;
		else
			this->m = m;
		if(y <= 0)
			this->y = 1990;
		else
			this->y = y;
	}

	// Ham nextDay dung de tang tung ngay 1
	void nextDay()
	{
		if(d < 31)
			d++;
		else
		{
			d = 1;
			if(m < 12)
				m++;
			else
			{
				m = 1;
				y++;
			}
		}
	}

	// Ham hien thi ngay thang nam
	void print()
	{
		cout<<d<<"-"<<m<<"-"<<y;
	}
};

int main(void)
{
	Date cal1(12, 9, 2012), cal2;

	cal1.print();
	cout<<endl;

	cal2.print();
	cout<<endl;

	cal2 = cal1;
	cal2.print();
	cout<<endl;

	for(int i = 0; i < 100; i++)
		cal1.nextDay();

	cal1.print();
	cout<<endl;

	return 0;
}
