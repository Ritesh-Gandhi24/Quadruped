import math
import serial
import time

arduino = serial.Serial(port='/dev/ttyACM1', baudrate=9600, timeout=.1)
def write(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
   
# while True:
#     num = input("Enter a number: ") # Taking input from user
#     value = write_read(num)
#     print(value) # printing the value

# cord=input()


# a1,a2=55,50
# x,y=float(cord.split(',')[0]), float(cord.split(',')[1])
# x=abs(111.921-abs(x))
# y=-(abs(y) - 2 + 11.667)
while True:
    x=int(input("Enter the x : "))
    y=int (input("Enter the y : "))
    i=0
    while i<5:
        a1,a2=80,92
        # x,y= 52, -58  
        # x, y=87, -102
        # x, y= 24, -125
        # x, y= 105, -113


        pos_offset_theta1= 0.523
        pos_offset_theta2=1.396
        theta1=math.atan2(y,x) - math.acos((a1**2 - a2**2 + x**2 + y**2)/(2*a1*math.hypot(x,y))) + math.pi/2 
        theta2=math.acos((x**2 + y**2-a1**2 -a2**2)/(2*a1*a2))

        theta2=180*theta2/math.pi
        theta1=theta1*180/math.pi

        theta1=90+theta1
        # theta2=90-(theta2-70)
        theta2=abs((theta2-70))
        # theta2=theta2+90
        # if theta1>0:
        #     theta1=theta1+90

        # if theta2>0:
        #     theta2=theta2+90;

        # if theta1<0:
        #     print("THETA1         ",theta1) 
        #     theta1=90+theta1
        # if theta2<0:
        #     print(theta2)
        #     theta2=90+theta2
        send=f"{round(theta1)},{round(theta2)}"
        print(round(theta1), round(theta2))
        write(send)
        i+=1

