import time
class Person:
    
  age = 13
  height = 172.5
  isMale = True
  money = 0
  name = "Sasha"

  def __init__(self, name, age, height, isMale):
    self.name = name
    self.age = age
    self.height = height
    self.isMale = isMale
    
  def work(self, days):
    while days != 0:
     time.sleep(1)
     self.money += 50
     days -= 1
    
    



  
me = Person("Sasha", 22, 15, isMale = True)
friend = Person("Ivan", 14, 17, isMale = True)

friend2 = Person("Ivan", 14, 185, isMale = True)
friend3 = Person("Ivan", 14, 185, isMale = "man")

print (me.age)
print (me.name)
print (friend.age)
print (friend.name)
print (friend2.height)
print (friend3.isMale)

print (me.money)
me.work(2)
print (me.money)





# friend.age = 15
# friend.height = 100
# print (friend.height)
# print (friend.age)

