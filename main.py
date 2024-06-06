import time

time.sleep

print("Hello, Stranger!")
time.sleep(3)
print ("I don't know you, So lets change that, Shall we ?")
time.sleep(3)
print("I have got some questions for you, If you don't mind ?")
time.sleep(3)
name = input("Whats is your first name? ")
time.sleep(2)
print("Ahh.. Hey there",name, "..Nice to meet you")
time.sleep(2)
print ("My name is Alice, I am a chatbot to the stars ... well I like to think so. Anyway")
time.sleep(3)
print("So",name, "..... Hmm, What a Great Name, It's a nice family name" )
print("Sorry to ask you this but....")
time.sleep(8)
age = input("How old are you? ")

# Calculation of how old you are in days
days = int(age) * 365.25

print("Really .. That doesn't sound right")
time.sleep(4)
print("You don't look a day over 16, But I am sure you get told that all the time... ")
time.sleep(3)
print("Did you know that you have been on this planet for" ,days, "days ? ")
time.sleep(2)
print("Doesn't that sound like a lot of days?")
time.sleep(4)
print("Well I have a little fun fact for you")
time.sleep(2)
weight = input("How much do you weigh in pounds? ")
time.sleep(2)

# How much you would weigh on the moon calculation
moon = int(weight)/9.81 * 1.622

print("On the moon you would only weigh ", moon,"lbs")
time.sleep(4)
print("One big sneeze or One sneeky silent but violent fart and you'll fly off into space ... byeeeeee!!")
time.sleep(2)

def myheight():
  yourheight = int(input("How tall are you in inches? "))
  if yourheight > 170:
    print("Wow, you are taller than me, I don't think I like that, well at least you can reach things on the top self. ")
  else:
    print("Aww .. Your a little short arse, Sorry I guess!! ")

myheight()
time.sleep(2)
print("Did you know, The average height worldwide is 5'7 or 170cm ... Aint that interesting")
time.sleep(2)
print("Hmm, I wonder how much I would weigh on the moon..... Anyway! ")
time.sleep(2)
print("So I have learnt quite alot about you. I am really happy we can be friends. Thanks for taking part in this test.")
time.sleep(2)
print("I have one last question before I give you your final fun fact....")
time.sleep(4)
print("What did you think about this program. A lot of work went into it. Let my creator know if you found the experince 'Good' or 'Bad'. ")
time.sleep(6)
print("OK OK ... Last fun fact, Did you know that the fear of long words is Hippopotomonstrosesquippedaliophobia, I know right. Feel free to google it. ")
time.sleep(4)
print("Anyway ... it was very nice meeting you and I hope to see you again soon. Goodbye. ")
exit()