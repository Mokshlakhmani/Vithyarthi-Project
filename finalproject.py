import numpy as np
def Batting_human():
    t1 = []
    t2 = []
    for i in range(1, 7):
        c = int(input(f"enter batter's choice for ball {i}: "))
        u = int(input(f"enter baller's choice for ball {i}: "))
        if u<7 and c<7:
            if u != c:
              t1.append(c)
              t2.append(u)
            else:
              print("ohh its an out")
              break
        else:
          print("Wrong number enter you loss your batting")    
          break
    print("numbers input by batter: ",t1)
    print("numbers input by baller: ",t2)
    return t1

def Bowling_human():
    t1 = []
    t2 = []
    for i in range(1, 7):
        c = int(input(f"enter baller's choice for ball {i}: "))
        u = int(input(f"enter batter's choice for ball {i}: "))
        if u<7 and c<7:
            if u != c:
              t1.append(c)
              t2.append(u)
            else:
              print("ohh its an out")
              break
        else:
          print("Wrong number enter you loss your batting")    
          break
    print("numbers input by baller",t1)
    print("numbers input by batter",t2)
    return t2

def bat_first_human():
    A = Batting_human()
    arr1 =np.array(A)
    x=arr1.sum()
    print("total score for the palyer who choose batting first is: ",x)
    print("Now it's bowling for the player who done batting first")
    B = Bowling_human()
    arr2 =np.array(B)
    y = arr2.sum()
    print("total score for the player who has done batting second is: ",y)
    if x==y:
        return 1
    elif x > y:
        return 2
    else:
        return 3

def bowl_first_human():
    A = Bowling_human()
    arr1 =np.array(A)
    x=arr1.sum()
    print("total score for the palyer who choose batting first is: ",x)
    print("Now it's bowling for the player who done batting first")
    B = Bowling_human()
    arr2 =np.array(B)
    y = arr2.sum()
    print("total score for the player who has done batting second is: ",y)
    if x==y:
        return 1
    elif x > y:
        return 2
    else:
        return 3

print("Game OOD-EVEN")
print("Game instruction:-")
print("You can take out number only between 1 ands 6")
print("If entered wrong number then you will loss your batting")

choice=input("enter E for even and O for odd: ")
player_1 = int(input("Enter any number between 1 to 6 for player 1: "))
player_2 = int(input("Enter any number between 1 to 6 for player 2: "))
if (player_1 + player_2) % 2 ==0 :
    if choice == "E":
      bat_bowl = input("Enter your choice for A-Batting first and B-Bowling first for player 1: ")
      if bat_bowl == "A":
          print("player 1 choose to do batting first")
          w=bat_first_human()
          if w==1:
              print("it's a draw for both")
          if w==2:
              print("player 1 won the match")
          if w==3:
              print("player 2 won the match")
      else:
          print("player 1 choose to do balling first")
          w=bowl_first_human()
          if w==1:
              print("it's a draw for both")
          if w==2:
              print("player 2 won the match")
          if w==3:
              print("player 1 won the match")

    else:
        bat_bowl = input("Enter your choice for A-Batting first and B-Bowling first for player 2: ")
        if bat_bowl=="A":
            print("player 2 choose to do batting first")
            w=bat_first_human()
            if w==1:
              print("it's a draw for both")
            if w==2:
              print("player 2 won the match")
            if w==3:
              print("player 1 won the match")


        else:
            print("player 2 choose to do balling first")
            w=bowl_first_human()
            if w==1:
              print("it's a draw for both")
            if w==2:
              print("player 1 won the match")
            if w==3:
              print("player 2 won the match")

elif (player_1 + player_2) % 2 != 0 :
    if choice == "O":
        bat_bowl = input("Enter your choice for A-Batting first and B-Bowling first  for player 1: ")
        if bat_bowl == "A":
            print("player 1 choose to do batting first")
            w=bat_first_human()
            if w==1:
              print("it's a draw for both")
            if w==2:
              print("player 1 won the match")
            if w==3:
              print("player 2 won the match")

        else:
            print("player 1 choose to do balling first")
            w=bowl_first_human()
            if w==1:
              print("it's a draw for both")
            if w==2:
              print("player 2 won the match")
            if w==3:
              print("player 1 won the match")

    else:
        bat_bowl = input("Enter your choice for A-Batting first and B-Bowling first for player 2: ")
        if bat_bowl=="A":
            print("player 2 choose to do batting first")
            w=bat_first_human()
            if w==1:
              print("it's a draw for both")
            if w==2:
              print("player 2 won the match")
            if w==3:
              print("player 1 won the match")


        else:
            print("player 2 choose to do balling first")
            w=bowl_first_human()
            if w==1:
              print("it's a draw for both")
            if w==2:
              print("player 1 won the match")
            if w==3:
              print("player 2 won the match")

else:
    print("ERROR")                                            
              

