'''

@author: Victor Rayan
        email: victorrayansouzaramos@gmail.com

'''



#import the nedded libraries to use the binary entropy combinations and seek into english
#dictionary after got the indexes by criptography process 
import os
import pandas as pd
import hashlib

#declares nedded variables
seed_binary_base = 4;   #ascii binary base representation (4 bits), to check the hash process
                        #**the 4 value is defined as default (to calculate 128 bits entropy) but can
                        #be changed in the future.
        
words_index_binary =[None]*12 #this will allocates the obtained words indexes in binary value
words_index_decimal =[None]*12 #this will allocates the obtained words indexes in decimal value
readable_words = [None]*12 #this will allocates the obtained words in string and readable format

'''
 the [words_index...] variables refers to indexes that forms the Seed Phrase from the dictionary
'''

#function that loads the entropy 'rainbown table' of binary combinations, to input into bip-39 process
def load_data():
    dataf = pd.read_csv('entropy.csv', header=None)
    return dataf

#function that loads the words dictionary that forms the Seed Phrase
def load_dict():
    dataf = pd.read_csv('english_bip39.txt', header=None)
    return dataf

df = load_data() #load dataframe with binary combinations 'entropy.txt'



def Bip_39_Procedure(index):
    
    #gets an entropy from binary combinations
    entropy = df[0][index]

    #get the number of bit padding, this will used after 
    #obtained the first character and their binary of hash256 result
    seed_binary_base=int((len(entropy))/32)

    #encode the entropy (binary sequence but in string) from string unknow format to bytes array
    #the standard input encryption used by SHA-256 in bits inputs to avoid future errors
    entropy_encoded = int(entropy, 2).to_bytes(len(entropy) // 8, byteorder='big')

    #create a 'pre SHA-256' object with the entropy input to make an operation 
    entropy_preHash = hashlib.sha256(entropy_encoded)

    #generates a hash (SHA-256 bits type) from entropy value 
    entropy_hash = entropy_preHash.hexdigest()

    #gets the first value from hash
    first_concat = int(entropy_hash[0:1], 16)

    #convert the first obtained characther from hash to hex format 
    #(abstract their binary representation)
    binary_concat = bin(first_concat)[2:] #the [2:] is used doesn't catch the first two values,
                                          #because it is in hex format, and we want to get only 
                                          #binary from this. (the bin from hex is from second bit onwards)
        
    #convets the obtained binary to string        
    bin_concat=str(binary_concat)
    bin_concat=binary_concat

    #fills the missings bit with zero (0) to get the ASCII format
    while(len(bin_concat)<seed_binary_base):
        bin_concat='0'+bin_concat
    
    #concats this binary value obtained from first hash characther into binary entropy value
    entropy=entropy+bin_concat

    #splits the final entropy value in blocks that results in 11 bits per block 
    #changing of ASCII after completation with extra bits to UTF-8 format
    #and convert each block to decimal values that will represent the index of each word in dictionary
    #and finally get the string words by the indexes in dictionay.
    for x in range(3*seed_binary_base):
        words_index_binary[x]=entropy[11*x:(11*x)+11]
        words_index_decimal[x]=int(words_index_binary[x], 2)
        readable_words[x]= load_dict()[0][words_index_decimal[x]]

    print(readable_words)
    
    return readable_words


#this method is called from another python file to get a number of generated hashs and your related seed phrases mainly
def GenPhrase(current_attemp):
    seed_phrase = Bip_39_Procedure(current_attemp)
    return seed_phrase