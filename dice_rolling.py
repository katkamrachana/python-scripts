#python2.7
import random
min = 1
max = 6

roll_again = "yes"

while roll_again in ["y", "Y"] or roll_again.lower() == "yes":
    print "Rolling the dice..."
    print "The value is: ", random.randint(min, max)
    roll_again = raw_input("Roll the dices again? Enter Y/Yes")