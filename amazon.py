from bs4 import BeautifulSoup
import requests, pyperclip
import re
def amazon():
    URL = pyperclip.paste()
    

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
    # headers can be found by searching on your browser 'what is my header'.
    
    page = requests.get(URL, headers=headers)
    #using requests module to going to the desired website
    

    soup1 = BeautifulSoup(page.content, "html.parser")
    #using beautiful module for parsing the website and the elements to web scrape

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    
  

    if soup2.find(id='productTitle'):

        title = soup2.find(id='productTitle').get_text().lstrip()
        print(title)
    else:
        print("no tittle")
    
    if '?' in URL:
             
            original = URL.split('?')
            print(original)
            my_link = original[0] + '?tag=dealteck-21'
            print(my_link)
            
            
            
            
    else:
        pass
        
   
    if soup2.select(".a-offscreen"):
         
            
        price = soup2.select(".a-offscreen")[0]
        p =(price.text)
        k =((p.split()))        
       
        print('▶️offer price',k[0])

        j = '👉🏻 '+ title + '\n\n✅offer price  '+ str(k[0]) +'\n buy link -- ' + my_link

        pyperclip.copy(j) 
    else:
        pyperclip.copy("no price found")
    
amazon()
