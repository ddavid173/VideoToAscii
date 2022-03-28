import os
import time
import cv2
import numpy as np
from Frame import frame as frameClass

def greyscale(r, g, b):
    return 0.21 * r + 0.72 * g + 0.07 * b

def render(frames):
    for frame in frames:
        frame.render()

def printVideo(frames, waitTime):
    for frame in frames:
        print(frame)
        time.sleep(waitTime)

def outputArt(frames, fps):
    print('Printing results...')
    f = open('C:\\Users\\delga\\Desktop\\classes\\Practice\\VideoToAscii\\Renders\\Rendered.txt', 'w')
    for frame in range(len(frames)):
        string = ''
        for x in range(len(frames[0])):
            for y in range(len(frames[0][0])):
                f.write(str(frames[frame][x][y]))
                string += str(frames[frame][x][y])
            string += '\n'
            f.write('\n')
        #os.system('CLS')
        print(string + '\n')
        f.write('\n')
        time.sleep(1/fps/2)
    f.close()

def videoConvert(inputDir):
    # Start capturing the feed
    cap = cv2.VideoCapture(inputDir)
    # Find the number of frames
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    print ("Number of frames: ", video_length)
    count = 0
    print ("Converting video..\n")
    frames = []
    # Start converting the video
    while cap.isOpened():
        # Extract the frame
        ret, frame = cap.read()
        if not ret:
            continue
        frame = cv2.resize(frame,(140,60),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
        frameOBJ = frameClass(frame)
        frames.append(frameOBJ)
        count = count + 1
        # If there are no more frames left
        if (count > (video_length-1)):
            # Log the time again
            time_end = time.time()
            # Release the feed
            cap.release()
            # Print stats
            print ("Done extracting frames.\n%d frames extracted" % count)
            return frames, video_length

if __name__=="__main__":
    running = True
    #while running:
    # input = input('Where is your Video stored?\n(use two backslash for a single backslash)')
    frames, video_length = videoConvert("C:\\Users\\delga\\Downloads\\ezgif.com-gif-maker.mp4")
    waitTime = 5 / video_length
    frames[0].render()
    render(frames)
    printVideo(frames, waitTime)
    outputArt(frames, waitTime)
    #framesAscii = toAscii(frames)
    #outputArt(framesAscii, int(video_length / 30))
    #print('el fin')