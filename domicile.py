def check_domicile():
  age=int(input("Enter your age: "))
  domicile=input("Enter your domicile: ")

  if domicile.lower()=="lahore" and age>=18:
      print("You are eligible to vote.")
  else:
        print("You are not eligible to vote.")
check_domicile()
