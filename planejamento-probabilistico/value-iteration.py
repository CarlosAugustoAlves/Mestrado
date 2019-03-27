import collections

gama = 1
reward_default = 1
state_count = 10
epson = 0.00001  # epson com valor acima de 0.9 não é levado em consideração
matrix_states_result = []
goal_state = 4


def fill_transition_matrix(direction):
    matrix = [[0]*state_count for i in range(state_count)]

    if(direction == 'N'):
        matrix[5][0] = 1
        matrix[6][1] = 1
        matrix[7][2] = 1
        matrix[8][3] = 1
        matrix[9][4] = 1

    if(direction == 'S'):
        matrix[0][0] = 0.5
        matrix[0][5] = 0.5
        matrix[1][1] = 0.5
        matrix[1][6] = 0.5
        matrix[2][2] = 0.5
        matrix[2][7] = 0.5
        matrix[3][3] = 0.5
        matrix[3][8] = 0.5

    if(direction == 'L'):
        matrix[0][0] = 0.5
        matrix[0][1] = 0.5
        matrix[1][1] = 0.5
        matrix[1][2] = 0.5
        matrix[2][2] = 0.5
        matrix[2][3] = 0.5
        matrix[3][3] = 0.5
        matrix[3][4] = 0.5
        matrix[5][6] = 1
        matrix[6][7] = 1
        matrix[7][8] = 1
        matrix[8][9] = 1

    if(direction == 'O'):
        matrix[1][1] = 0.5
        matrix[1][0] = 0.5
        matrix[2][2] = 0.5
        matrix[2][1] = 0.5
        matrix[3][3] = 0.5
        matrix[3][2] = 0.5
        matrix[6][5] = 1
        matrix[7][6] = 1
        matrix[8][7] = 1
        matrix[9][8] = 1

    return matrix


def build_iteration_zero():
    state_collection = [State() for i in range(state_count)]
    for i in range(state_count):
        state_collection[i].value = 0
    matrix_states_result.append(state_collection)


class State(object):
    value = None
    policyExecuted = None
    converge = False

    def value_fuction(self, current_state_index, iteration_index):

        for matrix_index, matrix_item in enumerate(matrix_complete):
            calculated_value = None
            for next_state, percent_transition in enumerate(matrix_item[current_state_index]):
                if percent_transition > 0:
                    if calculated_value == None:
                        calculated_value = 0
                    calculated_value += self.reward_calc(current_state_index,
                                                        percent_transition, next_state, iteration_index)

            if calculated_value != None and (self.value == None or calculated_value < self.value):
                self.policyExecuted = matrix_index
                self.value = calculated_value

    def reward_calc(self, current_state_index, percent_transition, next_state, iteration_index):
        return percent_transition * (reward_default +
                                     (gama * matrix_states_result[iteration_index - 1][next_state].value))


matrix_complete = [fill_transition_matrix('N'), fill_transition_matrix('S'),
                   fill_transition_matrix('L'), fill_transition_matrix('O')]

build_iteration_zero()

iteration_index = 1
continue_iteration = True

while(continue_iteration):
    state_collection = [State() for i in range(state_count)]
    matrix_states_result.append(state_collection)

    for current_state_index in range(state_count):
        if current_state_index == goal_state or matrix_states_result[iteration_index - 1][current_state_index].converge:
            matrix_states_result[iteration_index][current_state_index] = matrix_states_result[iteration_index - 1][current_state_index]
            matrix_states_result[iteration_index][current_state_index].converge = True
            continue

        matrix_states_result[iteration_index][current_state_index].value_fuction(
            current_state_index, iteration_index)

        if (matrix_states_result[iteration_index][current_state_index].value - matrix_states_result[iteration_index - 1][current_state_index].value) < epson:
            matrix_states_result[iteration_index][current_state_index].converge = True

    if any(s for s in matrix_states_result[iteration_index] if s.converge == False) == False:
        continue_iteration = False
    else:
        iteration_index += 1

for i, matrix_states_result_item in enumerate(matrix_states_result[(len(matrix_states_result) - 1)]):
    print("Result -> total iteration: " + str(iteration_index)+" state: " + str(i) + " policy: " + str(matrix_states_result_item.policyExecuted) +
          " calue: " + str(matrix_states_result_item.value) + " converge: " + str(matrix_states_result_item.converge))
