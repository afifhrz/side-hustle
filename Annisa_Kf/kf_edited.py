import serial
import pynmea2 as nmea
import time
# import gmplot
import math
from math import *
import RPi.GPIO as GPIO
import threading
from i2clibraries import i2c_hmc5883l
from pykalman import KalmanFilter
import haversine as hs
# import geopy
from mysteer2 import reset

lat = 0
lng = 0
heading = 0
degree = 0
nexHeading = 0
distance = 0
distance1 = 0
dt = 1

currentPosFiltered=[[None,None,None],
                    [None,None,None],
                    [[0,0,0],None,0]]

filtered_state= [[None,None,None],
                 [0,None,None],
                 [0,None,None]]

apikey = '' # (your API key here)
#gmap = gmplot.GoogleMapPlotter(-6.90797266607928, 107.7761143223271, 14, apikey=apikey)

nextPos = {'lat': -6.924261, 'lng': 107.773663}

port = serial.Serial("/dev/ttyS0", 9600)

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)  # Steer Right
GPIO.setup(16,GPIO.OUT)  # Steer Left
#GPIO.setup(6,GPIO.OUT)  # Control
GPIO.setup(20,GPIO.OUT)   # Move Forward
#GPIO.setup(xx,GPIO.OUT)   # Buzzer

GPIO.output(20,GPIO.LOW)
time.sleep(2)# Maju
#GPIO.output(xx,GPIO.LOW)   # Buzzer OFF


lat2 = nextPos['lat']
lon2 = nextPos['lng']

def readGPS() :
    try:
        while True:
            try:
                mdata = port.readline().decode().strip()
                try:
                    #print(mdata)
                    if "$GNGGA" in mdata:
                        msg = nmea.parse(mdata)
                        lat = float("{:.6f}".format(msg.latitude))
                        lon = float("{:.6f}".format(msg.longitude))
                        print(lat, lon )
                        coord = []
                        coord.append(lat)
                        coord.append(lon)
                        return coord
                except serial.SerialException as e:
                    print("Device error: {}". format(e))
                    break
            except nmea.ParseError as e:
                print("Parse error: {}".format(e))
                break
    except (KeyboardInterrupt, SystemExit):
        port.close()
        print("Selesai")

gpsMeasurements = []
nArray = 5

def getGPSFiltered(gpsMeasurements, lastPosition) :
    for i in range(nArray):
        gpsMeasurements.append(readGPS())
           
    #kecepatan (current_pos – last_position) / dt
    initial_state_mean = lastPosition
    
    measurements = [gpsMeasurements[0][0],
                    (gpsMeasurements[0][0] - lastPosition[0][0]) / dt,
                    gpsMeasurements[0][1]
                    (gpsMeasurements[0][1] - lastPosition[0][2]) / dt]

    transition_matrix = [[1, dt, 0, 0],
                         [0, 1, 0, 0],
                         [0, 0, 1, dt],
                         [0, 0, 0, 1]]

    observation_matrix = [[1, 0, 0, 0],
                          [0, 0, 1, 0]]

    kf1 = KalmanFilter(transition_matrices = transition_matrix,
                      observation_matrices = observation_matrix,
                      initial_state_mean = initial_state_mean)
    
    kf1 = kf1.em(measurements, n_iter=5)
    (smoothed_state_means, smoothed_state_covariances) = kf1.smooth(measurements)

    kf2 = KalmanFilter(transition_matrices = transition_matrix,
                       observation_matrices = observation_matrix,
                       initial_state_mean = initial_state_mean,
                       observation_covariance = 10 * kf1.observation_covariance,
                       em_vars=['transition_covariance', 'initial_state_covariance'])
    kf2 = kf2.em(measurements, n_iter=5)
    (filtered_state, smoothed_state_covariances) = kf2.filter(measurements)

    (smoothed_state_means, smoothed_state_covariances) = kf2.smooth(measurements)
    return (smoothed_state_means, filtered_state)

        
def getNextHeading(lat1, lon1, lat2, lon2) : #lat2 --> tujuan, #lat1 --> posisi saat ini
    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    X =  cos(lat2) * sin(dlon)
    Y = cos(lat1) * sin(lat2) - sin(lat1) * cos(lat2) * cos(dlon)
    heading = atan2(X,Y)#satuan masih radian
    heading = math.degrees(heading)
    compass_bearing = (heading + 360) % 360 #satuan dalam derajat
    return compass_bearing

def readCompass ():
    hmc5883l = i2c_hmc5883l.i2c_hmc5883l(1)
    hmc5883l.setContinuousMode()
    hmc5883l.setDeclination(0, 0)
    (heading, minutes) = hmc5883l.getHeading()
    return heading

def getDistancebyHaversine(lat1, lon1, lat2, lon2) :
    loc1 = (lat1, lon1)
    loc2 = (lat2, lon2)
    distance = hs.haversine(loc1,loc2)*1000
    return distance

try:
  while True:
        lat = 0
        lng = 0
        heading = 0
        degree = 0
        nexHeading = 0
        distance = 0
       
        currentPos = readGPS()
        lat2 = nextPos['lat']
        lon2 = nextPos['lng']
        gpsMeasurements.append(currentPos)
        gpsMeasurements.pop(0)
        
        init_state_kf = [currentPosFiltered[2][0], filtered_state[1][0], currentPosFiltered[2][2], filtered_state[2][0]]

        currentPosFiltered, filtered_state = getGPSFiltered(gpsMeasurements, init_state_kf)
        
        print("")
        print(gpsMeasurements)
        nextHeading = getNextHeading(currentPosFiltered[2, 0], currentPosFiltered[2, 2], lat2, lon2) 
        heading = readCompass()
       
        degree = nextHeading - heading
        
        print("")
        print("Heading: ", heading)
        print("Next Heading: ", nextHeading)
        print("Degree: ", degree)
        print("Latitude Filter: ", currentPosFiltered[0, 0])
        print("Longitude Filter: ", currentPosFiltered[0, 2])
        
        if (degree >= 0) :# belok kanan
            print("belok kanan")
            GPIO.output(21,GPIO.LOW)
            time.sleep(2)
            GPIO.output(21,GPIO.HIGH)
            GPIO.output(20,GPIO.LOW)
            time.sleep(4)
            GPIO.output(20,GPIO.HIGH)
            
        elif (degree < 0): #belok kiri
            print("belok kiri")
            GPIO.output(16,GPIO.LOW)
            time.sleep(2)
            GPIO.output(16,GPIO.HIGH)
            GPIO.output(20, GPIO.LOW)
            time.sleep(4)
            GPIO.output(20,GPIO.HIGH)
       
        distance = getDistancebyHaversine(currentPos[0], currentPos[1], lat2, lon2)
        print("Distance1:", distance1)
        
        #if round((distance - distance1,1) == 0.0):
        if abs(distance - distance1) == 0.0:
            print("ERROR, ULANGI")
            reset()
            break
        print('test',round(distance - distance1,0))
        distance1 = distance
        
        print("Distance: ", distance)
        if (distance <= 10) :
            print("Yeay, sudah sampaiii...")
            GPIO.output(20,GPIO.HIGH)
            time.sleep(2)
            GPIO.output(21,GPIO.HIGH)
            time.sleep(2)
            GPIO.output(16,GPIO.HIGH)
            time.sleep(2)# Stop
            reset()
            break
        
        hfile = open("position.txt","a")
        hfile.write("%s,%s,%s,%s,%s\n" % (currentPos[0], currentPos[1], degree, heading, distance))
        time.sleep(5)
        hfile.close()
        
except KeyboardInterrupt:        
  GPIO.cleanup()
  port.close()
