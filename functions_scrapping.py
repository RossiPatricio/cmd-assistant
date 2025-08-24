import requests, time
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from duck_search import *

# IMdb

def scrap_imdb(search):
    """ Extrae informacion sobre peliculas de IMDB. """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"}
    
    url = search
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    title = soup.title.text.replace(' - IMDb', '').strip() 
    director = soup.find('a', class_='ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link').text
    resume = soup.find('span', class_='sc-bf30a0e-0 iOCbqI').text
    names = soup.find_all('a', class_='ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link')
    crew= []
    for name in names[1:6]:
        crew.append(name.text)
     
    media = soup.find('div', class_='ipc-poster ipc-poster--baseAlt ipc-poster--media-radius ipc-poster--wl-true ipc-poster--dynamic-width ipc-sub-grid-item ipc-sub-grid-item--span-2')
    viewer = media.a['href']
    
    url2 = f'https://www.imdb.com/{viewer}'
    response2 = requests.get(url2, headers=headers)
    soup2 = BeautifulSoup(response2.content, 'html.parser')
    
    image = soup2.find('div', class_='sc-b66608db-2 cEjYQy')
    img = image.img['src']
    
    dic = {
        'TITLE': title.upper(),
        'DIRECTOR': director,
        'SYNOPSIS': resume,
        'TEAM': crew,
        'POSTER': img
    }
    return dic

def movie_info(element):
    url = get_url(element)
    content = scrap_imdb(url)
    return content


# Wikipedia

def get_face(search):
    """ Extrae foto de perfil de wikipedia usando web scrapping. """
    try:
        # Playwright
        pw = sync_playwright().start()
        browser= pw.chromium.launch(headless= True)
        page= browser.new_page()
        print('Accessing: https://www.wikipedia.org/')
        page.goto('https://www.wikipedia.org/')
        time.sleep(2)
        page.get_by_label("search").fill(search)
        print(f'Searching: {search.title()}')
        page.keyboard.press("Enter")
        time.sleep(2)
        # BeautifulSoup
        print(f'Processing data...')
        soup= BeautifulSoup(page.content(), 'html.parser')
        image = soup.find('td', class_="imagen")
        img_path = image.span.a.img['src']
        return(f'http:{img_path}')
        
    except Exception as e:
        return(f'Error:{e}')


# USD

def get_usd():
    dolar_types = {
    'Dolar oficial' : 'https://www.dolarnews.com.ar/cotizacion-dolar-oficial',
    'Dolar blue' : 'https://www.dolarnews.com.ar/cotizacion-dolar-blue'
    }
    for type, url in dolar_types.items():
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            data = soup.find_all('div', class_='pricing')

            for element in data:
                print(f'{type}: {element.text}')
        except Exception as e:
            print(e)

