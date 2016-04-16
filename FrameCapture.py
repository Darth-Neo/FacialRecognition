import numpy as np
import cv2

if __name__ == u"__main__":
    cap = cv2.VideoCapture(2)

    width = cap.get(3)
    height = cap.get(4)

    if cap.isOpened() is True:

        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()

            if ret is True and False:
                # Display the resulting frame
                cv2.imshow(u"frame", frame)

            # Our operations on the frame come here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Display the resulting frame
            cv2.imshow(u"frame", gray)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
