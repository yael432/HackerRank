using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Numerics;

    class Program
    {
        static void Main(string[] args)
        {
            BigInteger trysome =1;
            string[] digitsSums = new string[1001];

            digitsSums[0] = "1";
            for (int i = 1; i <= 1000; i++)
			{
			    trysome *= i;
                string str = trysome.ToString();

                digitsSums[i] = str;

			}

            
            int n = Convert.ToInt32(Console.ReadLine());
                Console.WriteLine(digitsSums[n]);
            
            //Console.WriteLine(trysome);
            Console.ReadLine();
        }
    }

