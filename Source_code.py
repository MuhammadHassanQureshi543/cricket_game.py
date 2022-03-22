user_1 = input("What you want to play bating or bolling : ")
user_name = input("Enter your name : ")
low = user_1.lower()
score = 0
game_over = False
cpu = 0

while not game_over:
    import random
    com = random.randint(1,6)
    if low == "bating":
        print(f"****{user_name} is now batting****")
        first = int(input("Please enter a number 1 to 6 : "))
        if first ==  com:
            print(f"{user_name} You are out :( !!! You make {score} runs")
            game_over = True
            break
        if first == 1:
            score += 1
            print(f"{user_name} makes 1 run :) ")
        if first == 2:
            score += 2
            print(f"{user_name} makes 2 run :) ")
        if first == 3:
            score += 3
            print(f"{user_name} makes 3 run :) ")
        if first == 4:
            score +=4
            print(f"{user_name} makes 4 run :) ")
        if first == 5:
            score += 5
            print(f"{user_name} makes 5 run :) ")
        if first == 6 :
            score += 6
            print(f"{user_name} makes 6 run :) ")
        if first == 50:
            print(f"{user_name} You make half century ")
        if first == 100:
            print(f"You make Century ")
        

    if low == "bolling":
        print(f"****{user_name} is now bolling****")
        second = int(input("Please enter a number 1 to 6 : "))

        if second == com:
            print(f"{user_name} You out the CPU :) and You Win !!! and CPU makes {cpu} runs")
            game_over = True
            break
        else:
            cpu += com
            print(f"{user_name} You didnot out any player :( and CPU makes {cpu} runs !!!")
            continue
    
     
