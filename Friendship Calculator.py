alphabet='bcghjklmpqrtvwxyz'
score=0
names=input('Enetr first name and give space and then enter second name:-')
for character in names:
    if character in 'aeiou':
        score+=5
    if character in 'friends':
        score+=10
    if character in alphabet:
        score+=alphabet.find(character)
    else:
        score+=0
if score>100:
    print('your friendship score is: ',score)
    print('Congratulation! you both are the best friends')
else:
    print('your friendship score is: ',score)
