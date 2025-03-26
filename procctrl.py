import psutil

def list_processes():
    print(f"{'PID':<10} {'Name':<25} {'CPU':<10} {'Memory%'}")
    print("="*55)

    for process in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        pid = process.info['pid']
        name = process.info['name']
        cpu = process.info['cpu_percent']
        mem = process.info['memory_percent']
        print(f"{pid:<10} {name:<25} {cpu:<10} {mem:.2f}%")

if __name__ == "__main__":
    list_processes()