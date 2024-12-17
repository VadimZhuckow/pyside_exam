import psutil
from PySide6 import QtWidgets


class ProcessInfoWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QtWidgets.QVBoxLayout(self)
        self.process_table = QtWidgets.QTableWidget(self)
        self.process_table.setColumnCount(1)
        self.process_table.setHorizontalHeaderLabels(["Процесс"])
        self.layout.addWidget(self.process_table)

        self.update_processes()

    def update_processes(self):
        processes = []
        for proc in psutil.process_iter(['name']):
            # print(proc)
            processes.append(proc.info)

        self.process_table.setRowCount(len(processes))
        for row, process in enumerate(processes):
            self.process_table.setItem(row, 1, QtWidgets.QTableWidgetItem(process['name']))

        self.process_table.resizeColumnsToContents()
