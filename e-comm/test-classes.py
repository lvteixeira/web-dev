import os
from classes import *

os.system('cls')
print('TEST STARTED.')
print('-------------------')
print('creating pets...')
print('-------------------')
print('created pet info::')
dog_1 = Dog('Bob', 1)
dog_2 = Dog('Lessie', 2)
print(dog_1)
print(dog_2)
cat_1 = Cat('Tom', 1)
cat_2 = Cat('Avocatto', 2)
print(cat_1)
print(cat_2)
print('-------------------')
print('testing say func...')
print('-------------------')
print('result::')
print(f"{dog_1.name} said -> '{dog_1.say()}'\n{dog_2.name} said -> '{dog_2.say()}'")
print(f"{cat_1.name} said -> '{cat_1.say()}'\n{cat_2.name} said -> '{cat_2.say()}'")
print('-------------------')
print('testing greet func...')
print('-------------------')
greeting = 'Hello Mr. Developer, how is your day going?'
print('result::')
print(f"{dog_1.name} said -> '{dog_1.greet(greeting)}'\n{dog_2.name} said -> '{dog_2.greet(greeting)}'")
print(f"{cat_1.name} said -> '{cat_1.greet(greeting)}'\n{cat_2.name} said -> '{cat_2.greet(greeting)}'")
print('-------------------')
print('testing has_owner property...')
print('-------------------')
print('result::')
print(f"{dog_1.name} -> '{dog_1.has_owner}'")
print(f"{cat_1.name} -> '{cat_1.has_owner}'")
print('-------------------')
print('giving them an owner...')
print('-------------------')
owner_1 = Person('Leo', 24)
owner_2 = Person('Ana', 20)
print('result::')
print('BEFORE')
print(f"{owner_1.name}'s 'has_pet' attr before adoption -> '{owner_1.has_pet}'")
print(f"{owner_2.name}'s 'has_pet' attr before adoption -> '{owner_2.has_pet}'")
print(f"{dog_1.name}'s 'has_owner' attr before adoption -> '{dog_1.has_owner}'")
print(f"{cat_1.name}'s 'has_owner' attr before adoption -> '{cat_1.has_owner}'")
owner_1.adoption(dog_1)
owner_2.adoption(cat_1)

print('')
print('AFTER')
print(f"{dog_1.name}'s 'has_owner' attr after adoption -> '{dog_1.has_owner}'")
print(f"{dog_1.name}'s new owner name -> '{dog_1.owner_name}'")
print(f"{cat_1.name}'s 'has_owner' attr before adoption -> '{cat_1.has_owner}'")
print(f"{cat_1.name}'s new owner name -> '{cat_1.owner_name}'")
print(f"{owner_1.name}'s 'has_pet' attr after adoption -> '{owner_1.has_pet}'")
print(f"{owner_1.name}'s new pet name -> '{owner_1.pet_name}'")
print(f"{owner_2.name}'s 'has_pet' attr after adoption -> '{owner_2.has_pet}'")
print(f"{owner_2.name}'s new pet name -> '{owner_2.pet_name}'")
