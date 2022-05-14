""" Madlibs game using string concatenation in python """

# youtuber = "Adrino"
# print(f"Subscribe to {youtuber}")
# print(f"Hello my name is {youtuber}")
# print("You are watching {}".format(youtuber))

QUALITY_1 = str(input("Enter a self-quality that you have: "))
ACTION_1 = str(input("Enter a action word: "))
VERB = str(input("Enter a verb: "))
FAMOUS_PERSON = str(input("Enter the name of a famous person: "))
print(f"With great {QUALITY_1} comes great responsibility. \
    Never {ACTION_1} yourself. \
        Always keep yourself {VERB} like {FAMOUS_PERSON}")


def game1(noun, verb1, adjective, self_quality):
    """This function basically takes three different catagories of words and arguments and
    generates a whole new sentence after concatenating them. Same applies to game2() """
    print(f"Hello {noun}, I hope your are {verb1}. You are very {adjective} \
            You are a very {self_quality} person.")


def game2(your_name, famous_person, favourite_location):
    print(f"Hello my name is {your_name}. \
            {famous_person} is my mom.\
                {favourite_location} is where I live")


game1("adrino", "playing", "tasty", "optimism")
game2("eric", "eminem", "Singapore")
