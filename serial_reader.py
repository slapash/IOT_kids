import serial


def readserial(comport, baudrate):

    ser = serial.Serial(comport, baudrate, timeout=0.1)         # 1/timeout is the frequency at which the port is read

    while True:
        data = ser.readline().decode().strip()
        if data.endswith("°C"):
            print(data)
            return(data)


if __name__ == '__main__':

    readserial('/dev/cu.usbmodem14101', 9600)