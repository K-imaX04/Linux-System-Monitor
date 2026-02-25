import psutil

def cpu():
    return psutil.cpu_percent(interval=0.5)

def ram():
    memory = psutil.virtual_memory()
    return memory.percent

def disk():
    Disk = psutil.disk_usage('/')
    return Disk.percent
