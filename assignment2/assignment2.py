#!/usr/bin/python3
import itertools
import random


#//////////////////////// EXTERNAL RESOURCES /////////////////////////////
# Cryptomath Module
# http://inventwithpython.com/hacking (BSD Licensed)

def gcd(a, b):
    # Return the GCD of a and b using Euclid's Algorithm
    while a != 0:
        a, b = b % a, a
    return b


def findModInverse(a, m):
    # Returns the modular inverse of a % m, which is
    # the number x such that a*x % m = 1

    if gcd(a, m) != 1:
        return None # no mod inverse if a & m aren't relatively prime

    # Calculate using the Extended Euclidean Algorithm:
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 # // is the integer division operator
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

print()
print()
print("------------------------------------------------------------------------------------------------------------")
print("Home assignment 2, cryptography.")
print("Data for 8804307752.")
print("Your generator is g=12.")
print("For task 2, the receiver's public key is X=4 and the message is m=16.")
print("For task 3, your private key is x=10 and the ciphertext is (16,17)(4,8)(2,2).")
print("------------------------------------------------------------------------------------------------------------")
X=4
m=16
I=21
N=23
g=12

print('/////////// Task 1A //////////')
print()
print('The following table was obtained by calculating the values of g^i from i=0 to i=21 such that g^(i+1)=(g^i)*g.')
print('For example:')
print('g^0 mod',N,' = 12^0 mod',N,' = 1 mod',N,' = 1')
print('g^1 mod',N,' = 12^1 mod',N,' = (12^0)*12 mod',N,' = 12')
print('g^2 mod',N,' = 12^2 mod',N,' = (12^1)*12 mod',N,' = 12*12 mod 23 = 6')
print('g^3 mod',N,' = 12^3 mod',N,' = (12^2)*12 mod',N,' = 6 * 12 mod 23 = 3')
print(".")
print(".")
print(".")
print('an so on')

Z_starN= list()
Z_starN.append((g**0)%N)

for i in range(1,(I+1)):
    Z_starN.append((g**(i-1))*(g)%N)

print()
print()
print("Table1A")
print("------------------------------------------------------------------------------------------------------------")
print()
print("[row i]:               ",list(range(0,(I+1))))
print("[row g^i mod",N,"]:      ",Z_starN)
print("-------------------------------------------------------------------------------------------------------------")

print()
print('/////////// Task 1B 1 //////////')
print()

S=set(Z_starN)
print("After removing duplicates, S is:" ,S)

#   Generate all combinations of S and select one of them
#   randomly
combs=random.sample([list(t) for t in itertools.combinations(S,2)],5)

print()

#   print the combinations
print("5 random pairs from set S is ",combs, "and their multiplication mod",N, "is as follows:")

print()
combs_product=list()

#   Multiply members of each combination and mod the result by 23
for i in range(len(combs)):
    combs_product.append(combs[i][0]*combs[i][1]%N)
    print(str(combs[i][0])+" * "+str(combs[i][1])+" mod",N, "="+str(combs_product[i]))

#   print the products
print(combs_product)

#  Check if the set of products is also in S
print()
print("Is "+str(combs_product)+" in S?:",(set(combs_product).issubset(S))) 
print("Therefore S is closed under multiplication")

print("------------------------------------------------------------------------------------------------------------")
print()

#   <<code segment task2a>>
print('/////////// Task 2A //////////')
print()

print("Since Alice's public key, X is", X, ", and g^x mod",N, "=", X )

x_values=[i for i, x in enumerate(Z_starN) if x ==X]

print("It follows that",X, "maps to i =",x_values )
print("Since 0 < x <= 10, it follows that x is ", x_values[0])
print("Therefore, Alice's secret key is: ",x_values[0])

print("------------------------------------------------------------------------------------------------------------")
print()

print('/////////// TASK 2B //////////')
print()

randomExponent=random.choice(list(range(0,11)))
randomExponent=5

P=Z_starN[randomExponent]
K=(X**randomExponent)%N
C=K*m%N


