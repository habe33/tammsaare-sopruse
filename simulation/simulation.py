#!/usr/bin/env python
import os
import sys
import optparse
import time

if 'SUMO_HOME' in os.environ and 'TS_SIMULATION' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("Please declare environment variables 'SUMO_HOME', 'TS_SIMULATION'")

from sumolib import checkBinary
import traci

from traffic_types import PEAK, OFFPEAK
from vehicles import generate as generate_vehicles
from buses import generate as generate_buses

from tammsaare_sopruse_controllers.i1 import control as control_tln_i1


def simulate_tln(max_green, max_green_diff):
    step = 0
    while traci.simulation.getMinExpectedNumber() > 0:
        control_tln_i1(step, max_green, max_green_diff)
        traci.simulationStep()
        step += 1
    traci.close()
    sys.stdout.flush()


def options():
    opt_parser = optparse.OptionParser()
    opt_parser.add_option("--nogui", action="store_true", default=False, help="run the commandline version of sumo")
    opt_parser.add_option("--new", action="store_true", default=False, help="generate new trip files")
    opt_parser.add_option("--type", action="store", type="string", dest="type", help=PEAK + " or " + OFFPEAK)
    opt_parser.add_option("--max-green", action="store", type="int", dest="max_green", help="max green in seconds")
    opt_parser.add_option("--mg-diff", action="store", type="int", dest="mg_diff", help="max green diff in seconds")
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
    path = os.environ['TS_SIMULATION']
    traci.start([sumoBinary, "-c", path + "/input/tammsaare_sopruse/" + config_name, "--tripinfo-output",
                 path + "/output/tammsaare_sopruse/trip_info-" + simulation_timestamp + ".txt",
                 "--device.emissions.probability", "1.0"])
    simulate_tln(options.max_green, options.mg_diff)
