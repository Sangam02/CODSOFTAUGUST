import random

wordlist = []
SYMBOLS = ['@', '#', '$', '%',  ':', '?', '.', '/', '*']
with open("..\\1st project (Pass-Generator)\\strong pass\\wikipedia-text.txt", 'r' ) as file:
    data = file.readlines()
    

    for line in data:
        words = line.split()
        
        for item in words:
            if len(item) > 5:
                wordlist.append(item.capitalize())
word = random.choice(wordlist)
schar = random.choice(SYMBOLS)
num = str(random.randint(10,99))

pasw = word + schar + num
print(pasw)