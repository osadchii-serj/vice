from interface import TaskManager

from dataclasses import dataclass


@dataclass
class RealTaskManager(TaskManager):

    tasks = {}

    def assign_task(self, employee, task):
        self.tasks[task] = {"employee": employee, "status": "Assigned"}
        print(f"Задача '{task}' назначена сотруднику {employee}")

    def get_task_status(self, task):
        return self.tasks.get(task, {}).get("status", "Задача не найдена")


if __name__ == "__main__":
    real_manager = RealTaskManager()
    real_manager.assign_task("Иван", "Подготовить отчет")
    print(real_manager.tasks)
    print(real_manager.get_task_status("Подготовить отчет"))
