from field_state import FieldState
from field_search import FieldSearch

import time
start_time = time.time()


# primal_state = FieldState([[8, 1, 3],         # extremely fast
#                            [2, 4, 5],
#                            [7, 6, 0]])

primal_state = FieldState([[2, 6, 1],         # not that fast
                           [4, 5, 3],
                           [7, 8, 0]])

# primal_state = FieldState([[1, 8, 3],         # endless search / error
#                            [6, 2, 7],
#                            [4, 0, 5]])

required_state = FieldState([[1, 2, 3],
                             [8, 0, 4],
                             [7, 6, 5]])

# required_state = FieldState([[1, 2, 3],
#                              [4, 5, 6],
#                              [7, 8, 0]])


fs = FieldSearch(primal_state, required_state)

for e in fs.start_search():
    e.draw_field()


print(f'Executing time: {round(time.time()-start_time, 5)} seconds')