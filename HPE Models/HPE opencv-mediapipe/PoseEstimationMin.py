import cv2 #for image processing
import mediapipe as mp #for pose esimation
import time

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

cap = cv2.VideoCapture('Pose videos/dance2.mp4') # for webcam use '0'
pTime = 0
while True:
    success, img = cap.read() # img is in BGR but mediapipe uses RGB
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # converts BGR to RGB
    results = pose.process(imgRGB) # sending the image to our model
    # print(results.pose_landmarks)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS) # to draw keypoints(pose_landmarks) and connections(pose_CONNECTION)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            print(id, lm)
            cx, cy = int(lm.x * w), int(lm.y * h) # to get pixel value of x,y landmarks
            cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)