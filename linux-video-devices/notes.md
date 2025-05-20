# Linux - Video Device
- idea: figure out if it is possible to dynamically change/modify video device before it is sent to an application? i.e. handle frame to do automatic zoom via movement recognition
## v4l2loopback
- deps: dkms
- after installation run: `sudo modprobe v4l2loopback video_nr=NR_OF_DEV card_label="NAME"`
    - ideally do not use an already occupied id
- verify after that you have a new video device via running `v4l2-ctl --list-devices`
- once you have created your loopback device figure out what video device contains yyour actual stream, in my case video0
    - or identify via showing the driver info of all video devices via running `v4l2-ctl --device=/dev/video(NR_OF_DEV) --all`, the command which results in the 
- to give the feed to your new device you can use ffmpeg e.g. `ffmpeg -i /dev/video(NR_OF_ACTUAL_VIDEO_DEVICE) -f v4l2 -vcodec rawvide -pix-fmt yuv420p /dev/video(NR_OF_LOOPBACK_DEVICE)`
## Links
- [Video Device Documentations](https://tldp.org/HOWTO/Webcam-HOWTO/dev-intro.html) 
- [Framegrabbing from video device](https://tldp.org/HOWTO/Webcam-HOWTO/framegrabbers.html) 
- [Camera Utils on Linux, repository](https://git.linuxtv.org/v4l-utils.git) 
- [v4l2-loopback](https://github.com/v4l2loopback/v4l2loopback) 
- [ffmpeg magic](https://stackoverflow.com/questions/56564895/ffmpeg-record-capture-stream-and-do-scene-detection-at-the-same-time) 
