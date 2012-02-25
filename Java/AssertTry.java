public class AssertTry
{
	public static void main(String[] args)
	{
		for(int i = 1; i < 4; i++)
		{
			if(i % 3 == 1)
				System.out.println("i = " + i);
			else if(i % 3 == 2)
				System.out.println("i = " + i);
			else 
				//We know here i = 3
				//Exp1 : expression want to check, Exp2: value to show 
				assert i == 3 : i;
		}
	}
}
