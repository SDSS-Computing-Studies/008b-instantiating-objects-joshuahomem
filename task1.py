#!python3

"""
Create a class that will store a database for a veterinarian.
Your class will need the following properties:

animal (dog, cat, fish, bird, turtle, etc)
breed
name (the pet's name)
owner (the owner's name)
birthdate (of the pet, expressed as yyyy-mm-dd)

The constructor will need to ask for each of those values
for the database when the pet is instantiated

Methods:
display() - should show the name of the pet and type followed by their breed and owner


Main block should have a menu that has the following options:
1. Enter a new pet
2. Retrieve a pet
3. Exit

If they choose to retrieve a pet,
display the following:
Enter pet's name:
and then go through the list, looking for the name of the pet.
If the pet is found, it should call the display() method from the object

Example output:
1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? cat
Breed? Domestic Long Hair
Name? Benjamin
Owner? Chris
Birthdate? 20015-10-01

1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? dog
Breed? Shih-tzu
Name? Buster
Owner? Christy
Birthdate? 2008-10-16

1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? cat
Breed? Domestic Long Hair
Name? Casey
Owner? Chris
Birthdate? 20015-10-01

1. Enter a new pet
2. Retrieve a pet
3. Exit
2

Which Pet? Buster

Buster dog
Shih-tzu is owned by Christy
(10 points) 
"""

class dogs:
    animal= None
    breed= None
    name= None
    owner= None
    birthday= None
    
    def __init__(self):

        self.animal=input("Enter In the Type of Animal here: ")
        self.breed=input("Enter in the type of breed here: ")
        self.name=input("Enter in the Name of the animal here: ")
        self.owner=input("Enter in the name of the owner here: ")
        self.birthday=input("Enter in the birthdate of the animal here: ")
        print("\n")
    
    def displaypet(self):
        print("The Animal is a " +self.animal)
        print("The breed is "+self.breed)
        print("The name of the pet is "+ self.name+"and the owner is "+self.owner)
        print("The pets birthday is "+self.birthday)
        print('\n')
    def exit(self):
        exit()

def Main():
    print("Welcome to the vet data base")
    print("Type 1 if you would like to add a pet")
    print("Type 2 two if you would like to look at the data of a pet")
    print('Type 3 three if you would like to exit')
    (x)=input("Enter in your choice here: ")
    print('\n')
    x=int(x)
    if x==1:
        # instantiate an object
        
        data.append(dogs())

    elif x==2:
        
        # get the name of the pet
        # cycle through all of the objects in the list to see if the name matches
        # save the index of the object that matches
        # use index to retrieve the rest of of the information
        x=input("Enter in the name of the pet: ")
        print("\n")
     
        for i in data:
            if x==i.name:
                dogs.displaypet(i)
            else:
                print("Not a pet we have please try again")
                print('\n')
                Main()
    elif x==3:
        exit()
    else:
        print("that is not a valid input please try again")
        Main()



data=[]
while True:
    Main()
    print(data)
