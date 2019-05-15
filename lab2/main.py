import simpy
import numpy
import random
from runstats import Statistics
import matplotlib.pyplot as plt

RANDOM_SEED = 1
NUM_SERVERS = 1
SIM_TIME = 60


def arrival(environment, arrival_rate):
    nations = ["china", "usa", "india", "brazil", "japan"]
    # keep track of client number client id
    # arrival will continue forever
    n = 0
    while True:

        # sample the time to next arrival
        inter_arrival = random.expovariate(lambd=arrival_rate)

        # yield an event to the simulator
        yield environment.timeout(inter_arrival)

        # a new client arrived
        n += 1
        i = random.choice(nations)
        Client(environment, i, n)


class Client(object):

    def __init__(self, environment, i="nations", n=0):
        self.env = environment
        self.nation = i
        self.number = n
        self.response_time = 0
        self.k = random.randint(1, 4)
        # the client is a "process"
        env.process(self.run())

    def run(self):
        # store the absolute arrival time
        time_arrival = self.env.now
        print("client", self.number, "from ", self.nation, "has arrived at", time_arrival)
        print("client tot request: ", self.k)
        for j in range(1, self.k+1):
            print("client request number : ", j)
            # The client goes to the first server to be served ,now is changed
            # until env.process is complete
            yield env.process(env.servers.serve())

        self.response_time = self.env.now - time_arrival
        print("client", self.number, "from ", self.nation, "response time ", self.response_time)
        stats.push(self.response_time)


class Servers(object):

    # constructor
    def __init__(self, environment, num_servers, service_rate):
        self.env = environment
        self.service_rate = service_rate
        self.servers = simpy.Resource(env, num_servers)

    def serve(self):
        # request a server
        with self.servers.request() as request:  # create obj then destroy
            yield request

            # server is free, wait until service is finished
            service_time = random.expovariate(lambd=self.service_rate)

            # yield an event to the simulator
            yield self.env.timeout(service_time)


if __name__ == '__main__':
    random.seed(RANDOM_SEED)  # same sequence each time

    mu = 20.0  # 2 customer on average per unit time (service time)
    lambd = 2  # one customer enter per time (arrival time)
    response_time = []

    # create lamda clients
    for i in range(1, lambd):
        env = simpy.Environment()
        stats = Statistics()

        # servers
        env.servers = Servers(env, NUM_SERVERS, mu)

        # start the arrival process
        env.process(arrival(env, i))  # customers

        # simulate until SIM_TIME
        env.run(until=SIM_TIME)
        response_time.append(stats.mean())

# totally occupied servers in this case
# we need parallel servers for example 5 servers for 5 continents