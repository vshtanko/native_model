from __future__ import division

__author__ = 'Vladimir Shtanko'

from bs4 import BeautifulSoup
from collections import Counter

try:
    from urllib.parse import urlparse
except:
    from urlparse import urlparse

def title_string(soup):
    return soup.title.string

def title_length(soup):
    return len(soup.title.string)

def tag_count(soup):
    return len(soup.findAll()) 

def link_count(soup):
    return len(soup.find_all('a'))

def images_count(soup):
    return len(soup.find_all('img'))

def images_alt_percentage(soup):
    #считает количество изображений с непустым атрибутом alt
    images = soup.find_all('img')
    total = len(images)

    c = 0 

    for image in images:
        if 'alt' in image.attrs and image['alt'] != '': c+=1
     
    return c/total

def links_domain_percentage(soup):
    #определить все домены в линках страницы
    #определить из них наиболее часто встречающийся
    #посчитать его долю среди всех линков страницы
    
    domains = []
    for link in soup.find_all('a'):    
        domains.append(urlparse(link.get('href')).netloc)
    c = Counter(domains)
    
    return c.most_common(1)[0][1]/sum(c.values())

def link_images_count(soup):
    #считает количество изображений, являющихся ссылками
    c = 0
    for link in soup.find_all('a'):
        if 'img' in link.attrs: c +=1
    return c

