n1=float(input("enter your numbder:"))
n2=float(input("enter your numbder:"))

while n2!=0:
    t=n2
    n2=n1%n2
    n1=t
hcf=n1
print("HCF=", hcf)
