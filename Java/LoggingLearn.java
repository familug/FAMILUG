import java.util.logging.FileHandler;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.io.IOException;
import java.util.logging.SimpleFormatter;

class LoggingLearn
{
	public static void main (String [] args)
	{
		Logger logger = Logger.getLogger("TestLogger");
		FileHandler fh;

		try {
			fh = new FileHandler("LoggingLearn.log", true);
			logger.addHandler(fh);
			logger.setLevel(Level.ALL);
			logger.log(Level.WARNING, "HEHEHEHEH");
			logger.info("HEHEHE");
			SimpleFormatter formatter = new SimpleFormatter();
			fh.setFormatter(formatter);

		} catch (SecurityException e)
		{
			e.printStackTrace();
		} catch (IOException e)
		{
			e.printStackTrace();
		}

	}//main

}//LoggingLearn

