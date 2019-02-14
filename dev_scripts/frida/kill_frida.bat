@echo off
adb shell kill -9 `pidof ./frida-server`
@pause