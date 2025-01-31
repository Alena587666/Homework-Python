# class User:

	#def __init__(self, name):
		#print("я создался")
		#print("меня зовут ", name) #добавили запрос

# user1 = User("Alex")
# user2 = User("Mark")
# user3 = User("Marta")


class User:
	age = 0

	def __init__(self, name):
		print("я создался")
		self.username = name

	def sayName(self):
		print("меня зовут ", self.username)

	def sayAge(self, newAge):
		self.age = newAge 

alex = User("Alex")
mark = User("Mark")
marta = User("Marta")

alex.sayName()
alex.sayAge()
alex.setAge(33)
alex.sayAge()
