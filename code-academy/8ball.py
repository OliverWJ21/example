#inputs for a magic 8 ball
name= "Blood"
question = "Will I be able to fly next year? "
if name == "" :
 print("Question: "+question)
elif question == "":
 print(name+":"+" Asks:")
else :
 print(name+":"+" Asks: "+"Question: "+question)
Answer= ""
#Number Generation
import random
random_number=random.randint(1,9)

if random_number == 1:
 Answer='Yes - definitely'
elif random_number == 2:
 Answer='It is decidedly so without a doubt'
elif random_number == 3:
 Answer='Without a doubt' 
elif random_number == 4:
 Answer='Reply hazy, try again'
elif random_number == 5:
 Answer='Ask again later'
elif random_number == 6:
 Answer='Better not tell you now'
elif random_number == 7:
 Answer='My sources say no'
elif random_number == 8:
 Answer='Outlook not so good'
else:
 Answer='Very doubtful'
print("Magic 8 Ball wisdom is...:"+Answer)