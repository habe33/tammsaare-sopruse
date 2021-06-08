# PETSSA in Tammsaare-Sõpruse
Priority-driven Enhanced Traffic Signal Scheduling Algorithm in Tammsaare-Sõpruse

## Set up
Add SUMO_HOME to env variable
https://sumo.dlr.de/docs/Basics/Basic_Computer_Skills.html#sumo_home

Add TS_SIMULATION to env variable
```
export TS_SIMULATION = ${clone_path}/simulation
```


## Commands
Run PETSSA simulation with GUI: 
```
sh run_petssa.sh
```
Run PETSSA with different inputs:
```
sh run_simulation.sh
```
Run current Tammsaare-Sõpruse intersection traffic signal logic simulation with GUI: 
```
sh run_baseline.sh
```

## Extending to another intersection
Change 
* simulation/input/
* simulation/pedestrians/input
* simulation/vehicles/input
* simulation/buses/input

## Changing priorities of traffic light management
Priorities are read before every BEST-GREEN calculation. Priorities can be defined in
```
simulation/input/map/priorities.csv
```
