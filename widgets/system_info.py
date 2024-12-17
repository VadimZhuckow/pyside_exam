import psutil
import platform

from PySide6 import QtCore


class SystemInfo(QtCore.QThread):
    systemInfoReceived = QtCore.Signal(tuple)

    def __init__(self):
        super().__init__()
        self.delay = 1

    def run(self):
        while True:
            cpu_load = psutil.cpu_percent(interval=self.delay)
            cpu_name = platform.processor()
            cpu_count = psutil.cpu_count()
            ram = psutil.virtual_memory()
            ram_load = ram.percent
            disk_info = self.get_disk_info()

            self.systemInfoReceived.emit((cpu_name, cpu_load, ram, ram_load, disk_info))

    def get_disk_info(self):
        disk_info = []
        disks = psutil.disk_partitions()
        for d in disks:
            usage = psutil.disk_usage(d.mountpoint)
            disk_info.append({
                'device': d.device,
                'total': usage.total / (1024 ** 3),
                'used': usage.used / (1024 ** 3),
            })
        return disk_info
