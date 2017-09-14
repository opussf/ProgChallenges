public void PrintBinaryGap(int number)
{
	if (number == 0)
  	{
    	return 0;
  	}

	string binary = Convert.ToString(number, 2);

	Console.WriteLine(number + " in binary " + binary);

	var chunks = binary.Split(new char[] { '1' });

	Console.WriteLine("Length of longest consecutive string of 0's is " + chunks.Max(x => x.Length));

}
