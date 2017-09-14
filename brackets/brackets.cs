// In a string containing any brackets (usually code) do all the brackets match in pairs?

public bool DoBracketsMatch(string input)
{
	string previous = "";
	
	while (input.Length != previous.Length)
	{
		previous = input;
		input = input.Replace("()", String.Empty).Replace("[]", String.Empty).Replace("{}", String.Empty);
	}
	
	return (input.Length == 0);
}
