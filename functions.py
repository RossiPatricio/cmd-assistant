from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import requests, time, subprocess, os

def add(result, update):
    """ Agregar lineas a un archivo txt. """
    my_lists = { 
    'websites': r'C:\Users\PRossi\documents-backup\Lists\Websites.txt',
    'website': r'C:\Users\PRossi\documents-backup\Lists\Websites.txt',
    'movies': r'C:\Users\PRossi\documents-backup\Lists\Movies.txt',
    'movie': r'C:\Users\PRossi\documents-backup\Lists\Movies.txt',
    'actor': r'C:\Users\PRossi\documents-backup\Lists\Actors.txt',
    'names': r'C:\Users\PRossi\documents-backup\Lists\Names.txt',
    'name': r'C:\Users\PRossi\documents-backup\Lists\Names.txt',
    'python': r'C:\Users\PRossi\documents-backup\Python.txt'}

    if result in my_lists:
        archivo = my_lists[result]
    else:
        archivo = r'C:\Users\PRossi\documents-backup\any.txt'
    
    try:
        with open(archivo, 'a') as object_file:
            object_file.writelines(f'{update}\n')
            return f'update agregada: "{update}"\n({archivo})'
    except FileNotFoundError:
        return 'El archivo no existe.'
    except Exception as e:
        return f'Error deconocido: {e}'

def word_finder(keyword):
    """" Buscar y contar palabras en archivos .txt """ 
    file = r'C:\Users\PRossi\documents-backup\Lists\Movies.txt'
    count= 0
    with open(file, 'r', encoding='utf-8') as file_object:
        for line in file_object:
            count += line.lower().count(keyword.lower())
        if count == 1:
            return f'La palabra "{keyword.title()}" aparece {count} vez.'
        else:
            return f'La palabra "{keyword.title()}" aparece {count} veces en el archivo"{file}".'

def update_show(show, episode):
    """ Actualizar una lista de shows. """
    archivo = r'C:\Users\PRossi\documents-backup\current\shows.txt'
    try:
        with open(archivo, encoding= "utf-8") as file_object:
            lineas= file_object.readlines()
    except FileNotFoundError:
        print('Archivo no encontrado.')
    except Exception as e:
        print(f'Error desconocido: {e}')

    update = ''
    for i in range(len(lineas)):   
        if show.lower() in lineas[i].lower():
            current_show = lineas[i].split(":")[0]
            lineas[i] = f"{current_show}: {episode}\n"
            update = lineas[i]
    
    with open(archivo, 'w', encoding="utf-8") as file_object:
        file_object.writelines(lineas)
        return f'Actualizado: {update.title()}({archivo})'

def get_face(search):
    try:
        # Playwright
        pw = sync_playwright().start()
        browser= pw.chromium.launch(headless= True)
        page= browser.new_page()
        page.goto('https://www.wikipedia.org/')
        time.sleep(2)
        page.get_by_label("search").fill(search)
        page.keyboard.press("Enter")
        time.sleep(2)
        # BeautifulSoup
        soup= BeautifulSoup(page.content(), 'html.parser')
        image = soup.find('td', class_="imagen")
        img_path = image.span.a.img['src']
        return(f'http:{img_path}')
        
    except Exception as e:
        return(f'Error:{e}')

def open_game(path):
    subprocess.Popen([path], shell=True)
    os._exit(0)

def open_software(path):
    subprocess.Popen([path], shell=True)
    os._exit(0)

# random, temp, download
