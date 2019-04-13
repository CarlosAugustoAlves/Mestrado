import collections
import numpy

gama = 1
reward_default = 1
goal_state_index = 4
epsilon = 0.00001
states = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
actions = [0, 1, 2, 3]
states_count = len(states)
actions_count = len(actions)
transition_matrix = numpy.zeros((states_count, actions_count, states_count))

transition_matrix[0, 1, 0] = 0.5
transition_matrix[0, 1, 5] = 0.5
transition_matrix[0, 2, 0] = 0.5
transition_matrix[0, 2, 1] = 0.5

transition_matrix[1, 1, 1] = 0.5
transition_matrix[1, 1, 6] = 0.5
transition_matrix[1, 2, 1] = 0.5
transition_matrix[1, 2, 2] = 0.5

transition_matrix[2, 1, 2] = 0.5
transition_matrix[2, 1, 7] = 0.5
transition_matrix[2, 2, 2] = 0.5
transition_matrix[2, 2, 3] = 0.5

transition_matrix[3, 1, 3] = 0.5
transition_matrix[3, 1, 8] = 0.5
transition_matrix[3, 2, 3] = 0.5
transition_matrix[3, 2, 4] = 0.5

transition_matrix[5, 0, 0] = 1
transition_matrix[5, 2, 6] = 1

transition_matrix[6, 0, 1] = 1
transition_matrix[6, 2, 7] = 1

transition_matrix[7, 0, 2] = 1
transition_matrix[7, 2, 8] = 1

transition_matrix[8, 0, 3] = 1
transition_matrix[8, 2, 9] = 1

transition_matrix[9, 0, 4] = 1

policy = [0 for state in range(states_count)]
policy[goal_state_index] = None

V = numpy.zeros(states_count)

iteration = 0
continue_iteration = True

while continue_iteration == True:
    iteration += 1
    continue_iteration = False

    for state in range(states_count):
        if state != goal_state_index:
            V[state] = sum([transition_matrix[state, policy[state],
                                              sNext] * (reward_default + (gama * V[sNext])) for sNext in range(states_count)])

        print("Iteration: "+str(iteration)+" State: " + str(state) +
              " Policy: " + str(policy[state]) + " Value: " + str(V[state]))

    for state in range(states_count):
        
        best_state_value = 0
        best_state_action = 0

        for action in range(actions_count):
            calculed_value = sum([transition_matrix[state, action,
                                                    sNext] * (reward_default + (gama * V[sNext])) for sNext in range(states_count)])

            if calculed_value > 0 and (best_state_value == 0 or calculed_value < best_state_value):
                best_state_value = calculed_value
                best_state_action = action

        if abs(best_state_value - V[state]) > epsilon:
            policy[state] = best_state_action
            continue_iteration = True
