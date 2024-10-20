#in python to declare a function we use a reserve key word called def


def say_hello(name):
  print(f"Hello {name}")
  
say_hello("nashe")#this function will return hello nashe 

#let try to create a function with some login inside


def elible_for_driving(name, age):
  if age > 18:
    print(f"{name} you are eligible for driving ")
  else:
    print(f"{name} you are too young for driving")


elible_for_driving("nashe",17)
elible_for_driving("nashe",45)
#if you try to see this functions you will see that they are returning meaningful results which means all is running well with no errors
  