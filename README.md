Repository made in order to show security and how probabilistically difficult it is to succeed in a brute force attack on the passphrase generation and path derivation algorithm of BIP-39 and PBKDF2 with base SHA-256 hash.

This project was designed to simulate user interaction to reuse the complexity involved in master key generation and path derivation, part of which involves PBKDF 2 on Bip-39.
With this, the Selenium Python library was used to create the interaction in the Metamask extension.


Among other requirements for Selenium are the third-party Metamask extension (where there is no masking protection by Google):
    https://www.crx4chrome.com/crx/28869/

And Chromedrive or Webdrive depending on the browser to be used to perform the automated navigation:
    https://chromedriver.chromium.org/downloads


                                HOW WORKS RECOVERY PHRASE GEN - BIP 39?
                                                                

This consist a mnemonic phrase thats able to generate a master seed and derive your paths looking up into any Blockchain for associated coins or tokens.
The master seed consist in something such as an account that can store with itself many wallets, and each wallet can have tokens or associated coins from Blockchain.

A simple and secure way to recover an account from Blockchain and all your related balance, is generating the all nedded keys to lookup in Blockchain althrough Seed Phrase.

The Seed Phrase is the result of a interation on mathematical algorithm that consists in use the oficial bitcoin dictionary known as "BIP-39 WORDLIST" within 2048 words where will by
an random entropy (some times, plus a Salt such as password typed by user) will generate a hash and do the checksum process to create and valid a new entropy
and through this, generate 12 indexes that represents the postion of each word in dictionary to form the seed phrase starting with 0 index until 2047, working in this form:


1 - First we need an entropy (different, unique entropy) between 128 bits and 256 bits as string: 
      ENTROPY='010101010101011.....010101010101'
      
2 - Now is necessary to get a BASE to others math operations by length of ENTROPY divided by 32: 
      ENTROPY LENGTH / 32 = BASE

3 - Now we will generate a hash with SHA-256 algorithm and store it as hexadecimal type:
      SHA256(ENTROPY) = ENTROPY_HASH ---> as hexadecimal

4 - And the main step, make a Checksum, which is take the first BASE bits from hexadecimal hash and append into end of ENTROPY, creating a new entropy:
      VALID_ENTROPY = ENTROPY + (First BASE bits from ENTROPY_HASH ---> as string)
      
5 - Split the all VALID_ENTROPY in required words into seed phrase (WORDS), for example 12, and converts the binary entropy blocks to decimal that will represents the index of each
word from "BIP-39 WORDLIST":
      for example, whether the VALID_ENTROPY result is: 
      
      from VALID_ENTROPY = '010101001110111101011010.....1011110101101101111'
      to:  SPLITED_VALID_ENTROPY-BLOCK-1 = ['010101001110']
            ..... ..... ....
           SPLITED_VALID_ENTROPY-BLOCK-12 = ['101101101111']
           
           each block is formed by every 12 bits in sequence.
           
           *we can call the obtained blocks of "word list indices in binary"
      ** This block above isn't a code or programming language, this is only a simple way to convey the idea.

6 - The last step is convert the binary blocks to decimal and use them to get te words from "WORDLIST" by line index.
      For test, you can test with this initial 128 bits entropy '11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111'
      to get 12 words from dictionary afer performing this entropy through previous steps.
      
      You must get this follwing seed phrase: [ zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo wrong ] 
      

____________________________________________________________________________________________________________________________________________________________________________________________________
            
            
            
            Now that we understand how recovery phrase generation or also called seed phrase works, let's do an analysis of what we can do with it very quickly.

With the a valid seed phrase we can create or accidentally acces a wallet of other people, where we can use the seed phrase to start the process of deriving account keys and wallets, also called account mapping addresses and their wallets.

Althrough the BIP-39 Phrase gen algoritm was designed to accidently or intentional ilegal account access from oher people *almost* never happens.
Almost because this can happens with chance of 1 in (2048^(12 or 24 words) - target Blockchain users), but still it is a astronomical number to easily happens.

But even so, exchanges still protect their applications even when they only serve as an API for lay users, not to provide an environment of easy confusion between deprivation of wallets, because there can still be insecurity where you can just put a combination of words and synchronize a whole wallet from a blockchain, where if by chance (or often not by chance) that phrase is the key to deriving someone else's wallet, you can (but shouldn't) steal that person's wallet, or make transfers without consent.

While Metamask in my point of view works as an Open Source API in order to only aim at simplifying a user to manage their tokens without having to program Bip-39 and PBKDF2 to retrieve their information from the Blockchain. Giving up these security aspects.

Then we can exploit them in order to make a brute force attack by the Metamask Extension simulating a user interaction.

And how would that work? As I still don't know the details about the Metamask project and its encoding, I can think that they have their own way of forming a master key that is derived from the recovery phrase, which mathematically results in other valid keys for mapping the wallet to retrieve the information from an account on the blockchain correctly, but we don't need to think about the master key part with PBKDF2 and its complexity, we can think that as soon as we have an algorithm that generates valid sentences, we just need to insert it on the Import page Metamask Wallet and then your API will take care of carrying out the other cryptographic operations.

In an attacker's view, the problem lies in not "accessing" a wallet, but which wallet or account to "access" (recover data), the probability as already said of recovering someone else's account is almost nil, so this possibility it wouldn't even exist, but as we want to bother, just think that we can within the range of 2048^12 (let's play with the 12-word pass phrases, which is the one that has the most users on Ethereum probably)

If we want to do that, we'll use Python with Automated User Interaction Simulation (Selenium), and with it the valid sentence generation algorithm. As we have 2048^12 entropies to try, i.e. it is estimated that it would take a century with all the computing power of Bitcoin mining, we are going to use pseudo-luck to generate only a very small percentage of this astronomical portion, the Python Random.

The chance of violating the privacy of a really important account is as close to zero as you can still imagine, but we can reduce it by some magnitudes that in terms of the growth in the number of Ethereum users could be worrying depending on the point of view. Getting an equation like this:
        T = estimated seconds to access a user's first wallet --> What we really want to know.

        x = amount of blockchain user whose target cryptocurrency.

        a = estimated difference between (2048^12) combinations and valid
        combinations generated by BIP-39.

        b = attempts per second with seed phrases generated from BIP-39 (by
        sequentially inserting multiple bits by 32, totaling 128 for the
        BIP-39 function, remembering 2^128 possible combinations)

                                              T = ((2048^12) - x - a) / b
                       


In the case of the algorithm I developed in this repository, it is able to access an account and check its balance in imported tokens and Ethers, in which case, the account access information will be saved in a file. That's about 15 seconds or less (which could be a lot less with hardware dedicated to such activity) for each different seed phrase, which would average out to 0.06 counts per second, and that's a relatively high number in comparison. to the entire manual process that would have to be done to go through Coinbase's anti-bot protection and two-factor authentication, which most of the time would be an exponentially greater magnitude of security as much.

      
