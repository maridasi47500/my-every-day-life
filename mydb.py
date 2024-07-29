from country import Country
from user import User
from job import Job
from pics import Pics
class Mydb():
  def __init__(self):
    print("hello")
    self.Country=Country()
    self.User=User()
    self.Job=Job()
    self.Pics=Pics()
