import numpy as np


class FieldState:
    def __init__(self, volume):
        self.__field = np.array(volume)


    def generate_possibilities(self):
        possibilities = []
        pos = [e[0] for e in np.where(self.__field == 0)]

        for j in range(2):
            for i in [-1, 1]:
                if pos[j-1]+i >= 3 or pos[j-1]+i < 0:
                    continue

                tmp_field, tmp_pos = self.__field.copy(), pos.copy()
                tmp_pos[j-1] += i

                tmp_field[tuple(pos)], tmp_field[tuple(tmp_pos)] = tmp_field[tuple(tmp_pos)], tmp_field[tuple(pos)]
                possibilities.append(tmp_field)

        return [FieldState(e) for e in possibilities]
    

    def get_values(self):
        return self.__field


    def find_equal(self, other):
        return np.count_nonzero(self.__field-other.get_values())


    def find_distances_sum(self, other):
        result = 0

        for e in self.__field.flatten():
            initial_field = np.array(np.where(self.__field == e))
            other_field = np.array(np.where(other.get_values() == e))

            result += int(sum(abs(initial_field - other_field)))

        return result


    def __eq__(self, other):
        if not isinstance(other, FieldState):
            return 0
        return (self.__field == other.get_values()).all()
    

    def draw_field(self):
        print('\n'+'-'*13)
        for i in range(3):
            print('| ', end='')
            for j in range(3):
                if self.__field[i, j]:
                    print(self.__field[i, j], end=' ')
                else: print(' ', end=' ')
                print('|', end=' ')
            print('\n'+'-'*13)