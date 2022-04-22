'''
    @author: Victor Rayan
             e-mail: victorrayansouzaramos@gmail.com
'''

import os
import pandas as pd
import random

#Check if the file already exists, and if not creates a new blank file to receive 
#all entropy combinations.
try:
    file = open('entropy.csv', 'a')
except:
    file = open('entropy.csv', 'w')
    file.write('')
    
file = open('entropy.csv', 'a')

seed_words=12 #use 128 bits ascii to generate 12 words in seed phrase
seed_bits=32 #use 256 bits ascii to generate 24 words in seed phrase

#verify the type of seed phrase will be generated
if(seed_words==12): 
    seed_bits=32
else:
    seed_bits=64

df=[] #initialize the dataframe object, that contais all combinations made
entropy=''
entropy=entropy.ljust(seed_bits*4) #alocate the nedded length (bits) to the entopry variable.
REQUIRED_COMBINATIONS_NUM = 1000 #number of new binary combinations to do

#fill a dataframe object with the entropy file values, separating each value by line breaks
def load_entropy():
    df_ = pd.read_csv('entropy.csv', header=None)
    return df_

#this funcion generates radom and different entropy combinations and save into 'entropy.txt'
def combinations_gen(dataf):
 
    
   for num in range(REQUIRED_COMBINATIONS_NUM):
        entropy = last_bin = dataf[0][len(dataf)-1]
        random_bin = [None]*(seed_bits*4)
        while(entropy==last_bin):
            entropy=''
            for x in range(len(random_bin)):
                random_bin[x]=random.randint(0,1)
                entropy += str(random_bin[x])
    
        file_entr = open('entropy.csv', 'a')
        file_entr.write(entropy+"\n")
        load_entropy()

        
df = load_entropy()
combinations_gen(df)