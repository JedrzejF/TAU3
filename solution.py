from nltk import trigrams
import datetime
from collections import defaultdict
from collections import OrderedDict
import itertools
import numpy as np
import math

dictionary = defaultdict(lambda: defaultdict(lambda: 0))

train = open('train/train.tsv', 'r', encoding='utf-8')
i = 0
for x in train.readlines()[0:59050]:
    i += 1
    x = x.split("\t")
    x[4].lower()
    for w1, w2, w3 in trigrams(x[4].split(), pad_left = True, pad_right = True):
        dictionary[(w1, w2)][w3] += 1
    if i%1000 == 0:
        print(datetime.datetime.now().time(), i)

for w1_w2 in dictionary:
    total_count = float(sum(dictionary[w1_w2].values()))
    for w3 in dictionary[w1_w2]:
        dictionary[w1_w2][w3] /= total_count
        dictionary[w1_w2][w3] = np.log(float(dictionary[w1_w2][w3]))

import math

test = open('test-A/in.tsv', 'r', encoding='utf-8')
with open('test-A/out.tsv', 'w+', encoding='utf-8') as test_result:
    for x in test.readlines():
         x = x.split("\t")
         x = x[2].lower()
         x = x.split(" ")
         rest = np.float(1)
         for w3 in dictionary[(x[-2], x[-1])]:
             if dictionary[(x[-2], x[-1])][w3] > -6:
                 rest -= math.e**(dictionary[(x[-2], x[-1])][w3])
                 test_result.write(str(w3).lower() + ':' + str(dictionary[(x[-2],x[-1])][w3])+ ' ')
         if rest < 0.000000001:
             rest = -20
         else:
             rest = np.log(rest)
         test_result.write(':' + str(rest) + '\n')

dev0 = open('dev-0/in.tsv', 'r', encoding='utf-8')
with open('dev-0/out.tsv', 'w+', encoding='utf-8') as dev0_result:
    for x in dev0.readlines():
         x = x.split("\t")
         x = x[2].lower()
         x = x.split(" ")
         rest = np.float(1)
         for w3 in dictionary[(x[-2], x[-1])]:
             if dictionary[(x[-2], x[-1])][w3] > -6:
                 rest -= math.e**(dictionary[(x[-2], x[-1])][w3])
                 dev0_result.write(str(w3).lower() + ':' + str(dictionary[(x[-2],x[-1])][w3])+ ' ')
         if rest < 0.000000001:
             rest = -20
         else:
             rest = np.log(rest)
         dev0_result.write(':' + str(rest) + '\n')

dev1 = open('dev-1/in.tsv', 'r', encoding='utf-8')
with open('dev-1/out.tsv', 'w+', encoding='utf-8') as dev1_result:
    for x in dev1.readlines():
         x = x.split("\t")
         x = x[2].lower()
         x = x.split(" ")
         rest = np.float(1)
         for w3 in dictionary[(x[-2], x[-1])]:
             if dictionary[(x[-2], x[-1])][w3] > -6:
                 rest -= math.e**(dictionary[(x[-2], x[-1])][w3])
                 dev1_result.write(str(w3).lower() + ':' + str(dictionary[(x[-2],x[-1])][w3])+ ' ')
         if rest < 0.000000001:
             rest = -20
         else:
             rest = np.log(rest)
         dev1_result.write(':' + str(rest) + '\n')