from main import movie_list

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
        'python': r'C:\Users\PRossi\documents-backup\Python.txt',
        'cartoon': r'C:\Users\PRossi\documents-backup\Lists\Cartoons.txt',
        'cartoons': r'C:\Users\PRossi\documents-backup\Lists\Cartoons.txt',
        'book': r'C:\Users\PRossi\documents-backup\Lists\Books.txt',
        'books': r'C:\Users\PRossi\documents-backup\Lists\Books.txt',
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