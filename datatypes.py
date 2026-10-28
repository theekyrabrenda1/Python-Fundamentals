age = 56 #Integer
height=3.5 #Float
greetings = "Hey Hey" #String
Interesting = True #Boolean

#Data Structures - A single variable stores multiple values
cars=["Mercedes","Ford","Toyota","Audi"] #List - Ordered but changeable and can hold variables of multiple datatypes
fruits=("Banana","Mango","Cherry","Orange")#Tuple - Ordered but unchangeable
countries = {"China", "Italy", "USA", "United States"} # Set - Unordered and unchangeable
lessons ={"Lesson 1":"Data Science", "Lesson 2":"Web Development"} #Dictionary
numbers = [2,4,6,8,10] #array - Ordered, can hold variables of only 1 datatype
numbers.append(20)

print(age)
print(cars)
print(cars[3])
print(lessons["Lesson 1"])
print(countries)
print(numbers)
print(numbers[0])

#Type casting
print(type(age))
age2=str(age)
print(type(age2))
