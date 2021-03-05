#CSE3130- Object Oriented Programming 2- Notes
## Inheritance
Inheritance is the process where one class inherits attributes and methods from another class. While some languages, such as Java, prohibits it, classes can inherit from multiple parent classes. However, 
this process of multiple inheritances is often avoided because of potential conflicts from duplicate attribute or method names.

* Inheritance describes an Is-A relationship
    * The _deck_ is a _group of cards_ and the _hand_ is a _group of cards_. (Both inherit card class)
    * __Abstract Classes__ (as opposed to concrete classes) are classes that are never instantiated by themselves, but are solely written for the purpose of inheritance. Oftentimes, these classes have _abstract methods_ which cannot fully called within the Abstract Class, but relies on data from the subclass 
    * TIP: Amateur mistakes include looking for inheritance, where classes inherit several levels deep. Inheritance often reveals itself in the design process. 
    
```python
class Mammal: # Abstract parent Class
    def __init__(self, genus,species,name):
        self.GENUS = genus
        self.SPECIES = species
        self.NAME = name
        self.CRY_SOUND = None
    def setCry(self, sound):
        self.CRY_SOUND = sound 
    def cry(self):
        print(f"{self.CRY_SOUND}!")

class Dog(Mammal): # put class where inherit from 
    def __init__(self, genus, species, name, cry_sound = "woof"):
        Mammal.__init__(genus, species, name)
        self.setCry(cry_sound)

class Cat(Mammal):
    def __init__(self,genus,species,name, cry_sound = "meow"):
        Mammal.__init__(genus,species,name)
        self.setCry(cry_sound)

HUSKY = Dog("Canis", "lupus", "Husky", "Arf")
SIAMESE = Cat("Felis", "catis", "Siamese")
```

## Polymorphism 
Polymorphism is the ability to have the same methods in different classes perform different tasks/outcomes.

```python
HUSKY.cry() # arf!
SIAMESE.cry() # meow!
```

Note that both objects have the same method, but have different outputs. 

## Public, Private and Protected Class Members
Classical object-oriented programming languages, such as C++ and Java, control the access to class resources by public, private, and protected keywords.
Private members (attributes/methods) of the class are denied access from the environment outside the class. They can be handled only from within the class. Controlling acces to members with a class increases the class's integrity only allowing access to certain members externally through encapsulation. 

__Public Members__ are accesible outside the Class. In Python, all members are defaulted as public.

__Protected Members__ are available to the class and its subclasses. They are denoted with an underscore at the beginning of the member name. Protected Members are still accessiblle outside of the class, but Python will throw a warning. 

__Private Members__ are only avalible within the class. They are denoted a double underscore at the beginning of the member name. Private Members are not accessible outside the class. 

```python
class MyClass:
    def__init__(self):
        self.FIRST_NAME = "Chelsea" # Public
        self._LAST_NAME = "Chen"
        self._MID_INIT = "H" # Private

    def _protectedMethods(self):
        pass
    def __privateMethod(self):
        pass
```
