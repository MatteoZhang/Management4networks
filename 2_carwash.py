#!/usr/bin/python3

import random
import simpy

RANDOM_SEED = 42
NUM_MACHINES = 2  # Number of machines in the carwash
WASHTIME = 5      # Minutes it takes to clean a car
T_INTER = 7       # Create a car every ~7 minutes
SIM_TIME = 20     # Simulation time in minutes


#*******************************************************************************
#
#*******************************************************************************
class Carwash(object):

    def __init__(self, env, num_machines, washtime):
        self.env = env
        self.machine = simpy.Resource(env, num_machines)
        self.washtime = washtime

    def wash(self, car):
        print("%s washing process started" % car)
        yield self.env.timeout(WASHTIME)
        print("%s washing process finished" % car)


#*******************************************************************************
# The car process
#*******************************************************************************
class Car(object):
    def __init__(self, env, name):
        self.env = env
        self.name = name
        env.process(self.run())

    def run(self):
        print('%s arrives at the carwash at %.2f.' % (self.name, env.now))
        with env.carwash.machine.request() as request:
            yield request

            print('%s enters the carwash at %.2f.' % (self.name, env.now))
            yield env.process(env.carwash.wash(self.name))

            print('%s leaves the carwash at %.2f.' % (self.name, env.now))


#*******************************************************************************
# Setup and initialize the environment
#*******************************************************************************

def setup(env, num_machines, washtime, t_inter):
    env.carwash = Carwash(env, num_machines, washtime)

    # Create 4 initial cars
    for i in range(4):
        Car(env, i)

    # Create more cars while the simulation is running
    while True:
        yield env.timeout(random.randint(t_inter - 2, t_inter + 2))
        i += 1
        Car(env, i)

#*******************************************************************************
# Main:
#*******************************************************************************

random.seed(RANDOM_SEED)

env = simpy.Environment()
env.process(setup(env, NUM_MACHINES, WASHTIME, T_INTER))
env.run(until=SIM_TIME)
