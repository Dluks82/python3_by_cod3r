#!/usr/bin/python3

from calendar import mdays, month_name
from functools import reduce

# month_31_days = filter(lambda m: mdays[m] == 31, range(1, len(month_name)))

# month_names = map(lambda m: month_name[m], month_31_days)

# together = reduce(
#     lambda all, m_name: f'{all}\n- {m_name}', month_names, 'Months with 31 days:')

# print(together)

print(
    reduce(
        lambda output, m_name: f'{output}\n- {m_name}',
        map(
            lambda m: month_name[m],
            filter(
                lambda m: mdays[m] == 31, range(1, len(month_name))
            )
        ),
        'Months with 31 days:',
    )
)
