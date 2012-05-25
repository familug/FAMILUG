/* Viet lop String de mo ta mot chuoi ky tu
 * Lop String gom cac thanh phan sau:
 * + Du lieu: char *s (bieu dien noi dung chuoi).
 * + Cac thanh phan:
 *   - Ham tao khong tham so (cho s = '\0')
 *   - Ham tao 1 tham so la chuoi
 *   - Ham tao sao chep
 *   - Ham huy
 *   - Toan tu gan = de copy noi dung cua
 *     chuoi nay sang chuoi khac.
 *   - Toan tu >, <, >=, <=, ==, != de so sanh
 *     noi dung cua hai chuoi (so sanh theo tu dien)
 *   - Ham Display() hien thi noi dung chuoi.
 */

using namespace std;

#include <iostream>
#include <string.h>

class String
{
	char *s;

	public:

	// Ham tao khong tham so
	String()
	{
		s = new char;
		*s = '\0';
	}

	// Ham tao 1 tham so la chuoi
	String(const char *s)
	{
		int len;

		len = strlen(s);

		this->s = new char[len + 1];

		strcpy(this->s, s);
	}

	// Ham tao sao chep
	String(const String &s1)
	{
		int len;

		len = strlen(s1.s);

		this->s = new char[len + 1];

		strcpy(this->s, s1.s);
	}

	// Ham huy
	~String()
	{
		delete[] s;
	}

	// Toan tu gan =
	String operator=(const String &s1)
	{
		int len;

		delete[] this->s;
		len = strlen(s1.s);
		this->s = new char[len + 1];
		strcpy(this->s, s1.s);

		return s1;
	}

	// Toan tu so sanh >
	int operator>(const String &s1)
	{
		int i;

		i = 0;
		while(s[i] != '\0' && s1.s[i] != '\0')
		{
			if(s[i] > s1.s[i])
				return 1;
			else if(s[i] < s1.s[i])
				return 0;
			i++;
		}
		if(s[i] != '\0')
			return 1;
		else
			return 0;
	}

	// Toan tu so sanh <
	int operator<(const String &s1)
	{
		int i;

		i = 0;
		while(s[i] != '\0' && s1.s[i] != '\0')
		{
			if(s[i] < s1.s[i])
				return 1;
			else if(s[i] > s1.s[i])
				return 0;
			i++;
		}
		if(s1.s[i] != '\0')
			return 1;
		else
			return 0;
	}

	// Toan tu so sanh >=
	int operator>=(const String &s1)
	{
		int i;

		i = 0;
		while(s[i] != '\0' && s1.s[i] != '\0')
		{
			if(s[i] > s1.s[i])
				return 1;
			else if(s[i] < s1.s[i])
				return 0;
			i++;
		}
		if(s1.s[i] == '\0')
			return 1;
		else
			return 0;
	}

	// Toan tu <=
	int operator<=(const String &s1)
	{
		int i;

		i = 0;
		while(s[i] != '\0' && s1.s[i] != '\0')
		{
			if(s[i] < s1.s[i])
				return 1;
			else if(s[i] > s1.s[i])
				return 0;
			i++;
		}
		if(s[i] == '\0')
			return 1;
		else
			return 0;
	}			

	// Toan tu ==
	int operator==(const String &s1)
	{
		int i;

		i = 0;
		while(s[i] != '\0' && s1.s[i] != '\0')
		{
			if(s[i] != s1.s[i])
				return 0;
			i++;
		}
		if(s[i] != '\0' || s1.s[i] != '\0')
			return 0;

		return 1;
	}

	// Toan tu !=
	int operator!=(const String &s1)
	{
		int i;

		i = 0;
		while(s[i] != '\0' && s1.s[i] != '\0')
		{
			if(s[i] != s1.s[i])
				return 1;
			i++;
		}
		if(s[i] == '\0' && s1.s[i] == '\0')
			return 0;

		return 1;
	}

	void display()
	{
		cout<<s;
	}
};

int main(void)
{
	String s1("Nguyen Van Hiep"), s2(s1), s3, s4("Hiep Nguyen Van");

	cout<<"Chuoi s1: ";
	s1.display();
	cout<<endl;

	cout<<"Chuoi s2 la copy tu s1 bang ham tao copy: ";
	s2.display();
	cout<<endl;

	s3 = s1;
	cout<<"Gan s1 cho s3: ";
	s3.display();
	cout<<endl;

	cout<<"Chuoi s4: ";
	s4.display();
	cout<<endl;

	if(s1 == s2)
		cout<<"Hai chuoi s1 va s2 bang nhau"<<endl;
	else
		cout<<"Hai chuoi s1 va s2 khong bang nhau"<<endl;

	if(s1 > s4)
		cout<<"s1 > s4 theo thu tu tu dien"<<endl;
	else
		cout<<"s1 <= s4 theo thu tu tu dien"<<endl;

	return 0;
}
