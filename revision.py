# def calculation (a,b):
#     addition=a+b
#     multiply =a*b
#     return addition,multiply

    # RECURSIVE
#  def addition(num):
#      if num:
#         return num + addition(num-1)
#     else:
#         return 0

# Positional Arguments
# In positional arguments,we dont use the = operator

def minus(a,b):
    print(a - b)

    # args=Positional arguments

# def firstname(**names):
#     for name in names:
#         return(f"My name is{name}")   
#           print(f"hello {final}") 
# firstname("jem","wanjiru","wilson")

    ##kwargs
def firstname(**names):
    for name in names.values():
        print (name)    
firstname(a="jem",b="wanjiru",c="wilson")    

 



