import os, time
from functions import *
from system import *

def main():
    print('Command-Line Assistant')
    print('Type -help- for cmds')
    while True:
        cmd = input('C:/user>').strip().lower()

        if cmd == 'q':
            break

        if cmd == 'help':
            commands = {
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
            }
            print()
            print('Actions:')
            print()
            for command, use in commands.items():
                print(f'{command}: {use}')
            print()

        if cmd == 'cls':
            os.system('cls')

        if cmd == 'add':
            keyword = input('Keyword: ')
            result = input('Any list?: ')
            print(add(result, keyword))

        if cmd.startswith('add movie '):
                keyword = cmd[len('add movie '):].strip()
                print(add('movie', keyword))

        if cmd == 'movie':
            while True:
                keyword= input('Search: ')
                if keyword == 'q':
                    break
                else: 
                    print(word_finder(keyword))

        if cmd.startswith('movie '):
            keyword = cmd[len('movie '):].strip()
            print(word_finder(keyword))

        if cmd == 'show':
            show = input('Show: ')
            episode = input('Episode: ')
            print(update_show(show, episode))
            
        software_list = {
            'vscode' : r"C:\Users\PRossi\AppData\Local\Programs\Microsoft VS Code\Code.exe",
        }
        
        game_list = {
            'skyrim' : r"C:\Archivos\The Elder Scrolls V Skyrim Legendary Edition\Skyrim.exe",
        }
        
        if cmd in software_list:
            open_software(software_list[cmd])

        if cmd in game_list:
            open_software(game_list[cmd])

        if cmd.startswith('get face '):
            search = cmd[len('get face '):].strip()
            print(get_face(search))
            

        # System

        if cmd == 'system':
            print(get_system_info())

        if cmd == 'ram':
            print(get_memory_usage())

        if cmd == 'disk':
            print(get_disk_usage())

        if cmd == 'cpu':
            print(get_cpu_usage())

        if cmd == 'system -a':
            print(get_cpu_usage())
            print(get_memory_usage())
            print(get_disk_usage())
            print(f'Network: {get_network_usage()}')

        if cmd == 'net':
            print(f'Network: {get_network_usage()}')

        # Folders

        if cmd == 'help folders':
            commands = {
                'docs': 'Documentos',
                'lists': 'Lists'}
            print()
            for command, use in commands.items():
                print(f'{command}: {use}')
            print()

        folders = {
            'docs' : 'C:/Users/PRossi/documents-backup',
            'lists' : 'C:/Users/PRossi/documents-backup/lists'}

        if cmd in folders.keys():
            os.system(f'start {folders[cmd]}')

        # Download

        if cmd.startswith('download game '):
            gamezfull = 'https://www.gamezfull.com/?s='
            zonaleros = 'https://www.zona-leros.com/search?q='
            search = cmd[len('download game '):].strip()
            title = search.split(' ')
            game = ('+').join(title)
            print(f'Gamezfull: {gamezfull+game}')
            print(f'Zona-Leros: {zonaleros+game}')

        if cmd == 'help download':
            commands = {
                'download game -title-': 'Gamess',
                'download song/album -title-': 'Music',
                'download movie -title-': 'Movies'}
            print()
            for command, use in commands.items():
                print(f'{command}: {use}')
            print()   

        # Watch

        if cmd.startswith('watch movie '):
            return f'Searching {cmd}'

if __name__ == '__main__':
    main()
