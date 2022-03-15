# target statement:
# "The quick brown fox jumped over the lazy dog."

def FORMATTED_LITERAL_F_STRING():
    print(f"The {adjectiveOne} {adjectiveTwo} {nounOne} jumped over the {adjectiveThree} {nounTwo}.")

#TAKES FIVE WORDS, FORMATS THEM INTO THE ICONIC PHRASE
def DOT_FORMATTED_STRING(wordOne,wordTwo,wordThree,wordFour,wordFive):
    print("The {} {} {} jumped over the {} {}.".format(wordOne,wordTwo,wordThree,wordFour,wordFive))

adjectiveOne = "quick"
adjectiveTwo = "brown"
adjectiveThree = "lazy"
nounOne = "fox"
nounTwo = "dog"
adjectiveFour = "lively"
adjectiveFive = "anxious"
nounThree = "kitty"

print("The " + adjectiveOne + adjectiveTwo + nounOne + " jumped over the " + adjectiveThree + nounTwo)

print("The {} {} {} jumped over the {} {}.".format(adjectiveOne,adjectiveTwo,nounOne,adjectiveThree,nounTwo))

print(f"The {adjectiveOne} {adjectiveTwo} {nounOne} jumped over the {adjectiveThree} {nounTwo}.")

adjectiveTwo = adjectiveFour

CLASSIC_LINE()

DOT_FORMATTED_STRING(adjectiveFour,adjectiveFive,nounThree,adjectiveOne,nounOne)
