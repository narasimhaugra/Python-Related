# #!/usr/bin/env python

# from __future__ import print_function
# import cv2
# print(cv2.__version__)

# class Button(object):

    # def __init__(self, text, x, y, width, height, command=None):
        # self.text = text
        # self.x = x
        # self.y = y
        # self.width = width
        # self.height = height
        
        # self.left = x
        # self.top  = y
        # self.right  = x + width - 1 
        # self.bottom = y + height - 1
        
        # self.hover = False
        # self.clicked = False
        # self.command = command
        
    # def handle_event(self, event, x, y, flags, param):
        # self.hover = (self.left <= x <= self.right and \
            # self.top <= y <= self.bottom)
            
        # if self.hover and flags == 1:
            # self.clicked = False
            # print(event, x, y, flags, param)
            
            # if self.command:
                # self.command()
        
    # def draw(self, frame):
        # if not self.hover:
            # cv2.putText(frame, "???", (40,40), FONT, 3 , (0,0,255), 2)
            # cv2.circle(frame, (20,20), 10 , (0,0,255), -1)
        # else:
            # cv2.putText(frame, "REC", (40,40), FONT, 3 , (0,255,0), 2)
            # cv2.circle(frame, (20,20), 10 , (0,255,0), -1)
        
# # ---------------------------------------------------------------------

# # keys 
# KEY_ESC = 27

# # font
# FONT = cv2.FONT_HERSHEY_PLAIN

# # ---------------------------------------------------------------------

# # states
# running = True 

# # ---------------------------------------------------------------------

# # create button instance
# button = Button('QUIT', 0, 0, 100, 30)

# # ---------------------------------------------------------------------

# # create VideoCapture
# vcap = cv2.VideoCapture(0) # 0=camera
 
# # check if video capturing has been initialized already
# if not vcap.isOpened(): 
    # print("ERROR INITIALIZING VIDEO CAPTURE")
    # exit()
# else:
    # print("OK INITIALIZING VIDEO CAPTURE")
 
    # # get vcap property 
    # width = int(vcap.get(cv2.CAP_PROP_FRAME_WIDTH))
    # height = int(vcap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # #fps = float(vcap.get(cv2.CAP_PROP_FPS))
    # fps = 15.0 # use different value to get slowmotion or fastmotion effect
    
    # print('VCAP width :', width)
    # print('VCAP height:', height)
    # print('VCAP fps   :', fps)
 
# while running:
    # # grab, decode and return the next video frame (and "return" status)
    # ret, frame = vcap.read()

    # if not ret:
        # running = False
    # else:
        # # add REC to frame
        # #cv2.putText(frame, "REC", (40,40), FONT, 3 , (0,0,255), 2)
        # #cv2.circle(frame, (20,20), 10 , (0,0,255), -1)

        # # add instruction to frame
        # cv2.putText(frame,"ESC - QUIT",(width - 200,20), FONT, 1 ,(255,255,255))

        # # add button to frame
        # button.draw(frame)
        
        # # displays frame
        # cv2.imshow('x', frame)         
        # # assign mouse click to method in button instance
        # cv2.setMouseCallback("x", button.handle_event)

     
        # # get key (get only lower 8-bits to work with chars)
        # key = cv2.waitKey(1) & 0xFF

        # if key == KEY_ESC:
            # print("EXIT")
            # running = False
     
# # release everything 
# vcap.release()
# cv2.destroyAllWindows()

# import sys

# from PyQt5 import QtWidgets, QtGui
# from PyQt5.QtCore import Qt


# class MyTree(QtWidgets.QTreeWidget):
    # def __init__(self):
        # super().__init__()

        # self.setDragDropMode(self.DragDrop)
        # self.setSelectionMode(self.ExtendedSelection)
        # self.setSelectionBehavior(self.SelectRows)
        # self.setDefaultDropAction(Qt.CopyAction)
        # self.setAcceptDrops(True)

    # def dropEvent(self, e: QtGui.QDropEvent):
        # if e.source() is self:
            # print("move")
            # e.setDropAction(Qt.MoveAction)
            # e.accept()
        # super().dropEvent(e)


