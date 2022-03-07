# import pandas as pd
# import altair as alt
# import numpy as np

# gdp = pd.read_excel(r'.\Assets\V32_DAE_All.xls', sheet_name='DAE_Valid(wo dup, NP)')
# alt.Chart(gdp).mark_bar().encode(
#     alt.X('SW_Version'),
#     alt.Y('count()'),
#     color = alt.value('#6495ED')
# )

import altair as alt
import pandas as pd
from vega_datasets import data

gdp = pd.read_excel(r'.\Assets\V32_DAE_All.xls', sheet_name='DAE_Valid(wo dup, NP)')
alt.Chart(gdp).mark_bar().encode(
    alt.X('SW_Version', sort=[
        'INT_V32.00_B07',
        'INT_V32.00_A08',
        'INT_V32.00_A09',
        'INT_V32.00_B10',
        'INT_V32.00_A11',
        'INT_V32.00_A12',
        'INT_V32.00_B13',
        'INT_V32.00_A14',
        'INT_V32.00_A15',
        'INT_V32.00_B16',
        'INT_V32.00_B16A',
        'INT_V32.00_A17',
        'INT_V32.00_B19',
        'INT_V32.00_A20',
        'INT_V32.00_A21A',
        'INT_V32.00_B22',
        'INT_V32.00_A23',
        'INT_V32.00_A24',
        'INT_V32.00_B25',
        'INT_V32.00_A26',
        'INT_V32.00_B27',
        'INT_V32.00_A28',
        'INT_V32.00_A29',
        'INT_V32.00_B30',
        'INT_V32.00_A31',
        'INT_V32.00_A32',
        'INT_V32.00_B33',
        'INT_V32.00_A34',
        'INT_V32.00_A35',
        'INT_V32.00_B36',
        'INT_V32.00_A37',
        'INT_V32.00_A38',
        'INT_V32.00_A39',
        'INT_V32.00_B40',
        'INT_V32.00_A41',
        'INT_V32.00_B42',
        'INT_V32.00_A43',
        'INT_V32.00_A44',
        'INT_V32.00_B45',
        'INT_V32.00_A46',
        'INT_V32.00_A47',
        'INT_V32.00_A48',
        'INT_V32.00_A49',
        'Other',
        'V32.00.00',
        'V32.01',
    ]),
    alt.Y('count()'),
    color = alt.value('#6495ED')
)
