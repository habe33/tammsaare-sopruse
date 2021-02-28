#!/usr/bin/env python
import os
import sys
import optparse
import time

if 'SUMO_HOME' in os.environ and 'SUMO_SIMULATION' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("Please declare environment variables 'SUMO_HOME', 'SUMO_SIMULATION'")

from sumolib import checkBinary
import traci

from traffic_types import PEAK, OFFPEAK
from vehicles import generate as generate_vehicles
from buses import generate as generate_buses

# Tallinn controllers
# from tammsaare_sopruse_controllers.i1 import control as control_tln_i1


def simulate_tln():
    step = 0
    while traci.simulation.getMinExpectedNumber() > 0:
        # control_tln_i1(step)
        traci.simulationStep()
        step += 1
    traci.close()
    sys.stdout.flush()


def options():
    opt_parser = optparse.OptionParser()
    opt_parser.add_option("--nogui", action="store_true", default=False, help="run the commandline version of sumo")
    opt_parser.add_option("--new", action="store_true", default=False, help="generate new trip files")
    opt_parser.add_option("--type", action="store", type="string", dest="type", help=PEAK + " or " + OFFPEAK)
    options, args = opt_parser.parse_args()
    return options


if __name__ == "__main__":
    options = options()

    if options.nogui:
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')

    if options.new:
        generate_vehicles(options.type, "tammsaare_sopruse")
        generate_buses(options.type, "tammsaare_sopruse")

    config_name = ""
    if options.type == PEAK:
        config_name = PEAK + ".sumo.cfg"
    elif options.type == OFFPEAK:
        config_name = OFFPEAK + ".sumo.cfg"

    simulation_timestamp = str(time.time())
    path = os.environ['SUMO_SIMULATION']
    traci.start([sumoBinary, "-c", path + "/input/tammsaare_sopruse/" + config_name, "--tripinfo-output",
                 path + "/output/tammsaare_sopruse/trip_info-" + simulation_timestamp + ".txt",
                 "--device.emissions.probability", "1.0"])
    simulate_tln()
