# midterm-cscc40

Explanation:

VacuumWorld Class:

Represents the state of the vacuum world.
Stores the status of rooms A and B (clean or dirty) and the agent's location (A or B).
is_goal_state(): Checks if both rooms are clean.
get_actions(): Returns a list of possible actions based on the current state.
perform_action(): Returns a new VacuumWorld object representing the state after performing an action.
__eq__ and __hash__: Enables using VacuumWorld objects in sets and dictionaries.
__str__: Provides a readable string representation of the state.
breadth_first_search(initial_state) Function:

Implements the Breadth-First Search algorithm.
Uses a deque (double-ended queue) for the frontier.
Maintains an explored set to track visited states.
Iteratively explores the state space until the goal state is found or the frontier is empty.
Returns the path (list of actions) to the solution, or None if no solution is found.
get_user_input() Function:

Gets initial state information from the user with input validation.
Returns the room statuses and agent location.
if __name__ == "__main__": Block:

Gets user input for the initial state.
Creates a VacuumWorld object for the initial state.
Calls breadth_first_search() to find a solution.
Prints the solution path (actions and state transitions) or a "No solution found" message.
The code now prints out each state change, and the action that caused the change. To run this code: