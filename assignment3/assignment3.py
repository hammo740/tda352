#!/usr/bin/python3
import random
from sympy import *
print()
print("--------------------------------------------")
print("Name: Ruslan Masinjila")
print("Personnummer: 198804307752")
print("Home assignment 3, Cryptography")
print("--------------------------------------------")
print()
print("-----------------------------------------------------------------------")
print()
print("Part (A): Decentralised Voting Protocol")
print("--------")
print(">>Question 0")

# date of birth
Y1=1
Y2=9
Y3=8
Y4=8
M1=0
M2=4
D1=3
D2=0

print("My birthday is:",str(Y1)+str(Y2)+str(Y3)+str(Y4)+str(M1)+str(M2)+str(D1)+str(D2))

print()
print()

print(">>Question 1")
print("List of choices = [-1,1] where -1 is for the Christmas Concert and 1 is for Christmas Market")

choices=[-1,1]

print()
print("Given Polynomials:")
print()
print("m1(x) = v1 - Y1x + M1x^2")
print("m2(x) = v2 - Y2x + M2x^2")
print("m3(x) = v3 - Y3x + D1x^2")
print("m4(x) = v4 - Y4x + D2x^2")
print()
print()

# Variables common to all members
x1=1
x2=2
x3=3



v1=random.choice(choices)
m1_x1=v1-Y1*x1+M1*x1**2
m1_x2=v1-Y1*x2+M1*x2**2
m1_x3=v1-Y1*x3+M1*x3**2

print("m1 chooses: "+str(v1))
print("Polynomials for m1")
print()

print("To A1: "+"m1("+str(x1)+")"+" = "+str(v1)+" - "+str(Y1)+"*"+str(x1)+" + "+str(M1)+"*"+str(x1)+"^2"+ " = "+str(m1_x1))
print("To A2: "+"m1("+str(x2)+")"+" = "+str(v1)+" - "+str(Y1)+"*"+str(x2)+" + "+str(M1)+"*"+str(x2)+"^2"+ " = "+str(m1_x2))
print("To A3: "+"m1("+str(x3)+")"+" = "+str(v1)+" - "+str(Y1)+"*"+str(x3)+" + "+str(M1)+"*"+str(x3)+"^2"+ " = "+str(m1_x3))

print()



v2=random.choice(choices)
m2_x1=v2-Y2*x1+M2*x1**2
m2_x2=v2-Y2*x2+M2*x2**2
m2_x3=v2-Y2*x3+M2*x3**2


print("m2 chooses: "+str(v2))
print("Polynomials for m2")
print()

print("To A1: "+"m2("+str(x1)+")"+" = "+str(v2)+" - "+str(Y2)+"*"+str(x1)+" + "+str(M2)+"*"+str(x1)+"^2"+ " = "+str(m2_x1))
print("To A2: "+"m2("+str(x2)+")"+" = "+str(v2)+" - "+str(Y2)+"*"+str(x2)+" + "+str(M2)+"*"+str(x2)+"^2"+ " = "+str(m2_x2))
print("To A3: "+"m2("+str(x3)+")"+" = "+str(v2)+" - "+str(Y2)+"*"+str(x3)+" + "+str(M2)+"*"+str(x3)+"^2"+ " = "+str(m2_x3))


print()


v3=random.choice(choices)
m3_x1=v3-Y3*x1+D1*x1**2
m3_x2=v3-Y3*x2+D1*x2**2
m3_x3=v3-Y3*x3+D1*x3**2


print("m3 chooses: "+str(v3))
print("Polynomials for m2")
print()

print("To A1: "+"m3("+str(x1)+")"+" = "+str(v3)+" - "+str(Y3)+"*"+str(x1)+" + "+str(D1)+"*"+str(x1)+"^2"+ " = "+str(m3_x1))
print("To A2: "+"m3("+str(x2)+")"+" = "+str(v3)+" - "+str(Y3)+"*"+str(x2)+" + "+str(D1)+"*"+str(x2)+"^2"+ " = "+str(m3_x2))
print("To A3: "+"m3("+str(x3)+")"+" = "+str(v3)+" - "+str(Y3)+"*"+str(x3)+" + "+str(D1)+"*"+str(x3)+"^2"+ " = "+str(m3_x3))


print()


v4=random.choice(choices)
m4_x1=v4-Y4*x1+D2*x1**2
m4_x2=v4-Y4*x2+D2*x2**2
m4_x3=v4-Y4*x3+D2*x3**2


print("m4 chooses: "+str(v4))
print("Polynomials for m2")
print()

print("To A1: "+"m4("+str(x1)+")"+" = "+str(v4)+" - "+str(Y4)+"*"+str(x1)+" + "+str(D2)+"*"+str(x1)+"^2"+ " = "+str(m4_x1))
print("To A2: "+"m4("+str(x2)+")"+" = "+str(v4)+" - "+str(Y4)+"*"+str(x2)+" + "+str(D2)+"*"+str(x2)+"^2"+ " = "+str(m4_x2))
print("To A3: "+"m4("+str(x3)+")"+" = "+str(v4)+" - "+str(Y4)+"*"+str(x3)+" + "+str(D2)+"*"+str(x3)+"^2"+ " = "+str(m4_x3))
print()
print()
print(">>Question 2")
print()
print("Each Auditor, Aj, receives 4 messages, one from each of the members m1, m2, m3 and m4. The sum of messages received by Auditor Aj:")
print()
print("sum_Aj=m1(j)+m2(j)+m3(j)+m4(j)")
print()
print("Therefore:")

sum_A1=m1_x1+m2_x1+m3_x1+m4_x1
sum_A2=m1_x2+m2_x2+m3_x2+m4_x2
sum_A3=m1_x3+m2_x3+m3_x3+m4_x3