# if __name__ == "__main__":
    # app = QtWidgets.QApplication(sys.argv)

    # my_list = QtWidgets.QListWidget()
    # my_list.addItems(list('1234'))
    # my_list.show()
    # my_list.setDragEnabled(True)
    # my_list.setAcceptDrops(True)

    # my_tree = MyTree()
    # for item in list('abcd'):
        # QtWidgets.QTreeWidgetItem(my_tree, [item])
    # my_tree.show()

    # sys.exit(app.exec_())


# import pyshine as ps
# import numpy as np

# # Create a blank image
# image = np.zeros((500, 500, 3), dtype=np.uint8)

# # Draw a rectangle on the image
# ps.rectangle(image, (10, 10), (100, 100), (0, 255, 0), 2)

# # Display the image
# ps.imshow(image)

# import tkinter as tk
# import time

# root = tk.Tk()

# canvas = tk.Canvas(root, width=400, height=400)
# canvas.pack()

# rc1 = canvas.create_rectangle(20, 260, 120, 360,
                    # outline='white', fill='blue')
# rc2 = canvas.create_rectangle(20, 10, 120, 110,
                    # outline='white', fill='red')

# y = x = 5
# for ctr in range(50):
    # time.sleep(0.025)
    # canvas.move(rc1, x, -y)
    # canvas.move(rc2, x, y)
    # canvas.update()

# root.mainloop()

# from tkinter import *
# import tkinter.messagebox as msg
# from PyQt5.QtWidgets import QMessageBox as Qmsg
# from PyQt5 import QtWidgets, QtCore, QtGui
# from PyQt5.Qt import *
# import cv2
# import sys
# import cvzone
# from cvzone.HandTrackingModule import HandDetector

# cap = cv2.VideoCapture(0)
# cap.set(3, 1280)
# cap.set(4, 720)
# detector = HandDetector(detectionCon=0.8)


# class Window(QWidget):
    # def __init__(self):
        # super().__init__()
        # #self.error_popup()

    # def error_popup(self,errTitle,errMsg):
        
        # # employee = 'Name 1'
        
        # # QMessageBox.critical(
            # # self,
            # # "ERREUR",
            # # f"Il n'est pas possible de bloquer cette plage horraire pour <b>{employee}</b>", 
            # # QMessageBox.Ok
        # # )
        # errTitle = errTitle + "					   ."
        # buttonReply = Qmsg.information(self,errTitle, errMsg, Qmsg.Ok) 
        # print(int(buttonReply))
                 

# while True:
    # success, img = cap.read()
    # img = cv2.flip(img, 1)
    # img = detector.findHands(img)
    # lmList, _ = detector.findPosition(img)

    # if lmList:

        # l, _, _ = detector.findDistance(8, 12, img, draw=False)
        # print(l)
        # if l < 50:
            # cursor = lmList[8]  # index finger tip landmark
            # #showdialog("Message","Select Excel File")
            # App = QApplication(sys.argv)
            # window = Window()
            # window.error_popup("Message","Select Excel File")

    # cv2.imshow("Asia S&T Quiz", img)
    # cv2.waitKey(1)
    
        
# if __name__ == "__main__":
    # App = QApplication(sys.argv)
    # window = Window()
    # window.show()
    # sys.exit(App.exec_())      
    
# from PyQt5 import QtCore,QtGui, QtWidgets
# import sys
# import cv2
# import numpy as np

# class ImageWidget(QtWidgets.QWidget):
    # def __init__(self,parent=None):
        # super(ImageWidget,self).__init__(parent)
        # self.image=None

    # def setImage(self,image):
        # self.image=image
        # sz=image.size()
        # self.setMinimumSize(sz)
        # self.update()

    # def paintEvent(self,event):
        # qp=QtGui.QPainter()
        # qp.begin(self)
        # if self.image:
            # qp.drawImage(QtCore.QPoint(0,0),self.image)
        # qp.end()

# class MainWindow(QtWidgets.QMainWindow):
    # def __init__(self,parent=None):
        # super(MainWindow,self).__init__(parent)
        # self.videoFrame=ImageWidget()
        # self.setCentralWidget(self.videoFrame)
        # self.timer=QtCore.QTimer(self)
        # self.timer.timeout.connect(self.updateImage)
        # self.timer.start(30)
        # self.capture = cv2.VideoCapture(0)

    # def updateImage(self):
        # _, img = self.capture.read()
        # #img=cv2.cvtColor(img, cv.CV_BGR2RGB)
        # height, width, bpc = img.shape
        # bpl = bpc * width
        # image = QtGui.QImage(img.data, width, height, bpl, QtGui.QImage.Format_RGB888)
        # self.videoFrame.setImage(image)


