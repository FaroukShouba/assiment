from results import Results
from voter import Voter

import json

# with open('results.json', 'r') as f:
#     date = json.load(f)
#     for p in date:
#         my_result = Results(p['Center Name'], p['Center Number'], p['Valid Votes'], None)
#         my_result.save_to_db()
#


# my_result = Voter('1', '2', '3', '4', '2018-09-15 ', '6', '7', '8', '9', '10', 1212, '12', 212, 21, None)
# my_result.save_to_db()


my_result = Voter('1', '2', '3', None)
my_result.save_to_db()


