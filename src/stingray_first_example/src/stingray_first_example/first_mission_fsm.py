import rospy
import smach
from stingray_missions_lib.fsm.missions_fsm import Mission, MissionsFSMFactory
import actionlib
import stingray_movement_msgs.msg


class ExampleMission(Mission):
    def __init__(self):
        super().__init__("EXAMPLE")

    def execute(self, userdata):
        print("Hello from the mission!")
        return self.outcome_ok

    
class FirstMissionsFactory(MissionsFSMFactory):
    def __init__(self) -> None:
        super().__init__()

    def create_fsm(self):
        sm = smach.StateMachine(outcomes=[self.outcome_ok, self.outcome_failed])
        with sm:
            smach.StateMachine.add("EXAMPLE_MISSION", ExampleMission(), transitions={"EXAMPLE_OK": self.outcome_ok,
                                                                                     "EXAMPLE_FAILED": self.outcome_failed})
        return sm