# def main():
    # app=QtWidgets.QApplication(sys.argv)
    # w=MainWindow()
    # w.show()
    # app.exec_()

# if __name__=='__main__':
    # main()
    

# import sys
# from PyQt5.Qt import *


# class Window(QWidget):
    # def __init__(self):
        # super().__init__()
        # self.error_popup()

    # def error_popup(self):
        
        # employee = 'Name 1'
        
        # QMessageBox.critical(
            # self,
            # "ERREUR",
            # f"Il n'est pas possible de bloquer cette plage horraire pour <b>{employee}</b>", 
            # QMessageBox.Ok
        # )
                 
        
# if __name__ == "__main__":
    # App = QApplication(sys.argv)
    # window = Window()
    # window.show()
    # sys.exit(App.exec_())    

# import numpy as np

# def delete_overlapped_rectangles(rectangles):
  # """Deletes overlapped rectangles from a list of rectangles.

  # Args:
    # rectangles: A list of rectangles, where each rectangle is represented as a tuple of four floats: (x1, y1, x2, y2).

  # Returns:
    # A list of non-overlapped rectangles.
  # """

  # # Create a set to store the non-overlapped rectangles.
  # non_overlapped_rectangles = set()
  # print(non_overlapped_rectangles)

  # # Iterate over the rectangles.
  # for rectangle in rectangles:
    # # Check if the rectangle overlaps with any of the non-overlapped rectangles.
    # for non_overlapped_rectangle in non_overlapped_rectangles:
      # if rectangle_overlaps(rectangle, non_overlapped_rectangle):
        # break

    # # If the rectangle does not overlap with any of the non-overlapped rectangles, add it to the set.
    # else:
      # non_overlapped_rectangles.add(rectangle)

  # # Return the list of non-overlapped rectangles.
  # return list(non_overlapped_rectangles)

# def rectangle_overlaps(rectangle1, rectangle2):
  # """Checks if two rectangles overlap.

  # Args:
    # rectangle1: A rectangle, represented as a tuple of four floats: (x1, y1, x2, y2).
    # rectangle2: A rectangle, represented as a tuple of four floats: (x1, y1, x2, y2).

  # Returns:
    # True if the rectangles overlap, False otherwise.
  # """

  # # Check if the x-coordinates of the rectangles overlap.
  # if rectangle1[0] > rectangle2[2] or rectangle2[0] > rectangle1[2]:
    # return False

  # # Check if the y-coordinates of the rectangles overlap.
  # if rectangle1[1] > rectangle2[3] or rectangle2[1] > rectangle1[3]:
    # return False

  # # The rectangles overlap.
  # return True

# # Example usage:

# rectangles = [(1, 1, 2, 2), (2, 2, 3, 3), (3, 3, 4, 4)]

# non_overlapped_rectangles = delete_overlapped_rectangles(rectangles)

# print(non_overlapped_rectangles)


# Python program to illustrate  
# saving an operated video 
  
# organize imports 
import numpy as np 
import cv2 
  
# This will return video from the first webcam on your computer. 
cap = cv2.VideoCapture(0)   
  
# Define the codec and create VideoWriter object 
fourcc = cv2.VideoWriter_fourcc(*'XVID') 
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480)) 
  
# loop runs if capturing has been initialized.  
while(True): 
    # reads frames from a camera  
    # ret checks return at each frame 
    ret, frame = cap.read()  
  
    # Converts to HSV color space, OCV reads colors as BGR 
    # frame is converted to hsv 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
      
    # output the frame 
    out.write(hsv)  
      
    # The original input frame is shown in the window  
    cv2.imshow('Original', frame) 
  
    # The window showing the operated video stream  
    cv2.imshow('frame', hsv) 
  
      
    # Wait for 'a' key to stop the program  
    if cv2.waitKey(1) & 0xFF == ord('a'): 
        break
  
# Close the window / Release webcam 
cap.release() 
  
# After we release our webcam, we also release the output 
out.release()  
  
# De-allocate any associated memory usage  
cv2.destroyAllWindows() 