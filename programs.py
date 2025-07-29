
def open_software(name):
    software = {
    'vscode' : r"C:\Users\PRossi\AppData\Local\Programs\Microsoft VS Code\Code.exe",
    }
    path = software[name]
    subprocess.Popen([path], shell=True)
    os._exit(0)
     
     
     








