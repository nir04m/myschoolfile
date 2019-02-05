dark = True
while True:
    if dark == True:
        print('It is dark.')
    cmd = input('? ')
    if cmd == 'eat':
        print('Nom nom nom.')
    elif cmd == 'drink':
        print('Glug glug glug *burp*')
    elif cmd == 'look':
        if dark == True:
            print('Did I mention that it was dark?')
        else:
            print('You are in a maze of twisty little passages, all alike.')
    elif cmd == 'lantern':
        print('You are enlightened.')
        dark = False
    elif cmd == 'quit':
        break
    else:
        print("I don't know that command.")

