import collections
import numpy

gama = 1
goal_state_index = 4
epsilon = 0.00001
states = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
actions = [0, 1, 2, 3]  # North, South, East, West
states_count = len(states)
actions_count = len(actions)

transition_matrix = numpy.zeros((states_count, actions_count, states_count))

transition_matrix[4, 0, 4] = 1
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
transition_matrix[4, 1, 4] = 1

transition_matrix[0, 2, 0] = 0.5
transition_matrix[0, 2, 1] = 0.5
transition_matrix[1, 2, 1] = 0.5
transition_matrix[1, 2, 2] = 0.5
transition_matrix[2, 2, 2] = 0.5
transition_matrix[2, 2, 3] = 0.5
transition_matrix[3, 2, 3] = 0.5
transition_matrix[3, 2, 4] = 0.5
transition_matrix[4, 2, 4] = 1
transition_matrix[5, 2, 6] = 1
transition_matrix[6, 2, 7] = 1
transition_matrix[7, 2, 8] = 1
transition_matrix[8, 2, 9] = 1

# First iteration: initialize values arbitrarily, e.g., zero
Value = [[0.0] * states_count]
policy = [None for state in range(states_count)]

reward = [-1 for state in range(states_count)]
reward[goal_state_index] = 0

iteration = 0
continue_iteration = True

while continue_iteration == True:
    iteration += 1
    continue_iteration = False

    Value.append([0] * states_count)

    for state in range(states_count):

        best_state_value = 0
        best_state_action = None

        for action in range(actions_count):
            calculed_value = sum([transition_matrix[state, action,
                                                    sNext] * (reward[sNext] + (gama * Value[iteration - 1][sNext])) for sNext in range(states_count)])

            if calculed_value != 0 and (best_state_value == 0 or calculed_value > best_state_value):
                best_state_value = calculed_value
                best_state_action = action

        if abs(best_state_value - Value[iteration - 1][state]) > epsilon:
            Value[iteration][state] = best_state_value
            policy[state] = best_state_action
            continue_iteration = True
        else:
            Value[iteration][state] = Value[iteration - 1][state]
            policy[state] = best_state_action

        print("Iteration: "+str(iteration)+" State: " + str(state) +
              " Policy: " + str(policy[state]) + " Value: " + str(Value[iteration][state]))
