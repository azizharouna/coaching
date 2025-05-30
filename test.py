from langgraph.graph import StateGraph

class RobotState:
    mess_detected: bool = False
    route_planned: bool = False

workflow = StateGraph(RobotState)
workflow.add_node("detect_mess", detect_mess_function)
workflow.add_node("plan_route", plan_route_function)
workflow.add_node("execute_clean", execute_clean_function)
# ^^^ DEFINE JUST THIS SKELETON. PERFECTION FORBIDDEN.  