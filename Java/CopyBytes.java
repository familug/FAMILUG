/**
 * This program copy a file and write to onother
 * Sun's tutorial
 */

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class CopyBytes 
{
	public static void main(String[] args) throws IOException
	{
		FileInputStream in = null;
		FileOutputStream out = null;

		try {
			in = new FileInputStream("CopyBytes.java");
			out = new FileOutputStream("CopyBytesClone.java");
			int c;
			while((c = in.read()) != -1)
			{
				out.write(c);
			}

			System.out.println("Done!");
		} finally {
			if(in != null) in.close();
			if(out != null) out.close();
		}
	}
}
