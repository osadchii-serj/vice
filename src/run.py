from logging_task_manager import LoggingTaskManager
from real_task_manager import RealTaskManager
from logger import TaskManagerLogger
from interface import TaskManager


def client_code(vice: LoggingTaskManager, employee: str, task: str):
    vice.assign_task(employee, task)
    vice.get_task_status(task)


if __name__ == "__main__":
    real_task = RealTaskManager()
    logging_task = TaskManagerLogger("TaskManagerLogger")
    logging_task = LoggingTaskManager(real_task, logging_task)
    client_code(logging_task, "Иванов Иван", "Подготовить отчет")
    client_code(logging_task, "Петрова Мария", "Провести встречу")
