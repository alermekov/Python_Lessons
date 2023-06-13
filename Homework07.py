# Задача 34

vowels = ['a', 'e', 'i', 'o', 'u', 'y']  

poem = input('Введите стихотворение: ')

phrases = poem.split() 

syllables = [] 

for phrase in phrases:
    words = phrase.split('-') 
    count = 0 
    for word in words:
        for letter in word:
            if letter.lower() in vowels:  
                count += 1
    syllables.append(count)  

if len(set(syllables)) == 1:  
    print('Парам пам-пам')
else:
    print('Пам парам')
    
    
# Задача 36

def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows+1):
        row = ""
        for j in range(1, num_columns+1):
            row += str(operation(i, j)) + " "
        print(row.strip())

print_operation_table(lambda x, y: x * y)



