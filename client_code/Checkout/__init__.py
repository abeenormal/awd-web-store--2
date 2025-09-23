from ._anvil_designer import CheckoutTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import stripe


class Checkout(CheckoutTemplate):
  def __init__(self,id_name, **properties):

    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.update_form('id_name')
    
    





    # Any code you write here will run before the form opens.


  def update_form(self,id_name):
    course = anvil.server.call('get_course_details')
    self.name_label.content = course['id_name']
    self.description_label.text = course['description']
    self.price_label.text = f"${course['price']} USD"
    self.image_content.source = course['image'] 
    

  def buy_click(self, **event_args):
    """This method is called when the button is clicked"""
    user = anvil.users.get_user()
    stripe.checkout.charge()
    token, info=stripe.checkout.get_token(amount= self.course["price"]*100, currency="USD",title=self.course["name"], description=self.course["description"])
    try:
      anvil.server.call("charge_user", token, user["email"], self.course["id_name"])
      alert("Success")
    except Exception as e:
      alert(str(e))

  def back_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.button_callback()
