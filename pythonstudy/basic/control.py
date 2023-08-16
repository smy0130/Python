'''
Created on 2023. 8. 16.

@author: 유승민
'''

a = 3
if a % 2 == 0 :
    print("a is even")
else:
    print("a is ood")

if "hello" in ("hello", "world"):
    print("포함")
else:
    print("미포함")

fruit = "banana"
if fruit == "apple":
    print("red")
elif fruit == "banana":
    print("yellow")
else:
    print("unknown")
    
a = 5
# a가 0보다 크면 x = 10, 아니면 x = 20
x = 10 if a > 0 else 20 
# a > 0 ? 10 : 20
print(x)

# 2. 반복문: for, while
counter = 0 
while counter < 20 :
    print("counter:", counter)
    counter += 5

# 튜플과 반복문
total = 0
index = 0
subject = (78, 95, 68, 62)
while index < len(subject):
    total += subject[index]
    index += 1
average = total / len(subject)
print("while:", average)


total= 0
for score in subject:    
    total += score 
average = total / len(subject)
print("for:", average)

# hi = ("h", "i", "!")
for letter in "hi!":
    print("letter", letter)

# range
total = 0
for val in range(10):
    total += val
print("total:", total)

for val in range(3, 7):
    print("val:", val)
    total =+ val
print("total:", total)

# 시작값(포함), 종료값(미포함), 증감
for val in range(1, 8, 2):
    print("val:", val)

# break/continue
count = 0
while True:
    if count > 3:
        break;
    print("count:", count)
    count += 1
    
for val in range(5):
    print("val:", val)
    if val % 2 == 0:
        continue
    print("===")

def add(a, b):
    return a + b








