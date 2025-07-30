import os, subprocess
from functions import *

software_list = {
    'vscode' : r'C:\Users\PRossi\AppData\Local\Programs\Microsoft VS Code\Code.exe',
}

game_list = {
    'skyrim' : r'C:\Archivos\The Elder Scrolls V Skyrim Legendary Edition\Skyrim.exe',
    'samp' : r'C:\Archivos\ASD+\samp.exe'
}

folder_list = {
    'docs' : 'C:/Users/PRossi/documents-backup',
    'lists' : 'C:/Users/PRossi/documents-backup/lists'
}

list_list= {
    'movies': 'C:\\Users\\PRossi\\documents-backup\\Lists\\Movies.txt',
    'cartoons': 'C:\\Users\\PRossi\\documents-backup\\Lists\\Cartoons.txt',
    'shows': 'C:\\Users\\PRossi\\documents-backup\\Lists\\Shows.txt',
    'actors': 'C:\\Users\\PRossi\\documents-backup\\Lists\\Actors.txt',
    'games': 'C:\\Users\\PRossi\\documents-backup\\Lists\\Games.txt'
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
}

def main():
    print('Command-Line Assistant')
    print('Type -help- for cmds')
    while True:
        cmd = input('C:/Users/PRossi>').strip().lower()

        if cmd == 'q':
            break

        if cmd == 'help':
            print()
            print('Actions:')
            for command, use in command_list.items():
                print(f'{command}: {use}')
            print()

        if cmd == 'cls':
            os.system('cls')

        if cmd in list_list:
            os.system(f'type {list_list[cmd]}')

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
            
        if cmd in software_list:
            subprocess.Popen([software_list[cmd]])
            os._exit(0)

        if cmd in game_list:
            subprocess.Popen([game_list[cmd]])
            os._exit(0)

        if cmd in folder_list:
            os.system(f'start {folder_list[cmd]}')
            os._exit(0)

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

if __name__ == '__main__':
    main()
