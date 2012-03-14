public class AdapterLearning
{
}

class MyAdapter
{
	String BaseAdapter = "Based class can be used in both ListView and Spinner(impletment SpinnerAdapter)""; 

	String CursorAdapter = "expose data from a Cursor to a ListView, cursor must include a column named _id";
	String ResourceCursorAdapter = "Extend CursorAdapter";
	String SimpleCursorAdapter = "extends from child of CursorAdapter, map columns from a cursor to TextViews or ImageViews defined in an XML file";

	String ArrayAdapter = "extends from BaseAdapter, toString all objects in array to an TextView, override getView() to display array by other view"; 

	String SimpleAdapter = "extends from BaseAdapter, Map static data to views defined in XML file, dtata backing the list as an ArrayList of Maps"; 

	String ListAdapter = "extend Adapter, bridge between a ListView and data list. Data comes from Cursor or anything";


	String HeaderViewListAdapter;
	String SpinnerAdapter;
	String WrapperListAdapter;
}

