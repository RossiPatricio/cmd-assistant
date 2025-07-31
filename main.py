import pyfiglet
from InquirerPy import inquirer
from functions import *
import os, subprocess
from colorama import init, Fore, Style

list_folder = r'C:\Users\PRossi\documents-backup\Lists'
music_folder = r'C:\Users\PRossi\Music'
movie_list = r'C:\Users\PRossi\documents-backup\Lists\Movies.txt'

software_list = {
    'vscode' : r'C:\Users\PRossi\AppData\Local\Programs\Microsoft VS Code\Code.exe',
}

game_list = {
    'skyrim' : r'C:\Archivos\The Elder Scrolls V Skyrim Legendary Edition\Skyrim.exe',
    'samp' : r'C:\Archivos\ASD+\samp.exe',
}

folder_list = {
    #
    'docs' : r'C:/Users/PRossi/documents-backup',
    'lists' : r'C:/Users/PRossi/documents-backup/lists',
}

doc_list= {
    'movies': movie_list,
    'cartoons': fr'{list_folder}\Cartoons.txt',
    'shows': fr'{list_folder}\Shows.txt',
    'actors': fr'{list_folder}\Actors.txt',
    'games': fr'{list_folder}\Games.txt',
}

command_list = {
    'q': 'exit',
    'cls': 'clear',
    'system': 'system info',
    'system -a': 'full system info',
    "ram-disk-cpu": 'hardware info',
    'help folders': 'folder list',
    'movie' : 'is movie in list?',
    'add' : 'add notes',
    'show': 'updates a list of shows',
    'get face -name': "shows wikipedia image",
    'play -song': "..."
}

def main():
    init(autoreset=True)
    banner = pyfiglet.figlet_format("CMDAssistant")
    print(Fore.CYAN + banner)

    while True:
        cmd = input('C:/Users/PRossi>').lower()

        if cmd == "":
            os.system("cls")
            print(Fore.CYAN + banner)
            opcion = inquirer.select(
                message="¿Qué querés hacer?",
                choices=["Back", "Games", "System", "Help", "Exit"]
            ).execute()

            if opcion == "System":
                print(get_system_info())
                
            if opcion == "Games":
                juego = inquirer.select(
                message="Elegí un juego:",
                choices=[
                    "Skyrim",
                    "SAMP",
                    "↩ Volver"
                ]
                ).execute()

                if juego == "Skyrim":
                    subprocess.Popen([game_list['skyrim']])
                elif juego == "SAMP":
                    subprocess.Popen([game_list['samp']])
                elif juego == "↩ Volver":
                    continue
                
            elif opcion == "Back":
                os.system("cls")
                print(Fore.CYAN + banner)
                
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

        elif cmd == "q":
            break
        
        elif cmd == "cls":
            os.system("cls")
            print(Fore.CYAN + banner)
            
        elif cmd == "help":
            print('\nComandos disponibles:')
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

        # DOCS 
        
        elif cmd == 'add':
            keyword = input('Keyword: ')
            result = input('Any list?: ')
            print(add(result, keyword))

        elif cmd in doc_list:
            os.system(f'type {doc_list[cmd]}')

        # Games

        elif cmd in game_list:
            subprocess.Popen([game_list[cmd]])
            os._exit(0)  
            
        # Music
        
        elif cmd.startswith('play '):
            query = cmd[len('play '):].strip().lower()

            # Búsqueda parcial
            matches = [name for name in music_list if query in name]
            
            if matches:
                # Si hay varias, elegí la primera
                selected = matches[0]
                print(f'Reproduciendo: {selected.title()}')
                os.startfile(music_list[selected])
            else:
                print('Canción no encontrada.')

        # Movies / Shows
        
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

        # System
        
        elif cmd.startswith('!'):
            os.system(cmd[1:].strip())

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