from ._anvil_designer import BaseTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from ..Home import Home
from ..MyCourses import MyCourses 

class Base(BaseTemplate):
  def __init__(self, **properties):

    user = anvil.users.get_user()
    if user:
      self.sign_in.text = f"Welcome, {user[email]}"
      self.log_out_button.visible = True

   

    # Set Form properties and Data Bindings.

    self.init_components(**properties) 

  
    
    
    self.content_panel.add_component(Home())

  



# Any code you write here will run before the form opens.

    

  def go_to_home(self):
    """This method is called """
    self.content_panel.clear()
    self.content_panel.add_component(Home())

  def title_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.go_to_home()

  def sign_in_click(self, **event_args):
    """This method is called when the link is clicked"""
    anvil.users.login_with_form()
    
  def log_out_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.logout()
    anvil.open_form('Base')
    







