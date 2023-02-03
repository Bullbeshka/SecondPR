import calendar
Year = int(input("Год?: "))
leap = bool(calendar.isleap(Year))
Count, i, j = 0, 0, 0   
list1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31 , 30, 31]
list2 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31 , 30, 31]
if leap == False:
    while i<len(list1):
        j = int(list1[i])
        while j !=0:
            first, second = divmod(j, 10) 
            Count += (first + second)
            j-=1
        i+=1
if leap == True:
    while i<len(list2):
        j = int(list2[i])
        while j !=0:
            first, second = divmod(j, 10) 
            Count += (first + second)
            j-=1
        i+=1
print(f"Сумма всех чисел: {Count}")
