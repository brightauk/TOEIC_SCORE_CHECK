answer = input('Enter The Real Answer: ').strip()
Number = int(input('Enter How Number of question: '))
Answer = []
'Real answer format = 1) D 2) C 3) A'
import re
word = " ".join(re.findall("[a-zA-Z]+", answer))
Answer = word.split(" ")
print('Enter Your Answer:')
#Your Answer format = 1)A'
                     #2)A"
                     #3)B'
my_answer = "" 
for i in range (Number):
    my_answer +=input() + '\n'

my_answer = " ".join(re.findall("[a-zA-Z]+", my_answer))
my_answer = my_answer.split(" ")

score = 0 
for i in range(Number): 
    if Answer[i] == my_answer[i]:
        score += 1
    else: print("Wrong at No." + str(i+1))
print('Your Score: ' + str(score) + '/' + str(Number) )
