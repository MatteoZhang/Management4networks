#!/usr/bin/python3

import random
from queue import Queue, PriorityQueue

# ******************************************************************************
# Constants
# ******************************************************************************
SIM_TIME = 1000

SEVICE_TIME        = 4
INTER_ARRIVAL_TIME = 10

# ******************************************************************************
# Client
# ******************************************************************************
class Client(object):

    # constructor
    def __init__(self, arrival_time):

        # the arrival time
        self.arrival_time = arrival_time

# ******************************************************************************
# Server
# ******************************************************************************
class Server(object):

    # constructor
    def __init__(self):

        # whether the server is idle or not
        self.idle = True

# ******************************************************************************
# Model environment
# ******************************************************************************
class Environment(object):

    # constructor
    def __init__(self):

        # variables of our model: the queue of "clients"
        self.waiting_line = Queue()

        # server
        self.server = Server()

# ******************************************************************************
def arrival(time, events, environment):
    # sample the time until the next event
    inter_arrival = 1 + random.uniform(0, INTER_ARRIVAL_TIME)

    # schedule the next arrival
    events.put((time + inter_arrival, "arrival"))

    # create a record for the client
    client = Client(time)

    # insert the record in the queue
    environment.waiting_line.put(client)

    # if the server is idle start the service
    if environment.server.idle:
        environment.server.idle = False

        # sample the service time
        service_time = 1 + random.uniform(0, SEVICE_TIME)

        # schedule when the client will finish the server
        events.put((time + service_time, "departure"))

# ******************************************************************************
def departure(time, events, environment):

    # get the first element from the queue
    client = environment.waiting_line.get()

    # do whatever we need to do when clients go away
    print("departure %d, %d, %d" % (client.arrival_time, time, time - client.arrival_time))

    # see whether there are more clients to in the line
    if not environment.waiting_line.empty():
        # sample the service time
        service_time = 1 + random.uniform(1, SEVICE_TIME)

        # schedule when the client will finish the server
        events.put((time + service_time, "departure"))

    else:
        environment.server.idle = True

# ******************************************************************************
# the "main" of the simulation
# ******************************************************************************
if __name__ == '__main__':

    random.seed(42)

    # environment
    environment = Environment()

    # the list of events in the form: (time, type)
    events = PriorityQueue()

    # the time control
    time = 0

    # schedule the first arrival at t=0
    events.put((0, "arrival"))

    # simulate until the simulated time reaches a constant
    while time < SIM_TIME:
        (time, event_type) = events.get()

        if event_type == "arrival":
            arrival(time, events, environment)

        elif event_type == "departure":
            departure(time, events, environment)
