print("Arithmetic Exception")
try:  
    a = int(input("Enter a:"))    
    b = int(input("Enter b:"))    
    c = a/b  
except:  
    print("Can't divide with zero")  
print("")
print("IOError")
try:         
    fileptr = open("file.txt")    
except IOError:    
    print("File not found")    
else:    
    print("The file opened successfully")    
    fileptr.close() 
print("")
print("Value Error")
try:  
     num = int(input("Enter a positive integer: "))  
     if(num <= 0):    
         raise ValueError("That is  a negative number!")  
except ValueError as e:  
     print(e)    
print("")
print("Index Error")
a = [0,1,2,3,4]
try:
    print(a[5])
except IndexError:
    print("Key not Found")