from ._anvil_designer import CoursesTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from ..CourseItem import CourseItem


class Courses(CoursesTemplate):
  def __init__(self, **properties):

  
    # Set Form properties and Data Bindings.
    self.init_components(**properties)    
    self.load_courses()
   
     # Any code you write here will run before the form opens.
  def load_courses(self):
    courses = anvil.server.call("get_course_details").search()
    course_panel = GridPanel()

    for i, course in enumerate(courses):
      c = CourseItem(name=course["name"], button_text=f"Purchase for ${course['price']}", description=course["description"], image=course["image"], button_callback=None)
    course_panel.add_component(c, row=str(i//2), width_xs=6)
  
    
    
   
   
    self.content_panel.add_component(course_panel)
    
      
   

  