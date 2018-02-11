class Circle():
  
  pi = 3.14
  
  def __init__(self,radius=1):
    self.radius = radius
  def area(self):
    return self.radius * self.radius * Circle.pi
    
    
class Book():
  
  def __init__(self,title,author,pages):
    self.title = title
    self.author = author
    self.pages = pages
  def __str__(self):
    return 'Title is {} and Author is {}'.format(self.title,self.author)
    
  def __len__(self):
    return self.pages
    
  def __del__(self):
    print('Book has been deleted.')
