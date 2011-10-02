/**
 * Sun's tutorial
 * This program demonstrate Scanner
 */
import java.util.Scanner;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.FileReader;

public class ScannerTest
{
	public static void main(String[] args) throws IOException
	{

		Scanner s = null;

		try {
			s = new Scanner(new BufferedReader(new FileReader("ScannerTest.java")));

			//Print current using delimiter
			System.out.println("Delimiter:" +  s.delimiter());
			//changer delimiter
			s.useDelimiter(";");
			System.out.println("Delimiter:" +  s.delimiter());

			while(s.hasNext())
			{
				System.out.println(s.next());
			}

		} finally {
			if(s != null) s.close();
		}//finally

	}//main()
}//ScannerTest
