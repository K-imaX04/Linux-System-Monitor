import tkinter as tk
import psutil

# Functions
def get_cpu():
    return psutil.cpu_percent(interval=1)

def get_ram():
    return psutil.virtual_memory().percent

def get_disk():
    return psutil.disk_usage('/').percent

# Update UI
def update_stats():
    cpu_label.config(text=f"CPU Usage: {get_cpu()} %")
    ram_label.config(text=f"RAM Usage: {get_ram()} %")
    disk_label.config(text=f"Disk Usage: {get_disk()} %")
    
    root.after(1000, update_stats)  # refresh every 1s

# Window
root = tk.Tk()
root.title("Linux System Monitor")
root.geometry("400x200")

# Labels
title = tk.Label(root, text="🖥️ Linux System Monitor", font=("Arial", 16, "bold"))
title.pack(pady=10)

cpu_label = tk.Label(root, text="CPU Usage: ", font=("Arial", 12))
cpu_label.pack()

ram_label = tk.Label(root, text="RAM Usage: ", font=("Arial", 12))
ram_label.pack()

disk_label = tk.Label(root, text="Disk Usage: ", font=("Arial", 12))
disk_label.pack()

# Start updating
update_stats()

# Run GUI
root.mainloop()
