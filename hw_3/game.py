import player, x_o_maps


def start():
    print("Выберите режим игры:\n1-Игрок-Игрок\n2-Игрок-Искуственный интелект")
    var = int(input())
    if(var == 1):
        user1 = player.User("X")
        user1.set_name(input("Введите имя первого игрока: "))
        user2 = player.User("O")
        user2.set_name(input("Введите имя второго игрока: "))
        play(user1, user2)
    if(var == 2):
        user1 = player.User("X")
        user1.set_name(input("Введите имя игрока: "))
        bot = player.II("O")
        play(user1, bot)
        

    
    


def play(user_1:player.Player, user_2:player.Player):
    maps = x_o_maps.X_o_maps()
    game = True
    user = user_1
    while(game):
        
        maps.print_maps()
        print(f'Ходит {user.name}')
        if(isinstance(user, player.II)):
            maps.update_maps(user.symbol, player.II.step(maps.get_maps()))
        else:
            while(maps.update_maps(user.symbol, int(input())) == False):
                print("Неправильный ход повторите попытку!")
        result = maps.result_game()
        if(result!= None):
            game = False
            if(result == user.symbol):
                print(f"Победил {user.name}")
            else: print(result)
        if(user == user_2):
            user = user_1
        elif user == user_1:
            user = user_2       
