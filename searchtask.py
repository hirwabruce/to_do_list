from addtask import tasks

def search_tasks(query):
    return [task for task in tasks if query.lower() in task['name'].lower()]