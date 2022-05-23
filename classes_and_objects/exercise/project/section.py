from task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task.name in [x.name for x in self.tasks]:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {''.join([f'{d}' for d in Task.details(new_task)])} is added to the section"

    def complete_task(self, task_name: str):
        if task_name not in [x.name for x in self.tasks]:
            Task.completed = False
            return f"Could not find task with the name {task_name}"
        Task.completed = True
        return f"Completed task {task_name}"

    def clean_section(self):
        completed_tasks_counter = 0
        for current_task in self.tasks:
            if current_task.completed:
                completed_tasks_counter += 1
                self.tasks.remove(current_task)
        return f"Cleared {completed_tasks_counter} tasks."

    def view_section(self):
        result = ""
        result += f"Section {self.name}:\n"
        for x in self.tasks:
            result += "".join([f'{d}' for d in Task.details(x)])
            result += "\n"
        return result.strip()


# task = Task("Tst", "27.04.2020")
# print(task.change_name("Tst"))
# print(task.change_name("Tst"))
# print(task.change_due_date("28.05.2020"))
# task.add_comment("Don't forget laptop")
# print(task.edit_comment(0, "Don't forget laptop and notebook"))
# print(task.details())
# task = Task("Tst", "27.04.2020")
# section = Section("New section")
# print(section.add_task(task))
# print(section.complete_task("Tst"))
# print(section.add_task(task))
# print(section.clean_section())
# print(section.view_section())


