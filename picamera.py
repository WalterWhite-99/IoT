1. Display preview of camera for 5 seconds

	from picamera import PiCamera
	from time import sleep

	camera = PiCamera()

	camera.start_preview()
	sleep(5)
	camera.stop_preview()

//If your preview is upside-down, you can rotate it by 180 degrees with the following code:

camera.rotation = 180

2. Capture an image

	camera.start_preview()
	sleep(5)
	camera.capture('/home/pi/Desktop/image.jpg')
	camera.stop_preview()


3. Capture 5 images at the interval of 5 seconds

camera.start_preview()
for i in range(5):
    sleep(5)
    camera.capture('/home/pi/Desktop/image%s.jpg' % i)
camera.stop_preview()


4. Record a video

camera.start_preview()
camera.start_recording('/home/pi/Desktop/video.h264')
sleep(5)
camera.stop_recording()
camera.stop_preview()


5. Add annotate text on image

camera.start_preview()
camera.annotate_text = "Hello world!"
sleep(5)
camera.capture('/home/pi/Desktop/text.jpg')
camera.stop_preview()


6. Change the brightness of preview

camera.start_preview()
for i in range(100):
    camera.annotate_text = "Brightness: %s" % i
    camera.brightness = i
    sleep(0.1)
camera.stop_preview()

7. Change the contrast of preview

camera.start_preview()
for i in range(100):
    camera.annotate_text = "Contrast: %s" % i
    camera.contrast = i
    sleep(0.1)
camera.stop_preview()

8. Apply all image effects on the preview

camera.start_preview()
for effect in camera.IMAGE_EFFECTS:
    camera.image_effect = effect
    camera.annotate_text = "Effect: %s" % effect
    sleep(5)
camera.stop_preview()
