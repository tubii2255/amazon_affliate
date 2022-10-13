from bs4 import BeautifulSoup
import requests, pyperclip

def amazon():

    # getting link by pasting from clipboard
    link1 = pyperclip.paste()
    # getting browser url to add your affliate code
    data = requests.request("GET", link1)
    m_url = data.url
    
    URL = m_url

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
    # headers can be found by searching on your browser 'what is my header'.
    
    page = requests.get(URL, headers=headers)
    #using requests module to going to the desired website
    

    soup1 = BeautifulSoup(page.content, "html.parser")
    #using beautiful module for parsing the website and the elements to web scrape

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    

    
  

    if soup2.find(id='productTitle'): #through the html finding the product tittle class  

        title = soup2.find(id='productTitle').get_text().lstrip()
    else:
        pass
    
    if '?' in URL: # this is for the link changing from the original link to our desired 
             
            original = URL.split('?')
            print(original)
            my_link = original[0] + '?tag=dealteck-21'           
    else:
        pass  
   #class offscreen contains the list value of the price
    if soup2.select(".a-offscreen"):            
        price = soup2.select(".a-offscreen")[0]
        p =(price.text)
        k =((p.split()))        
       

        j = '👉🏻 '+ title + '\n\n✅offer price  '+ str(k[0]) + '\n buy link -- ' + my_link

        pyperclip.copy(j) 
    else:
        pyperclip.copy("no price found")
amazon()



