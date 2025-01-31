//programm küsib nime
//kui sisestasid nime, siis konsool vastab
//TERE, sinu nimi
//peab kasutama if ja else
//kui nime ei sisetata, siis tuleb vastuseks
// ERROR ja konsool teeb Beep kolm korda 

using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Palun sisesta oma nimi:");
        string nimi = Console.ReadLine();

        if (string.IsNullOrEmpty(nimi))  // Kontrollime, kas nimi on sisestatud
        {
            Console.Beep();  // Teeb ühe beep'i
            Console.Beep();  // Teeb teise beep'i
            Console.Beep();  // Teeb kolmanda beep'i
            Console.WriteLine("ERROR");
        }
        else
        {
            Console.WriteLine($"TERE, sinu nimi on {nimi}");
        }
    }
}