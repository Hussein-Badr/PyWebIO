from pywebio.input import *
from pywebio.output import *
import math
import pandas as pd

def calculate_teoq(A, D, v, r):
    # Calculate Teoq
    teoq = math.sqrt((2 * A * D) / (v * r))
    teoq_time = teoq / D  # Convert Teoq to time

    # Display result in table format
    result_table = [
        ["Parameter", "Value"],
        ["Major setup cost ($)", A],
        ["Demand rate (units per time unit)", D],
        ["Unit variable cost ($/unit)", v],
        ["Carrying charge per unit of inventory per time unit ($/time unit)", r],
        ["Time-based Economic Order Quantity (Teoq)", teoq_time],
    ]
    put_table(result_table)

def file_upload_callback(data):
    try:
        # Read the uploaded Excel file
        df = pd.read_excel(data['content'])

        # Extract required parameters from the Excel data
        major_cost = df['A'].iloc[0]
        demand_rate = df['D'].iloc[0]
        variable_cost = df['v'].iloc[0]
        carrying_charge = df['r'].iloc[0]

        # Call the function to calculate Teoq with the extracted parameters
        calculate_teoq(major_cost, demand_rate, variable_cost, carrying_charge)
        
        put_text("File uploaded and processed successfully!")

    except KeyError as e:
        put_text(f"An error occurred: Missing column '{e.args[0]}' in the Excel file.")
    except Exception as e:
        put_text(f"An error occurred: {e}")

if __name__ == "__main__":
    # Display file upload button
    put_markdown("Upload an Excel file containing the required data:")
    uploaded_file = file_upload(accept=".xlsx")

    # If file is uploaded, read the data and calculate TEOQ
    if uploaded_file:
        file_upload_callback(uploaded_file)
from pywebio.input import *
from pywebio.output import *
import math
import pandas as pd

def calculate_teoq(A, D, v, r):
    # Calculate Teoq
    teoq = math.sqrt((2 * A * D) / (v * r))
    teoq_time = teoq / D  # Convert Teoq to time

    # Display result in table format
    result_table = [
        ["Parameter", "Value"],
        ["Major setup cost ($)", A],
        ["Demand rate (units per time unit)", D],
        ["Unit variable cost ($/unit)", v],
        ["Carrying charge per unit of inventory per time unit ($/time unit)", r],
        ["Time-based Economic Order Quantity (Teoq)", teoq_time],
    ]
    put_table(result_table)

def file_upload_callback(data):
    try:
        # Read the uploaded Excel file
        df = pd.read_excel(data['content'])

        # Extract required parameters from the Excel data
        major_cost = df['A'].iloc[0]
        demand_rate = df['D'].iloc[0]
        variable_cost = df['v'].iloc[0]
        carrying_charge = df['r'].iloc[0]

        # Call the function to calculate Teoq with the extracted parameters
        calculate_teoq(major_cost, demand_rate, variable_cost, carrying_charge)
        
        put_text("File uploaded and processed successfully!")

    except KeyError as e:
        put_text(f"An error occurred: Missing column '{e.args[0]}' in the Excel file.")
    except Exception as e:
        put_text(f"An error occurred: {e}")

if __name__ == "__main__":
    # Display file upload button
    put_markdown("Upload an Excel file containing the required data:")
    uploaded_file = file_upload(accept=".xlsx")

    # If file is uploaded, read the data and calculate TEOQ
    if uploaded_file:
        file_upload_callback(uploaded_file)
