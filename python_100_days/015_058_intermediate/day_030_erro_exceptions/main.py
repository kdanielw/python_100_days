# FileNotFoundError
# with open("file.txt") as file:
#     file.read()

# KeyError
# a_dictionary = {"key": "value"}
# value  =  a_dictionary["another_key"]

# IndexError
# list = [1, 2, 3]
# print(list[3])

# TypeError
# text = "abc"
# print(text + 5)

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     value = a_dictionary["key"]
# except FileNotFoundError:
#     file = open("a_file.txt", mode="w")
#     file.write("Sonotori")
# except KeyError as error_message:
#     print(f"That key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed")
#     raise KeyError("This error was intentional")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)
