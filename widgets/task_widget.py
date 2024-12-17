import win32com.client
from PySide6 import QtWidgets


class TaskSchedulerWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QtWidgets.QVBoxLayout(self)
        self.task_table = QtWidgets.QTableWidget(self)
        self.task_table.setColumnCount(2)
        self.task_table.setHorizontalHeaderLabels(["Имя задачи", "Следующее выполнение"])
        self.layout.addWidget(self.task_table)

        self.update_tasks()

    def update_tasks(self):
        scheduler = win32com.client.Dispatch("Schedule.Service")
        scheduler.Connect()

        tasks = scheduler.GetFolder("\\").GetTasks(0)
        task_list = []
        for task in tasks:
            task_list.append({
                'name': task.Name,
                'next_run': task.NextRunTime
            })

        self.task_table.setRowCount(len(task_list))
        for row, task in enumerate(task_list):
            self.task_table.setItem(row, 0, QtWidgets.QTableWidgetItem(task['name']))
            self.task_table.setItem(row, 1, QtWidgets.QTableWidgetItem(str(task['next_run'])))

        self.task_table.resizeColumnsToContents()
