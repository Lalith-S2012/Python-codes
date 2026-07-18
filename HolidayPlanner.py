print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("|             Welcome to The best Holiday Planner              |")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")

name = input("What is your Name!? ")
print("Nice meeting you" ,name)
print("I shall be your Trip planner for the day, let us start. \n ")
print("I need to ask you a few question before I advice you a Holiday\n")

cont = input("Type in the number next to the continent you are planning to go to:\n1. North America\n2. South America\n3. Europe\n4. Asia\n5. Africa\n6. Australia\n7. Antarctica\nType Here ==> ").strip().lower()

if cont == "1" or cont == "north america":
   
    place = input("What type of place in North America, (Choose from the options below)\n 1. Beach\n  2. Mountains\n   3. Cruise\n    4. Hiking\n     5. Adventure\n      6. Ski and Winter Holidays\n       7. Island Getaways\nType Here ==> ").strip().lower() 

    if place == "1" or place == "beach":
       # Copy and paste this exact block into your Python editor:
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                          | Food & Drink Style          |

        | :---------------- | :----------------- | :-----------------------------------------  | :-------------------------- |
        | **Budget**        | $500 – $800        | Downtown hostel/hotel ($17–$46/night)       | Local street food & tacos   |
        | **Mid-Range**     | $1,200 – $2,000    | 4-star Hotel Zone resort ($138–$232/night)  | Mix of sit-down restaurants |
        | **All-Inclusive** | $2,000 – $2,500    | Beachfront all-inclusive resort ($200-$500) | All meals & drinks included |
        | **Luxury**        | $2,500+            | 5-star luxury resort ($600+/night)          | Fine dining & private tours |""")

    elif place == "2" or "mountains":
        print("")
    elif place == "3" or "cruise":
        print("")
    elif place == "4" or "hiking":
        print("")
    elif place == "5" or "adventure":
        print("")
    elif place == "6" or "ski and winter holiday":
        print("")
    elif place == "7" or "island getaway":
        print("")







