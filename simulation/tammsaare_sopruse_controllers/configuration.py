import os

TL_LOGIC_ID = 'cluster_11791147_2032404487_27789090_81290972'
MAX_SPEED = 13.9
INTERSECTION_NAME = 'Tammsaare-Sõpruse'

PATH = os.environ['TS_SIMULATION']

FLOWS_PATH = PATH + '/input/tammsaare_sopruse/flows.csv'
#CROSSINGS_PATH = PATH + '/input/tammsaare_sopruse/crossings.csv'
PRIORITIES_PATH = PATH + '/input/tammsaare_sopruse/priorities.csv'
PHASES_PATH = PATH + '/input/tammsaare_sopruse/phases.csv'
GREEN_TSL_STATES_PATH = PATH + '/input/tammsaare_sopruse/green_tsl_states.csv'
PROTECTION_TSL_STATES_PATH = PATH + '/input/tammsaare_sopruse/protection_tsl_states.csv'
LOGGING_PATH = PATH + '/output/tammsaare_sopruse'
