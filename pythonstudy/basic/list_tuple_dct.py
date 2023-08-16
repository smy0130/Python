'''
Created on 2023. 8. 16.

@author: 유승민
'''

# 과목별 변수
math = 78; english = 95; chemistry = 68; science = 62;
total = math + english + chemistry + science
average = total / 4
print("단순값:", average)

# 리스트(배열): 인덱스 0 부터
subject1 = [78, 95, 68, 62]
subject1[0] = 82
print("리스트:", subject1)

# 튜플
subject2 = (78, 95, 68, 62)
total = subject2[0] + subject2[1] + subject2[2] + subject2[3]
average = total / 4 
print("튜플:", average)
#subject2[0] = 82

# 문자열 배열
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# 추가(append)
weekdays.append("Saturday")
# 삽입(insert)
weekdays.insert(2, "TestString")
print("문자배열:", weekdays)

# 딕셔너리(dictionary)
score ={
    "math" : 78,
    "english" : 95,
    "chemistry" : 68,
    "science" : 62,
}
print("딕셔너리1: ", score)
score["math"] = 82
print("딕셔너리2: ", score)

# 리스트와 튜플을 다루는 주요 함수 : len, copy, in
print(len(weekdays))
# 리스트: 2차원
data = ([1, 2], [4, 5, 6], [7, 8, 9, 10])
print("1:", len(data))
print("2:", len(data[0]))
print("3:", len(data[1]))
print("4:", len(data[2]))
print("이차원뱅열의 하나의 요소::", data[2][3])

#in
greets = ("morning", "afternoon", "evening")
print("evening" in greets)