print("Sum for A1  = m1(1)+m2(1)+m3(1)+m4(1) = "+"("+str(m1_x1)+")"+"+"+"("+str(m2_x1)+")"+"+"+"("+str(m3_x1)+")"+"+"+"("+str(m4_x1)+")"+" = "+str(sum_A1))
print("Sum for A2  = m1(2)+m2(2)+m3(2)+m4(2) = "+"("+str(m1_x2)+")"+"+"+"("+str(m2_x2)+")"+"+"+"("+str(m3_x2)+")"+"+"+"("+str(m4_x2)+")"+" = "+str(sum_A2))
print("Sum for A3  = m1(3)+m2(3)+m3(3)+m4(3) = "+"("+str(m1_x3)+")"+"+"+"("+str(m2_x3)+")"+"+"+"("+str(m3_x3)+")"+"+"+"("+str(m4_x3)+")"+" = "+str(sum_A3))

print()
print()
print(">>Question 3")
print()
print("In order to reconstruct the secret, the members can use the three [A(j), Sum_Aj] pairs to calculate 2-degree polynomial.")
print("The constant term in the polnomial is the secret.")
print()
print("Let [x1,y1] = ",list([x1,sum_A1]))
print("Let [x2,y2] = ",list([x2,sum_A2]))
print("Let [x3,y3] = ",list([x3,sum_A3]))

#f_x,x,x0,y0,x1,y1,x2,y2,sum_A1,sum_A2,sum_A3=symbols('f(x) x x0 y0 x1 y1 x2 x2 sum_A1 sum_A2 sum_A3')
x=Symbol('x')

print()
print("Lagrange's basis polynomial is given by:")
print()
print()


init_printing()
print(sum_A1*(((x-x2)/(x1-x2))*((x-x3)/(x1-x3)))+sum_A2*(((x-x1)/(x2-x1))*((x-x3)/(x2-x3)))+sum_A3*(((x-x1)/(x3-x1))*((x-x2)/(x3-x2))))
print()
print()
print("Which expands into:")
print()
print()

print(pretty(expand(sum_A1*(((x-x2)/(x1-x2))*((x-x3)/(x1-x3)))+sum_A2*(((x-x1)/(x2-x1))*((x-x3)/(x2-x3)))+sum_A3*(((x-x1)/(x3-x1))*((x-x2)/(x3-x2))))))
print()
print()
print(">>Question 4")
print()
print("m1 can make sure that the result is always positive by sending a value, v1, greater than or equal to the number of members")
print()
print()
print(">>Question 5")
print("m1 could be prevented from cheating by deviding his/her value by the absolute value of the magnitude of the value so that it becomes either a 1 or -1")
print()
print()
print()
print("Part B: Cryptographic Protocols")
print()
print()
print("Task 1")
print()
print()
print("Question 1a")
print()
print("Suppose the following exchange takes place between A and B")
print()
print("1. A -> B: {A, {M}eb}eb")
print("2. B -> A: {M}ea")
print()
print("If adversary C can intercept the acknowledgement from B to A (i.e., communication #2), then C can relay the tampered with message to A as follows:")
print("3a. C -> A: {C, {M}ea}ea")
print()
print("As a consequence, A would send another acknowledgement back to C as follows:")
print("4a. A -> C: {M}ec")
print()
print("Finally, adversary C can then decrypt the message using its own private key")
print()
print()
print()
print()
print("Question 1b")
print()
print("If adversary C intercepts the message from A to B instead (i.e., communication #1), C can relay the tampered with message to B as follows:")
print("3b. C -> B: {C, {A, {M}eb}eb}eb ")
print()
print("B would send an acknowledgement to adversary C as follows:")
print("4b. B -> C: {A, {M}eb}ec")
print()
print("At this point, adversary C decrypts the message once, using its own private key to get the following:")
print("{A,{M}eb}")
print()
print("Now adversary C can change the sender's ID part from A to C because the unencrypted ID can be modified or completely removed from the rest of the message.")
print("The resulting message is as follows:")
print("{C,{M}eb}")
print()
print("Adversary C then encrypts the message using B's public key, and send it to B as follows:")
print("5b. C -> B: {C,{M}eb}eb")
print()
print("B sends acknowledgement back to C")
print("5c. B -> C: {M}ec")
print()
print("Now Adversary C can decrypt the message again using its private key to reveal the message.")
print()
print()
print("Task 2")
print()
print()
print("Question 2")
print()
print()
print("Suppose A and C establish a connection, since C is a legitimate user despite having adverserial intentions.")
print("A then sends the first message to C as follows:")
print("A -> C: {A,nA}ec")
print()
print("C then decryptes the message with its own key, establishes connection with B, and forwards the message to B using B's public key as follows:")
print("C -> B: {A, nA}eb")
print()
print("B will now decrypt the message, add a random nounce, nB, and send the message to A using A's public key because the sender's ID in the message is A")
print("B -> A: {nA,nB}ea")
print()
print("A checks its nouce and verifies that it is the same as sent earlier, but, instead of sending acknowledgement to B,")
print("A sends it to C because of the connection with C established earlier.")
print("A -> C: {nB}ec")
print()
print("C then decrypts the message using its own key to recover B's nounce")
print()
print("But B is still waiting for acknowledgement from A. So C encrypt's B's nounce and sends it to B as follows")
print("C -> B: {nB}eB")
print()
print("B of course will decrypt and verify the nounce, but the problem now is C has achieved authentication with A, while B thinks it is talking with A")






 

print()
print()
print("------------------------------------- END OF ASSIGNMENT 3 ------------------------------------- ")
print()
print()

