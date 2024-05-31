import psutil
import logging
from time import sleep

# Setup logging
logging.basicConfig(filename='system_health.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Define thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 90

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f"High CPU usage detected: {cpu_usage}%")
    return cpu_usage

def check_memory_usage():
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f"High memory usage detected: {memory_usage}%")
    return memory_usage

def check_disk_usage():
    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info.percent
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f"High disk usage detected: {disk_usage}%")
    return disk_usage

def check_running_processes():
    processes = [(proc.pid, proc.info['name']) for proc in psutil.process_iter(['name'])]
    logging.info(f"Running processes: {processes}")
    return processes

def monitor_system():
    while True:
        check_cpu_usage()
        check_memory_usage()
        check_disk_usage()
        check_running_processes()
        sleep(60)  # Run the monitoring every 60 seconds

if __name__ == "__main__":
    monitor_system()