import app.basic

from lib import testmongo

class NotFound(app.basic.BaseHandler):

  def get(self):
    """
    quick example of rendering html template
    """
    self.render('page_not_found.html')

class TestMongo(app.basic.BaseHandler):

  def get(self):
    """
    quick example of communicating with Mongo
    """
    items_in_collection = testmongo.items_in_collection()
    self.api_response(items_in_collection)

class ToDo(app.basic.BaseHandler):

  def get(self):
    to_do_list = testmongo.get_todos() 
    self.render('todo.html', todos = to_do_list)
  
  def post(self):
    try:
      print "Adding new todo"
      new_todo = self.get_argument("new_todo")
      if not new_todo:
        return self.write({"success":False})
      testmongo.create_todo(new_todo)
      self.write({"success":True})
      # self.render('todo.html')
    except:
      self.write({"success":False})


class ToDoDelete(app.basic.BaseHandler):

  def post(self):
    try:
      print "Deleting task"
      remove_todo = self.get_argument("remove_todo")
      testmongo.delete_todo(remove_todo)
      self.write({"success":True})
    except:
      self.write({"success":False})


class ToDoUpdate(app.basic.BaseHandler):

  def post(self):
    try:
      print "Updating task"
      update_todo = self.get_argument("update_todo")
      testmongo.update_todo(update_todo)
      self.write({"success":True})
    except:
      self.write({"success":False})