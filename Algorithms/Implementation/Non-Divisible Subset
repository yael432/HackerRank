using System;
using System.Collections.Generic;
using System.IO;
class Solution {
    static void Main(String[] args) {
        int maxIntger = 0;

            string[] userInput;

            userInput = Console.ReadLine().Split(' ');
            int totalInt = int.Parse(userInput[0]);
            byte denominator = byte.Parse(userInput[1]);

            int [] myInts = Array.ConvertAll(Console.ReadLine().Split(' '), s => int.Parse(s));

            var moduloCounter = new int[denominator];

            int modulo;

            for (int i =0; i< myInts.Length;i++)
            {
                modulo = myInts[i] % denominator;

                moduloCounter[modulo]++;
                
            }

           if (moduloCounter[0] >0)
           {
               maxIntger++;
           }

           if (denominator%2 ==0)
           {
               if (moduloCounter[denominator / 2] > 0)
               {
                   maxIntger++;
               }
           }

           int k;
           int finalIndex =(int) Math.Ceiling((decimal)denominator / 2);

           for (int i = 1; i < finalIndex; i++)
           {
               k = moduloCounter.Length - i;

               maxIntger += Math.Max(moduloCounter[i], moduloCounter[k]);

           }

           Console.WriteLine(maxIntger);
    }
}
