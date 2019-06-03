import simpy

def main():
    env = simpy.Environment()
    env.process(traffic_light(env))
    env.run(until=100)
    print("Simulation ended")

def traffic_light(env):
    while True:
        print("GREEN \tat t= ", env.now)
        yield env.timeout(10)
        print("YELLOW \tat t= ", env.now)
        yield env.timeout(5)
        print("RED \tat t= ", env.now)
        yield env.timeout(10)

if __name__ == '__main__':
    main()



