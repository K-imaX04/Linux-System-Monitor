from rich.console import Console
from rich.progress import BarColumn, Progress, TextColumn
from rich.live import Live
from rich.table import Table
import time
from monitor import cpu, ram, disk

console = Console()

def generate_table():
    table = Table(title="🖥️ Linux System Monitor")

    table.add_column("Resource", style="cyan")
    table.add_column("Usage", style="magenta")
    table.add_column("Bar")

    c = cpu()
    r = ram()
    d = disk()

    table.add_row("CPU", f"{c}%", f"[green]{'█'*int(c/5)}[/]")
    table.add_row("RAM", f"{r}%", f"[yellow]{'█'*int(r/5)}[/]")
    table.add_row("Disk", f"{d}%", f"[red]{'█'*int(d/5)}[/]")

    return table

with Live(generate_table(), refresh_per_second=1) as live:
    while True:
        time.sleep(1)
        live.update(generate_table())
