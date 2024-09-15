formatter ="{} {} {} {}"

formatter1 ="{} {} {} and {}"

print(formatter.format(1,2,3,4))
print(formatter.format('Jan','Feb','Mar','Apr'))
print(formatter.format(True,False,True,False))
print(formatter.format(formatter1,formatter1,formatter1,formatter1))


print(formatter.format("Python is an",
                       "Interpreted Language",
                       ". It excecuted the code",
                       "line by line"))
