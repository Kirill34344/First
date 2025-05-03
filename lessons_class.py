class Human:
    def __init__(self, name):
        self.name = name


    def show_name(self):
        print(f" Name: {self.name}")


output_name = Human("Oleg")
print(id(Human.show_name))
print(id(output_name.show_name))
output_name.show_name()

output_name = Human("Vova")
print(id(Human.show_name))
print(id(output_name.show_name))
output_name.show_name()