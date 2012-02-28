import java.io.*;
import java.io.InputStreamReader;
import java.io.IOException;

/**
 * Try to read Vietnamese - it works
 */
public class UnicodeReadTry
{
	final private static String FILE_NAME = "unicode";
	public static void main (String [] args) throws UnsupportedEncodingException, FileNotFoundException
	{
		FileInputStream is = new FileInputStream(FILE_NAME);
		/* BufferedReader wrap ISR. ISR is a bridge from byte stream to character stream */
		BufferedReader br = new BufferedReader(new InputStreamReader(is, "UTF-8"));
		String line = null;
		try
		{
			while((line = br.readLine()) != null)
			{
				System.out.println(line);
			}//while
		} catch (Exception e)
		{
			e.printStackTrace();
		}//catch
	}//main
}//UnicodeReadTry
