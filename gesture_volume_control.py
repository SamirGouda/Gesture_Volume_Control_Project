import cv2
import time
import numpy as np
import hand_tracking_module as hand_module
import math
import audio_controller as ac


cap = cv2.VideoCapture(0)
# set width and height for webcam
cap.set(3, 640) # set width
cap.set(4, 480) # set height
prev_time = 0

detector = hand_module.HandDetector(detection_confidence=0.7)
master_controller = ac.MasterAudioController()
while cap.isOpened():
    success, img = cap.read()
    detector.find_hands(img)
    lm_list = detector.find_position(img)
    if len(lm_list) != 0:
        # print(lm_list)
        # extract landmarks of tip of thumb [4], and tip of index finger [8]
        x1, y1 = lm_list[4][1], lm_list[4][2]
        x2, y2 = lm_list[8][1], lm_list[8][2]
        cx, cy = (x1+x2)//2, (y1+y2)//2
        # highlight the two landmarks
        cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3, cv2.LINE_AA)
        cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
        length = math.hypot(x2-x1, y2-y1)
        print(length)
        if length < 25:
            cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)
        level_range = master_controller.get_volume_range()
        min_level, max_level = level_range[0], level_range[1]
        # audio_level_db = (max_level-min_level)/300* length+ min_level
        audio_level_db = np.interp(length, [25, 300], [min_level, max_level])
        # not needed as numpy.interp limits the output
        # audio_level_db = min(max_level, max(min_level, audio_level_db))
        master_controller.set_volume(audio_level_db)
        audio_level_percentage = np.interp(audio_level_db, [min_level, max_level], [0, 100])
        cv2.rectangle(img, (50, 150), (85, 350), (255, 0, 0), 3)
        cv2.rectangle(img, (85, 350), (50, 350-int(audio_level_percentage*2)), (255, 0, 0), cv2.FILLED)
        cv2.putText(img, f"vol: {int(audio_level_percentage)}%",
                    (40, 140), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
    # fps = cap.get(cv2.CAP_PROP_FPS) # does not work with my webcam
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time
    cv2.putText(img, f"fps: {int(fps)}", (40,50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
    cv2.imshow('gesture volume control', img)

    if cv2.waitKey(1) & 0XFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break