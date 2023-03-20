class Pet:
    def __init__(self, name: str, age: int, xtype: str):
        self.name = name
        self.age = age
        self.xtype = xtype
        self.__has_owner = False
        self.owner_name = None

    def __str__(self):
        info = {
            'name': self.name,
            'age': self.age,
            'has_owner': self.has_owner
        }
        return f"{self.xtype} object info -> {info}"

    @property
    def has_owner(self) -> bool:
        return self.__has_owner

    @has_owner.setter
    def has_owner(self, new_owner_name: str) -> None:
        if self.__has_owner:
            print('Pet already has an owner, aborting...')
        else:
            self.__has_owner = True
            self.owner_name = new_owner_name

    def greet(self, greeting: str) -> str:
        return f'{greeting}'

    def say(self) -> str:
        pass

class Dog(Pet):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, xtype='Dog')

    def say(self) -> str:
        return 'Hulf huLf hUlF!!'

class Cat(Pet):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, xtype='Cat')

    def say(self) -> str:
        return 'Meoww meowwww mEoowWwwwW'



class Person:
    xtype = 'Human Being'

    def __init__(self, name: str, age: int, xtype: str = xtype):
        self.name = name
        self.age = age
        self.xtype = xtype
        self.__has_pet = False
        self.pet_name = None

    def __str__(self) -> str:
        info = {'name': self.name, 'age': self.age, 'has_pet': self.has_pet}
        return f"{self.xtype} object info -> {info}"

    @property
    def has_pet(self) -> bool:
        return self.__has_pet

    @has_pet.setter
    def has_pet(self, new_pet_name: str) -> None:
        if self.__has_pet:
            print('Owner already has a pet, aborting...')
        else:
            self.__has_pet = True
            self.pet_name = new_pet_name

    def adoption(self, pet: Dog) -> None:
        self.has_pet = pet.name
        pet.has_owner = self.name