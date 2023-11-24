import requests
import time
import random
import click
from sense_hat import SenseHat

sense = SenseHat()

def get_direction():
    d_long = 0
    d_la = 0
    send_vel = False
    for event in sense.stick.get_events():
        if event.action == "pressed":

            if event.direction == "up":
                print('Up')
                send_vel = True
                d_long = 0
                d_la = 1
            elif event.direction == "down":
                print('Down')
                send_vel = True
                d_long = 0
                d_la = -1
            elif event.direction == "left":
                print('Left')
                send_vel = True
                d_long = -1
                d_la = 0
            elif event.direction == "right":
                print('Right')
                send_vel = True
                d_long = 1
                d_la = 0
    return d_long, d_la, send_vel




if __name__ == "__main__":
    SERVER_URL = "http://127.0.0.1:5000/drone"
    while True:
        d_long, d_la, send_vel = get_direction()
        if send_vel:
            with requests.Session() as session:
                current_location = {'longitude': d_long,
                                    'latitude': d_la
                                    }
                resp = session.post(SERVER_URL, json=current_location)
