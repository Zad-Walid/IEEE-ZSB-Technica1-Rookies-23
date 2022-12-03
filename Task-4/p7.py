print("enter num of words")
num = int(input())

list =[]
for i in range (0,num):
  n = str(input())
  list.append(n)

class S():
 def Anagrams(self,list):

    dictionary = {}
    for word in list:
        sortedWord = ''.join(sorted(word))
        if sortedWord not in dictionary:
            dictionary[sortedWord] = [word]
        else:
            dictionary[sortedWord] += [word]
    return [dictionary[i] for i in dictionary]


print(S().Anagrams(list))