print("Let a random exponent from [row i] of Table 1A  be: ","r ="+str(randomExponent))
print("The corresponding public key from [row g^i mod",N,"] is given by: P =",P)
print("Using Alice's receiver Key X =",X,", K is given by X^r mod",N," = ",X,"^",randomExponent,"mod",N," =",K)
print("The Message m =",m,"can be encrypted into Cyphertext C as follows: C=K*m mod", N,"=",K,"*",m,"mod",N,"=",C)
print("Using C and P, the message Alice receives is given by: m=(P,C)=",list([P,C]))


print("------------------------------------------------------------------------------------------------------------")
print()
print('/////////// TASK 2C //////////')
print()
K_alice=P**x_values[0]%N
modInv=findModInverse(K_alice,N);
m_alice=C*modInv%N
print("From Task 2A, we know that Alice's secret Key is x=",x_values[0])
print("The secret key will be used to find Key K as follows: K_alice= P^x mod",N,"=",P,"^",x_values[0],"mod",N,"=",K_alice)
print("Knowing the key, the message m can be decrypted from ciphertext C as follows: m = C/K = C*K^(-1) mod",N,"=",C,"*",K,"^(-1) mod",N,"=",C,"*",modInv,"mod",N,"=",m_alice)

#-------------------------------------------------------------------------------------------------------------------
print()
print("Proof for 8x12^(-1) mod 23 = 8 x 2 mod 23 by  Euclidean Extend Algorithm")
print()
print("12^(-1) mod 23 can be expressed as follows:")
print("23   = 12   + 11  => 11 = 23   - 12")
print("12   = 11   + 1   => 1  = 12   - 11 = 12 - (23 - 12) = 12 - 23 + 12 = 12x2 - 23")
print("Dividing by [12] on both sides we get 12^(-1) = 2 - (23/12)")
print("Therefore: 12^(-1) mod 23 = (2 mod 23) - 0    = 2 mod 23")
print("Hence 8x12^(-1) mod 23    = 8 x 2 mod 23      = 16 ")
print()

#-------------------------------------------------------------------------------------------------------------------

print("The decryprted message, m_alice is: ",m_alice, "which is the same as the one sent to alice, m=",m)

print("------------------------------------------------------------------------------------------------------------")
print()

print("For task 3, your private key is x=10 and the ciphertext is (16,17)(4,8)(2,2).")
X=10
print("Private Key, X=",X)
print("------------------------------------------------------------------------------------------------------------")
print()

c1=[16,17]
c2=[4,8]
c3=[2,2]

print('/////////// Task 3A //////////')
print()
print("Given private Key X =",X)
P=Z_starN[X]
print("The corresponding public key from [row g^i mod 23] corresponding to private Key",X, "in [row i] is",P)

print("------------------------------------------------------------------------------------------------------------")
print()
print('/////////// Task 3B //////////')
print()


k1=c1[0]**X%N
k2=c2[0]**X%N
k3=c3[0]**X%N

print("First ciphertext, c1 =",c1)
print("Second ciphertext, c2 =",c2)
print("Third ciphertext, c3 =",c3)
print()
print("For k1, we have: k1 =c1[0]^x mod",N,"=",c1[0],"*",X,"mod",N,"=",k1)
print("For k2, we have: k2 =c2[0]^x mod",N,"=",c2[0],"*",X,"mod",N,"=",k1)
print("For k3, we have: k3 =c3[0]^x mod",N,"=",c3[0],"*",X,"mod",N,"=",k1)



modInv1=findModInverse(k1,N);
modInv2=findModInverse(k2,N);
modInv3=findModInverse(k3,N);

m1=c1[1]*modInv1%N
m2=c2[1]*modInv2%N
m3=c3[1]*modInv3%N

print()
print("As in TASK 2 C, the message can be decoded to the following:")
print()
print("------------------------------------------------------------------------------------------------------------")
print()
print("Knowing k1, m1 can be decrypted from ciphertext c1[1] as follows: m1 = c1[1]/k1 = c1[1]*k1^(-1) mod",N,"=",c1[1],"*",k1,"^(-1) mod",N,"=",c1[1],"*",modInv1,"mod",N,"=",m1)


