#!/bin/bash
# https://askubuntu.com/questions/742180/cmake-error-when-i-try-install-opencv-3-1?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
mkdir /usr/include/ffmpeg
cd /usr/include/ffmpeg
ln -sf /usr/include/x86_64-linux-gnu/libavcodec/*.h ./
ln -sf /usr/include/x86_64-linux-gnu/libavformat/*.h ./
ln -sf /usr/include/x86_64-linux-gnu/libswscale/*.h ./
# https://stackoverflow.com/questions/5842235/linux-videodev-h-no-such-file-or-directory-opencv-on-ubuntu-11-04?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
cd /usr/include/linux
ln -s ../libv4l1-videodev.h videodev.h

# apt-get install -y default-jre
# apt-get install -y openjdk-7-jre
# apt-get install -y oracle-java7-installer

apt-get install -y cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev
apt-get install libxvidcore-dev libx264-dev

mkdir /opencv-2.4.10/build && cd /opencv-2.4.10/build && cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D BUILD_NEW_PYTHON_SUPPORT=ON -D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON -D OPENCV_EXTRA_MODULES_PATH=/opencv-2.4.10/modules -D BUILD_opencv_java=OFF -D BUILD_EXAMPLES=ON ..
