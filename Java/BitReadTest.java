import java.util.*;
public class BitReadTest
{
	public static void main (String [] args)
	{
		int[] bits = new int[8];
		int oneByte = 10;
		for(int i = 0; i < bits.length && oneByte != 0 ; i++)
		{
			if(oneByte % 2 == 1)
			{
				bits[i] = 1;
			}
			System.out.println("bit[i] " + bits[i] + "oneByte " + oneByte);
			oneByte >>= 1;
		}//for
		System.out.println(Arrays.toString(bits));
	}//main
}
