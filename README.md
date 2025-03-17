# Vacuum World Agent Documentation

## Introduction
This program simulates an intelligent vacuum cleaner operating in a two-room environment. The vacuum agent determines the best sequence of actions to clean both rooms using a **Breadth-First Search (BFS)** algorithm.

## PEAS Description

| **Component**          | **Description** |
|-----------------------|----------------|
| **Performance Measure** | The agent's success is measured by how efficiently it cleans both rooms. It aims to clean the rooms in the shortest possible sequence of actions. |
| **Environment**        | Two rooms (A and B), each of which can be either clean or dirty. The agent moves between the rooms and perceives their status. |
| **Actuators**         | The agent can: (1) Suck dirt (`suck` action), and (2) Move between rooms (`move_to_A` or `move_to_B`). |
| **Sensors**          | The agent perceives the cleanliness of its current room using its built-in perception mechanism. It also maintains memory to track previously visited rooms. |
| **Exploration Strategy** | The agent initially has no knowledge of the rooms' states. It explores in a **Breadth-First Search (BFS) manner**, checking each room before deciding on cleaning or moving actions. This ensures that it systematically searches for dirty rooms and cleans them efficiently. |

## Features
- The agent starts in either Room A or Room B.
- It perceives the cleanliness of its current location.
- The agent can **suck** to clean a dirty room.
- The agent can **move** between rooms.
- The goal is to clean both rooms in the shortest number of moves.

## How It Works
1. The user inputs the initial state:
   - Room A status (clean/dirty)
   - Room B status (clean/dirty)
   - Agent's starting location (A/B)
2. The program initializes the **VacuumWorld** environment.
3. The **Breadth-First Search (BFS)** algorithm finds the optimal sequence of actions.
4. The solution is displayed step by step, showing the agent's actions and state changes.

## Code Structure
### 1. `VacuumWorld` Class
This class models the environment and agent's behavior.
- **Attributes:**
  - `room_a_status`: Clean or dirty
  - `room_b_status`: Clean or dirty
  - `agent_location`: Current agent position (A/B)
  - `agent_perceived_room_status`: What the agent believes about the room's state
  - `agent_memory`: Keeps track of previously visited rooms
- **Methods:**
  - `is_goal_state()`: Checks if both rooms are clean.
  - `get_actions()`: Returns possible actions (`suck`, `move_to_A`, `move_to_B`).
  - `perform_action(action)`: Executes an action and returns a new state.
  - `__eq__()` & `__hash__()`: Ensures states can be compared and stored in sets.
  - `__str__()`: Provides a readable representation of the state.

### 2. `breadth_first_search()`
Finds the shortest sequence of actions to clean both rooms.
- Uses a **queue (deque)** for BFS traversal.
- Keeps track of visited states.
- Returns the shortest action sequence.

### 3. `get_user_input()`
- Collects user input for the initial state.
- Ensures valid input (clean/dirty for rooms, A/B for location).

### 4. Main Execution (`__main__`)
- Gets user input.
- Initializes the environment.
- Runs the **BFS search** to find the solution.
- Displays each step of the agent's actions and new states.

## Example Execution
```
Enter Room A status (clean/dirty): dirty
Enter Room B status (clean/dirty): clean
Enter Agent location (A/B): A

Agent's action history:
Initial State: Room A: dirty, Agent: A
Action: suck,
New State: Room A: clean, Agent: A
Action: move_to_B,
New State: Room B: clean, Agent: B
```

## Conclusion
This program demonstrates a simple AI search strategy for an intelligent vacuum agent. The BFS ensures that the agent finds the shortest path to clean both rooms efficiently.

