#defining a funcion that returns if the year passed was a leap year or not
def is_leap(year):
    
    leap = False
    
    if(year % 400 == 0 or year % 4 == 0 and year % 100 != 0):
      leap = True
      
    return leap

#simply getting the input
year = int(input())
print(is_leap(year))