from curses import tigetflag
import os
from subprocess import Popen
from threading import currentThread
from time import sleep
from datetime import datetime
from subprocess import call 

print('###########  CiRA Autorun ############')
import getpass
username = getpass.getuser()
print('user : ', username)

date = datetime.now()
hour = date.hour
min = date.minute
sec = date.second

sleep(10)
# run ros core
Popen(["gnome-terminal", '-x' , 'bash', '-c' ,'source /opt/ros/noetic/setup.bash && roscore'])

cur_path = "/home/ilm/Desktop/count_customer/flow"
# run camera 1-3 flow
flow1_3 = cur_path + "/1_3.flow"
Popen(["gnome-terminal", '-x' , 'bash', '-c' ,'LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/local/lib && source /opt/ros/noetic/setup.bash && source ~/.cira_core_install/cira_libs_ws/install/setup.bash --extend && export LD_LIBRARY_PATH=$(find /usr/lib -iname nvidia-* -type d 2>&1 | sed "{:q;N;s/\\n/:/g;t q}"):${LD_LIBRARY_PATH} && export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/opt/qt511/lib:/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64 && while true; do rosrun cira_core cira_core_run --geometry +0+100 _file:='+f'{flow1_3} _hide_toolbar:=true; sleep 2s; done ;$SHELL'])
sleep(2)
# run camera 4-6 flow
flow4_6 = cur_path + "/4_6.flow"
Popen(["gnome-terminal", '-x' , 'bash', '-c' ,'LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/local/lib && source /opt/ros/noetic/setup.bash && source ~/.cira_core_install/cira_libs_ws/install/setup.bash --extend && export LD_LIBRARY_PATH=$(find /usr/lib -iname nvidia-* -type d 2>&1 | sed "{:q;N;s/\\n/:/g;t q}"):${LD_LIBRARY_PATH} && export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/opt/qt511/lib:/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64 && while true; do rosrun cira_core cira_core_run --geometry +0+100 _file:='+f'{flow4_6} _hide_toolbar:=true; sleep 2s; done ;$SHELL'])
sleep(2)
# run camera 7-9 flow
flow7_9 = cur_path + "/7_9.flow"
Popen(["gnome-terminal", '-x' , 'bash', '-c' ,'LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/local/lib && source /opt/ros/noetic/setup.bash && source ~/.cira_core_install/cira_libs_ws/install/setup.bash --extend && export LD_LIBRARY_PATH=$(find /usr/lib -iname nvidia-* -type d 2>&1 | sed "{:q;N;s/\\n/:/g;t q}"):${LD_LIBRARY_PATH} && export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/opt/qt511/lib:/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64 && while true; do rosrun cira_core cira_core_run --geometry +0+100 _file:='+f'{flow7_9} _hide_toolbar:=true; sleep 2s; done ;$SHELL'])
sleep(2)
# run camera 10-11 flow
flow10_11 = cur_path + "/10_11.flow"
Popen(["gnome-terminal", '-x' , 'bash', '-c' ,'LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/local/lib && source /opt/ros/noetic/setup.bash && source ~/.cira_core_install/cira_libs_ws/install/setup.bash --extend && export LD_LIBRARY_PATH=$(find /usr/lib -iname nvidia-* -type d 2>&1 | sed "{:q;N;s/\\n/:/g;t q}"):${LD_LIBRARY_PATH} && export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/opt/qt511/lib:/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64 && while true; do rosrun cira_core cira_core_run --geometry +0+100 _file:='+f'{flow10_11} _hide_toolbar:=truex; sleep 2s; done ;$SHELL'])
sleep(2)
