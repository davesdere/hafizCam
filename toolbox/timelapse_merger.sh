# From there
# https://www.raspberrypi.org/forums/viewtopic.php?t=72435
gst-launch-1.0 multifilesrc location=img_%04d.jpeg index=1 caps="image/jpeg,framerate=24/1" ! jpegdec ! omxh264enc ! avimux ! filesink location=timelapse.avi
