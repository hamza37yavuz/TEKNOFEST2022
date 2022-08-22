import dronekit as dr
import time
import argparse


def connectMyCopter():
    parser = argparse.ArgumentParser(description='commands')
    parser.add_argument('--connect')
    args = parser.parse_args()
    connection_string =args.connect
    baud_rate = 57600
    vehicle = dr.connect(connection_string,baud=baud_rate,wait_ready=True)
    return arm()
def arm():
        while vehicle.is_armable is not True:
            print("IHA arm edilebilir degil")
            time.sleep(1)
        print("IHA arm edilebilir")
        vehicle.mode = dr.VehicleMode("GUIDED")
        vehicle.armed = True
        while vehicle.armed is not True:
            print("IHA arm ediliyor")
            time.sleep(1)
            
        print("iha arm edildi")
        
vehicle = connectMyCopter()