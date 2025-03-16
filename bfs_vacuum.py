from collections import deque

class VacuumWorld:
    def __init__(self, room_a_status, room_b_status, agent_location, agent_perceived_room_status=None, agent_memory=None):
        self.room_a_status = room_a_status
        self.room_b_status = room_b_status
        self.agent_location = agent_location
        if agent_perceived_room_status is None:
            if agent_location == 'A':
                self.agent_perceived_room_status = room_a_status
            else:
                self.agent_perceived_room_status = room_b_status
        else:
            self.agent_perceived_room_status = agent_perceived_room_status
        if agent_memory is None:
            agent_memory = {}
            if agent_location == 'A':
                agent_memory['A'] = self.agent_perceived_room_status
            else:
                agent_memory['B'] = self.agent_perceived_room_status
        self.agent_memory = agent_memory

    def is_goal_state(self):
        return 'A' in self.agent_memory and self.agent_memory['A'] == 'clean' and \
               'B' in self.agent_memory and self.agent_memory['B'] == 'clean'

    def get_actions(self):
        actions = []
        if self.agent_location == 'A':
            if self.agent_perceived_room_status == 'dirty':
                actions.append('suck')
            if 'B' not in self.agent_memory or self.agent_memory['B'] != 'clean':
                actions.append('move_to_B')
        else:
            if self.agent_perceived_room_status == 'dirty':
                actions.append('suck')
            if 'A' not in self.agent_memory or self.agent_memory['A'] != 'clean':
                actions.append('move_to_A')
        return actions

    def perform_action(self, action):
        new_room_a_status = self.room_a_status
        new_room_b_status = self.room_b_status
        new_agent_location = self.agent_location
        new_agent_perceived_room_status = self.agent_perceived_room_status
        new_agent_memory = self.agent_memory.copy()

        if action == 'move_to_A':
            new_agent_location = 'A'
            new_agent_perceived_room_status = self.room_a_status
            new_agent_memory['A'] = new_agent_perceived_room_status
        elif action == 'move_to_B':
            new_agent_location = 'B'
            new_agent_perceived_room_status = self.room_b_status
            new_agent_memory['B'] = new_agent_perceived_room_status
        elif action == 'suck':
            if self.agent_location == 'A':
                new_room_a_status = 'clean'
                new_agent_perceived_room_status = 'clean'
                new_agent_memory['A'] = 'clean'
            else:
                new_room_b_status = 'clean'
                new_agent_perceived_room_status = 'clean'
                new_agent_memory['B'] = 'clean'

        return VacuumWorld(new_room_a_status, new_room_b_status, new_agent_location, new_agent_perceived_room_status, new_agent_memory)

    def __eq__(self, other):
        return (self.room_a_status == other.room_a_status and
                self.room_b_status == other.room_b_status and
                self.agent_location == other.agent_location and
                self.agent_perceived_room_status == other.agent_perceived_room_status and
                self.agent_memory == other.agent_memory)

    def __hash__(self):
        return hash((self.room_a_status, self.room_b_status, self.agent_location, self.agent_perceived_room_status, tuple(sorted(self.agent_memory.items()))))

    def __str__(self):
        if self.agent_location == 'A':
            return f"Room A: {self.agent_perceived_room_status}, Agent: {self.agent_location}"
        else:
            return f"Room B: {self.agent_perceived_room_status}, Agent: {self.agent_location}"

def breadth_first_search(initial_state, max_depth=10):
    frontier = deque([(initial_state, [], 0)])
    explored = set()
    goal_paths = []

    while frontier:
        current_state, path, depth = frontier.popleft()

        if current_state.is_goal_state():
            goal_paths.append(path)

        if depth >= max_depth:
            continue

        explored.add(current_state)

        for action in current_state.get_actions():
            new_state = current_state.perform_action(action)
            if new_state not in explored:
                frontier.append((new_state, path + [action], depth + 1))

    if goal_paths:
        return min(goal_paths, key=len)
    else:
        return None

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
        print("\nAgent's action history:")
        current_state = initial_state
        print(f"Initial State: {current_state}")
        for action in solution:
            current_state = current_state.perform_action(action)
            print(f"Action: {action}, "
                  f"New State: {current_state}")
    else:
        print("No solution found.")