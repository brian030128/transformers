
memory_metrics = []
time_metrics = []

def clear():
    global memory_metrics, time_metrics
    memory_metrics = []
    time_metrics = []

import time
import GPUtil
import torch
def get_gpu_usage():
    gpus = GPUtil.getGPUs()
    total = 0
    for gpu in gpus:
        total += (torch.cuda.memory_allocated(device=gpu.id) / 1000000) 

    return total


def measure():
    memory_metrics.append(get_gpu_usage())
    time_metrics.append(time.time())