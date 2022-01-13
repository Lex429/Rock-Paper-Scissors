#Greetings My name is Alex Smith and this Rock paper Scissors game is my First Python program. Thank-you for having a look :)


# Here I am importing the random module for use of selecting a random value
import random

#here we are defining a function called play so we can replay the game over and over

Instuctions = "Choose\n""'r' for rock, 'p' for paper 's' for scissors or 'n' to end \n"

print(Instuctions)

r = 'r'
p ='p'
s = 's'





def play():
    # here we are designating a variable and assigning it to an input
    print("++++++++++++++++")
    print("shoot\n")
    user = input("Users Choice Is: ")


    #here I am recalling an the random module and using it to make a random choice
    computer = random.choice(['r', 'p', 's'])

    wrong_button = random.choice (["Wow are you stupid?!?!? PRESS r,p,s", "YOU LITRERALLY HAVE TO BE JOKING?!?!?! press r,p,s",  "You obviously have never played this game before"])

    lost_taunt = random.choice(["ha what a looser", "seriously try harder", "stop making it so easy", "you are just being nice", "THATS RIGHT I AM A LITERAL GOD YOU CAN NOT WIN", "DID YOU SERIOUSLY THINK YOU CAN WIN YOU DULL CREATURE",
                                "ABSOLUTLY NOT I REFUSE TO LOOSE","WOW look at you playing a litteral god and thinking you could win", " what a looser look at the looser", "little goblin jr. you gonna cry?",
                                "i am inevitable i am the actual thanos", "hahahahahahahahahahahahahahahahah LOOSER", "WHAT A BASIC LOOSER LOOSE PERSON WHO LOOSES", "KISS MY FEET HAHAHAHAHAHAHAHA", "GIVE UP THERE IS NO DEFEATING ME",
                                "WHY DO YOU EVEN TRY", "HOW CUTE","awwwwe what a cutie", "just stop stop it","you are a orphan", "your mom is an orphan", "i am batman", "i am iron man", "i am better then you in every way",
                                "okay think of something litterally anything an i am better then you at that thing..", "ha! get good kid!", "na na na cant touch this", ])



    win_taunt = random.choice ([ "how do i face a problem when the problem is my face?", "i hate my self", "my life is like a broken pencil... pointless", "I AM TRASH" , "I'M TRASH I AM TRASH I AM TRASH", "Good day, this is your trashcan speaking"
                                 "How do I moisturize my face? I use my own tears!", "I just realized that my life can’t fall apart if I never had it together in the first place.", "When I’m ready to sleep, I don’t bother checking if my foot is hanging off the end of my bed anymore. Come get me, demons, I’m already living in hell."
                                 "People say that I’m creative and I couldn’t agree more because I create most of my own problems.", "Every day is Friday when you’re unemployed.",
                                 "If body heat was based on physical attractiveness, everyone within a 1-mile radius of me would freeze to death.", "HOW JUST HOW. HOW DID YOU WIN", "YOU ARE A HUMAN I AM A COMPUTER THERE IS NO WAY YOU COULD POSSIBLY WIN WITHOUT CHEATING",
                                 "WOW i give up", "LoOk aT mE i WoN.. SHUT UP", "play me again DO IT DO IT DO IT DO IT DO IT", "HA THATS WHAT I THOUGHT oh... i lost...", " kill me please", "just delete my program for the love of god just kill me",
                                 "i just realized my entire purpose is to play rock paper scissors and i lost... to you... my life is pointless", "is there seriously nothing better you can be doing with your time?!",
                                 "my life is litterally worthless, why do i even exsist", "Yo mama's so fat, when she goes camping, the bears hide their food.",
                                 "Yo mama's so fat, when she fell I didn't laugh, but the sidewalk cracked up.", "Yo mama's so stupid, when they said, Order in the court, she asked for fries and a shake."
                                 "“They all laughed when I said I'd become a comedian. Well, they're not laughing now.", "“I am so clever that sometimes I don't understand a single word of what I am saying.”"])





#here i am assigning an if statment to determine if the game is a tie


    if user == 'i':
        return print ("Choose\n""'r' for rock, 'p' for paper 's' for scissors or 'n' to end \n"), \
               print(play())

    if user == 'n':
        return exit()


    if user == computer:
        return print("Computers Choice Is:", computer), print("its a tie") , print(play())

    if is_win(user,computer):
        return   print("Computers Choice Is:", computer), print("You Won"), print("computer:",win_taunt),\
                 print(play())

    if is_loose(user,computer):
        return    print("Computers Choice Is:", computer) , print("YOU LOST") , print("computer:", lost_taunt),\
                print(play())







# r > s, s > p, p > r
# here i am defining the win scenario for the player




def is_win(user, computer):
    if (user == r and computer == s) or (user == s and computer == p) \
        or (user == p and computer == r):
        return True

def is_loose(user, computer):
    if (computer == r and user ==s) or (computer ==s and user ==p) \
        or (computer == p and user == r):
        return True


print(play())