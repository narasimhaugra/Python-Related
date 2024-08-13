# import cv2

# cap = cv2.VideoCapture(0)

# while True:
    # ret, frame = cap.read()

    # if ret:
        # cv2.imshow('frame', frame)

        # if cv2.waitKey(1) & 0xFF == ord('q'):### 113(0x71) & 0xFF == 0x71
            # break

    # else:
        # break

# cap.release()
# cv2.destroyAllWindows()

# import cv2
# from cvzone.HandTrackingModule import HandDetector
# import cvzone

# cap = cv2.VideoCapture(0)
# cap.set(3,1280) ## cv2.CAP_PROP_FRAME_WIDTH,
# cap.set(4,720)  ## cv2.CAP_PROP_FRAME_HEIGHT

# detector = HandDetector(detectionCon=0.8)
# coloR = (255,0,255)

# cx = 100
# cy = 100 
# w = 200 
# h = 200

# while True:
    # success, img = cap.read()
    # # ## Flip - Imag, Flip code( Horizontal flip - 1, vertical flip - 0)
    # img = cv2.flip(img,1)
    
    # hands, img = detector.findHands(img, flipType=False)

    # ## Land Mark List, Bounding Box 
    # #lmList, _ = detector.findPosition(img)
    
    # if hands:
        # # Hand 1
        # hand1 = hands[0]
        # lmList1 = hand1["lmList"]  # List of 21 Landmark points
        # bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
        # centerPoint1 = hand1['center']  # center of the hand cx,cy
        # handType1 = hand1["type"]  # Handtype Left or Right

        # fingers1 = detector.fingersUp(hand1)

    # if len(hands) == 2:
        # # Hand 2
        # hand2 = hands[1]
        # lmList2 = hand2["lmList"]  # List of 21 Landmark points
        # bbox2 = hand2["bbox"]  # Bounding box info x,y,w,h
        # centerPoint2 = hand2['center']  # center of the hand cx,cy
        # handType2 = hand2["type"]  # Hand Type "Left" or "Right"

        # fingers2 = detector.fingersUp(hand2)

        # # Find Distance between two Landmarks. Could be same hand or different hands
        # length, info, img = detector.findDistance(lmList1[8][:2], lmList2[8][:2], img)  # with draw
        # # length, info = detector.findDistance(lmList1[8], lmList2[8])  # with draw
    
    # if hands:
        # lmList = hands[0]['lmList']
        # cursor = lmList[8] ## X & Y of the Tip
        # if cx - w // 2 < cursor[0] < cx + w // 2 and cy - h // 2 < cursor[1] < cx + h // 2:
           # coloR = 0,255,0 # Green Color
           # cx = cursor
           # cy = cursor
        # else:
            # coloR = (255,0,255)
    
    # # Arguments - image, pt1, pt2, color(purple), thickness(filed)
    # cv2.rectangle(img, ((cx-w//2), (cy-h//2)), ((cx+w // 2), (cx+h // 2)), coloR, -1)
    
    # cv2.imshow("image ", img)
    # if cv2.waitKey(1) == ord('q'):
        # break
        
        
        
import cv2
from cvzone.HandTrackingModule import HandDetector
import cvzone
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8)
colorR = (255, 0, 255)

cx, cy, w, h = 100, 100, 200, 200


class DragRect():
    def __init__(self, posCenter, size=[200, 200]):
        self.posCenter = posCenter
        self.size = size

    def update(self, cursor):
        cx, cy = self.posCenter
        w, h = self.size

        # If the index finger tip is in the rectangle region
        if cx - w // 2 < cursor[0] < cx + w // 2 and \
                cy - h // 2 < cursor[1] < cy + h // 2:
            self.posCenter = cursor


rectList = []
for x in range(5):
    rectList.append(DragRect([x * 250 + 150, 150]))

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList, _ = detector.findPosition(img)

    if lmList:

        l, _, _ = detector.findDistance(8, 12, img, draw=False)
        print(l)
        if l < 30:
            cursor = lmList[8]  # index finger tip landmark
            # call the update here
            for rect in rectList:
                rect.update(cursor)

    ## Draw solid
    for rect in rectList:
        cx, cy = rect.posCenter
        w, h = rect.size
        cv2.rectangle(img, (cx - w // 2, cy - h // 2),
                      (cx + w // 2, cy + h // 2), colorR, cv2.FILLED)
        cvzone.cornerRect(img, (cx - w // 2, cy - h // 2, w, h), 20, rt=0)

    ## Draw Transperency
    # imgNew = np.zeros_like(img, np.uint8)
    # for rect in rectList:
        # cx, cy = rect.posCenter
        # w, h = rect.size
        # cv2.rectangle(imgNew, (cx - w // 2, cy - h // 2),
                      # (cx + w // 2, cy + h // 2), colorR, cv2.FILLED)
        # cvzone.cornerRect(imgNew, (cx - w // 2, cy - h // 2, w, h), 20, rt=0)

    out = img.copy()
    # alpha = 0.5
    # mask = imgNew.astype(bool)
    # out[mask] = cv2.addWeighted(img, alpha, imgNew, 1 - alpha, 0)[mask]

    cv2.imshow("Image", out)
    cv2.waitKey(1)
    
   # https://www.youtube.com/watch?v=5LUOh3eh5Fw