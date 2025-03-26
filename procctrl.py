import psutil
import argparse

def list_processes():
    """List all running processes without sorting."""
    print(f"{'PID':<10} {'Name':<25} {'CPU%':<10} {'Memory%'}")
    print("="*56)

    for process in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        print(f"{process.info['pid']:<10} {process.info['name']:<25} {process.info['cpu_percent']:<10} {process.info['memory_percent']:.2f}%")

def list_processes_sorted_by_memory():
    """List processes sorted by memory usage (highest first)."""
    processes = [p.info for p in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent'])]
    processes.sort(key=lambda p: p['memory_percent'], reverse=True)

    print(f"{'PID':<10} {'Name':<25} {'CPU%':<10} {'Memory%'}")
    print("="*56)

    for process in processes:
        print(f"{process['pid']:<10} {process['name']:<25} {process['cpu_percent']:<10} {process['memory_percent']:.2f}%")

def list_processes_sorted_by_cpu():
    """List processes sorted by CPU usage (highest first)."""
    processes = [p.info for p in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent'])]
    processes.sort(key=lambda p: p['cpu_percent'], reverse=True)

    print(f"{'PID':<10} {'Name':<25} {'CPU%':<10} {'Memory%'}")
    print("="*56)

    for process in processes:
        print(f"{process['pid']:<10} {process['name']:<25} {process['cpu_percent']:<10} {process['memory_percent']:.2f}%")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ProcCtrl - Linux Process Manager")
    parser.add_argument("--sort", choices=['cpu', 'memory'], help="Sort processes by 'cpu' or 'memory'. If omitted, shows unsorted list.")

    args = parser.parse_args()

    if args.sort == "cpu":
        list_processes_sorted_by_cpu()
    elif args.sort == "memory":
        list_processes_sorted_by_memory()
    else:
        list_processes()
