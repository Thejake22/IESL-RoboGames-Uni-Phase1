from pymavlink import mavutil

# Establish connection
master = mavutil.mavlink_connection('udp:0.0.0.0:14550')

# Wait for heartbeat to confirm connection
master.wait_heartbeat()
print(f"Connected to system {master.target_system}, component {master.target_component}")
