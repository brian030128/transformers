
memory_metrics = []
time_metrics = []

def clear():
    memory_metrics = []
    time_metrics = []

import time
import GPUtil

def get_gpu_usage():
    gpus = GPUtil.getGPUs()
    total = 0
    for gpu in gpus:
        total += gpu.memoryUsed
    return total


def measure():
    memory_metrics.append(get_gpu_usage())
    time_metrics.append(time.time())