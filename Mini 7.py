age = int(input("Enter Your Age:"))
parental_permission = input("Do you have parental permission? (yes/no):")
if age >= 18 or parental_permission == "yes":
    print ("You can watch the movie")
else: 
    print ("you can't watch this movie")