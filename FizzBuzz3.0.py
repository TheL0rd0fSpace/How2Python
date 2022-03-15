from sys import exit

class Number():
    def __init__(self,number):
        self.title = ''
        if number%3 == 0:
            self.title = self.title + 'Fizz'
        elif number%5 == 0:
            self.title = self.title + 'Buzz'
        else:
            self.title = number

def YN(reply):
    if reply == 'Y':
        print("User has accepted.")
        return True
    elif reply == 'N':
        print("User has declined.")
        return False
    else:
        return False

def choose_number(userReply):
    try:
        output = int(userReply)
    except:
        print("You have not typed an integer. Please try again")
        return False
    else:
        ("You have typed an integer.")
        return True


while True:
    notreadytoplay = True
    while notreadytoplay:
        print("How long would you like to play FizzBuzz?")
        try:
            game_length = int(input())
            break
        except:
            print("You have not typed an integer. Please try again.")



if game_length > 0:
    print(f"You will play FizzBuzz for {game_length}. Okay? Y/N")
    if YN(input()):
        print("dummy codeY")
    else:
        ("You want to play for a different length.")





print("Success! For now....")
