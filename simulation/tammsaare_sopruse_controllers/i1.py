import traci

from tammsaare_sopruse_controllers.configuration import TL_LOGIC_ID, INTERSECTION_NAME, MAX_SPEED
from tammsaare_sopruse_controllers.configuration import PHASES_PATH, FLOWS_PATH, PRIORITIES_PATH, \
    PROTECTION_TSL_STATES_PATH, GREEN_TSL_STATES_PATH, LOGGING_PATH, CROSSINGS_PATH
from configuration.parser import construct_phases, read_protection_states, read_green_states, read_crossings
from simulation import tsl, Config, State

_phases = construct_phases(INTERSECTION_NAME, PHASES_PATH, FLOWS_PATH, PRIORITIES_PATH)
_crossings = read_crossings(INTERSECTION_NAME, CROSSINGS_PATH)
_protection_phases = read_protection_states(INTERSECTION_NAME, PROTECTION_TSL_STATES_PATH)
_green_states = read_green_states(INTERSECTION_NAME, GREEN_TSL_STATES_PATH)

_config = Config(_phases, _protection_phases, _green_states, MAX_SPEED, TL_LOGIC_ID, INTERSECTION_NAME, LOGGING_PATH, crossings=_crossings)
_state = State([(p.id, False) for p in _phases])


def control(step):
    global _state
    if step == traci.trafficlight.getNextSwitch(TL_LOGIC_ID):
        _state = tsl(step, _config, _state)
