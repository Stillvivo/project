class person:
    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self.age = age

    @classmethod
    def personality(self, namee):
        namee = namee


person_1 = person(input("please enter your name : "), input("please enter your family :"),
                  input(("please enter your age : ")))
namee = input("please tell me about your self!! :")

if not person_1.name.isalpha():
    raise ValueError("name must be word")
if not person_1.family.isalpha():
    raise ValueError("family name must be word")
if not person_1.age.isdigit():
    raise ValueError("age must be an integer")

print(f"Person name is : ({person_1.name}) and Family is : ({person_1.family}) and Age is : ({person_1.age})")
print(f"about : {person_1.name} ({namee})")
