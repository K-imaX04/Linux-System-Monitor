from rich.console import Console
from rich.table import Table
from rich.live import Live
import time
from monitor import top_processes

console = Console()

def generate_process_table():
    table = Table(title="🔥 Top Running Processes")

    table.add_column("PID", style="cyan")
    table.add_column("Name", style="magenta")
    table.add_column("CPU %", style="green")
    table.add_column("RAM %", style="yellow")

    for p in top_processes():
        table.add_row(
            str(p["pid"]),
            p["name"][:15],
            f"{p['cpu_percent']}",
            f"{p['memory_percent']:.2f}"
        )

    return table

with Live(generate_process_table(), refresh_per_second=1) as live:
    while True:
        time.sleep(1)
        live.update(generate_process_table())
