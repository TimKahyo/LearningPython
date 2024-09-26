import shutil

class DiskUsage:  # Keep class name as DiskUsage
    def __init__(self, disk):
        self.disk = disk
        self.du = shutil.disk_usage(self.disk)

    def check_disk_usage(self):
        print(f"Total space: {self.du.total / (1024**3):.2f} GB")
        print(f"Space used : {self.du.used / (1024**3):.2f} GB")
        print(f"Space free : {self.du.free / (1024**3):.2f} GB")
        print(" ")
        print("Free space: %.2f%% of total." % (self.du.free/self.du.total * 100))
        print("Used space: %.2f%% of total." % (self.du.used/self.du.total * 100))

    def is_the_space_critical(self):
        return self.du.free < (20 * 1024**3)
