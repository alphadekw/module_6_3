class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            for floor in range(1, new_floor + 1):
                print(f'{floor}')
            else:
                print("Такого этажа не существует")


    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return False

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return False

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return False

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return False

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return False

    def __add__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)


    def __len__(self):
        return  self.number_of_floors

    def __str__(self):
        return (f'Название: {self.name} кол-во этажей: {self.number_of_floors}')


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)
print(h1 == h2) # __eq__



h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)
h1 += 10 # __iadd__
print(h1)
h2 = 10 + h2 # __radd__
print(h2)
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__