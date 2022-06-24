import random

print("How many pencils would you like to use: ")
while True:
    try:
        pencils = int(input())
    except ValueError:
        print("The number of pencils should be numeric")
        continue
    if pencils <= 0:
        print("The number of pencils should be positive")
        continue
    print("Who will be the first (John, Jack): ")
    names = ["John", "Jack"]
    turn = ""
    user_turn = 0
    while True:
        name = input()
        bot = "Jack"
        player = "John"
        if name not in names:
            print("Choose between 'John' and 'Jack'")
            continue
        elif name == "John":
            turn = player
            break
        elif name == 'Jack':
            turn = bot
            break
    while True:
        if pencils <= 0:
            break
        print(f'{"|" * pencils}')
        if turn == player:
            print(f"{player}'s turn!")
            use = 0
            while True:
                try:
                    use = int(input())
                except ValueError:
                    print("Possible values: '1', '2' or '3'")
                    continue
                if use > 3:
                    print("Possible values: '1', '2' or '3'")
                elif use <= 0:
                    print("Possible values: '1', '2' or '3'")
                elif use > pencils:
                    print("Too many pencils were taken")
                else:
                    user_turn = use
                    break
            pencils -= use
            turn = bot
            if pencils == 0:
                print(f'{names[1]} won!')
        elif turn == bot:
            print(f"{bot}'s turn:")
            rand = random.choice([1, 2, 3])
            while True:
                if pencils % 4 == 0:
                    print("3")
                    pencils -= 3
                elif pencils % 4 == 3:
                    print("2")
                    pencils -= 2
                elif pencils % 4 == 2:
                    print("1")
                    pencils -= 1
                else:
                    if pencils == 1:
                        print(1)
                        pencils -= 1
                    else:
                        print(rand)
                        pencils -= rand
                turn = player
                if pencils == 0:
                    print(f'{names[0]} won!')
                break
    break
