import numpy as np
from field_state import FieldState


class FieldSearch:
    def __init__(self, primal_state, required_state):
        self.__primal_state = primal_state
        self.__required_state = required_state

        self.__used_values = []


    def start_search(self):
        level = [self.__primal_state]
        depth = 0

        while self.__required_state not in level:
            f_score = np.array([], dtype=np.int64)

            for e in level:
                f_score = np.append(f_score, e.find_distances_sum(self.__required_state) + depth)

            while level[f_score.argmin()] in self.__used_values:
                level.pop(f_score.argmin())
                f_score = np.delete(f_score, f_score.argmin())

                if len(f_score) == 0:
                    return [FieldState([['N', 'O', ' '],
                                      ['A', 'N', 'S'],
                                      ['W', 'E', 'R']])]

            self.__used_values.append(level[f_score.argmin()])
            level = level[f_score.argmin()].generate_possibilities()
            depth += 1

        self.__used_values.append(self.__required_state)
        return self.__used_values