from ._anvil_designer import BaseTemplate
from anvil import *
from ..Home import Home
from ..MyCourses import MyCourses 


class Base(BaseTemplate):
  def __init__(self, **properties):
    self.content_panel.add_component(Home()) 
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def my_courses_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component (MyCourses())

  def title_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component (Home())
    
