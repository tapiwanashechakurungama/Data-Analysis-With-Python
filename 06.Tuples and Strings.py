numbers = (1,2,3,6)
print(numbers[1])
#the above one is a tuple the only difference between a tuple and list is that we cant manipulate tuples but we can manipulate lists 

#like if we try this 
#  numbers[1] = 10 this code will return an error but lemme give the same code with list
numbers = [1,2,3,6]
numbers[1] = 10
print(numbers) #this code will not give us an error this code will run as expected so tuples are used when we want to protect our data from direct modifications 

 