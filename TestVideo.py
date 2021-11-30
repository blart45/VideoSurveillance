# -*- coding: utf-8 -*-

import time
import os

	##montage video
##ffmpeg -framerate 1 -i happy%d.jpg -c:v libx264 -r 30 -pix_fmt yuv420p output.mp4



try:
		for i in range(50):
			text = "out"+str(i)
			os.system("ffmpeg -f v4l2 -video_size 1280x720 -i /dev/video0 -frames 1 "+text+".jpg")
			time.sleep(0.1)
        
except KeyboardInterrupt:
    print("\nApplication stopped!")