#-------------------------------------------------------------------------------------------------------------------
print()
print("Proof for 17x13^(-1) mod 23 = 17 x 16 mod 23 by  Euclidean Extend Algorithm")
print("---------------------------------------------------------------------------")
print()
print("13^(-1) mod 23 can be expressed as follows:")
print("23   =  13   + 10   => 10 = 23   - 13")
print("13   =  10   + 3    => 3  = 13   - 10")
print("10   =  3x3  + 1    => 1  = 10   - 3x3 = 10 - 3x(13 - 10) = 10 - 3x13 + 3x10 = 4x10 - 3x13 = 4x(23-13)-3x13 = 4x23-4x13 - 3x13 = 4x23 - 7x13")
print("Dividing by [13] on both sides we get 13^(-1)  = 4x(23/13) - 7")
print("Therefore: 13^(-1) mod 23 = 0 - (7 mod 23) = 16 mod 23")
print("Hence 17x13^(-1) mod 23   = 17 x 16 mod 23 = 19 ")
print()

#-------------------------------------------------------------------------------------------------------------------


print("------------------------------------------------------------------------------------------------------------")
print()
print("Knowing k2, m2 can be decrypted from ciphertext c2[1] as follows: m2 = c2[1]/k2 = c2[1]*k2^(-1) mod",N,"=",c2[1],"*",k2,"^(-1) mod",N,"=",c2[1],"*",modInv2,"mod",N,"=",m2)


#-------------------------------------------------------------------------------------------------------------------
print()
print("Proof for 8x6^(-1) mod 23 = 8 x 4 mod 23 by  Euclidean Extend Algorithm")
print("-----------------------------------------------------------------------")
print()
print("6^(-1) mod 23 can be expressed as follows:")
print("23   = 3x6   + 5   => 5 = 23   - 3x6")
print("6    = 5     + 1   => 1 = 6    - 5 = 6 - (23 - 3x6) = 6 - 23 +3x6 4x6 - 23")
print("Dividing by [6] on both sides we get 6^(-1) = 4 - 23/6")
print("Therefore: 6^(-1) mod 23 = (4 mod 23) - 0   = 4 mod 23")
print("Hence 8x6^(-1) mod 23    = 8 x 4 mod 23     = 9 ")
print()

#-------------------------------------------------------------------------------------------------------------------



print("------------------------------------------------------------------------------------------------------------")
print()
print("Knowing k3, m3 can be decrypted from ciphertext c3[1] as follows: m3 = c3[1]/k3 = c3[1]*k3^(-1) mod",N,"=",c3[1],"*",k3,"^(-1) mod",N,"=",c3[1],"*",modInv3,"mod",N,"=",m3)


#-------------------------------------------------------------------------------------------------------------------
print()
print("Proof for 2x12^(-1) mod 23 = 2 x 2 mod 23 by  Euclidean Extend Algorithm")
print("------------------------------------------------------------------------")
print()
print("12^(-1) mod 23 can be expressed as follows:")
print("23   =  12  + 11  => 11 = 23   -  12")
print("12   = 11   + 1   => 1  = 12   -  11 = 12 - (23 - 12) = 12 - 23 + 12 = 12x2 - 23")
print("Dividing by [12] on both sides we get 12^(-1) = 2 - (23/12)")
print("Therefore: 12^(-1) mod 23 = (2 mod 23) - 0    = 2 mod 23")
print("Hence 2x12^(-1) mod 23    = 2 x 2 mod 23      = 4 ")
print()
#-------------------------------------------------------------------------------------------------------------------

dict={1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J',11:'K',12:'L',13:'M',14:'N',15:'O',16:'P',17:'Q',18:'R',19:'S',20:'T',21:'U',22:'V',23:'W',24:'X',25:'Y',26:'Z'}


print()
print()

print("The message is:",m1,m2,m3,"=",dict[m1]+dict[m2]+dict[m3])
print()
print()
print("////////////////////////////////////////////// END OF ASSIGMENT 2 ///////////////////////////////////////////////////")




