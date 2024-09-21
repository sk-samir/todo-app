name = input("Please enter new name: ")
file = open ("../files/members.txt", "a")
file.write(name)
file.close()
