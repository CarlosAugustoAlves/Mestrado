import collections
import numpy
import heapq

gama = 1
goal_state_index = 4
epsilon = 0.00001
states = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
actions = [0, 1, 2, 3]  # North, South, East, West
states_count = len(states)
actions_count = len(actions)

transition_matrix = numpy.zeros((states_count, actions_count, states_count))

transition_matrix[5, 0, 0] = 1
transition_matrix[6, 0, 1] = 1
transition_matrix[7, 0, 2] = 1
transition_matrix[8, 0, 3] = 1
transition_matrix[9, 0, 4] = 1

transition_matrix[0, 1, 0] = 0.5
transition_matrix[0, 1, 5] = 0.5
transition_matrix[1, 1, 1] = 0.5
transition_matrix[1, 1, 6] = 0.5
transition_matrix[2, 1, 2] = 0.5
transition_matrix[2, 1, 7] = 0.5
transition_matrix[3, 1, 3] = 0.5
transition_matrix[3, 1, 8] = 0.5

transition_matrix[0, 2, 0] = 0.5
transition_matrix[0, 2, 1] = 0.5
transition_matrix[1, 2, 1] = 0.5
transition_matrix[1, 2, 2] = 0.5
transition_matrix[2, 2, 2] = 0.5
transition_matrix[2, 2, 3] = 0.5
transition_matrix[3, 2, 3] = 0.5
transition_matrix[3, 2, 4] = 0.5
transition_matrix[5, 2, 6] = 1
transition_matrix[6, 2, 7] = 1
transition_matrix[7, 2, 8] = 1
transition_matrix[8, 2, 9] = 1

# First iteration: initialize values arbitrarily, e.g., zero
Value = [0 for state in range(states_count)]
policy = [None for state in range(states_count)]
reward = [-1 for state in range(states_count)]
priority_queue = []
state_priority = {}


def neighbors(state):
    neighbors_list = []
    for state_neighbor in range(states_count):
        for action in range(actions_count):
            if transition_matrix[state_neighbor, action, state] > 0 and state_neighbor not in neighbors_list:
                neighbors_list.append(state_neighbor)
    return neighbors_list


for state in range(states_count):

    best_state_value = 0
    best_state_action = None

    for action in range(actions_count):
        calculed_value = sum([transition_matrix[state, action,
                                                sNext] * (reward[sNext] + (gama * Value[sNext])) for sNext in range(states_count)])

        if calculed_value != 0 and (best_state_value == 0 or calculed_value > best_state_value):
            best_state_value = calculed_value
            best_state_action = action

    delta = abs(best_state_value - Value[state])
    if delta > 0:
        heapq.heappush(priority_queue, (-delta, state))
        state_priority[state] = -delta

iteration = 0

while len(priority_queue) > 0:    
    _, state = heapq.heappop(priority_queue)
    del state_priority[state]

    best_state_value = 0
    best_state_action = None

    for action in range(actions_count):
        calculed_value = sum([transition_matrix[state, action,
                                                sNext] * (reward[sNext] + (gama * Value[sNext])) for sNext in range(states_count)])

        if calculed_value != 0 and (best_state_value == 0 or calculed_value > best_state_value):
            best_state_value = calculed_value
            best_state_action = action

    delta = abs(best_state_value - Value[state])

    if delta > epsilon:
        Value[state] = best_state_value
        policy[state] = best_state_action
    else:
        policy[state] = best_state_action
        continue

    for state_neighbor in neighbors(state):
        new_priority = - \
            max([delta * transition_matrix[state_neighbor, action, state]
                 for action in actions])
        if new_priority < 0:
            if state_neighbor in state_priority and state_priority[state_neighbor] > new_priority:
                old_priority = state_priority[state_neighbor]
                index = priority_queue.index((old_priority, state_neighbor))
                priority_queue[index] = (new_priority, state_neighbor)
                state_priority[state_neighbor] = new_priority
            elif state_neighbor not in state_priority:
                heapq.heappush(priority_queue, (new_priority, state_neighbor))
                state_priority[state_neighbor] = new_priority
    iteration += 1
    
for state in range(states_count):
    print("Iteration: "+str(iteration)+" State: " + str(state) +
          " Policy: " + str(policy[state]) + " Value: " + str(Value[state]))
