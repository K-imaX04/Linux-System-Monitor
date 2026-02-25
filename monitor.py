import psutil

def cpu():
    return psutil.cpu_percent(interval=0.5)

def ram():
    memory = psutil.virtual_memory()
    return memory.percent

def disk():
    Disk = psutil.disk_usage('/')
    return Disk.percent

def top_processes(limit=5):
    processes = []

    for p in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            processes.append(p.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    # Sort by CPU usage
    processes.sort(key=lambda p: p['cpu_percent'], reverse=True)

    return processes[:limit]
