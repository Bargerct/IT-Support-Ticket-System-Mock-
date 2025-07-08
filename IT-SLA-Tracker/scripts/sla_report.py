# sla_report.py

import pandas as pd
import numpy as np
import datetime

print("✅ SLA script started... loading data...")
tickets_df = pd.read_csv("tickets/tickets.csv")
print("✅ Data loaded:")
print(tickets_df)



# Read the tickets data from CSV into a DataFrame
tickets_df = pd.read_csv("tickets/tickets.csv")

# Convert the CreatedDate column from string to datetime
tickets_df['CreatedDate'] = pd.to_datetime(tickets_df['CreatedDate'])

# Calculate how many days each ticket has been open
today = datetime.datetime.today()   # current date and time (you could also use datetime.datetime.now())
tickets_df['DaysOpen'] = (today - tickets_df['CreatedDate']).dt.days

# Flag overdue tickets: True/False or Yes/No based on DaysOpen > 3
tickets_df['Overdue'] = np.where(tickets_df['DaysOpen'] > 3, 'Yes', 'No')

# Filter only overdue tickets
overdue_df = tickets_df[tickets_df['Overdue'] == 'Yes']

# Save the overdue tickets to a new CSV file
overdue_df.to_csv("tickets/overdue_tickets.csv", index=False)

# Save the full tickets data with the new columns to a CSV
tickets_df.to_csv("tickets/tickets_updated.csv", index=False)

# Print a summary
total_tickets = len(tickets_df)
overdue_count = len(overdue_df)
print(f"Processed {total_tickets} tickets. Overdue tickets found: {overdue_count}.")
print("Overdue tickets have been saved to tickets/overdue_tickets.csv")
if overdue_count > 0:
    overdue_ids = overdue_df['TicketID'].tolist()
    print("Overdue Ticket IDs:", ", ".join(overdue_ids))
