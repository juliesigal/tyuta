import random

def check_letter(lst1,ltt,lst2,count):
    for i in range(len(lst1)):
        if lst1[i] == ltt:
            lst2[i] = ltt
    return "".join(lst2)

def get_string(a):
    lst3 = []
    for i in a:
        for j in i:
            lst3.append(j)
        lst3.append(' ')
    return lst3


_main_ls = [['always', 'be', 'yourself'],['beilive', 'in', 'yourself'],['never', 'say', 'never'],['dreams', 'comes', 'true'],['always', 'stay', 'strong'],['keep', 'it', 'cool'],['trust', 'in', 'yourself'],['whatever', 'you', 'like'],['the', 'rolling', 'stones'],['guns', 'and', 'roses']]
_choice = random.randint(0,9)
lst_words = _main_ls[_choice]
counter = 0
_currnt_ls = ["_" * len(i) for i in lst_words]
print('Hello and welcome to the guess words game! Every right guess you get 5 points and wrong guess u lose 1 point. Good luck dear user' )
print(' '.join(_currnt_ls))

new_hidden_st = get_string(lst_words)
new_under_st = get_string(_currnt_ls)
while '_' in new_under_st:
    letter = input('please enter letter: ')
    print(check_letter(new_hidden_st,letter,new_under_st,counter))
    if letter in new_under_st:
        counter = counter + 5
    else:
        counter = counter - 1
    print('Your current score is:', counter)

print('your final score is: ', counter)
