# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
player_one = 'Ruud Gullit'
player_two = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = player_one + ' ' + str(goal_0) + ', ' + player_two + ' ' + str(goal_1)

report = f'{player_one} scored in the {goal_0}nd minute\n{player_two} scored in the {goal_1}th minute'

player = "Jan Wouters"
first_name = player[:player.find(" ")]
last_name = player[player.find(" ") + 1:]
last_name_len = len(player[player.find(" ") + 1:])
name_short = player[:1] + '. ' + last_name
chant = (first_name + '! ') * len(first_name)
chant = chant[:-1]
good_chant = chant[-1] != " "

print(chant)