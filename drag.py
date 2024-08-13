import cv2
from cvzone.HandTrackingModule import HandDetector
import cvzone
import numpy as np
import csv
import sys
import time 
import re
from PyQt5.QtWidgets import QMessageBox as Qmsg
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.Qt import *

##Capturing Video 
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8)
colorR = (255, 0, 0) # B,G,R

cx, cy, w, h = 100, 100, 200, 200

rectBox0 = 0
rectBox1 = 0
rectBox2 = 0
rectBox3 = 0

firstInstance = 0

Overlap12 = 0

EmptyScreen = 0

previousQno = False

checked = False

idxLenList = 0
maxIdxNos = False



class Window(QWidget):
    def __init__(self):
        super().__init__()
        #self.error_popup()

    def error_popup(self,errTitle,errMsg):
        errTitle = errTitle + "					   ."
        buttonReply = Qmsg.information(self,errTitle, errMsg, Qmsg.Ok) 
        print(int(buttonReply))
                 

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def convertChartoStr(s):
    str1 = ""
    return (str1.join(s))
    
def do_overlap(l1,r1,l2,r2):

    #print("l1.x = , r1.x= ,l1.y =, r1.y = , l2.x =, l2.y= ,r2.x = , r2.y = ",l1.x,r1.x,l1.y,r1.y,l2.x,r2.x,l2.y,r2.y)
    if l1.x == r1.x or l1.y == r1.y or r2.x == l2.x or l2.y == r2.y:
        return False

    # If one rectangle is on left side of other
    if l1.x >= r2.x or l2.x >= r1.x:
        return False

    # If one rectangle is above other
    if r1.y <= l2.y or r2.y <= l1.y:
        return False
 
    return True
        


class MCQ():
    def __init__(self, data):
        self.question = data[0]
        self.choice1 = data[1]
        self.choice2 = data[2]
        self.choice3 = data[3]
        self.choice4 = data[4]
        self.answer = data[5]
        self.userAns = None
        self.curSubmitX = 0

    def update(self,cursor, bboxs):
        for x, bbox in enumerate(bboxs):
            x1,y1,x2,y2 = bbox
            if x1<cursor[0]<x2 and y1<cursor[1]<y2:
                cv2.rectangle(img, (x1,y1), (x2,y2), color, cv2.FILLED  )

class DragRect():
    def __init__(self, posCenter, size=[180, 180]):
        self.posCenter = posCenter
        self.size = size


    def updateData(self, cursor):
        cx, cy = self.posCenter
        w, h = self.size
        global firstInstance
        global rectBox0
        global rectBox1
        global rectBox2
        global rectBox3

        # If the index finger tip is in the rectangle region
        if cx - w // 2 < cursor[0] < cx + w // 2 and \
                cy - h // 2 < cursor[1] < cy + h // 2:
            self.posCenter = cursor
            # print("pos-center = , 0 =, 1= ", self.posCenter,cursor[0],cursor[1])
            # print("x value = y value = ", cx, cy)
            mcq.curSubmitX = cx

            if ( cx == 150 and cy == 270 ) : #and ( firstInstance == 0 ) :
                rectBox0 = 1
                firstInstance = 1
                mcq.userAns = 1
                print("setting box 0 = ", rectBox0)
            elif ( cx == 350 and cy == 270 ) :#and ( firstInstance == 0 ):
                rectBox1 = 1
                firstInstance = 1
                mcq.userAns = 2
                print("setting box 1 = ", rectBox1)
            elif ( cx == 150 and cy == 470 ) :#and ( firstInstance == 0 ):
                rectBox2 = 1
                firstInstance = 1
                mcq.userAns = 3
                print("setting box 2 = ", rectBox2)
            elif ( cx == 350 and cy == 470 ) :#and ( firstInstance == 0 ):
                rectBox3 = 1
                firstInstance = 1
                mcq.userAns = 4
                print("setting box 3 = ", rectBox3)

rectList = []
rectList.append(DragRect([0 * 200 + 150, 270]))
rectList.append(DragRect([1 * 200 + 150, 270]))
rectList.append(DragRect([0 * 100 + 150, 470]))
rectList.append(DragRect([1 * 200 + 150, 470]))

pathCSV = "Mcqs.csv"
with open(pathCSV, newline='\n') as f:
    reader = csv.reader(f)
    dataAll = list (reader)[1:]
    print("length of = ", len(dataAll))

mcqList = []
for q in dataAll:
    mcqList.append(MCQ(q))

