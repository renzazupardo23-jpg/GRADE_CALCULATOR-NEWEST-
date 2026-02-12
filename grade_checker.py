#test scores
"""I added try to handle the error when the user input letter or words or invalid inputs"""
try:
    score = int(input("Enter your test score (0-100): "))

    if score >= 90 or score <= 100:
          print("Grade: A - excellento!")
    elif score >= 80:
          print("Grade: B - Good job bro!")
    elif score >= 70:
          print("Grade: C - Nice one")
    elif score >= 60:
          print("Grade: D - Nice try..")
    else:
          print("Grade: F - BARAHOOOO")
#to change the message of ValueError   
except ValueError:
   print("ERROR!! Please enter a number between 0 and 100.")    