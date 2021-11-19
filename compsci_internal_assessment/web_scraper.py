from bs4 import *
import requests as rq 

from selenium import webdriver
from selenium.webdriver.common.keys import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.By import 
from selenium.webdriver.common.By import *

import random_2

import random
import os
import math


# r2 = rq.get("https://www.studiogronda.com/projects/")
# soup2 = BeautifulSoup(r2.text, "html.parser")

def web_scraper(link):

    links = []

    image = BeautifulSoup.select('img[src^="https://www.studiogronda.com/wp-content"')

    for img in image:
        links.append(img['src'])

    os.mkdir('arch_pictures')
    i = 1

    for index, img_link in enumerate(links):
        if i <=10:
            img_data = rq.get(img_link).content
            with open(f'arch_pictures/{str(index+1)}.jpg', 'wb+') as f:
                f.write(img_data)
            i += 1
        else:
            f.close()
            break

    for index, img_ling


def web_scraper(link_2):

