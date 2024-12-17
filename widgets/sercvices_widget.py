import psutil
from PySide6 import QtWidgets


class ServiceInfoWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QtWidgets.QVBoxLayout(self)
        self.service_table = QtWidgets.QTableWidget(self)
        self.service_table.setColumnCount(2)
        self.service_table.setHorizontalHeaderLabels(["Имя службы", "Статус"])
        self.layout.addWidget(self.service_table)

        self.update_services()

    def update_services(self):
        services = []
        for service in psutil.win_service_iter():
            services.append({
                'name': service.name(),
                'status': service.status(),

            })

        self.service_table.setRowCount(len(services))
        for row, service in enumerate(services):
            self.service_table.setItem(row, 0, QtWidgets.QTableWidgetItem(service['name']))
            self.service_table.setItem(row, 1, QtWidgets.QTableWidgetItem(service['status']))

        self.service_table.resizeColumnsToContents()
