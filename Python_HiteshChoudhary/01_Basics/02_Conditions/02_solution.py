#-------------------------------------------------------------------------------#
#                         2. Movie Ticket Pricing
#-------------------------------------------------------------------------------#
# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. 
#Everyone gets a $2 discount on Wednesday.


age = int(input("enter age : "))
day = input("enter day : ")

# below statement say that set price 12 if age is grater than or equals to 18 else set price to 8.
ticketPrice = 12 if age >= 18 else 8

if day == "Wednesday" or day == "wednesday" :
    ticketPrice = ticketPrice - 2

print("Ticket Price is ",ticketPrice)