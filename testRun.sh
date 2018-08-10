#!/bin/bash
echo '"$1"'
SSHPASS="ubuntu"
SSHCOMMAND="ssh"
SSHACCOUNT="ubuntu@10.200.21.197"
sshpass -p "$SSHPASS" $SSHCOMMAND $SSHACCOUNT << EOF_run_commands
source ~/catkin_ws/devel/setup.bash
rostopic pub /cmd_vel geometry_msgs/Twist -r 10000 '$1' '$2'
EOF_run_commands

