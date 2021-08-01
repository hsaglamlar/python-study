age = int(input("Are you a cigarette addict older than 75 years old? Enter '1' for 'YES' '0' for 'NO' :"))
chronic = int(input("Do you have a severe chronic disease? Enter '1' for 'YES' '0' for 'NO' :"))
immune = int(input("Is your immune system too weak? Enter '1' for 'YES' '0' for 'NO' :"))

risk = age or chronic or immune

print("You have " + risk*"risk." + (not risk)*"no risk.")