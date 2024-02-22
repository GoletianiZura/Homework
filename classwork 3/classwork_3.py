#რომელ წელს დაიბადა კითხე
ask_age = input("which year were you born? ")

#დაიანგარიშე ასაკი
user_age = 2024 - int(ask_age)
#რამდენი წლისაცაა დაპრინტე იმდენი happy birthday
print("so you are " + str(user_age) + " years old!")

for _ in range(user_age):
    print("Happy Birthday!")
