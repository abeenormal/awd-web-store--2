from ._anvil_designer import BaseTemplate
from anvil import *
import stripe.checkout
import anvil.server
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
  
    
    
   

    # Set Form properties and Data Bindings.

    self.init_components(**properties)
   
   

  
    
    
    self.content_panel.add_component(Home())

  



# Any code you write here will run before the form opens.

  def change_sign_in_text(self):
      user = anvil.users.get_user()
      if user:
        email = user["email"]
        self.sign_in.text = email
      else:
        self.sign_in.text = "Sign in" 

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
    self.change_sign_in_text()
    self.update_login_ui()
    
  def log_out_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.logout()
    anvil.open_form('Base')

  def update_login_ui(self):
    user = anvil.users.get_user()
    if user:
     self.log_out_button.visible = True 
     self.my_course.visible = True
     self.sign_in.visible = False
    else:
     self.log_out_button.visible = False
     

  def my_course_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(MyCourses())
    

 
    







