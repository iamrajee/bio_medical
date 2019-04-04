import serial,time

ser = serial.Serial("/dev/ttyACM0", 115200)

inputfile = "1.txt"

def flush():
    f = open(inputfile,"w+")
    f.close()

flush()

if ser.isOpen():

    try:
        ser.flushInput()
        ser.flushOutput()
        # ser.write("AT+CSQ")
        # print("write data: AT+CSQ")
        # ser.write('0')
        # time.sleep(0.5)
        # numOfLines = 0
        # while True:
        #     response = ser.readline()
        #     print("read data: " + response)
        # numOfLines = numOfLines + 1
        # if (numOfLines >= 5):
        #     break

        count = 0
        
        while True:
            l = len(open(inputfile,"r").read().split("\n"))
            if l > 100:
                flush()
            f = open(inputfile,"a+")
            flag = ser.read()
            print("flag = ",flag,"".join([str(ord(ele)) for ele in list(flag)]))
            str1 = str(count)+","+str("".join([str(ord(ele)) for ele in list(flag)]))+"\n"
            f.write(str1)
            f.close()
            count = count+1
        ser.close()

    except Exception, e1:
        print "error communicating...: " + str(e1)

else:
    print "cannot open serial port "