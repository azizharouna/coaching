# === NODE/EDGE CERTIFIED KILL PROTOCOL === 
import random
from langgraph.graph import StateGraph, END

class RobotState:
    mess_detected: bool = False
    route_planned: bool = False

# NODES = FUNCTIONS
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
    print(f"🚀 LASER-CLEANING {random_coordinates()} !")
    return state

# ---- UTILITIES ----
def random_coordinates():  # <-- MISSING WEAPON DEPLOYED
    return f"[{random.randint(0,10)}, {random.randint(0,10)}]"


# ---- GRAPH ASSEMBLY ----
builder = StateGraph(RobotState)


# Adding nodes
builder.add_node("detect_mess", detect_mess_function)
builder.add_node("plan_route", plan_route_function)
builder.add_node("execute_clean", execute_clean_function) 


# Adding the edges
builder.add_edge("detect_mess", "plan_route")
builder.add_edge("plan_route", "execute_clean")
builder.add_edge( "execute_clean", END) # TERMINAL STATE

#s setting the entry point
builder.set_entry_point("detect_mess")

# ---- LAUNCH SEQUENCE ----#
cleaning_bot = builder.compile()  # sometimes  graph = builder.compile()

cleaning_bot.invoke(RobotState()) # FIRE!