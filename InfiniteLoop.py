print("Lets safely peak into the infinte loop!")
test_value=0
safety_counter=0
while test_value<= 0:
    print("This codition never changes, so this would run forever!")
    safety_counter += 1
    if safety_counter == 3:
        print("(Stopping here on purpose, a real infinite loop never stops on its own.)")
        break
    
    