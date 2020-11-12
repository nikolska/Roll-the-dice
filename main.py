import random


def roll_the_dice(data):
    list_of_data = [i for i in data]
    first_part = 0
    last_part = 0
    action = ''
    number_of_dice = 0
    type_of_dice = 0
    answer = []
    for i in list_of_data:
        if '+' in list_of_data:
            first_part = data.split('+')[0]
            last_part = data.split('+')[-1]
            action = '+'
        elif '-' in list_of_data:
            first_part = data.split('-')[0]
            last_part = data.split('-')[-1]
            action = '-'
        elif '+' or '-' not in data:
            first_part = data
            last_part = 0
    for i in first_part:
        if 'D' in first_part:
            number_of_dice = first_part.split('D')[0]
            if not number_of_dice:
                number_of_dice = 1
            type_of_dice = first_part.split('D')[-1]
        else:
            return 'The string is not valid!'
    if type_of_dice not in cube_types:
        return 'The string is not valid!'
    rand_num = random.randint(1, int(type_of_dice))
    if action == '+':
        answer = int(number_of_dice) * rand_num + int(last_part)
    elif action == '-':
        answer = int(number_of_dice) * rand_num - int(last_part)
    else:
        answer = int(number_of_dice) * rand_num
    return answer


cube_types = ['3', '4', '6', '8', '10', '12', '20', '100']

print(roll_the_dice('2D10+10'))
print(roll_the_dice('2D3'))
print(roll_the_dice('D6'))
print(roll_the_dice('D12-1'))
print(roll_the_dice('D54-1'))
print(roll_the_dice('5451'))
print(roll_the_dice('D12/1'))
print(roll_the_dice('D12/1'))
print(roll_the_dice('5B68-1'))
