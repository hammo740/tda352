// Compilation (CryptoLibTest contains the main-method):
//   javac CryptoLibTest.java
// Running:
//   java CryptoLibTest

public class CryptoLib 

{

	/**
	 * Returns an array "result" with the values "result[0] = gcd",
	 * "result[1] = s" and "result[2] = t" such that "gcd" is the greatest
	 * common divisor of "a" and "b", and "gcd = a * s + b * t".
	 **/
	public static int[] EEA(int a, int b) 

	{
		// Note: as you can see in the test suite,
		// your function should work for any (positive) value of a and b.

		int gcd = -1;
		int s = 0, old_s = 1;
		int t = 1, old_t = 0;
		int r = b, old_r = a;


		int[] result = new int[3];
		result[0] = gcd;
		result[1] = s;
		result[2] = t;


		if(a==b)
		{
			result[0]=a;
			result[1]=1;
			result[2]=0;

		}
		else
		{
			while (r!=0)
			{
				int quotient=old_r/r;
				int temp;

				temp	=	r;
				r		=	old_r-quotient*r;
				old_r	=	temp;

				temp = s;
				s = old_s -quotient*s;
				old_s = temp;

				temp = t;
				t = old_t - quotient*t;
				old_t = temp;
			}
		}

		gcd = old_r;
		result[0]=gcd;
		result[1]=old_s;
		result[2]=old_t;

		return result;
	}

	/**
	 * Returns Euler's Totient for value "n".
	 **/
	public static int EulerPhi(int n) 

	{
		int count = 0;
		for (int i = 1; i < n; i++) 
		{
			count=(EEA(n, i)[0]==1)?count+1:count;
		}
		return count;
	}

	/**
	 * Returns the value "v" such that "n*v = 1 (mod m)". Returns 0 if the
	 * modular inverse does not exist.
	 **/
	public static int ModInv(int n, int m) 

	{

		// Considers both positive and negative numbers n
		int rem = (n%m+m)%m;
		for (int i=1; i<m; i++)
		{
			if ((rem*i) % m == 1) 
			{
				return i;
			}
		}

		return 0;
	}

	/**
	 * Returns 0 if "n" is a Fermat Prime, otherwise it returns the lowest
	 * Fermat Witness. Tests values from 2 (inclusive) to "n/3" (exclusive).
	 **/
	public static int FermatPT(int n) 

	{
		for (int i = 2; i < (n / 3); i++)
		{
			if (modular_pow(i, n-1, n) != 1)
			{
				return i;
			}
		}
		return 0;
	}

	//	Modular exponentiation
	//	Source: https://en.wikipedia.org/wiki/Modular_exponentiation

	public static int modular_pow(int base, int exponent, int modulus)
	{
		if (modulus == 1)
		{
			return 0; 
		}
		int rem = 1;
		for(int e_prime = 1; e_prime <= exponent; e_prime++)
		{
			rem = (rem * base)%modulus;
		}
		return rem;
	}


	/**
	 * Returns the probability that calling a perfect hash function with
	 * "n_samples" (uniformly distributed) will give one collision (i.e. that
	 * two samples result in the same hash) -- where "size" is the number of
	 * different output values the hash function can produce.
	 **/
	public static double HashCP(double n_samples, double size) {
		  double probability = 1;
		  for(double i=size-(n_samples-1);i <= (size-1); i++)
		  {
			  probability=probability*(i/size);
		  }
		  
		  return 1-probability;

	}

}