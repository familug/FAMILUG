/**
 * By HVNSweeting @ familug.com
 */
import java.util.logging.*;
import java.io.IOException;

class HelloLog
{
	public static void main (String [] args)
	{
		Logger logger = Logger.getLogger("com.familug.hvn");
		FileHandler fh;
		try
		{
			fh = new FileHandler("HelloLog.log");
			logger.addHandler(fh);
			logger.setLevel(Level.ALL);

			logger.info("Do re mi");
			logger.log(Level.WARNING, "Vim fan");
		}//try
		catch (IOException e)
		{
			e.printStackTrace();
			logger.log(Level.WARNING, "LOI ROI HUHU");
		}//catch
	}//main
}//HelloLog

