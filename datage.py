def allowed_dating_age():
    my_age = int(input("Enter your age: "))
    girls_age = my_age/2 + 7
    return(girls_age)


desire_limit = allowed_dating_age()
print("Desire can date", desire_limit, "years or older")