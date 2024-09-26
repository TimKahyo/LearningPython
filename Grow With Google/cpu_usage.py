import psutil 

def check_cpu_usage():
    for i in range(10):
        # percentage per n seconds
        print(psutil.cpu_percent(0.1))
        
def is_the_cpu_okay():
    usage = psutil.cpu_percent(1)
    return usage < 75

