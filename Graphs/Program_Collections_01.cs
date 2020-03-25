using System;
using System.Collections;

class ArrayListProgram
{
    static void Main(string[] args)
    {
        ArrayList al = new ArrayList(100);
        al.Add("S1");
        al.Add("S2");
        Console.WriteLine(al.Add("S3"));
        al.Add("S4");
        al.Add("S5");
        al.AddRange(new string[] { "A1", "A2", "A3" });
        al.Insert(2, "I1");
        al.Remove("S4");
        al.RemoveAt(4);
        al.Sort();
        al.Reverse();
        al.TrimToSize();
        foreach (string s in al)
            Console.WriteLine(s);
        Console.WriteLine(al.Capacity + " " + al.Count);
        string[] ar = (string[])al.ToArray(typeof(string));
    }
}