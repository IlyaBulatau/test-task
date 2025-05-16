from schemes import TaskScheme


def prepare_mytasks_answer(tasks: list[TaskScheme]) -> str:
    lines = []
    for task in tasks:
        lines.append(
            f"Задача #{task['id']}: {task['title']}\n"
            f"Описание: {task['description']}\n"
            f"Статус: {task['status']}\n"
            f"Дедлайн: {task['deadline']}\n"
            f"{'-' * 40}"
        )
    return "\n".join(lines)


def prepare_done_anwser(task: TaskScheme) -> str:
    return (
        f"Задача #{task['id']}: {task['title']}\n"
        f"Описание: {task['description']}\n"
        f"Статус: {task['status']}\n"
        f"Дедлайн: {task['deadline']}\n"
    )
