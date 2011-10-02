/**
 * Sun's tutorial
 */
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;
import java.util.Locale;

public class ScanNumber 
{
	public static void main(String[] args) throws IOException
	{
		Scanner s = null;
		double sum = 0;

		try {
			s = new Scanner(new BufferedReader(new FileReader("ScanNumberData.txt")));
			s.useLocale(Locale.US);


			while(s.hasNext())
			{
				if(s.hasNextDouble())
				{
					sum += s.nextDouble();
				} 
				else 
				{
					s.next();
				}
			}//while
		} finally {
			if(s != null) s.close();
		}//finally

		System.out.println("Sum: " + sum);
	}
}
