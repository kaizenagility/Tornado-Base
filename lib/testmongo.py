from lib.mongo import db
from bson.objectid import ObjectId

def items_in_collection():
  return db.test_collection.count()

# READ operation to return list of tasks from MongoDB
def get_todos():
  todolist = list(db.ToDoList.find({}))
  # tasks = map(lambda x: x['task'], todolist)
  return todolist;

# CREATE operation to add new task to DB
def create_todo(new_todo):
  db.ToDoList.insert_one({'task': new_todo})

# DELETE operation
def delete_todo(remove_todo):
  try:
    id = ObjectId(remove_todo)
    db.ToDoList.delete_one({'_id': id})
    print "Deleted from database."
  except:
    print "Failed at Model step."

# UPDATE operation
def update_todo(update_todo, new_todo):
  try:
    id = ObjectId(update_todo_todo)
    db.ToDoList.update_one({'_id': id, 'task': new_todo})
    print "Updated database."
  except:
    print "Failed at Model step."