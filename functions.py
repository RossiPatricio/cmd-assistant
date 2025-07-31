from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time, psutil, os


music_folder = r'C:\Users\PRossi\Music'
movie_list = r'C:\Users\PRossi\documents-backup\Lists\Movies.txt'



music_list = {}

for filename in os.listdir(music_folder):
    if filename.endswith(('.mp3', '.wav')):
        name = os.path.splitext(filename)[0].lower()
        path = os.path.join(music_folder, filename)
        music_list[name] = path

def add(result, update):
    """ Agregar lineas a un archivo txt. """
    my_lists = { 
        'websites': r'C:\Users\PRossi\documents-backup\Lists\Websites.txt',
        'website': r'C:\Users\PRossi\documents-backup\Lists\Websites.txt',
        'movies': movie_list,
        'movie': movie_list,
        'actor': r'C:\Users\PRossi\documents-backup\Lists\Actors.txt',
        'names': r'C:\Users\PRossi\documents-backup\Lists\Names.txt',
        'name': r'C:\Users\PRossi\documents-backup\Lists\Names.txt',
        'python': r'C:\Users\PRossi\documents-backup\Python.txt'
    }

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
    count= 0
    with open(movie_list, 'r', encoding='utf-8') as file_object:
        for line in file_object:
            count += line.lower().count(keyword.lower())
        if count == 1:
            return f'La palabra "{keyword.title()}" aparece {count} vez.'
        else:
            return f'La palabra "{keyword.title()}" aparece {count} veces en el archivo"{movie_list}".'

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

# SYSTEM 

def get_system_info():
    """Devuelve información general del sistema."""
    info = {
        'CPU Cores': psutil.cpu_count(logical=True),
        'CPU Frequency': f"{psutil.cpu_freq().current:.2f} MHz",
        'Total Memory': f"{psutil.virtual_memory().total / (1024**3):.2f} GB",
        'Disk Total': f"{psutil.disk_usage('/').total / (1024**3):.2f} GB",
    }
    return '\n'.join([f"{key}: {value}" for key, value in info.items()])

def get_cpu_usage():
    """Devuelve el porcentaje de uso de CPU."""
    return f"CPU Usage: {psutil.cpu_percent(interval=1)}%"

def get_memory_usage():
    """Devuelve el uso de memoria RAM."""
    memory = psutil.virtual_memory()
    return f"Memory Usage: {memory.percent}% ({memory.used / (1024**3):.2f} GB / {memory.total / (1024**3):.2f} GB)"

def get_disk_usage():
    """Devuelve el uso del disco duro."""
    disk = psutil.disk_usage('/')
    return f"Disk Usage: {disk.percent}% ({disk.used / (1024**3):.2f} GB / {disk.total / (1024**3):.2f} GB)"

def get_network_usage():
    counters = psutil.net_io_counters()
    sent    = counters.bytes_sent
    recv    = counters.bytes_recv
    return f"Enviados: {sent/1024/1024:.2f} MB  Recibidos: {recv/1024/1024:.2f} MB"
