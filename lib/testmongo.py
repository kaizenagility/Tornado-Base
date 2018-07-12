"""
example of querying to a mongo instance
"""

from lib.mongo import db

def items_in_collection():
  return db.test_collection.count()

# Troubleshooting with findOne() method instead of iterating through find()

def get_todos():
  return db.ToDoList.findOne();

