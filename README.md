# 🚀 ProcCtrl
A minimal and efficient Linux process manager built with Python.

## 🛠 Features
- List all running processes with PID, CPU usage, and memory usage.
- Sort processes by CPU or Memory usage (optional).
- Lightweight & fast – Runs smoothly on Linux.
- Simple CLI interface using argparse.

## 📦 Installation
Make sure to install python3 and requirements.txt

### 1. Clone the repository
```sh
git clone https://github.com/selfxiron/procctrl.git
cd procctrl
```
### 2. Install the dependencies
```sh
pip install -r requirements.txt
```
### 3. Run the procgram
Run the script with different options.
1. List all running processes (unsorted)
```sh
python procctrl.py
```
2. List all running processes sorted by memory usage
```sh
python procctrl.py --sort memory
```
3. List all running processes sorted by CPU usage
```sh
python procctrl.py --sort cpu
```

## 🤝 Contributing 
Feel free to fork this project and submit pull requests for improvements!

## 📜 License
This project is open-source and free to use.
