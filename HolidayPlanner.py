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
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                      | Food & Drink Style            |

        | :---------------- | :----------------- | :-------------------------------------- | :---------------------------- |
        | **Budget**        | $600 – $900        | Budget mountain lodge                   | Cafes & local diners          |
        | **Mid-Range**     | $1,200 – $2,000    | Comfortable mountain resort             | Restaurants & grills          |
        | **Luxury**        | $2,500+            | Luxury mountain chalet                  | Gourmet dining                |""")

    elif place == "3" or "cruise":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                      | Food & Drink Style            |

        | :---------------- | :----------------- | :-------------------------------------- | :---------------------------- |
        | **Budget**        | $800 – $1,200      | Interior cruise cabin                   | Buffet meals                  |
        | **Mid-Range**     | $1,500 – $2,500    | Ocean-view cabin                         | Restaurants & buffet          |
        | **Luxury**        | $3,500+            | Balcony or Suite                         | Fine dining included          |""")

    elif place == "4" or "hiking":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                      | Food & Drink Style            |

        | :---------------- | :----------------- | :-------------------------------------- | :---------------------------- |
        | **Budget**        | $500 – $900        | Camping & hostels                        | Packed meals & cafes          |
        | **Mid-Range**     | $1,000 – $1,800    | Cabins & hotels                          | Restaurants                   |
        | **Luxury**        | $2,500+            | Luxury wilderness lodge                  | Gourmet dining                |""")

    elif place == "5" or "adventure":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                      | Food & Drink Style            |

        | :---------------- | :----------------- | :-------------------------------------- | :---------------------------- |
        | **Budget**        | $700 – $1,000      | Budget hotel                             | Fast food & local restaurants |
        | **Mid-Range**     | $1,500 – $2,500    | 3-4 Star Hotel                           | Variety of restaurants        |
        | **Luxury**        | $3,500+            | Luxury Resort                            | Fine dining                   |""")

    elif place == "6" or "ski and winter holidays":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                      | Food & Drink Style            |

        | :---------------- | :----------------- | :-------------------------------------- | :---------------------------- |
        | **Budget**        | $900 – $1,500      | Ski hostel                               | Cafes & pubs                  |
        | **Mid-Range**     | $2,000 – $3,000    | Ski resort                               | Resort restaurants            |
        | **Luxury**        | $4,000+            | Luxury ski lodge                         | Fine dining                   |""")

    elif place == "7" or "island getaways":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                      | Food & Drink Style            |

        | :---------------- | :----------------- | :-------------------------------------- | :---------------------------- |
        | **Budget**        | $700 – $1,200      | Beach hostel                             | Local seafood                 |
        | **Mid-Range**     | $1,500 – $2,500    | Beach resort                             | Seafood & restaurants         |
        | **Luxury**        | $3,500+            | Private island villa                     | Gourmet dining                |""")


