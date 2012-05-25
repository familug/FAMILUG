class Time
{
	int h;
	int m;
	int s;

	public:

	// Ham thiet lap
	Time(int h = 0, int m = 0, int s = 0)
	{
		if(h < 0 || h >= 24)
			this->h = 0;
		else this->h = h;
		if(m < 0 || m >= 60)
			this->m = 0;
		else this->m = m;
		if(s < 0 || s >= 60)
			this->s = 0;
		else this->s = s;
	}

	// Ham cai dat thoi gian
	void set(int, int, int);

	// Ham cai dat gio
	void setHour(int);

	// Ham lay gia tri gio
	int getHour();

	// Ham cai dat phut
	void setMinute(int);

	// Ham lay gia tri phut
	int getMinute(void);

	// Ham cai dat giay
	void setSecond(int);

	// Ham lay gia tri giay
	int getSecond();

	// Ham tang 1s 1 lan
	int tick();

	// Ham hien thi voi dinh dang 24h
	void display24();

	// Ham hien thi voi dinh dang 12h
	void display12();
};
