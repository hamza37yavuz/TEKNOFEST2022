from dronekit import Command, connect, VehicleMode, LocationGlobalRelative
from pymavlink import mavutil
import time
import argparse

class Move:
    lat = 0
    lon = 0
    def _init_(self):
        self.lat = self.info.lat
        self.lon = self.info.lon
        self.arm()

    def arm(self):
        while iha.is_armable is not True:
            print("İHA arm edilebilir durumda değil.")
            time.sleep(1)
        print("İHA arm edilebilir.")
        iha.mode = VehicleMode("GUIDED")
        iha.armed = True
        while iha.armed is not True:
            print("İHA arm ediliyor...")
            time.sleep(0.5)

        print("İHA arm edildi.")
    def takeOff(self,alt):
        iha.simple_takeoff(alt)
    
        while iha.location.global_relative_frame.alt < alt * 0.9:
            print("İha hedefe yükseliyor.")
            time.sleep(1)
            
    def goIha(self,x, y, down):

        msg = iha.message_factory.set_position_target_local_ned_encode(
            0,       # time_boot_ms (not used)
            0, 0,    # target system, target component
            mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED, # frame
            0b0000111111111000, # type_mask (only positions enabled)
            x, y, down,
            0, 0, 0, # x, y, z velocity in m/s  (not used)
            0, 0, 0, # x, y, z acceleration (not supported yet, ignored in GCS_Mavlink)
            0, 0)    # yaw, yaw_rate (not supported yet, ignored in GCS_Mavlink)
        # send command to drone
        iha.send_mavlink(msg)
        
    def goEarth(self,north, east, down):
        """
        Send SET_POSITION_TARGET_LOCAL_NED command to request the drone fly to a specified
        location in the North, East, Down frame.
        """
        msg = iha.message_factory.set_position_target_local_ned_encode(
            0,       # time_boot_ms (not used)
            0, 0,    # target system, target component
            mavutil.mavlink.MAV_FRAME_LOCAL_NED, # frame
            0b0000111111111000, # type_mask (only positions enabled)
            north, east, down,
            0, 0, 0, # x, y, z velocity in m/s  (not used)
            0, 0, 0, # x, y, z acceleration (not supported yet, ignored in GCS_Mavlink)
            0, 0)    # yaw, yaw_rate (not supported yet, ignored in GCS_Mavlink)
        # send command to drone
        iha.send_mavlink(msg)
        
    def info(self):
        return iha.location.global_frame   
    def gorev_ekle(self):
        global komut
        komut = iha.commands

        komut.clear()
        time.sleep(1)
        # LAND
        komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_LAND, 0, 0, 0, 0, 0, 0, self.lat, self.lon, 0))
        
        # CONTROL
        komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_LAND, 0, 0, 0, 0, 0, 0, self.lat, self.lon, 0))

        komut.upload()
        print("Komutlar yukleniyor...")
    def run(self):
        self.gorev_ekle()
        komut.next = 0
        iha.mode = VehicleMode("AUTO")

        while True:
            next_waypoint = komut.next
            print(self.info())
            print(f"Siradaki komut {next_waypoint}")
            time.sleep(1)

            if next_waypoint is 2:
                print("Gorev bitti.")
                break
    @staticmethod
    def connectMyCopter():
        parser = argparse.ArgumentParser(description='commands')
        parser.add_argument('--connect')
        args = parser.parse_args()
        connection_string =args.connect
        baud_rate = 57600
        iha = connect(connection_string,baud=baud_rate,wait_ready=True)
        return iha

#MAİN
iha = Move.connectMyCopter()

m = Move()
m.takeOff(1)
m.goEarth(0,2,-1)
time.sleep(5)
m.run()
iha.close()
