/**
 * @author: FamiHug
 */
import java.io.*:

public class WriteToFile 
{
	public static void main(String[] args)
	{
		try{
			BufferedWriter out = new BufferedWriter(new File("out.txt"));
			out.write("FAMILUG");
			//close output stream
			out.close();
		} catch(IOException e)
		{
			e.printStackTrace();
		}
	}
}
