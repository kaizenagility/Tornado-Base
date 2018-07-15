"""
example of querying to a mongo instance
"""

from lib.mongo import db

def items_in_collection():
  return db.test_collection.count()

# Troubleshooting with findOne() method instead of iterating through find()

def get_todos():
  todolist = list(db.ToDoList.find({},{ '_id': 0 }))
  tasks = map(lambda x: x['task'], todolist)
  return tasks;

