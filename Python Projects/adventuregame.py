name = input("What is your name? ")

answer = input("You are on a adventure! You are on a path and come to a fork in the road. Do you go left or right? ")
 
if answer == "left":
    answer = input ("You come to a lake. There is an island in the middle of the lake. Do you swim across or go around the lake? ")
    
    if answer == "swim":
        print("You swim across and are eaten by an alligator.")
        
    elif answer == "around":
        print("You go around and reach the island.")
    
    else:
        print("Not a valid option. You lose.")
        
elif answer == "right":
    answer = input ("You come to a bridge. It looks wobbly. Do you cross it or go back? ")
    
    if answer == "cross":
        print("You cross the bridge and are eaten by a troll.")
        
    elif answer == "back":
        print("You go back and are eaten by a wolf.")
    
    else:
        print("Not a valid option. You lose.")
        
else:
    print("Not a valid option. You lose.")
    
print("Thank you for playing", name)