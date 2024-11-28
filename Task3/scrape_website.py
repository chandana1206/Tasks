import os
import requests
from bs4 import BeautifulSoup

url = "https://ghconline.gov.in/index.php/consolidated-cause-list/"
response = requests.get(url)

if response.status_code == 200:
    soup= BeautifulSoup(response.text, 'html.parser')

    links= soup.find_all('a', href=True)
        
    pdf_link= None
    for link in links:
        if ".pdf" in link['href']:
            pdf_link= link['href']
            break

    pdf_response= requests.get(pdf_link)
    if pdf_response.status_code== 200:
        pdf_name = os.path.basename(pdf_link)
            
        with open(pdf_name, 'wb') as f:
            f.write(pdf_response.content)
            print(f"PDF downloaded successfully: {pdf_name}")