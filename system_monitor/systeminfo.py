import psutil
import time
from rich.console import Console
from rich.table import Table

def get_system_info():
    info = {}
    info['CPU Usage'] = f"{psutil.cpu_percent(interval=1)}%"
    info['Memory Usage'] = f"{psutil.virtual_memory().percent}%"
    info['Disk Usage'] = f"{psutil.disk_usage('/').percent}%"
    info['Network Sent'] = f"{psutil.net_io_counters().bytes_sent / (1024 * 1024):.2f} MB"
    info['Network Received'] = f"{psutil.net_io_counters().bytes_recv / (1024 * 1024):.2f} MB"
    return info

def display_system_info():
    console = Console()
    while True:
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Metric", style="dim")
        table.add_column("Value")

        system_info = get_system_info()
        for key, value in system_info.items():
            table.add_row(key, value)

        console.clear()
        console.print(table)
        time.sleep(2)

if __name__ == "__main__":
    display_system_info()

