import dataclasses as dc
from intersection.FlowCharacteristic import FlowCharacteristic
from intersection.Priority import Priority


@dc.dataclass(unsafe_hash=True)
class Flow:
    id: int
    # Usually 2 edges from the flow are sensed
    e1_lane_ids: list
    e2_lane_ids: list
    e3_lane_ids: list
    shortest_green: int
    max_green: int = None
    priority: Priority = None
    characteristics: FlowCharacteristic = None
