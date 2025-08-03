import psutil, os, sys

def reset_program():
    os.system("cls")
    print("Reseting..\n")
    python = sys.executable
    os.execl(python, python, *sys.argv)

def get_system_info():
    """ Devuelve información general del sistema. """
    info = {
        'CPU Cores': psutil.cpu_count(logical=True),
        'CPU Frequency': f"{psutil.cpu_freq().current:.2f} MHz",
        'Total Memory': f"{psutil.virtual_memory().total / (1024**3):.2f} GB",
        'Disk Total': f"{psutil.disk_usage('/').total / (1024**3):.2f} GB",
    }
    return '\n'.join([f"{key}: {value}" for key, value in info.items()])

def get_cpu_usage():
    """ Devuelve el porcentaje de uso de CPU. """
    return f"CPU Usage: {psutil.cpu_percent(interval=1)}%"

def get_memory_usage():
    """ Devuelve el uso de memoria RAM. """
    memory = psutil.virtual_memory()
    return f"Memory Usage: {memory.percent}% ({memory.used / (1024**3):.2f} GB / {memory.total / (1024**3):.2f} GB)"

def get_disk_usage():
    """ Devuelve el uso del disco duro. """
    disk = psutil.disk_usage('/')
    return f"Disk Usage: {disk.percent}% ({disk.used / (1024**3):.2f} GB / {disk.total / (1024**3):.2f} GB)"

def get_network_usage():
    counters = psutil.net_io_counters()
    sent = counters.bytes_sent
    recv = counters.bytes_recv
    return f"Enviados: {sent/1024/1024:.2f} MB  Recibidos: {recv/1024/1024:.2f} MB"
