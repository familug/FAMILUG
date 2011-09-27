/**
 * @author: FamiHug
 */
import java.io.*;

public class WriteToFile 
{
	public static void main(String[] args)
	{
		try{
			//create file ad BufferedWriter obj
			BufferedWriter out = new BufferedWriter(new FileWriter("out.txt"));
			out.write("FAMILUG");
			out.newLine();//write \n
			out.write("20110927");
			out.newLine();//write \n

			//Test with write a array of int
			int[] arr = {1, 2, 3, 4, 5, 4, 3, 2, 1};
			for(int i : arr)
				out.write(i + " ");
			//close output stream
			out.close();
		} catch(IOException e)
		{
			e.printStackTrace();
		}
	}
}
