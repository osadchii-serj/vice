from abc import ABC, abstractmethod


class TaskManager(ABC):

    @abstractmethod
    def assign_task(self, employee, task):
        pass

    @abstractmethod
    def get_task_status(self, task):
        pass
