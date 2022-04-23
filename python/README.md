How to execute this project?

First we need to have in mind that we need to generate a random entropy (a binary number of 128 bits), fro this, we can generate a random list, which we can call of "rainbow table" where each line represents a hiden seed phrase that will be revealed later.
 - Execute the entropyBinGen.py file, before take a look inside this file to do any changes of yout preference.

Now, we need to understand that this program will take the entropy list and to each entropy from list, will generates a unique Seed Phrase, we just need this Seed Phrase to access an wallet. For this we will execute the file bruteForce_Metamask.py that opens the chromium in developer mode and with a third extension of Metamask, input automatically the values related the Seed Phrase to import an wallet and access this to check your balance.
- The file bruteForce_Metamask.py invokes the SeedPhraseGen.py algortihm to do take the entropy line and make a Checksum generating a valid Seed Phrase and returns it to bruteForce_Metamask.py to inject into Recovery / Import Wallet Page.

**** Pay attention if was created a file named WALLETS_WITH_BALANCE.txt, it means will have gathered a wallet access with balance related!!!
