# class Shape():
#     def what_am_i(self):
#         print("I am a Shape.")
        

# class Rectangle(Shape):
#     def __init__(self, len, width):
#         self.length = len
#         self.width = width
    
#     def cal_perimeter(self):
#         return self.width * 2 + self.length * 2
    
# class Square():
#     square_list = []
    
#     def __init__(self, s1):
#         self.s1 = s1
#         self.square_list.append(self.s1)
    
#     def cal_perimeter(self):
#         return self.s1 * 2
    
#     def change_size(self, new_size):
#         self.s1 += new_size
        
#     def __repr__(self):
#         return "{} by {} by {} by {}".format(self.s1, self.s1, self.s1, self.s1)
        
           

# a_rec = Rectangle(20, 25)
# a_squ = Square(100)
# print(a_squ)

# a_rec.what_am_i()
# a_squ.what_am_i()

# class Rider():
#     def __init__(self, name):
#         self.name = name

# class Horse():
#     def __init__(self, name, rider):
#         self.name = name
#         self.rider = rider

# a_rider = Rider('takeshi')
# horse = Horse("pony", a_rider)

# print("the {}".format(horse.name))
# print("the rider {}".format(horse.rider.name))


def Judge(obj1, obj2):
    return obj1 is obj2

print(Judge("a", "a"))