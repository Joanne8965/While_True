while True:
    mode = input('請輸入遊戲模式/Please choose one of the game mode： ')
    if mode == 'q':  # quit
        break
    elif mode == '1':
        print('啟動模式一/Game Mode1')
    elif mode == '2':
        print('請動模式二/Game Mode2')
    else:
        print('只能輸入1/2/q Please select 1/2/q mode')
