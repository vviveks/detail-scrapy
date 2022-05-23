# Import Libraries

import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import re

def ExtractParaFromWebsite(URL):
    # Scraping HTML
    html = requests.get(URL)
    html_text = html.text

    # Soup!!
    soup = BeautifulSoup(html_text, 'lxml')
    paragraph = soup.find_all('p')

    para = []

    for p in paragraph:
        para.append(p.text.replace('\n', '').replace('  ', ''))
    
    return para
