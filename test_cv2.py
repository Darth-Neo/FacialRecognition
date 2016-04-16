
if __name__ == '__main__':
    print "Test 'import cv2'"

    try:
        import cv2
        print "Yeah!"
    except Exception, msg:
        print "Ops --> %s failed" % msg