elif cont == "2" or cont == "south america":

    place = input("What type of place in South America, (Choose from the options below)\n 1. Beach\n  2. Mountains\n   3. Cruise\n    4. Hiking\n     5. Adventure\n      6. Ski and Winter Holidays\n       7. Island Getaways\nType Here ==> ").strip().lower()

    if place == "1" or place == "beach":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                         | Food & Drink Style          |

        | :---------------- | :----------------- | :----------------------------------------- | :-------------------------- |
        | **Budget**        | $500 – $900        | Beach hostel                               | Local seafood & street food |
        | **Mid-Range**     | $1,200 – $2,000    | Beach resort                               | Restaurants & cafes         |
        | **Luxury**        | $2,500+            | 5-Star beachfront resort                   | Fine dining                |""")

    elif place == "2" or "mountains":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                         | Food & Drink Style          |

        | :---------------- | :----------------- | :----------------------------------------- | :-------------------------- |
        | **Budget**        | $600 – $900        | Budget mountain lodge                      | Local cafes                |
        | **Mid-Range**     | $1,300 – $2,200    | Mountain hotel                             | Restaurants                |
        | **Luxury**        | $3,000+            | Luxury mountain resort                     | Gourmet dining             |""")

    elif place == "3" or "cruise":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                         | Food & Drink Style          |

        | :---------------- | :----------------- | :----------------------------------------- | :-------------------------- |
        | **Budget**        | $900 – $1,300      | Interior cruise cabin                      | Buffet meals               |
        | **Mid-Range**     | $1,800 – $2,800    | Ocean-view cabin                           | Restaurants & buffet       |
        | **Luxury**        | $4,000+            | Luxury suite                               | Fine dining                |""")

    elif place == "4" or "hiking":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                         | Food & Drink Style          |

        | :---------------- | :----------------- | :----------------------------------------- | :-------------------------- |
        | **Budget**        | $500 – $900        | Camping & hostels                          | Packed meals               |
        | **Mid-Range**     | $1,200 – $2,000    | Cabins & hotels                            | Restaurants                |
        | **Luxury**        | $2,800+            | Luxury eco-lodge                           | Gourmet dining             |""")

    elif place == "5" or "adventure":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                         | Food & Drink Style          |

        | :---------------- | :----------------- | :----------------------------------------- | :-------------------------- |
        | **Budget**        | $700 – $1,200      | Budget hotel                               | Local food                 |
        | **Mid-Range**     | $1,500 – $2,500    | 4-Star hotel                               | Restaurants                |
        | **Luxury**        | $3,500+            | Luxury resort                              | Fine dining                |""")

    elif place == "6" or "ski and winter holidays":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                         | Food & Drink Style          |

        | :---------------- | :----------------- | :----------------------------------------- | :-------------------------- |
        | **Budget**        | $900 – $1,400      | Ski lodge                                  | Cafes                      |
        | **Mid-Range**     | $2,000 – $3,000    | Ski resort                                 | Resort restaurants         |
        | **Luxury**        | $4,000+            | Luxury ski lodge                            | Fine dining               |""")

    elif place == "7" or "island getaways":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                         | Food & Drink Style          |

        | :---------------- | :----------------- | :----------------------------------------- | :-------------------------- |
        | **Budget**        | $700 – $1,100      | Beach hostel                               | Local seafood             |
        | **Mid-Range**     | $1,500 – $2,400    | Island resort                              | Restaurants              |
        | **Luxury**        | $3,500+            | Private beachfront villa                   | Gourmet dining           |""")


elif cont == "3" or cont == "europe":

    place = input("What type of place in Europe, (Choose from the options below)\n 1. Beach\n  2. Mountains\n   3. Cruise\n    4. Hiking\n     5. Adventure\n      6. Ski and Winter Holidays\n       7. Island Getaways\nType Here ==> ").strip().lower()

    if place == "1" or place == "beach":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                         | Food & Drink Style          |

        | :---------------- | :----------------- | :----------------------------------------- | :-------------------------- |
        | **Budget**        | $700 – $1,000      | Beach hostel                               | Local cafes & street food   |
        | **Mid-Range**     | $1,500 – $2,500    | Coastal hotel                              | Restaurants & cafes         |
        | **Luxury**        | $3,500+            | 5-Star seaside resort                      | Fine dining                |""")

    elif place == "2" or "mountains":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                         | Food & Drink Style          |

        | :---------------- | :----------------- | :----------------------------------------- | :-------------------------- |
        | **Budget**        | $700 – $1,200      | Mountain hostel                            | Local restaurants           |
        | **Mid-Range**     | $1,500 – $2,800    | Mountain hotel                             | European cuisine            |
        | **Luxury**        | $4,000+            | Luxury chalet                              | Gourmet dining              |""")

    elif place == "3" or "cruise":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                         | Food & Drink Style          |

        | :---------------- | :----------------- | :----------------------------------------- | :-------------------------- |
        | **Budget**        | $900 – $1,400      | Cruise cabin                               | Buffet meals                |
        | **Mid-Range**     | $2,000 – $3,000    | Ocean-view cabin                           | Restaurants                 |
        | **Luxury**        | $4,000+            | Luxury cruise suite                        | Fine dining                 |""")

    elif place == "4" or "hiking":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                         | Food & Drink Style          |

        | :---------------- | :----------------- | :----------------------------------------- | :-------------------------- |
        | **Budget**        | $600 – $1,000      | Camping & hostels                          | Packed meals                |
        | **Mid-Range**     | $1,500 – $2,400    | Mountain cabins                            | Local restaurants           |
        | **Luxury**        | $3,000+            | Eco-lodges                                 | Gourmet meals               |""")

    elif place == "5" or "adventure":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                         | Food & Drink Style          |

        | :---------------- | :----------------- | :----------------------------------------- | :-------------------------- |
        | **Budget**        | $800 – $1,300      | Budget hotel                               | Local European food         |
        | **Mid-Range**     | $1,700 – $2,800    | 4-Star hotel                               | Restaurants                 |
        | **Luxury**        | $4,000+            | Luxury resort                              | Fine dining                 |""")

    elif place == "6" or "ski and winter holidays":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                         | Food & Drink Style          |

        | :---------------- | :----------------- | :----------------------------------------- | :-------------------------- |
        | **Budget**        | $900 – $1,500      | Ski hostel                                 | Cafes                       |
        | **Mid-Range**     | $2,000 – $3,500    | Ski resort                                 | Mountain restaurants        |
        | **Luxury**        | $5,000+            | Luxury ski chalet                          | Fine dining                 |""")

    elif place == "7" or "island getaways":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                         | Food & Drink Style          |

        | :---------------- | :----------------- | :----------------------------------------- | :-------------------------- |
        | **Budget**        | $800 – $1,300      | Island hostel                              | Seafood & local food        |
        | **Mid-Range**     | $1,800 – $2,800    | Island hotel                               | Restaurants                 |
        | **Luxury**        | $4,000+            | Private island resort                      | Gourmet dining              |""")


