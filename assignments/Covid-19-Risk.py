age =  input("Are you a cigarette addict older than 75 years old? (y/n):")
chronic =  input("Do you have a severe chronic disease? (y/n): ")
immune =  input("Is your immune system too weak? (y/n)")
risk = (age == "y") or (chronic == "y") or (immune == "y")
if risk:
  print("You are in risky group.")
else:
  print("You are not in risky group.")
