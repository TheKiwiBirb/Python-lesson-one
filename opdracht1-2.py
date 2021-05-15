print('Welkom bij dit programma')
print('Wat is jouw leeftijd?')
age = int(input())
print('Wat is jouw geslacht? Typ "Man" of "Vrouw"')
sex = input()
if sex == 'Man':
    print('Jij hebt een sluf')
elif sex == 'Vrouw':
    print('Er zit een gat in')
else:
    print('Sorry geen helicopters toegestaan!')
