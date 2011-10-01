/*
 * Sun's tutorial
 * This program use BufferedReader and PrintWriter to print a line-oriented document
 */

import java.io.FileReader;
import java.io.FileWriter;
import java.io.BufferedReader;
import java.io.PrintWriter;
import java.io.IOException;

public class CopyLines 
{
	public static void main(String[] args) throws IOException
	{
		BufferedReader in = null;
		PrintWriter out = null;

		try {
			in = new BufferedReader(new FileReader("CopyLines.java"));
			out = new PrintWriter(new FileWriter("CloneCopyLines"));

			String l;

			//in.readLine() doesn't read \n char?
			while((l = in.readLine()) != null) 
			{
				out.println(l);
			}
		} finally {
			if(in != null) in.close();
			if(out != null) out.close();
		}

		System.out.println("Done");

	}
}