elif cont == "4" or cont == "asia":

    place = input("What type of place in Asia, (Choose from the options below)\n 1. Beach\n  2. Mountains\n   3. Cruise\n    4. Hiking\n     5. Adventure\n      6. Ski and Winter Holidays\n       7. Island Getaways\nType Here ==> ").strip().lower()

    if place == "1" or place == "beach":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                         | Food & Drink Style          |

        | :---------------- | :----------------- | :----------------------------------------- | :-------------------------- |
        | **Budget**        | $400 – $800        | Beach hostel                               | Street food                 |
        | **Mid-Range**     | $1,200 – $2,200    | Beach hotel                                | Restaurants                 |
        | **Luxury**        | $3,000+            | Luxury beachfront resort                   | Fine dining                 |""")

    elif place == "2" or "mountains":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                         | Food & Drink Style          |

        | :---------------- | :----------------- | :----------------------------------------- | :-------------------------- |
        | **Budget**        | $500 – $900        | Mountain guesthouse                        | Local meals                 |
        | **Mid-Range**     | $1,300 – $2,500    | Mountain resort                            | Restaurants                 |
        | **Luxury**        | $4,000+            | Luxury mountain lodge                      | Gourmet food                |""")

    elif place == "3" or "cruise":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                         | Food & Drink Style          |

        | :---------------- | :----------------- | :----------------------------------------- | :-------------------------- |
        | **Budget**        | $800 – $1,300      | Cruise cabin                               | Buffet meals                |
        | **Mid-Range**     | $1,800 – $3,000    | Ocean-view cabin                            | International food          |
        | **Luxury**        | $4,000+            | Luxury cruise suite                        | Fine dining                 |""")

    elif place == "4" or "hiking":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                         | Food & Drink Style          |

        | :---------------- | :----------------- | :----------------------------------------- | :-------------------------- |
        | **Budget**        | $400 – $900        | Camping & hostels                          | Local food                  |
        | **Mid-Range**     | $1,200 – $2,000    | Hiking lodge                               | Restaurants                 |
        | **Luxury**        | $3,000+            | Luxury eco-resort                          | Gourmet meals               |""")

    elif place == "5" or "adventure":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                         | Food & Drink Style          |

        | :---------------- | :----------------- | :----------------------------------------- | :-------------------------- |
        | **Budget**        | $600 – $1,100      | Budget hotel                               | Street food                 |
        | **Mid-Range**     | $1,500 – $2,500    | Adventure lodge                            | Local restaurants           |
        | **Luxury**        | $3,500+            | Luxury resort                              | Fine dining                 |""")

    elif place == "6" or "ski and winter holidays":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                         | Food & Drink Style          |

        | :---------------- | :----------------- | :----------------------------------------- | :-------------------------- |
        | **Budget**        | $800 – $1,400      | Ski hostel                                 | Cafes                       |
        | **Mid-Range**     | $2,000 – $3,200    | Ski resort                                 | Mountain restaurants        |
        | **Luxury**        | $4,500+            | Luxury ski chalet                          | Fine dining                 |""")

    elif place == "7" or "island getaways":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                         | Food & Drink Style          |

        | :---------------- | :----------------- | :----------------------------------------- | :-------------------------- |
        | **Budget**        | $500 – $1,000      | Island hostel                              | Seafood & street food       |
        | **Mid-Range**     | $1,500 – $2,500    | Island resort                              | Restaurants                 |
        | **Luxury**        | $3,500+            | Private island villa                       | Gourmet dining              |""")


elif cont == "5" or cont == "africa":

    place = input("What type of place in South Africa, (Choose from the options below)\n 1. Beach\n  2. Mountains\n   3. Safari\n    4. Hiking\n     5. Adventure\n      6. Ski and Winter Holidays\n       7. Island Getaways\nType Here ==> ").strip().lower()

    if place == "1" or place == "beach":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                         | Food & Drink Style          |

        | :---------------- | :----------------- | :----------------------------------------- | :-------------------------- |
        | **Budget**        | R5000 – R9000      | Guesthouse near beaches                    | Local seafood & cafes       |
        | **Mid-Range**     | R12000 – R20000    | Beach hotel                                | Restaurants                 |
        | **Luxury**        | R30000+            | Luxury beachfront resort                   | Fine dining                 |""")

    elif place == "2" or "mountains":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                         | Food & Drink Style          |

        | :---------------- | :----------------- | :----------------------------------------- | :-------------------------- |
        | **Budget**        | R5000 – R8000      | Mountain cabin near Drakensberg            | Local meals                 |
        | **Mid-Range**     | R10000 – R18000    | Mountain lodge                              | Restaurant meals            |
        | **Luxury**        | R25000+            | Luxury mountain resort                      | Fine dining                 |""")

    elif place == "3" or "safari":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                         | Food & Drink Style          |

        | :---------------- | :----------------- | :----------------------------------------- | :-------------------------- |
        | **Budget**        | R7000 – R12000     | Camps near Kruger National Park             | Local food                  |
        | **Mid-Range**     | R15000 – R30000    | Safari lodge                                | Meals included              |
        | **Luxury**        | R50000+            | 5-Star private game lodge                   | Luxury dining               |""")

    elif place == "4" or "hiking":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                         | Food & Drink Style          |

        | :---------------- | :----------------- | :----------------------------------------- | :-------------------------- |
        | **Budget**        | R4000 – R8000      | Hiking camps                                | Packed meals                |
        | **Mid-Range**     | R10000 – R18000    | Mountain lodges                             | Restaurants                 |
        | **Luxury**        | R25000+            | Private eco-lodge                           | Gourmet meals               |""")

    elif place == "5" or "adventure":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                         | Food & Drink Style          |

        | :---------------- | :----------------- | :----------------------------------------- | :-------------------------- |
        | **Budget**        | R5000 – R10000     | Budget accommodation                       | Local restaurants            |
        | **Mid-Range**     | R12000 – R25000    | Adventure lodge                             | South African cuisine       |
        | **Luxury**        | R40000+            | Luxury resort                               | Fine dining                 |""")

    elif place == "6" or "ski and winter holidays":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                         | Food & Drink Style          |

        | :---------------- | :----------------- | :----------------------------------------- | :-------------------------- |
        | **Budget**        | R5000 – R9000      | Mountain accommodation                     | Cafes                      |
        | **Mid-Range**     | R12000 – R20000    | Mountain resort                             | Restaurants                |
        | **Luxury**        | R30000+            | Luxury lodge                                | Fine dining                |""")

    elif place == "7" or "island getaways":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                         | Food & Drink Style          |

        | :---------------- | :----------------- | :----------------------------------------- | :-------------------------- |
        | **Budget**        | R6000 – R10000     | Coastal guesthouse                          | Seafood                     |
        | **Mid-Range**     | R15000 – R25000    | Beach resort                                | Restaurants                 |
        | **Luxury**        | R35000+            | Private coastal villa                       | Gourmet dining              |""")


