print("\n          YOUR PLANE CRASHED!!\n        To an Abandoned Island\n")
print("""                        __
              __________/ F
            c'____---__=_/
           ___o_____o________""")
print(""" 
                       (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        """)

print("\n       WELCOME TO GORILLA TREASURE ISLAND!\n")
print("""                     ."`".
                 .-./ _=_ \.-.
                {  (,(oYo),) }}
                {{ |   "   |} }
                { { \(---)/  }}
                {{  }'-=-'{ } }
                { { }._:_.{  }}
                {{  } -:- { } }
                {_{ }`===`{  _}
               ((((\)     (/))))""")

input("Write any character to start\n")
print("You are standing at the sea shore, you body is wounded and you are bleeding, all the other passengers are dead, and your quest for survival begins......\nYou can go in three directions: \n1).Left \n2).Centre\n3).Right ....\n")
a = input()
if(a=='1'):
    print("You kept on bleeding and walking and you died....")
    exit()
elif(a=='3'):
    print("You went right and found a group of gorillas fighting each other, you remember that you read about DANGEROUS! gorilla island on your flight and gorillas caught you! and they chased and KILLED you....\n")
    exit()
elif(a=='2'):
  print("You went inside the forest and found some medicine leaves to heal your wounds and coconut to eat, now you can go:\n 1). cave or 2). climb the mountain\n")
else:
  print("you entered wrong input start the game again...")
  exit()

b = input()
if(b=='1'):
  print("You went inside cave and found Gorilla King, he thought of you as threat and decided to execute you!...\n")
  exit()
elif(b=='2'):
  print("You climb to the mountain top and you slept there for the night, next day you wake up and found yourself surrounded by Gorillas and you: \n1).Climb up the tree\n2).Run towards sea\n3).act like dead\n")
else:
  print("you entered wrong input start the game again...")
  exit()
c = int(input())
if(c==1):
  print("You climb the tree and you saw one gorilla also climbing... you :\n1).Kick him down \n2).Shake the tree\n 3).Jump off the tree\n")
  d = int(input())
  if(d==1 or d==2):
    print("You were caught by Gorilla and Died...\n")
    exit()
  elif(d==3):
    print("you jumped off the tree and broke your legs, you started crying and gorillas find it funny and they left you die...")
    exit()
  else:
    print("you entered wrong input start the game again...")
    exit()
elif(c==3):
  print("You acted like dead but that didn't worked on gorillas and they killed you...\n")
  exit()
elif(c==2):
  print("you went down the hill and jump in the sea and now gorillas cant reach you but you cant swim forever! so you swim to: \n1).left side\n 2).right side\n")
e = int(input())
if(e==1):
  print("You went left and Sharks eat you...\n")
  exit()
elif(e==2):
  print("you went right and found one gorilla on the shore, you picked up a stone and hit the gorilla from behind until he died, now you own his territory! now you will\n 1).Make a Boat\n2).Start a fire to signal on the sky\n3).Do Nothing and leave your fate to the gods!\n")
else:
  print("you entered wrong input start the game again...")
  exit()
f = int(input())
if(f==2):
  print("You start the fire to signal to skies but you also signal the Gorillas they found you and for killing thier brother they gave you a painful death...\n")
  exit()
elif(f==3):
  print("you prayed to god and God came to rescue you and when he saw your past deeds god decided to let you die and you starved to death...\n")
  exit()
elif(f==1):
  print("You made a Boat and now you will: \n1). Start a Fire to signal to the skies and if gorillas came escape from boat\n2). Escape from boat...\n")
else:
  print("you entered wrong input start the game again...")
  exit()
g = int(input())
if(g==2):
  print("You had nothing to eat and you starved to death...\n")
  exit()
elif(g==1):
  print("Your signal got detected by a plane but gorillas also came! now\n1).wait for helicopter to come down and leave the fate to god!\n2).fight the gorillas until helipcopter rescues you!\n")
h = int(input())
if(h==1):
  print("You got caught by Gorilla and were teared up in half for killing a Gorilla!")
  exit()
elif(h==2):
  print("You fought back and got injured but hopefully crew members had gun, they shot three gorillas and rescued you!!!\nCONGRATULATIONS YOU SURVIVED THE GORILLA TREASURE ISLAND\n")