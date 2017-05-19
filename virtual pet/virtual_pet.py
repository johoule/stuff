class Pet():

    def __init__(self, name):
        self.name = name
        self.energy = 10
        self.is_alive = True

    def sleep(self):
        if self.is_alive:
            print(self.name + " goes 'zzzzzzz' ")
            if self.energy + 5 <= 10:
                self.energy += 5
            else:
                self.energy = 10
            print("Energy is " + str(self.energy))
        else:
            print("Error: " + self.name + " is dead!")

    def eat(self):
        if self.is_alive:
            print(self.name + " 'nom nom nom' ")
            if self.energy + 2 <= 10:
                self.energy += 2
            else:
                self.energy = 10
        else:
            print(self.name + " goes 'nom nom nom' on brains!")
        print("Energy is " + str(self.energy))
        
    def roll_over(self):
        if self.is_alive:
            print(self.name + " wants a belly rub")
            if self.energy + 1 <= 10:
                self.energy += 1
            else:
                self.energy = 10
        else:
            print(self.name + "'s ghost misses belly rubs")
            
    def play(self):
        if self.is_alive:
            print(self.name + " goes 'yippee!!!!!!!!!'")
            self.energy -= 4

            if self.energy <= 0:
                self.die()
        else:
            print("Error: " + self.name + " is dead!")
        print("Energy is " + str(self.energy))
        

    def speak(self, words):
        if self.is_alive:
            print(self.name + " says '" + words + "'")
        else:
            print("A ghostly moan coming from " + self.name + "'s grave says '" + words + "'")

    def pee(self, where):
        if self.is_alive:
            if where == "inside":
                print(self.name + " was a bad dog, and peed in the house.  How do you want to punish him/her? yell at them or lock them outside?")
                answer = input
                if answer == "yell at them":
                    self.energy -= 1
                elif answer == "lock them outside":
                    self.energy -= 2
                else:
                    print("Your lenient.")
            elif where == "outside":
                print("Yay! " + self.name + " went outside")
                self.energy += 2
            else:
                print(self.name + " really has to pee, you should let them out.")
        else:
            print(self.name + "'s ghost peed on your bed.")
        print("Energy is " + str(self.energy))
        
    def kill(self, other):
        if self.is_alive:
            print(self.name + " kills " + other.name + "!")
            other.die()
        else:
            print(self.name + " passes right through because he/she is a ghost")
        
    def die(self):
        print(self.name + " writes 'aaarrrrrgggggggg!!!!!!' and dies!")
        self.energy = 0
        self.is_alive = False
    
