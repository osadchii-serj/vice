from real_task_manager import RealTaskManager

from logger import TaskManagerLogger

from interface import TaskManager

from dataclasses import dataclass

import datetime


@dataclass
class LoggingTaskManager(TaskManager):

    real_task_manager: RealTaskManager
    task_logger: TaskManagerLogger

    def assign_task(self, employee, task):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.task_logger.log_info(
            f"Задача: '{task}' сотрудник: {employee}"
        )
        print(f"[{timestamp}] Начало задачи: '{task}' сотрудник: {employee}")
        status = self.real_task_manager.assign_task(employee, task)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.task_logger.log_info(f"Задача '{task}' успешно назначена")
        print(f"[{timestamp}] Задача '{task}' успешно назначена")

    def get_task_status(self, task):
        status = self.real_task_manager.get_task_status(task)
        self.task_logger.log_info(f"Запрос статуса задачи '{task}'")
        self.task_logger.log_info(f"Статус задачи '{task}': {status}")
        return status


if __name__ == "__main__":
    real_task_manager = RealTaskManager()
    task_logger = TaskManagerLogger("LoggingTaskManager")
    logging_manager = LoggingTaskManager(real_task_manager, task_logger)
    logging_manager.assign_task("Иван", "Подготовить отчет")
    print(logging_manager.get_task_status("Подготовить отчет"))
