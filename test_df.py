# -*- coding: utf-8 -*-
import random
import pandas as pd

if __name__ == '__main__':
    
    id = []
    text=['A','B','C','D','E']
    name = []
    namelistF = ['Thom','Walter','Alexis','Allan','Hubert','Amy','Anastasia','Lorna','Barbara']
    namelistL=['Abernethy','Ackroyd','Collins','Guises','Haworth','Hayden','Kingsley','Leyland','McLennan']

    for i in range(200):
        id.append(text[random.randint(0,len(text))-1] + text[random.randint(0,len(text))-1] + str(random.randint(0,len(text))) + str(random.randint(0,9)) + str(random.randint(0,9) )+ str(random.randint(0,9)))
        name.append(namelistF[random.randint(0,len(namelistF)-1)] + ' ' + namelistL[random.randint(0,len(namelistL)-1)])

    data = {'ID' : id,
            'Name' : name}

    frame = pd.DataFrame(data)

    print(frame)
    test_df = frame[frame['ID'].str.contains('24')]
    print(test_df['ID'])
