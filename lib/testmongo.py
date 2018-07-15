from lib.mongo import db

def items_in_collection():
  return db.test_collection.count()

# READ operation to return list of tasks from MongoDB
def get_todos():
  todolist = list(db.ToDoList.find({},{ '_id': 0 }))
  tasks = map(lambda x: x['task'], todolist)
  return tasks;

# CREATE operation to add new task to DB
def create_todo(new_todo):
  db.ToDoList.insert_one({'task': new_todo})

# def update_todo():

# def delete_todo():

