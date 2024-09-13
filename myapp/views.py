from django.shortcuts import render
from models import *
# 1 Create a New Django Project:
MyModel.objects.create(name="Test")

# 2. Running in the Same Thread
import threading
def my_function():
    
    MyModel.objects.create(field1="value")
    print("Thread ID:", threading.get_ident())

    threading.Thread(target=my_function).start()


# Custom Classes in Python
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

rect = Rectangle(4, 3)
for item in rect:
    print(item)




