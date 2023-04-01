class Person:
  age = 13
  height = 172.5
  isMale = True
  name = "Sasha"

  def __init__(self, name, age):
    self.name = name
    self.age = age
    




  
me = Person()
friend = Person()

friend.age = 15
friend.height = 100
print (friend.height)
print (friend.age)