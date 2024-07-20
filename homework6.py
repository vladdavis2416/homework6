#словари
my_dict = {"Vlad": 2001, "Grigory": 2000, "Arina": 2002}
print(my_dict)
print(my_dict["Vlad"])
print(my_dict.get("Sasha", "Такого человека нет в списке"))
my_dict.update({"Sasha": 1997,
                "Alexey": 2001})
a= my_dict.pop("Vlad")
print(a)


#Множества
my_set= {2, 3, 2, 25, 2.3, "Vlad", True}
print(my_set)
my_set.add(13)
my_set.add(24)
my_set.remove(3)
print(my_set)
