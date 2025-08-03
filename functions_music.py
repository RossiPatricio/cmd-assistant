import os

music_folder = r'C:\Users\PRossi\Music'
movie_list = r'C:\Users\PRossi\documents-backup\Lists\Movies.txt'

music_list = {}

for filename in os.listdir(music_folder):
    if filename.endswith(('.mp3', '.wav', '.flac')):
        name = os.path.splitext(filename)[0].lower()
        path = os.path.join(music_folder, filename)
        music_list[name] = path

def play_music(query):
    matches = [name for name in music_list if query in name]
    
    if matches:
        if len(matches) == 1:
            selected = matches[0]
            print(f'Reproduciendo: {selected.title()}')
            os.startfile(music_list[selected])
        elif len(matches) >= 2:
            ls= {}
            for i, song in enumerate(matches, start=1):
                ls[i] = song
                print(f'{i}- {song}')
            number = int(input("Select:"))
            print(f'Reproduciendo: {ls[number]}')
            os.startfile(music_list[ls[number]])
        else:
            print('Canción no encontrada.')
