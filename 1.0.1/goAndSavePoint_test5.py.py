from dronekit import Command, connect, VehicleMode, LocationGlobalRelative
from pymavlink import mavutil
import time
import argparse

class Move:
    lat,lon,lat1,lon1 = 0,0,0,0
    def _init_(self):
        self.arm()

    def arm(self):
        while iha.is_armable is not True:
            print("IHA arm edilebilir durumda degil.")
            time.sleep(1)
        print("IHA arm edilebilir.")

        iha.mode = VehicleMode("GUIDED")

        iha.armed = True

        while iha.armed is not True:
            print("IHA arm ediliyor...")
            time.sleep(0.5)

        print("IHA arm edildi.")
    def takeOff(self,alt):
        iha.simple_takeoff(alt)
    
        while iha.location.global_relative_frame.alt < alt * 0.9:
            print("Iha hedefe yükseliyor.")
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
        
    def info(self):
        return iha.location.global_frame      
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
    def gorev_ekle(self):
        global komut
        komut = iha.commands

        komut.clear()
        time.sleep(1)
        #WAYPOINT
        komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0, self.lat1, self.lon1, 6))
        komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0, self.lat1, self.lon1, 3))
        komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0, self.lat1, self.lon1, 6))
        
        # LAND
        komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_LAND, 0, 0, 0, 0, 0, 0, self.lat, self.lon, 0))
        
        # CONTROL
        komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_LAND, 0, 0, 0, 0, 0, 0, self.lat, self.lon, 0))

        komut.upload()
        print("Komutlar yukleniyor...")
        
    def run(self,lat,lon,lat1,lon1):
        self.lat,self.lon = lat,lon # iha rtl ile indigi zaman once yukselir sonra iner bunu engelleme amacli ilk konum kayit altina alinmistir.
        self.lat1,self.lon1 = lat1,lon1 # parkurun tam ortasindan aldigi konum  
        self.gorev_ekle()

        komut.next = 0

        iha.mode = VehicleMode("AUTO")

        while True:
            next_waypoint = komut.next
            print(self.info())
            print(f"Siradaki komut {next_waypoint}")
            time.sleep(1)

            if next_waypoint is 4:
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
@MAIN
iha = Move.connectMyCopter()

m = Move()
m.takeOff(6)
lat = m.info.lat()
lon = m.info.lon()
a,b,c=0,0,0 # a:x b:y eksenini ifade eder. c kumanda devreye girerse stabilize modda kodu durdurmak için denetleme amaclidir. 

for i in range(30):
    a += 2
    m.goEarth(a,0,-1)
    if iha.mode != "GUIDED":
        c = 1
        break
    if a == 30:
        lat1 = m.info.lat()
        lon1 = m.info.lon()
        
if c==0:
    time.sleep(10)
    m.run(lat,lon,lat1,lon1)
    iha.close()
