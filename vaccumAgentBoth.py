import random

class Environment:
    def __init__(self, num_rooms=2):
        self.num_rooms = num_rooms
        self.rooms = {f'Room {i+1}': random.choice(['Clean', 'Dirty']) for i in range(num_rooms)}
        self.agent_location = random.choice(list(self.rooms.keys()))

    def display(self):
        print('\n--- Environment State ---')
        for room, state in self.rooms.items():
            print(f'{room}: {state}')
        print(f'Agent is in: {self.agent_location}')
        print('-------------------------')

    def is_dirty(self, room):
        return self.rooms[room] == 'Dirty'

    def clean_room(self, room):
        self.rooms[room] = 'Clean'

    def move_agent(self, new_location):
        self.agent_location = new_location

    def all_rooms_clean(self):
        return all(state == 'Clean' for state in self.rooms.values())

class SimpleReflexAgent:
    def __init__(self, environment):
        self.environment = environment
        self.actions_taken = 0

    def sense(self):
        current_room_state = self.environment.rooms[self.environment.agent_location]
        return (self.environment.agent_location, current_room_state)

    def act(self, percept):
        location, state = percept
        self.actions_taken += 1

        if state == 'Dirty':
            self.environment.clean_room(location)
            return 'Suck'
        else:
            other_rooms = [room for room in self.environment.rooms.keys() if room != location]
            if other_rooms:
                next_location = random.choice(other_rooms)
                self.environment.move_agent(next_location)
                return f'Move to {next_location}'
            else:
                return 'NoOp'
class GoalBasedAgent:
    def __init__(self, environment):
        self.environment = environment
        self.model = {room: 'Unknown' for room in environment.rooms.keys()}
        self.goal = {room: 'Clean' for room in environment.rooms.keys()}
        self.actions_taken = 0

    def sense(self):
        current_room_state = self.environment.rooms[self.environment.agent_location]
        return (self.environment.agent_location, current_room_state)

    def update_model(self, location, state):
        self.model[location] = state

    def act(self, percept):
        location, state = percept
        self.actions_taken += 1
        self.update_model(location, state)

        if state == 'Dirty':
            self.environment.clean_room(location)
            return 'Suck'
        else:
            for room, room_state in self.model.items():
                if room_state == 'Dirty':
                    self.environment.move_agent(room)
                    return f'Move to {room}'
            other_rooms = [room for room in self.environment.rooms.keys() if room != location]
            if other_rooms:
                next_location = random.choice(other_rooms)
                self.environment.move_agent(next_location)
                return f'Explore to {next_location}'
            else:
                return 'NoOp'

def simulate_agent(agent_type, num_rooms=2, max_steps=100):
    print(f'\n--- Simulating {agent_type} Agent ---')
    env = Environment(num_rooms)
    if agent_type == 'Simple Reflex':
        agent = SimpleReflexAgent(env)
    elif agent_type == 'Goal-Based':
        agent = GoalBasedAgent(env)
    else:
        raise ValueError('Invalid agent type')

    env.display()
    steps = 0
    while not env.all_rooms_clean() and steps < max_steps:
        percept = agent.sense()
        action = agent.act(percept)
        print(f'Step {steps+1}: Agent {action}')
        env.display()
        steps += 1

    if env.all_rooms_clean():
        print(f'{agent_type} Agent finished in {agent.actions_taken} actions. All rooms clean!')
    else:
        print(f'{agent_type} Agent did not clean all rooms within {max_steps} steps.')
simulate_agent('Simple Reflex')
simulate_agent('Goal-Based')
