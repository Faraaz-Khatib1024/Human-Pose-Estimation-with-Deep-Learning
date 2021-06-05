import cv2
import mediapipe as mp
mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
# cv2.namedWindow("output", cv2.WINDOW_NORMAL)        # Create window with freedom of dimensions

# For static images:
with mpPose.Pose(
    static_image_mode=True,
    model_complexity=1,
    min_detection_confidence=0.5) as pose:

  while True:
    image = cv2.imread('Pose images/image2.jpg')
    # image_height, image_width, _ = image.shape
    results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    # print(results.pose_landmarks)
    if results.pose_landmarks:
      mpDraw.draw_landmarks(image, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
      for id, lm in enumerate(results.pose_landmarks.landmark):
        h, w, c = image.shape
        print(id, lm)
        cx, cy = int(lm.x * w), int(lm.y * h)  # to get pixel value of x,y landmarks
        cv2.circle(image, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
    # img = cv2.resize(image, (1060, 980))  # Resize image
    cv2.imshow("Image", image)
    cv2.waitKey(0)