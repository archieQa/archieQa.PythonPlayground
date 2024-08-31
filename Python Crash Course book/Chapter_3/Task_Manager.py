tasks = ['Read book', 'Exercise', 'Code']

tasks.insert(0, 'Push-ups')
tasks.append("Pull-ups")

print(sorted(tasks, reverse=False))
print(sorted(tasks, reverse=True))

completed_task = tasks.pop(2)

print(f"Completed task is: {completed_task} \n")

print('Remaining Tasks are:')
for index, task in enumerate(tasks, start=1):
    print(f'{index} - {task}')