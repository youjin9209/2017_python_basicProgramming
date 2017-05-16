# Chapter 5. Processing Data
# 0515. 월요일
# 연습문제 숙제 중에 4.1의 26번  - nonoverlapping string 찾기
"""
# step 1
def occur(strword, subword):
    count = 0 # 몇번 등장하는지
    i = strword.find(subword)
    while i != -1: # 찾았을 경우
        count += 1
        strword = strword[i+len(subword):] # 매번 새로 복사-> 결정적 단점
        i = strword.find(subword)
    return count

print(occur("abcd", "abc"))

# step 2
def occur(strword, subword):
    count = 0
    strlen = len(strword)
    sublen = len(subword)
    for i in range(strlen):
        if strword[i:i+sublen] == subword:
            count += 1
    return count

"""


"""
# Reading Text Files
# file : 원래 hard disc에 저장 된다
# hard disc: 1) 용량이 더 크지   2) 다음 번에 또 쓸 수 있다   3) 속도가 느리다
# open() : 하드디스크에 있던 것을 메모리에서 access할 수 있도록 적재
# infile = open (fileName, 'r') -> read하기 위해 연다
# line 단위로 읽어준다 - line.rstrip() for line in infile
# 제일 앞부터 읽어준다 .
#infile = open("/Users/scarlett/PycharmProjects/programming_python2017/Live.txt", 'r')

def main():
    file = "/Users/scarlett/PycharmProjects/programming_python2017/Live.txt"
    displayWithForLoop(file)
    print()
    displayWithListComprehension(file)

def displayWithForLoop(file):
    infile = open(file, 'r') # hard disc에 있는 파일 메모리로 불러와
    for line in infile: # line 이라는 변수끝에 줄바꿈이 이미 되어있는 상태로 읽혀서
        print (line, end="")  # 여기서 줄바꿈을 처리를 안해줘도 줄바꿈이 되어있는 상태로 찍히는거다
    infile.close()

def displayWithListComprehension(file):
    infile = open(file, 'r')
    listPres = [line.rstrip() for line in infile] # white space날려버리고 list 로 만들어
    infile.close()
    print(listPres) # 그래서 줄바꿈 없다

main()
# read () : 통채로 읽어온다
# readLine() : 한줄씩 읽는다
# ex1 displayWithReadLine 함수
"""


"""
# Creating Text Files
def main():
    outfile = open("/Users/scarlett/PycharmProjects/programming_python2017/Live2.txt", 'w')
    createWithWritelines(outfile)
    outfile = open("/Users/scarlett/PycharmProjects/programming_python2017/Live3.txt", 'w')
    createWithWrite(outfile)

def createWithWritelines(outfile):
    list1 = ["George Washington", "John Adams", "Thomas Jefferson"]
    for i in range(len(list1)):
        list1[i] = list1[i] + "\n" # 개행문자 붙여줌
    outfile.writelines(list1) # writelines의 파라미터는 list다!!
    outfile.close()

def createWithWrite(outfile):
    outfile.write("George Washington\n")
    outfile.write("John Adams\n")
    outfile.write("Thomas Jefferson\n")
    outfile.close()

main()
"""


# Adding Lines to an Existing Text File : 'a' 기존 내용에 맨 뒤부터 붙여 쓴다
# Altering Items in a Text File : 그냥 파일을 새로 만들어라
# remove file -> import os 해준다음에 os.remove(filespec)

# Sets : {}
# Set is an unordered collection of items
# 중복을 허용하지 않는다