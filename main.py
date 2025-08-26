import pyfiglet
from InquirerPy import inquirer
import os, subprocess, time
from colorama import init, Fore, Style
from functions_scrapping import *
from functions_system import *
from functions_music import *
from functions_download import *
from functions_documents import *
from duck_search import *

list_folder = r'C:\Users\PRossi\documents-backup\Lists'
music_folder = r'C:\Users\PRossi\Music'
movie_list = r'C:\Users\PRossi\documents-backup\Lists\Movies.txt'

software_list = {
    'vscode' : r'C:\Users\PRossi\AppData\Local\Programs\Microsoft VS Code\Code.exe',
}

game_list = {
    'skyrim' : r'C:\Archivos\The Elder Scrolls V Skyrim Legendary Edition\Skyrim.exe',
    'samp' : r'C:\Archivos\ASD+\samp.exe',
    'far cry' : r'C:\Program Files (x86)\Far Cry 3 Complete Collection\Far Cry 3\bin\farcry3.exe'
    #copmo hacer autocompletado para far cr tab-> far cry 3?
}

folder_list = {
    'docs' : r'C:\Users\PRossi\documents-backup',
    'lists' : list_folder,
    'projects': r'C:\Users\PRossi\code\.programming\.PROJECTS'
}

doc_list= {
    'movies': movie_list,
    'cartoons': fr'{list_folder}\Cartoons.txt',
    'shows': fr'{list_folder}\Shows.txt',
    'actors': fr'{list_folder}\Actors.txt',
    'games': fr'{list_folder}\Games.txt',
    'current shows': r'C:\Users\PRossi\documents-backup\current\shows.txt'
}

command_list = {
    'q': 'exit',
    'cls': 'clear',
    'system': 'system info',
    'system -a': 'full system info',
    "ram-disk-cpu": 'hardware info',
    'help folders': 'folder list',
    'movie' : 'is movie in list?',
    'movie -title' : 'is movie in list?',
    'add' : 'add notes',
    'show': 'updates a list of shows',
    'get face -name': "shows wikipedia image",
    'play -song': 'finds and reproduces songs',
    'yt l -url': 'download youtube video using url',
    'yt t -title': 'download youtube video using title',
    'mp3 l -url': 'download youtube mp3 using url',
    'mp3 t -title': 'download youtube mp3 using title',
    '! -cmd': 'enter any windows cli cmd',
    'music ls': 'shows music list'
}

