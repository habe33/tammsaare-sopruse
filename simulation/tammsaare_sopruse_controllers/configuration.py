import os

TL_LOGIC_ID = '11156380'
MAX_SPEED = 13.9
INTERSECTION_NAME = 'Tammsaare-Sõpruse'

PATH = os.environ['SUMO_SIMULATION']

FLOWS_PATH = PATH + '/input/tammsaare_sopruse/flows.csv'
CROSSINGS_PATH = PATH + '/input/tammsaare_sopruse/crossings.csv'
PRIORITIES_PATH = PATH + '/input/tammsaare_sopruse/priorities.csv'
PHASES_PATH = PATH + '/input/tammsaare_sopruse/phases.csv'
GREEN_TSL_STATES_PATH = PATH + '/input/tammsaare_sopruse/green_tsl_states.csv'
PROTECTION_TSL_STATES_PATH = PATH + '/input/tammsaare_sopruse/protection_tsl_states.csv'
LOGGING_PATH = PATH + '/output/tammsaare_sopruse'
