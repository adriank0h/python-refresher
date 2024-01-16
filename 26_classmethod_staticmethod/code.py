# class ClassTest:
#     def instance_method(self):
#         print(f"Called instance_method of {self}")

#     @classmethod
#     def class_method(cls):
#         print(f"Called class_method of {cls}")

#     @staticmethod
#     def static_method():
#         print(f"Called static_method. We don't get any object or class info here.")


# instance = ClassTest()
# instance.instance_method()

# ClassTest.class_method()
# ClassTest.static_method()

# # -- What are they used for? --

# # Instance methods are used for most things. When you want to produce an action that uses the data stored in an object.
# # Static methods are used to just place a method inside a class because you feel it belongs there (i.e. for code organisation, mostly!)
# # Class methods are often used as factories.


# class Book:
#     TYPES = ("hardcover", "paperback")

#     def __init__(self, name, book_type, weight):
#         self.name = name
#         self.book_type = book_type
#         self.weight = weight

#     def __repr__(self):
#         return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

#     @classmethod
#     def hardcover(cls, name, page_weight):
#         return cls(name, cls.TYPES[0], page_weight + 100)

#     @classmethod
#     def paperback(cls, name, page_weight):
#         return cls(name, cls.TYPES[1], page_weight)


# heavy = Book.hardcover("Harry Potter", 1500)
# light = Book.paperback("Python 101", 600)

# print(heavy)
# print(light)

class ClassTest:
    # when you want to produce an action that uses the data of an obj u created earlier 
    def instance_method(self):
        print(f"Called instance_method of {self}")
    #used as factories
    @classmethod
    def class_method(cls):
        print(f'Called class method of {cls}')
    #place a method in a class just meh LOL for code organisation can use static, not used that much 
    @staticmethod
    def static_method():
        print("Called static method")
 

#instance methods needs the instance to call it 
# test = ClassTest()
# test.instance_method()
# ClassTest.instance_method(test)


# ClassTest.class_method()

# ClassTest.static_method()

class Book:
    #class properties
    TYPES = ("hardcover","paperback")
    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight
        
    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"
    
    @classmethod
    def hardcover(cls,name,page_weight):
        return cls(name, Book.TYPES[0], page_weight + 100)
    
    @classmethod
    def paperback(cls,name,page_weight):
        return cls(name, Book.TYPES[1], page_weight)
    
    @staticmethod
    def getBook(name,weight):
        return Book(name,Book.TYPES[0],weight+100)
    
    
book = Book.hardcover("Harry Potter", 1500)
lightbook = Book.paperback("Python 101", 600)
test_method = Book.getBook("test", 100)

print(test_method)