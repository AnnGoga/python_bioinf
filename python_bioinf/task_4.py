def Task():
   dict = [2, 3, 5, 7, 11]
   while True:
     i = int(input())
     if i == "":
         break
     else:
       for num in dict:
         if (i % num) == 0:
           print ('Это число делится на', ' ', num)
         else:
           print ('Это число не делится на', ' ', num)
   return

 Task()