from pymavlink import mavutil

# Establish connection
master = mavutil.mavlink_connection('udp:0.0.0.0:14550')

# Wait for heartbeat to confirm connection
master.wait_heartbeat()
print(f"Connected to system {master.target_system}, component {master.target_component}")

# Standard arm command
master.arducopter_arm()

# OR use force-arm if needed
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
    0,
    1,      # 1 to arm, 0 to disarm
    21196,  # Force-arm magic number for ArduPilot
    0, 0, 0, 0, 0
)
