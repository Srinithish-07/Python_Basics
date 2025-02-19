'''Write a Python program to get the third side of a right-angled triangle from two given sides'''
def sides_of_Triangle(adj,hyp,opp):
    if adj == 'x':
        print("Adjacent = ",round((((float(hyp)**2)-(float(opp)**2))**0.5),2))
    if opp == 'x':
        print("Opposite = ", round((((float(opp)**2)-(float(adj)**2))**0.5),2))
    if hyp == 'x':
        print("Hypotenuse = ",round((((float(adj)**2)+(float(opp)**2))**0.5),2))
    else:
        print("you know the answer bro!")
    
print("To find any side give input as x to its respective input!!")
adj = input("enter Adjacent side : ")
opp = input("enter Opposite side : ")
hyp = input("enter Hypotenuse side : ")
sides_of_Triangle(adj,hyp,opp)
