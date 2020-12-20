 ins = str(input())
 string = ins.lower()
 vowels = ['a', 'u', 'i', 'o', 'e']

 def firsttask(string, vowels):
   for i in vowels:
     string = string.replace(i, '')
   print (string)

 def secondtask(string, vowels):
   dict = []
   for i in vowels:
     if string.find(i) != -1:
         dict.append(i)
   print (dict)

 def thirdtask(string, vowels):
   dict = []
   for i in vowels:
     if string.find(i) != -1:
       dict.append(i)
   print (len(dict))

 def fourtask(string, vowels):
   dict = []
   for i in vowels:
     if string.find(i) != -1:
       dict.append(i)
       dict.append(string.count(i))
   print (dict)

 firsttask(string, vowels)
 secondtask(string, vowels)
 thirdtask(string, vowels)
 fourtask(string, vowels)