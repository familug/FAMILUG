/*
 * =====================================================================================
 *
 *       Filename:  FriendExample.cpp
 *
 *    Description:  friend function 
 *
 *        Version:  1.0
 *        Created:  05/28/2012 05:00:56 PM
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

class Pokemon
{
	private:
		bool sex; // 0 is female, 1 is male
	public:
		Pokemon()
		{
			sex = 0;
		}

		//Ham ban khai bao dau ham trong nay. Them tu khoa friend, doi so phai la 1 object.
		friend void checkSex(Pokemon &aPokemon);
};//Pokemon

//Ham friend khong phai la ham thanh vien cua class Pokemon,
//the nhung vi duoc class Pokemon coi la ban nen duoc phep truy cap den thanh phan private

//Diem khac biet duy nhat la cua ham ban voi ham binh thuong la no duoc khai bao la friend trong than class 
void checkSex(Pokemon &aPokemon)
{
	if(aPokemon.sex == 0)
		cout<<"It's female\n";
	else 
		cout<<"It's male\n";
}

int main()
{
	Pokemon aPokemon;
	checkSex(aPokemon);
	return 0;
}
