#ჩავასმევინოთ მომხარებელს ციფრი
user_input = input("Enter a number: ")

#მიღებული ციფრი დავაკონვერტოთ ინტეჯერად
number = int(user_input)

#შევამოწმოთ რიცხვი ლუწია თუ კენტი და დავბეჭდოთ პასუხი
if number % 2 == 0:
    print("The number "+ str(number) + " is even")

else:
    print("The number "+ str(number) + " is odd.")
    
