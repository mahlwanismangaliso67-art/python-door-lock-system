print("Welcome")
print("Press any key to continue")

pin = input("Enter your pin to unlock")

correct_pin = "660533"
correct_favourite_name = "Exquisite"

while pin != correct_pin:
   print("Access Denied") 
   while True:
       print("1. Change your pin")
       print("2. Try again")
       print("3. Exit")
       users_choice = input("Choose option:")
       if users_choice == "1":
          favourite_name = input("Enter your favourite name to continue")
          if favourite_name == correct_favourite_name:
              print("Correct answer")
              while True:
                  New_pin = input("Enter new pin then press Enter")
                  correct_pin = New_pin
                  print('Your New pin is', New_pin)
                  print("Access Granted")
                  break
          else:
              print("Incorrect answer") 

       
       elif users_choice == "2":
           pin = input("Enter your pin to unlock")
           if pin == correct_pin:
               print("Access Granted")
               break
           else:
              print("Access Denied") 
              while False:
                  print("1. Change your pin")
                  print("2. Try again")
                  print("3. Exit")
       elif users_choice == '3':
           print("Bye")
           break
   
else:
    print("Access Granted")
