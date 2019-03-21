import collections

gama = 1
state_count = 10


def fill_transition_matrix(direction):
    matrix = [[0]*state_count for i in range(state_count)]

    if(direction == 'N'):
        matrix[9][5] = 1

    if(direction == 'S'):
        matrix[0][5] = 0.5
        matrix[1][6] = 0.5
        matrix[2][7] = 0.5
        matrix[3][8] = 0.5

    if(direction == 'L'):
        matrix[0][1] = 0.5
        matrix[1][2] = 0.5
        matrix[2][3] = 0.5
        matrix[3][4] = 0.5
        matrix[5][6] = 1
        matrix[6][7] = 1
        matrix[7][8] = 1
        matrix[8][9] = 1

    return matrix


class State(object):
    reward = 0

    def policy(self, current_state_index):
        for matrix_index, matrix_item in enumerate(matrix_complete):
            print("Matrix: " + str(matrix_index) +
                  " State: " + str(current_state_index))
            for next_state, percent_transition in enumerate(matrix_item[current_state_index]):
                if percent_transition > 0:
                    self.reward_calc(current_state_index,
                                     percent_transition, next_state)
        print("")

    def reward_calc(self, current_state_index, percent_transition, next_state):
        print("     Reward -> state: " + str(current_state_index) + " percent: " +
              str(percent_transition) + " next: " + str(next_state))
        # calcular a recompensa
        # compara o calculo com o reward atual e se for maior substitui
        pass


matrix_complete = [fill_transition_matrix('N'), fill_transition_matrix('S'),
                   fill_transition_matrix('L'), fill_transition_matrix('O')]

state_collection = [State() for i in range(state_count)]

for i in range(10):
    state_collection[i].policy(i)
