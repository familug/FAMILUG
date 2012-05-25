/* Khai bao, dinh nghia, va su dung lop time
 * mo ta cac thong tin ve gio, phu va giay
 * voi yeu cau nhu sau:
 * Tao tep tin tieu de TIME.H chua khai bao
 * cua lop time voi cac thanh phan du lieu
 * mo ta gio, phut va giay: hour, minute, second.
 * Trong lop khai bao:
 * + Mot ham thiet lap ngam dinh, gan cac
 *   gia tri thanh phan bang 0.
 * + Ham set(int,int,int) voi 3 tham so ung
 *   voi 3 thanh phan du lieu cua lop.
 * + Ham hien thi o dinh dang 24h
 * + Ham hien thi o dinh dang 12h
 * Tao tep tin chuong trinh TIME.CPP chua dinh
 * nghia cua cac ham thanh phan trong lop time
 * va chuong trinh minh hoa cach su dung.
 */

using namespace std;

#include <iostream>
#include "time.h"

void Time::set(int h, int m, int s)
{
	if(h >= 0 && h < 24)
		this->h = h;

	if(m >= 0 && m < 60)
		this->m = m;

	if(s >= 0 && s < 60)
		this->s = s;
}

void Time::setHour(int h)
{
	if(h >= 0 && h < 24)
		this->h = h;
}

int Time::getHour()
{
	return h;
}

void Time::setMinute(int m)
{
	if(m >= 0 && m < 60)
		this->m = m;
}

int Time::getMinute()
{
	return m;
}

void Time::setSecond(int s)
{
	if(s >= 0 && s < 60)
		this->s = s;
}

int Time::getSecond()
{
	return s;
}

int Time::tick()
{
	if(s >= 59)
	{
		s = 0;
		if(m >= 59)
		{
			m = 0;
			if(h >= 23)
			{
				h = 0;
				return 1;
			}
			else
				h++;
		}
		else
			m++;
	}
	else
		s++;

	return 0;
}

void Time::display24()
{
	cout<<h<<":"<<m<<":"<<s;
}

void Time::display12()
{
	if(h <= 12)
		cout<<h;
	else
		cout<<h - 12;

	cout<<":"<<m<<":"<<s;

	if(h < 12)
		cout<<" AM";
	else
		cout<<" PM";
}

int main(void)
{
	Time clock;

	clock.set(22, 30, 40);	
	
	clock.display24();
	cout<<endl;
	clock.display12();
	cout<<endl;

	clock.setHour(12);
	clock.setMinute(49);
	clock.setSecond(20);

	cout<<clock.getHour()<<":"<<clock.getMinute()<<":"<<clock.getSecond()<<endl;

	for(int i = 0; i < 10003; i++)
		clock.tick();

	clock.display24();
	cout<<endl;

	return 0;
}
