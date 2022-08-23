def connectMyCopter():
    parser = argparse.ArgumentParser(description='commands')
    parser.add_argument('--connect')
    args = parser.parse_args()
    connection_string =args.connect
    baud_rate = 57600
    iha = connect(connection_string,baud=baud_rate,wait_ready=True)
    return iha
def arm():
        while iha.is_armable is not True:
            print("IHA arm edilebilir degil")
            time.sleep(1)
        print("IHA arm edilebilir")
        iha.mode = VehicleMode("GUIDED")
        iha.armed = True
        while iha.armed is not True:
            print("IHA arm ediliyor")
            time.sleep(1)
            
        print("iha arm edildi")
        
iha = connectMyCopter()
arm()
time.sleep(5)
iha.close()
