#!/bin/sh
MAX_GREEN=25
MG_DIFF=5
PRIORITY=True
TYPE=peak

IDENTIFIER="${TYPE}-${MAX_GREEN}-${MG_DIFF}-${PRIORITY}"
SIM_OUTPUT_FILE="${TS_SIMULATION}/output/tammsaare_sopruse/petssa/trip_info-${IDENTIFIER}.xml"
RES_OUTPUT_FILE="${TS_SIMULATION}/output/tammsaare_sopruse/petssa/result-${IDENTIFIER}.csv"
AGG_OUTPUT_FILE="${TS_SIMULATION}/output/tammsaare_sopruse/petssa/aggregated_result-${IDENTIFIER}.csv"
python $TS_SIMULATION/simulation.py --nogui --type ${TYPE} --max-green ${MAX_GREEN} --mg-diff ${MG_DIFF} --priority ${PRIORITY}
python $SUMO_HOME/tools/xml/xml2csv.py ${SIM_OUTPUT_FILE} --output ${RES_OUTPUT_FILE}
python $TS_SIMULATION/output/aggregate_output.py --input ${RES_OUTPUT_FILE} --output ${AGG_OUTPUT_FILE}