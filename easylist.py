

'''
List all questions and hints from 100exercices.txt

The file is a bit of a mess, so it's not easy to split it.
3.	Questions

Questions are divided by #-----
Sometimes end with #---
They should contain:
Question:
Hints:
Example:
Solution:
'''

filename = '100exercices.txt'
allquestions = []

def main():
    start = False
    question = []
    with open(filename ,'r') as f:
        for line in f:
            if not start:
                if '3.	Questions' in line:
                    #start here:
                    start = True
            else:
                if '#--------------------' in line:
                    if len(question) >2:
                        allquestions.append(question)
                    question = []
                else:
                    line = line.strip()
                    if len(line) > 2:
                        question.append(line)

    while True:
        sel = input('Pick a question number (1,{})or (q)uit: '.format(len(allquestions)))
        if sel == 'q':
            exit()
        else:
            try:
                val = int(sel)-1
                result = getQuestion(val)
                playQuestion(result)
            except ValueError:
                print("That's not an int!")
            
    
def playQuestion(question):
    while True:
        print('(q)uestion, (h)int, (e)xample, (s)olution, (a)ll, e(x)it')
        sel = input('Pick one: ')
        if sel == 'q':
            printPart(question,'Question:')
        elif sel == 'h':
            printPart(question,'Hints:')
        elif sel == 'e':
            printPart(question,'Example:')
        elif sel == 's':
            printPart(question,'Solution:')
        elif sel == 'a':
            printQuestion(question)
        elif sel == 'x':
            return
    
def printPart(question,part):
    try:
        mypart = question[part]
        print()
        print(part)
        for l in mypart:
            print(l)
        print()
    except KeyError:
        print('{} missing'.format(part))

def printQuestion(question) :
    for k,v in question.items():
        print(k)
        for l in v:
            print(l)
        print("--")

def getQuestion(q_number):
    if q_number > len(allquestions):
        return False
    q = allquestions[q_number]

    list_block_titles = ['Question:','Hints:','Example:','Solution:']
    myblock = []

    question = {}    
    block_name = 'noname'
    for line in q:
        # https://stackoverflow.com/questions/3389574/check-if-multiple-strings-exist-in-another-string
        match = next((x for x in list_block_titles if x in line), False)
        if match:
            question[block_name] = myblock
            block_name = match
            myblock = []
        else:
            myblock.append(line)
    question[block_name] = myblock

    return question

if __name__ == '__main__':
	main()