
#
# def add(*args):
#     sum_no = []
#     for n in args:
#         sum_no.append(n)
#     print(sum(sum_no))
#
#
# add(2, 4, 5, 7, 100, 50, 55)

# working with *args
def add(*args):
    sum_no = 0
    for n in args:
        sum_no += n
    return sum_no


print(add(2, 4, 5, 7, 100, 50, 55))


# working with **kwargs
def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n


print(calculate(2, add=4, multiply=5))


# How to use a **kwargs dictionary safely
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)


