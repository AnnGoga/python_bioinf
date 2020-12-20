 dict = []

 def FirstTask(i):
   while i != "":
     i = input()
     if i == "":
         return dict
     dict.append(i)
   return dict

 def SecondTask():
   sum = 0
   for i in dict:
     sum = int(i) + sum
   return sum

 def ThirdTask():
   max = dict[0]
   for i in dict:
     if int(max) < int(i):
       max = i
   return max


 print (FirstTask(0))
 print (SecondTask())
 print (ThirdTask())