elif cont == "6" or cont == "australia":

    place = input("What type of place in Australia, (Choose from the options below)\n 1. Beach\n  2. Mountains\n   3. Cruise\n    4. Hiking\n     5. Adventure\n      6. Ski and Winter Holidays\n       7. Island Getaways\nType Here ==> ").strip().lower()

    if place == "1" or place == "beach":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                         | Food & Drink Style          |

        | :---------------- | :----------------- | :----------------------------------------- | :-------------------------- |
        | **Budget**        | $700 – $1200       | Beach hostel                               | Cafes & local food          |
        | **Mid-Range**     | $1800 – $3000      | Beach hotel                                | Restaurants                 |
        | **Luxury**        | $4000+             | Luxury beachfront resort                   | Fine dining                 |""")

    elif place == "2" or "mountains":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                         | Food & Drink Style          |

        | :---------------- | :----------------- | :----------------------------------------- | :-------------------------- |
        | **Budget**        | $700 – $1200       | Mountain cabin                             | Local meals                 |
        | **Mid-Range**     | $1500 – $2800      | Mountain lodge                              | Restaurants                 |
        | **Luxury**        | $4000+             | Luxury mountain resort                      | Fine dining                 |""")

    elif place == "3" or "cruise":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                         | Food & Drink Style          |

        | :---------------- | :----------------- | :----------------------------------------- | :-------------------------- |
        | **Budget**        | $1000 – $1500      | Cruise cabin                               | Buffet meals                |
        | **Mid-Range**     | $2500 – $3500      | Ocean-view cabin                            | Restaurants                 |
        | **Luxury**        | $5000+             | Luxury cruise suite                         | Fine dining                 |""")

    elif place == "4" or "hiking":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                         | Food & Drink Style          |

        | :---------------- | :----------------- | :----------------------------------------- | :-------------------------- |
        | **Budget**        | $600 – $1000       | Camping areas                              | Packed meals                |
        | **Mid-Range**     | $1500 – $2500      | Hiking lodge                               | Restaurants                 |
        | **Luxury**        | $3500+             | Luxury eco-lodge                           | Gourmet meals               |""")

    elif place == "5" or "adventure":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                         | Food & Drink Style          |

        | :---------------- | :----------------- | :----------------------------------------- | :-------------------------- |
        | **Budget**        | $800 – $1300       | Budget hotel                               | Local food                  |
        | **Mid-Range**     | $2000 – $3500      | Adventure resort                          | Restaurants                 |
        | **Luxury**        | $5000+             | Luxury wilderness resort                   | Fine dining                 |""")

    elif place == "6" or "ski and winter holidays":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                         | Food & Drink Style          |

        | :---------------- | :----------------- | :----------------------------------------- | :-------------------------- |
        | **Budget**        | $900 – $1500       | Ski lodge                                  | Cafes                       |
        | **Mid-Range**     | $2000 – $3500      | Ski resort                                 | Mountain restaurants        |
        | **Luxury**        | $5000+             | Luxury ski chalet                           | Fine dining                 |""")

    elif place == "7" or "island getaways":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                         | Food & Drink Style          |

        | :---------------- | :----------------- | :----------------------------------------- | :-------------------------- |
        | **Budget**        | $800 – $1300       | Island hostel                              | Seafood                     |
        | **Mid-Range**     | $1800 – $3000      | Island resort                              | Restaurants                 |
        | **Luxury**        | $4500+             | Private island villa                       | Gourmet dining               |""")


elif cont == "7" or cont == "antarctica":

    place = input("What type of place in Antarctica, (Choose from the options below)\n 1. Expedition Cruise\n  2. Mountains\n   3. Wildlife Adventure\n    4. Hiking\n     5. Photography Adventure\n      6. Winter Experience\n       7. Island Exploration\nType Here ==> ").strip().lower()

    if place == "1" or place == "expedition cruise":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                         | Food & Drink Style          |

        | :---------------- | :----------------- | :----------------------------------------- | :-------------------------- |
        | **Budget**        | $5000 – $8000      | Basic expedition ship                      | Included meals              |
        | **Mid-Range**     | $9000 – $15000     | Comfortable cruise cabin                    | Restaurant meals            |
        | **Luxury**        | $20000+            | Luxury expedition ship                      | Fine dining                 |""")

    elif place == "2" or "mountains":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                         | Food & Drink Style          |

        | :---------------- | :----------------- | :----------------------------------------- | :-------------------------- |
        | **Budget**        | $6000 – $9000      | Expedition ship                            | Included meals              |
        | **Mid-Range**     | $10000 – $16000    | Polar lodge                                | Hot meals                   |
        | **Luxury**        | $25000+            | Luxury polar accommodation                 | Gourmet dining              |""")

    elif place == "3" or "wildlife adventure":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                         | Food & Drink Style          |

        | :---------------- | :----------------- | :----------------------------------------- | :-------------------------- |
        | **Budget**        | $5000 – $9000      | Expedition ship                            | Included meals              |
        | **Mid-Range**     | $10000 – $17000    | Polar cruise cabin                         | Restaurant meals            |
        | **Luxury**        | $25000+            | Luxury expedition suite                    | Fine dining                 |""")

    elif place == "4" or "hiking":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                         | Food & Drink Style          |

        | :---------------- | :----------------- | :----------------------------------------- | :-------------------------- |
        | **Budget**        | $6000 – $10000     | Expedition camp                            | Simple meals                |
        | **Mid-Range**     | $12000 – $18000    | Adventure ship                             | Included meals              |
        | **Luxury**        | $30000+            | Premium expedition                         | Luxury dining               |""")

    elif place == "5" or "photography adventure":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                         | Food & Drink Style          |

        | :---------------- | :----------------- | :----------------------------------------- | :-------------------------- |
        | **Budget**        | $5000 – $9000      | Expedition vessel                          | Included meals              |
        | **Mid-Range**     | $10000 – $17000    | Polar cruise cabin                         | Restaurant meals            |
        | **Luxury**        | $25000+            | Luxury polar suite                         | Fine dining                 |""")

    elif place == "6" or "winter experience":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                         | Food & Drink Style          |

        | :---------------- | :----------------- | :----------------------------------------- | :-------------------------- |
        | **Budget**        | $7000 – $11000     | Research-style camp                        | Basic meals                 |
        | **Mid-Range**     | $15000 – $20000    | Expedition accommodation                   | Warm meals                  |
        | **Luxury**        | $30000+            | Luxury polar camp                           | Gourmet food                |""")

    elif place == "7" or "island exploration":
        print("""        | Travel Style      | Average Total Cost | Accommodation Type                         | Food & Drink Style          |

        | :---------------- | :----------------- | :----------------------------------------- | :-------------------------- |
        | **Budget**        | $5000 – $9000      | Expedition ship                            | Included meals              |
        | **Mid-Range**     | $10000 – $16000    | Cruise cabin                               | Restaurants                 |
        | **Luxury**        | $25000+            | Luxury expedition suite                    | Fine dining                 |""")

    else:
        print("Invalid Input")


else:
    print("Invalid Input")


print("Hope you enjoy your Holiday, Bye", name)
print("Use this Holiday Planner Again!!!")