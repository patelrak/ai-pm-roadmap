my_age = 35
#print(my_age)
my_height = 5.6
#print(my_height)
my_name = "Rakesh"
#print(my_name)
is_learning_python = True
#print(is_learning_python)
this_is_fun = 1
#print(this_is_fun)
my_skills = ["Python", "Product Manangement", "AI"]
#print(my_skills)
var1 = 10
#print(var1)


intro_1 = "My name is " +my_name + " and I am " + str(my_age) + " years old."
#print(intro_1)
intro_2 = f"My name is {my_name} and I am {my_age} years old."
#print(intro_2)
intro_3 = "My name is {} and I am {} years old.".format(my_name, my_age)
#print(intro_3)

user_name = input("Enter your name: ")
#user_age_txt = input("Enter your age: ")
#user_age = int(user_age_txt)

#print(f"Hello {user_name}, you will be {user_age +5} in 5 years.")

if len(user_name) > 6:
    print(f"your name {user_name} is long")
else: print(f"your name {user_name} is short")