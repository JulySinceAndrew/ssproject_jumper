import cv2 as cv
import numpy as np
import math

def phi(a,b):
    return math.exp(-100*(abs(int(a[0])-int(b[0]))+abs(int(a[1])-int(b[1]))+abs(int(a[2])-int(b[2])))**4)

def check_end(img):
    fliter=cv.imread("./final.PNG")
    sum=0
    count=0
    for i in range(0,fliter.shape[0]):
        for j in range(0,fliter.shape[1]):
            sum+=phi(fliter[i,j,:],img[i+1500,j+410,:])
            count+=1
    print(sum)
    print(count)
    return sum>70000


def check_new_record(img):
    fliter=cv.imread("./record.PNG")
    sum=0
    count=0
    for i in range(0,fliter.shape[0]):
        for j in range(0,fliter.shape[1]):
            sum+=phi(fliter[i,j,:],img[i+230,j+430,:])
    print(sum)
    print(count)
    return sum>15000


def check_score():


def check_score_new_record():



'''
def check_result(img):
       input: the img of the game now
       output: the result of the game 
               return_value=-1 stand for the game is continuing
               return_value>=0 stand for the game is end and the return_value is the score of the player.
    if check_end(img)==False:
        return -1
    if check_new_record(img): 
        return check_score_new_record(img)
    else:
        return check_score(img)          
    
    '''
    

img=cv.imread("pr1.jpg")
print(check_end(img))
print(check_new_record(img))