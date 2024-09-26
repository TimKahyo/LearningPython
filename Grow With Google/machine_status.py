from cpu_usage import check_cpu_usage, is_the_cpu_okay
from DiskUsage import DiskUsage


disk_checker = DiskUsage("/") 
disk_checker.check_disk_usage()

print()
check_cpu_usage()

print()

if disk_checker.is_the_space_critical() or not is_the_cpu_okay():
    print("Something Wrong With the Computer")
else:
    print("Everything is Okay!")