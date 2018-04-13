import java.io.*;

import javax.xml.bind.DatatypeConverter;

public class CBCXor {

	public static int blockPtr_cipher=0;
	public static int blockSize=12;

	public static void main(String[] args) {
		String filename = "input.txt";
		byte[] first_block = null;
		byte[] encrypted = null;
		try {
			BufferedReader br = new BufferedReader(new FileReader(filename));
			first_block = br.readLine().getBytes();
			encrypted = DatatypeConverter.parseHexBinary(br.readLine());
			br.close();
		} catch (Exception err) {
			System.err.println("Error handling file.");
			err.printStackTrace();
			System.exit(1);
		}
		String m = recoverMessage(first_block, encrypted);
		System.out.println("Recovered message: " + m);
	}

	/**
	 * Recover the encrypted message (CBC encrypted with XOR, block size = blockSize).
	 *
	 * @param first_block
	 *            We know that this is the value of the first block of plain
	 *            text.
	 * @param encrypted
	 *            The encrypted text, of the form IV | C0 | C1 | ... where each
	 *            block is blockSize bytes long.
	 */
	private static String recoverMessage(byte[] first_block, byte[] encrypted) {

		// Recover Key, then use the recovered key to recover plaintext.
		// Use the key to recover the whole message
		return new String(recoverPlainText(recoverKey(first_block, encrypted), encrypted));
	}

	// Let the plainText be of the form: m0-m1-m2-m3-...-mn where mi is a 12-byte block for i=1,2,3,...,n

	// The corresponding ciphertext is of the form: IV-c0-c1-c2-c3-...-cn where IV and Ci are 12-byte blocks for i=1,2,3...,n

	// But we know m0 (198804307752)
	// Therefore, from the formula ci = k + (mi + c(i-1)) we get k = ci + (mi + c(i-1))
	// When i=0, C(i-1) = IV
	// Hence K = C0 + (m0 + IV)

	public static byte[] recoverKey(byte[] first_block, byte[] encrypted) {

		// Get first block (i.e Initialization Vector, IV)
		byte[] IV = nextBlock(encrypted);

		// get second block (i.e c0)
		byte[] c0 = nextBlock(encrypted); 

		// reset global block pointer to 0 for second pass
		blockPtr_cipher = 0;

		// recover key by using K = c0 xor (m0 xor IV)
		return xorFunction(c0,xorFunction(first_block,IV));

	}


	// Get the next block from the current global block pointer blockPtr_cipher 
	public static byte[] nextBlock(byte[] cipherText) {

		byte[] nextBlock = new byte[blockSize];

		int i=0;
		while(i<blockSize)
		{
			nextBlock[i++]=cipherText[blockPtr_cipher++];
		}

		return nextBlock;
	}

	public static byte[] xorFunction(byte[] block1, byte[] block2){
		byte[] xor = new byte[blockSize];
		int i=0;
		while (i < blockSize)
		{
			xor[i] = (byte) (0xff & (block1[i] ^ block2[i]));
			i++;
		}

		return xor;
	}

	public static byte[] recoverPlainText(byte[] key, byte[] encrypted) {
		int blockPtr_plain = 0;

		int lengthCT=encrypted.length;

		byte[] recoveredPT = new byte[lengthCT];

		// Get the first block
		byte[] previousC = nextBlock(encrypted);


		// loop needs to stop one block before last block because
		// nextBlock will be out of bounds
		while (blockPtr_cipher <= lengthCT-blockSize){

			// Decrypt a block using key, previous and current cipher text block
			// Since ci = k + (mi + c(i-1)). It follows that: mi = (k + ci) + c(i-1)
			byte[] currentC = nextBlock(encrypted);
			byte [] decryptedBlock = xorFunction(xorFunction(key,currentC),previousC);
			previousC = currentC;


			// Add the newly decrypted block to plain text block
			int i=0;
			while(i<blockSize)
			{
				recoveredPT[blockPtr_plain++] = decryptedBlock[i++];
			}
		}

		return recoveredPT;
	}








}
