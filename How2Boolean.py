##Zero always returns False
if 0 == True:
    print("0 returns 'True'!")
elif 0 == False:
    print("0 returns 'False'!")
else:
    print("Fuck.")

##Add 'not' before something to reverse its normal boolean return value
myWords = True

if not myWords:
    print("'myWords' is True, and 'not myWords' returned True.")
else:
    print("'myWords' is true, and 'not myWords' returns False.")
