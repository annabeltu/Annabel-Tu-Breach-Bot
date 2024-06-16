breachYear = 2019

#Greets user
print("Hello! I'm Breach Bot.")
userName = input("What is your name?\n")
print("Nice to meet you " + userName)

#Recounts year of breach
todaysYear = input("What year is it?\n")
timePassed = int(todaysYear) - breachYear
print("Wow! That means it has been " + str(timePassed) + " years since the Facebook Breach.")



#Introduces breach
print("Would you like to learn about the Facebook 2019 Breach?")
giveInfo = input("Type 'yes' or 'no'\n")

#Explains breach
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) breach details, (b) organization's response, or (c) I would like to hear your reflection")
  topic = input()
  
  if topic.lower() == "a":
    print("Over 530 million Facebook users in 106 countries were involved in this data breach. Information such as phone numbers, full names, and email addresses were taken. It happened through “malicious actors” exploiting a vulnerability in the platform that allowed users to find one another through phone numbers.")
  
  elif topic.lower() == "b":
    print("The organization decided not to inform the users affected. The organization did not recommend any actions.")
  
  elif topic.lower() == "c":
    break;
  
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")



#Introduces my take
print("\nI'm excited to share my perspective with you. Are you ready to hear my take?")
giveInfo = input("Type 'yes' or 'no'\n")

#Shares my take
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) relation to the CIA Triad, (b) my reaction, or (c) my advice, or (d) none")
  topic = input()
  
  if topic.lower() == "a":
    print("The Facebook 2019 breach focused on a break in confidentiality between users and hackers; therefore, hackers were able to access personal information such as phone numbers, full names, and email addresses.")
  
  elif topic.lower() == "b":
    print("I do not agree with the organization’s response because the users that were harmed from the breach did not know they were affected, and the users affected were not able to find ways to keep their information safe in the future.")
  
  elif topic.lower() == "c":
    print("I would convince victims to take action by contacting the company’s customer service. My advice would be to change any passwords and allow for two factor authentication to access the account.")
    
  elif topic.lower() == "d":
    break
  
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")

#Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")