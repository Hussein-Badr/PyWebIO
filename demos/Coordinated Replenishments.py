from pywebio.input import *
from pywebio.output import *
import math

def calculate_eoq(info):
    A = info['major_cost']
    D = info['demand_rate']
    v = info['variable_cost']
    r = info['carrying_charge']

    eoq = math.sqrt((2 * A * D) / (v * r))

    # Create a table to display inputs and result
    input_table = [
        ["Parameter", "Value"],
        ["Major setup cost ($)", A],
        ["Demand rate (units per time unit)", D],
        ["Unit variable cost ($/unit)", v],
        ["Carrying charge per unit of inventory per time unit ($/time unit)", r],
        ["Economic Order Quantity (EOQ)", eoq],
    ]
    put_table(input_table)

if __name__ == "__main__":
    info = input_group(
        "Economic Order Quantity (EOQ) Calculator",
        [
            input("Major setup cost for the whole family ($)", name="major_cost", type=FLOAT),
            input("Demand rate of the item (units per time unit)", name="demand_rate", type=FLOAT),
            input("Unit variable cost of the item ($/unit)", name="variable_cost", type=FLOAT),
            input("Carrying charge per unit of inventory per time unit ($/time unit)", name="carrying_charge", type=FLOAT),
        ]
    )
    calculate_eoq(info)
