/**
 * Sun's tutorial
 *This program copy characters from input file to output file
 */
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class CopyCharacters
{
	public static void main(String[] args) throws IOException
	{
		FileReader in = null;
		FileWriter out = null;

		try {
			in = new FileReader("CopyCharacters.java");
			out = new FileWriter("CloneCopyCharacters");

			//This var will hold a character value in its last 16 bits
			int c;

			while((c = in.read()) != -1)
			{
				out.write(c);
			}
		} finally {
			if(in != null) in.close();
			if(out != null) out.close();
		}

		System.out.println("Done");
	}
}
