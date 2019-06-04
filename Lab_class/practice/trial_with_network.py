import simpy
import random

RANDOM_SEED = 0
NUM_SERVERS = 1
SIM_TIME = 100  # seconds


def arrival(environment):
    client_id = 0
    while True:
        inter_arrival = random.expovariate(lambd=1)
        yield environment.timeout(inter_arrival)
        Client(environment, client_id)
        client_id += 1


class Client(object):

    def __init__(self, environment, client_id):
        self.env = environment
        self.client_id = client_id
        self.response_time = 0
        env.process(self.run())

    def run(self):
        time_arrival = self.env.now
        pack_dim = 10
        print("client ", self.client_id, "\tarrived at ", time_arrival)
        yield env.process(env.servers.serve(pack_dim))
        self.response_time = self.env.now - time_arrival
        print("client ", self.client_id, "\tresponse time ", self.response_time)


class Servers(object):

    def __init__(self, environment, service_rate):
        self.env = environment
        self.servece_rate = service_rate
        self.servers = simpy.Resource(env, capacity=10)
        self.capacity = 2
        self.client_arrive = 0

    def serve(self, pack_dim):

        with self.servers.request() as request:
            self.client_arrive = random.uniform(0, 1)
            results = yield request | env.timeout(self.client_arrive)

            if request in results:
                shared_capacity = self.capacity / self.servers.count
                service_time = pack_dim / shared_capacity
                yield env.timeout(service_time)
            else:
                print("not serving")


class Network(object):
    pass


if __name__ == '__main__':
    random.seed(RANDOM_SEED)
    env = simpy.Environment()
    env.servers = Servers(env, 1)
    env.process(arrival(env))
    env.run(until=SIM_TIME)