print("MCQlist = ", len(mcqList))
qNo = 0
qTotal = len(dataAll)
print("qtotal = ", qTotal)
    
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList, _ = detector.findPosition(img)
    
    
    if qNo < qTotal:

        mcq = mcqList[qNo]
        
        ### After Every Question Right Option - required to display on the Screen 
        if previousQno == True:
           option = mcq.answer
           cv2.rectangle(img, (50,100),(1098,580), colorR, cv2.FILLED)
           data = []
           actual_data = ""
           data_row2 = mcq.question
           writeIdx = 0
           flag = 0
           previousWriteIdx = 0
           Idxcount = 0
           for index, character in enumerate(data_row2):
                if character == "\n":                      
                    if flag == 1:
                       actual_data = convertChartoStr(data)
                       #print("actual_data : ", actual_data)                       
                       if writeIdx == 1:
                          cv2.putText(img, actual_data, (70, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
                          previousWriteIdx = 1 
                          #break
                       elif writeIdx == 2:
                          cv2.putText(img, actual_data, (70, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
                          previousWriteIdx = 2 
                          #break
                       elif writeIdx == 3:
                          cv2.putText(img, actual_data, (60, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
                          previousWriteIdx = 3
                       elif writeIdx == 4:
                          cv2.putText(img, actual_data, (65, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)                       
                          previousWriteIdx = 4
                       elif writeIdx == 5:
                          cv2.putText(img, actual_data, (65, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)                       
                          previousWriteIdx = 5
                       elif writeIdx == 6:
                          cv2.putText(img, actual_data, (65, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)                       
                          previousWriteIdx = 6
                       elif writeIdx == 7:
                          cv2.putText(img, actual_data, (65, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)                       
                          previousWriteIdx = 7
                       elif writeIdx == 8:
                          cv2.putText(img, actual_data, (65, 500), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)                       
                          previousWriteIdx = 8
                       elif writeIdx == 9:
                          cv2.putText(img, actual_data, (65, 550), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)                       
                          previousWriteIdx = 9
                       flag = 0
                       data = []
                    #print("\n postion : ", index)
                else:
                    data.append(character)                    
                    flag = 1
                    writeIdx = previousWriteIdx + 1
         
           cv2.ellipse(img,(550,600),(110,50),0,0,180,255,-1)
           cv2.putText(img, "Next", (500, 630), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
           if lmList:
            l, _, _ = detector.findDistance(4, 8, img, draw=False)
            print(l)
            SubmitClked = 0
            if l < 50 :
                cursor = lmList[8]
                cx = 500
                w = 110
                cy = 600
                h = 50
                if cx - w // 2 < cursor[0] < cx + w // 2 and \
                cy - h // 2 < cursor[1] < cy + h // 2:
                    #print("Click on Submit ", cursor[0], cursor[1]) 
                    SubmitClked = cursor[0]
                    if SubmitClked > 500:
                        previousQno = False
                        qNo += 1
                        #qNo = 15
        else:
            #image, start_point(x,y - tuple), end_point(x,y - tuple), color, thickness
            cv2.rectangle(img, (50,50),(900,100), colorR, cv2.FILLED)
            ### The Img Draw on, Position and Dimensions of the rAn, Leng of corner objects,
            ### Thickness of the corner objects, Thickness of the rectangle, colr of the rAn, 
            ### colr of the cornere edges
            #cvzone.drawBorder(img, (50, , 50, 50), 20, rt=0)
            cv2.putText(img, mcq.question, (90,90),cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
            cv2.rectangle(img, (810,470),(1050,180), colorR, cv2.FILLED)
            cv2.putText(img, "Drop your ", (850,280), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2) 
            cv2.putText(img, "Answer Here ", (830,340), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)         

            # Draw solid
            idx = 0
            for rect in rectList:
                if (rect.posCenter == (0,0) and rect.size == (0,0)) :
                    if idx == 0:
                        rect.posCenter = [150,270]
                    elif idx == 1:
                        rect.posCenter = [350,270]
                    elif idx == 2:
                        rect.posCenter = [150,470]
                    elif idx == 3:
                        rect.posCenter = [350,470]
                        #print("poscenter zero ")
                    rect.size = [180,180]            
                cx, cy = rect.posCenter 
                w, h = rect.size
                #print("cx,cy,w,h,pos,size",cx,cy,w,h,rect.posCenter,rect.size)
                rectimg = cv2.rectangle(img, (cx - w // 2, cy - h // 2), 
                              (cx + w // 2, cy + h // 2), colorR, cv2.FILLED)
                
                cvzone.cornerRect(img, (cx - w // 2, cy - h // 2, w, h), 20, rt=0)
                
                ## Rectangel Co-Ordinates 
                x1 = cx - w // 2 #60  #260 #60  #260                 #75  #275 #75  #275
                x2 = cx + w // 2 #240 #440 #240 #440                 #225 #425 #225 #425  ====> 150,150
                y1 = cy - h // 2 #380 #380 #180 #180                 #195 #195 #395 #395
                y2 = cy + h // 2 #560 #560 #360 #360                 #345 #345 #545 #545
                
                #print("x1 = ,x2 = , y1 = , y2 = ", x1,y1,x2,y2)          

                if idx == 0:
                    box1 = cv2.putText(img, mcq.choice1, (cx-70, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
                    L1 = Point(x1, y1)
                    R1 = Point(x2, y2)    
                elif idx == 1:
                    box2 = cv2.putText(img, mcq.choice2, (cx-70, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
                    L2 = Point(x1, y1)
                    R2 = Point(x2, y2)                
                elif idx == 2:
                    box3 =cv2.putText(img, mcq.choice3, (cx-70, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
                    L3 = Point(x1, y1)
                    R3 = Point(x2, y2) 
                elif idx == 3:                
                    box4 = cv2.putText(img, mcq.choice4, (cx-70, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
                    L4 = Point(x1, y1)
                    R4 = Point(x2, y2) 
                idx = idx + 1
            
            ### Avoiding Over Lapping Rectangels 
            indx = 0
            for rect in rectList:
                if(do_overlap(L1,R1,L2,R2) and indx == 1):
                    print("overlap for 1 and 2 Rectangele")
                    rect.posCenter = 0,0
                    rect.size = 0,0
                elif(do_overlap(L3,R3,L4,R4)and indx == 3):
                    print("overlap for 3 and 4 Rectangele")
                    rect.posCenter = 0,0
                    rect.size = 0,0
                # elif(do_overlap(L2,R2,L4,R4)and indx == 3):
                    # print("overlap for 2 and 4 Rectangele")
                    # rect.posCenter = 0,0
                    # rect.size = 0,0
                elif(do_overlap(L1,R1,L3,R3)and indx == 2):
                    print("overlap for 1 and 3 Rectangele ")
                    rect.posCenter = 0,0
                    rect.size = 0,0
                indx = indx + 1

            if lmList:
                l, _, _ = detector.findDistance(4, 8, img, draw=False)
                print(l)
                if l < 50 :
                    cursor = lmList[8]  # index finger tip landmark
                    #print("cursor inside lessthan", cursor)
                    # call the update here
                    print("Clicked")
                    
                    for rect in rectList:
                        rect.updateData(cursor)
                    
                    
                    #print("before curSubmitX", mcq.curSubmitX)
                    if  ( mcq.curSubmitX > 900 ) and \
                            ( rectBox0 == 1 or rectBox1 == 1 or rectBox2 == 1 or rectBox3 == 1) and (firstInstance == 1):
                        index = 0
                        #print("after curSubmitX", mcq.curSubmitX)
                        for rect in rectList:                   
                            if index == 0 and rectBox0 == 1:
                                rect.posCenter = 0, 0
                                rect.size = 0, 0
                                rectBox0 = 0
                                firstInstance = 0
                                print("entered here box0")
                                previousQno = True
                                #break
                            elif index == 1 and rectBox1 == 1:
                                rect.posCenter = 0, 0
                                rect.size = 0, 0
                                rectBox1 = 0
                                firstInstance = 0
                                print("entered here box1")
                                previousQno = True
                                #break
                            elif index == 2 and rectBox2 == 1:
                                rect.posCenter = 0, 0
                                rect.size = 0, 0
                                rectBox2 = 0
                                firstInstance = 0
                                print("entered here box2")
                                previousQno = True
                                #break
                            elif index == 3 and rectBox3 == 1:
                                rect.posCenter = 0, 0
                                rect.size = 0, 0
                                rectBox3 = 0
                                firstInstance = 0
                                print("entered here box3")
                                previousQno = True
                                #break

                            index = index + 1
                        print("User Answer ", mcq.userAns)    
                        if mcq.userAns != 0:
                            time.sleep(1)
                            qNo += 1
    else:
        score = 0
        for mcq in mcqList:
            mcq.userAns = str(mcq.userAns)
            if mcq.answer == mcq.userAns:                
                score = score + 1
        qTotal = 8
        score = round(score/qTotal*100, 2)
        cv2.rectangle(img, (90,250),(600,320), colorR, cv2.FILLED)
        cv2.putText(img, "Thank You!!, Quiz Completed", (100, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
        cv2.rectangle(img, (780,250),(1200,320), colorR, cv2.FILLED)
        cv2.putText(img, f'Your Score: {score}%', (800, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

    if previousQno == True:# or qNo == qTotal:
        pass
    else:
        #Draw Progress Bar
        progressBarValue = 150 + (950//qTotal)*qNo
        cv2.rectangle(img, (150,600), (progressBarValue, 650), (255,0,0), cv2.FILLED)
        cv2.rectangle(img, (150, 600), (1100, 650), (255,  0, 0), 5)#color = B,G,R
        cv2.putText(img, f'{(round((qNo/qTotal)*100))}%', (1130, 635), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
        
    out = img.copy()

    cv2.imshow("Asia S&T Quiz", out)
    cv2.waitKey(1)
