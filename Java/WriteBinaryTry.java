import java.io.DataOutputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class WriteBinaryTry
{
	public static void main (String [] args) throws IOException
	{
		//int i = Integer.parseInt(args[0]);
		String s = "con meokeu";

		String FILENAME = "binary.txt";
		//DataOutputStream os = new DataOutputStream(new FileOutputStream(FILENAME));

		//os.writeInt(i);
		//os.close();

		FileOutputStream fos = new FileOutputStream(FILENAME);
		fos.write(s.getBytes());
		fos.close();
		//System.out.println("wrote " + i);
	}
}
