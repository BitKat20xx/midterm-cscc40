from collections import deque

class VacuumWorld:
    def __init__(self, room_a_status, room_b_status, agent_location):
        self.room_a_status = room_a_status
        self.room_b_status = room_b_status
        self.agent_location = agent_location

    def is_goal_state(self):
        return self.room_a_status == 'clean' and self.room_b_status == 'clean'

    def get_actions(self):
        actions = []
        if self.agent_location == 'A':
            actions.append('move_to_B')
            if self.room_a_status == 'dirty':
                actions.append('suck')
        else:
            actions.append('move_to_A')
            if self.room_b_status == 'dirty':
                actions.append('suck')
        return actions

    def perform_action(self, action):
        new_room_a_status = self.room_a_status
        new_room_b_status = self.room_b_status
        new_agent_location = self.agent_location

        if action == 'move_to_A':
            new_agent_location = 'A'
        elif action == 'move_to_B':
            new_agent_location = 'B'
        elif action == 'suck':
            if self.agent_location == 'A':
                new_room_a_status = 'clean'
            else:
                new_room_b_status = 'clean'

        return VacuumWorld(new_room_a_status, new_room_b_status, new_agent_location)

    def __eq__(self, other):
        return (self.room_a_status == other.room_a_status and
                self.room_b_status == other.room_b_status and
                self.agent_location == other.agent_location)

    def __hash__(self):
        return hash((self.room_a_status, self.room_b_status, self.agent_location))

    def __str__(self):
        return f"Room A: {self.room_a_status}, Room B: {self.room_b_status}, Agent: {self.agent_location}"

def breadth_first_search(initial_state):
    frontier = deque([(initial_state, [])])  # (state, path)
    explored = set()

    while frontier:
        current_state, path = frontier.popleft()

        if current_state.is_goal_state():
            return path

        explored.add(current_state)

        for action in current_state.get_actions():
            new_state = current_state.perform_action(action)
            if new_state not in explored and new_state not in [state for state, _ in frontier]:
                frontier.append((new_state, path + [action]))

    return None  # No solution found

def get_user_input():
    while True:
        room_a_status = input("Enter Room A status (clean/dirty): ").lower()
        if room_a_status in ['clean', 'dirty']:
            break
        else:
            print("Invalid input. Please enter 'clean' or 'dirty'.")

    while True:
        room_b_status = input("Enter Room B status (clean/dirty): ").lower()
        if room_b_status in ['clean', 'dirty']:
            break
        else:
            print("Invalid input. Please enter 'clean' or 'dirty'.")

    while True:
        agent_location = input("Enter Agent location (A/B): ").upper()
        if agent_location in ['A', 'B']:
            break
        else:
            print("Invalid input. Please enter 'A' or 'B'.")

    return room_a_status, room_b_status, agent_location

if __name__ == "__main__":
    room_a_status, room_b_status, agent_location = get_user_input()
    initial_state = VacuumWorld(room_a_status, room_b_status, agent_location)

    solution = breadth_first_search(initial_state)

    if solution:
        print("\nSolution found:")
        current_state = initial_state
        print(f"Initial State: {current_state}")
        for action in solution:
            current_state = current_state.perform_action(action)
            print(f"Action: {action}, New State: {current_state}")
    else:
        print("No solution found.")