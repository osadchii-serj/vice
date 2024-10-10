from real_task_manager import RealTaskManager

from interface import TaskManager

from dataclasses import dataclass

from icecream import ic

import datetime


@dataclass
class LoggingTaskManager(TaskManager):

    real_task_manager: RealTaskManager

    def assign_task(self, employee, task):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] Начало назначения задачи {task} сотруднику {employee}")

        status = self.real_task_manager.assign_task(employee, task)

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] Задача '{task}' успешно назначена")

    def get_task_status(self, task):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status = self.real_task_manager.get_task_status(task)
        return status


if __name__ == "__main__":
    logging_manager = LoggingTaskManager(RealTaskManager())
    logging_manager.assign_task("Иван", "Подготовить отчет")
    print(logging_manager.get_task_status("Подготовить отчет"))
