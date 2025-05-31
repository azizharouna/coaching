

%reset


from langgraph.graph import StateGraph


def detect_mess_function(state):
    # DUMMY LOGIC: ALWAYS DETECTS MESS (REPLACE LATER)
    state.mess_detected = True
    return state

def plan_route_function(state):
    # DUMMY PATH: STRAIGHT LINE TO MESS (OPTIMIZE LATER)
    state.route_planned = True
    return state


def execute_clean_function(state):
    # DUMMY ACTION: PRETEND TO CLEAN (HARDWARE INTEGRATION LATER)
    print(f"⚡ ZAPPING MESS at {random_coordinates()}!")
    return state

# UTILITY (PASTE THIS TOO)
def random_coordinates():
    return f"[{random.randint(0,10)}, {random.randint(0,10)}]"



class RobotState:
    mess_detected: bool = False
    route_planned: bool = False

workflow = StateGraph(RobotState)


# Adding nodes
workflow.add_node("detect_mess", detect_mess_function)
workflow.add_node("plan_route", plan_route_function)
workflow.add_node("execute_clean", execute_clean_function) 



