import java.io.BufferedOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.io.File;
import java.io.FileWriter;
import java.io.FileOutputStream;


public class WriteBitLearn
{
	// 8bit - buffer
	private static int buffer = 0; 
	// number of bits remaining in buffer
	private static int N; 
	//
	//private static BufferedOutputStream out = new BufferedOutputStream("hihi");
	private static FileOutputStream out	= null;



	//Singleton
	private WriteBitLearn() {}

	private static void writeByte()
	{
		for(int i = 0; i < 8; i++)
		{
			buffer <<= 1;
			buffer |= 1;
		}
		try{
		out.write(buffer);
		} catch (Exception e)
		{
			e.printStackTrace();
		}//catch
	}

	private static void writeBit(boolean bit)
	{
		//shift to left 1 bit
		buffer <<= 1;

		if(bit)
		{
			buffer |= 1;
		}

		N++;
		System.out.println(N);
		if (N == 8)
			clearBuffer();

	}//writeBit

	private static void clearBuffer()
	{
		if(N == 8) return;
		if(N > 0) buffer <<= (8 - N);
		try
		{
			out.write(buffer);
		} catch (IOException e)
		{
			e.printStackTrace();
		}
		N = 0;
		buffer = 0;
	}

	/**
	 * Flush standard output...
	 */

	public static void flush()
	{
		clearBuffer();
		try
		{
			out.flush();
		}
		catch (IOException e) 
		{
			e.printStackTrace();
		}
	}

	public static void close()
	{
		flush();
		try
		{
			out.close();
		}
		catch (IOException e)
		{
			e.printStackTrace();
		}
	}//close()

	public static void write(boolean x)
	{
		writeBit(x);
	}

	public static void writeATest()
	{
		String str = "1011010110010101";
		boolean b;
		for(int i = 0; i < str.length(); i++)
		{
		if((str.charAt(i)) == 1)
			{
				b = true;
			} else
				b = false;
			WriteBitLearn.write(b);
		}//for
	}//writeATest

	public static void main (String [] args)
	{
		try 
		{
			out = new  FileOutputStream("hihi");
		} catch (Exception e)
		{
			e.printStackTrace();
		}
		WriteBitLearn.writeByte();
		//WriteBitLearn.writeATest();
		//clearBuffer();
	}//main

}//WriteBitLearn