def main():
    init(autoreset=True)
    banner = pyfiglet.figlet_format("CMDAssistant")
    print(Fore.CYAN + banner)

    while True:
        cmd_raw = input('C:/Users/PRossi>').strip()
        cmd = cmd_raw.lower()

        if cmd == "":
            # MENU
            os.system("cls")
            print(Fore.CYAN + banner)
            opcion = inquirer.select(
                message="¿Qué querés hacer?",
                choices=["Back", "Games", "Shows", "Add","System", "Help", "Reset","Exit"]
            ).execute()

            if opcion == "System":
                try:
                    while True:
                        os.system("cls")
                        print(Fore.CYAN + banner)
                        print(get_system_info())
                        print(f'Network: {get_network_usage()}')
                        time.sleep(1)
                except KeyboardInterrupt:
                    print("\nSaliendo del modo System.")           
 
            if opcion == "Games":
                juego = inquirer.select(
                message="Elegí un juego:",
                choices=[
                    "Skyrim",
                    "Far Cry 3",
                    "SAMP",
                    "↩ Volver"
                ]
                ).execute()

                if juego == "Skyrim":
                    subprocess.Popen([game_list['skyrim']])
                elif juego == "Far Cry 3":
                    subprocess.Popen([game_list['far cry']])
                elif juego == "SAMP":
                    subprocess.Popen([game_list['samp']])
                elif juego == "↩ Volver":
                    continue
 
            if opcion == "Shows":
                show = input('Show: ')
                episode = input('Episode: ')
                print(update_show(show, episode))             

            if opcion == "Add":
                document = inquirer.select(
                message="Elegí un Documento:",
                choices=[
                    "Movies",
                    "Cartoons",
                    "Books",
                    "Any", 
                    "↩ Volver"
                ]
                ).execute()

                if document == "Movies":
                    movie = input('Movie: ')
                    print(add('movie', movie))
                elif document == "Cartoons":
                    cartoon = input('Cartoon: ')
                    print(add('cartoon', cartoon))
                elif document == "↩ Volver":
                    continue
                elif document == "Any":
                    any = input('Any: ')
                    print(add('any', any))
                elif document == "↩ Volver":
                    continue 
                elif document == "Books":
                    book = input('Book: ')
                    print(add('book', book))
                elif document == "↩ Volver":
                    continue          

            elif opcion == "Back":
                os.system("cls")
                print(Fore.CYAN + banner)

            elif opcion == "Help":
                os.system("cls")
                print(Fore.CYAN + banner)
                print('\nComandos disponibles:')
                for k, v in command_list.items():
                    print(f"{k} -> {v}")

            elif opcion == "Exit":
                break

            elif opcion == "Reset":
                reset_program()
                
        elif cmd == "q":
            break
        
        elif cmd == "cls":
            os.system("cls")
            print(Fore.CYAN + banner)

        elif cmd == "help":
            print('\nComandos / Funciones')
            for k, v in command_list.items():
                print(f"{k} -> {v}")

        elif cmd in software_list:
            subprocess.Popen([software_list[cmd]])
            #os._exit(0)

        elif cmd in folder_list:
            os.system(f'start {folder_list[cmd]}')

        elif cmd.startswith('get face '):
            search = cmd[len('get face '):].strip()
            print(get_face(search))

        elif cmd == "reset":
            reset_program()

        elif cmd.startswith('!'):
            os.system(cmd[1:].strip())

        # Docs

        elif cmd == 'add':
            keyword = input('Keyword: ')
            result = input('Any list?: ')
            print(add(result, keyword))

        elif cmd in doc_list:
            os.system(f'start {doc_list[cmd]}')
            
        elif cmd == 'txt':
            a = search_for(input('Search:'))
            for e in a:
                print(e)

        # Games

        elif cmd in game_list:
            subprocess.Popen([game_list[cmd]])
            os._exit(0)  

        # USD

        elif cmd == 'usd':
            get_usd()

        # Music

        elif cmd.startswith('play '):
            query = cmd[len('play '):].strip().lower()
            play_music(query)
        
        elif cmd == 'music ls':
            for song in music_list.keys():
                print(song)

        # Movies / Shows

        elif cmd.startswith('info '):
            search = cmd[len('info '):].strip()
            info = movie_info(search)
            for a, b in info.items():
                print(f'{a}: {b}')

        elif cmd.startswith('add movie '):
                keyword = cmd[len('add movie '):].strip()
                print(add('movie', keyword))

        elif cmd == 'movie':
            while True:
                keyword= input('Search: ')
                if keyword == 'q':
                    break
                else: 
                    print(word_finder(keyword))

        elif cmd.startswith('movie '):
            keyword = cmd[len('movie '):].strip()
            print(word_finder(keyword))

        elif cmd == 'show':
            show = input('Show: ')
            episode = input('Episode: ')
            print(update_show(show, episode))

        # Download

        elif cmd.startswith('mp3 l '):
            url = cmd_raw[len('mp3 l '):].strip()
            mp3_url(url)

        elif cmd.startswith('mp3 t '):
            search = cmd_raw[len('mp3 t '):].strip()
            mp3_title(search)

        elif cmd.startswith('yt l '):
            url = cmd_raw[len('yt l '):].strip()
            video_url(url)

        elif cmd.startswith('yt t '):
            search = cmd_raw[len('yt t '):].strip()
            video_title(search)

        # System

        elif cmd == 'system':
            print(get_system_info())

        elif cmd == 'ram':
            print(get_memory_usage())

        elif cmd == 'disk':
            print(get_disk_usage())

        elif cmd == 'cpu':
            print(get_cpu_usage())

        elif cmd == 'system -a':
            print(get_cpu_usage())
            print(get_memory_usage())
            print(get_disk_usage())
            print(f'Network: {get_network_usage()}')

        elif cmd == 'net':
            print(f'Network: {get_network_usage()}')

if __name__ == '__main__':
    main()
