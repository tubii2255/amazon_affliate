from bs4 import BeautifulSoup
import requests, pyperclip
import re
def amazon():
    URL = 'https://amzn.to/3g3oYzc'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
    # headers can be found by searching on your browser 'what is my header'.
    
    page = requests.get(URL, headers=headers)
    #using requests module to going to the desired website
    

    soup1 = BeautifulSoup(page.content, "html.parser")
    #using beautiful module for parsing the website and the elements to web scrape

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    path_info = request.META.get('PATH_INFO')
    http_host = request.META.get('HTTP_HOST')
    print(path_info)

    
  

    if soup2.find(id='productTitle'): #through the html finding the product tittle class  

        title = soup2.find(id='productTitle').get_text().lstrip()
    else:
        pass
    
    # if '?' in URL: # this is for the link changing from the original link to our desired 
             
    #         original = URL.split('?')
    #         print(original)
    #         my_link = original[0] + '?tag=dealteck-21'           
    # else:
    #     pass  
   
    if soup2.select(".a-offscreen"):            
        price = soup2.select(".a-offscreen")[0]
        p =(price.text)
        k =((p.split()))        
       

        j = '👉🏻 '+ title + '\n\n✅offer price  '+ str(k[0]) + '\n'
        # +'\n buy link -- ' + my_link

        pyperclip.copy(j) 
    else:
        pyperclip.copy("no price found")
amazon()



