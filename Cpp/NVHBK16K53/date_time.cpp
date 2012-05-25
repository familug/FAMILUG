/* Ket hop hai lop date, time de mo ta
 * dong thoi ngay va gio.
 * Thay doi ham thanh phan tick() de
 * goi toi ham tang ngay moi khi can thiet.
 * Them cac ham hien thi thong tin ve ngay gio.
 * Hoan thien chuong trinh va kiem tra.
 */

using namespace std;

#include <iostream>
#include "time.h"

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

class date_time
{
	Date date;
	Time time;

	public:

	// Ham thiet lap khong tham so
	date_time()
	{
	}

	// Ham thiet lap co tham so ngam dinh.
	date_time(Date &date, Time &time)
	{
		if(&date != NULL)
			this->date = date;
		if(&time != NULL)
			this->time = time;
	}

	void tick()
	{
		if(time.tick() == 1)
			date.nextDay();
	}

	void display()
	{
		date.print();
		cout<<"	";
		time.display24();
	}
};

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
	date_time clock;

	clock.display();
	cout<<endl;

	for(int i = 0; i < 10000000; i++)
		clock.tick();

	clock.display();
	cout<<endl;
}
