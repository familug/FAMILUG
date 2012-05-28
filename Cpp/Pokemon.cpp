/*
 * =====================================================================================
 *
 *       Filename:  Pokemon.cpp
 *
 *    Description:  OOP with pokemon :))
 *
 *        Version:  1.0
 *        Created:  05/28/2012 04:37:18 PM
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
	//bool sex; // 0 is female, 1 is male
	public:
	virtual void sayMyName()
	{
		cout<<"I'm a pokemon\n";
	}
};//Pokemon

class Pichu : public Pokemon
{
	public:
		void sayMyName()
		{
			cout<<"Pichu pichu\n";
		}
};

class Pikachu :public Pichu
{
	public:
		void sayMyName()
		{
			cout<<"Pikachu pikachu\n";
		}
};

class Bulbasaur :public Pokemon
{
	public:
		void sayMyName()
		{
			cout<<"Bulbasaur bulbasaur\n";
		}
};

void say(Pokemon& p)
{
	p.sayMyName();
}

int main()
{
	Pichu aPichu;
	Pikachu aPikachu;
	Bulbasaur aBulbasaur;

	//	aPichu.sayMyName();
	//	aPikachu.sayMyName();

	say(aPichu);
	say(aPikachu);
	say(aBulbasaur);

	return 0;
}
