# From: ZYL
# Time: 2025-12-27  23:20:29
# Mail: 2790299631@qq.com

class Person(object):
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def run(self):
        print(self.name + " is running!")

    def eat(self):
        print(self.name + " is eating!")
        self.height += 1
        print(self.name + " 现在的身高为" + str(self.height) + "m!")


me = Person("小明", 21, 175)
me.name = "笑笑"
me.eat()