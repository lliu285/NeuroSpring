'''
INSTRUCTIONS (in terminal):
pip install streamlit
streamlit run filter_interface.py
'''

import streamlit as st
import pandas as pd

df = pd.read_csv("neurospring_donors_with_categories.csv")

st.title("Grantmaker Filter System")
st.sidebar.header("Select Filters")

# Category filter
categories = df["General Category"].dropna().unique()
selected_categories = st.sidebar.multiselect("Select one or more categories", sorted(categories))

# Amount funded filter
amount_funded_ranges = {
    "No selection": (0, df['Amount Funded'].max()),
    "> 10,000,000": (10000000, df['Amount Funded'].max()),
    "9,000,000 - 10,000,000": (9000000, 9999999),
    "8,000,000 - 9,000,000": (8000000, 8999999),
    "7,000,000 - 8,000,000": (7000000, 7999999),
    "6,000,000 - 7,000,000": (6000000, 6999999),
    "5,000,000 - 6,000,000": (5000000, 5999999),
    "4,000,000 - 5,000,000": (4000000, 4999999),
    "3,000,000 - 4,000,000": (3000000, 3999999),
    "2,000,000 - 3,000,000": (2000000, 2999999),
    "1,000,000 - 2,000,000": (1000000, 1999999),
    "500,000 - 1,000,000": (500000, 999999)
}
selected_amount_funded_range = st.sidebar.selectbox("Select amount funded range", list(amount_funded_ranges.keys()))
min_amount_funded, max_amount_funded = amount_funded_ranges[selected_amount_funded_range]

# Total giving filter
total_giving_ranges = {
    "No selection": (0, df['Total Giving'].max()),
    "> 9,000,000": (9000000, df['Total Giving'].max()),
    "8,000,000 - 9,000,000": (9000000, 8999999),
    "7,000,000 - 8,000,000": (7000000, 7999999),
    "6,000,000 - 7,000,000": (6000000, 6999999),
    "5,000,000 - 6,000,000": (5000000, 5999999),
    "4,000,000 - 5,000,000": (4000000, 4999999),
    "3,000,000 - 4,000,000": (3000000, 3999999),
    "2,000,000 - 3,000,000": (2000000, 2999999),
    "1,000,000 - 2,000,000": (1000000, 1999999),
    "500,000 - 1,000,000": (500000, 999999)
}
selected_total_giving_range = st.sidebar.selectbox("Select total giving range", list(total_giving_ranges.keys()))
min_total_giving, max_total_giving = total_giving_ranges[selected_total_giving_range]

# Grant count filter
grant_count_ranges = {
    "No selection": (0, df['Grant Count'].max()),
    "> 120": (120, df['Grant Count'].max()),
    "110 - 120": (110, 119),
    "100 - 110": (100, 109),
    "90 - 100": (90, 99),
    "80 - 90": (80, 89),
    "70 - 80": (70, 79),
    "60 - 70": (60, 69),
    "50 - 60": (50, 59),
    "40 - 50": (40, 49),
    "30 - 40": (30, 39),
    "20 - 30": (20, 29),
    "10 - 20": (10, 19),
    "0 - 10": (0, 9)
}
selected_grant_count_range = st.sidebar.selectbox("Select grant count range", list(grant_count_ranges.keys()))
min_grant_count, max_grant_count = grant_count_ranges[selected_grant_count_range]

filtered_df = df[
    (df["General Category"].isin(selected_categories)) &
    (df["Grant Count"] >= min_grant_count) & (df["Grant Count"] <= max_grant_count) &
    (df["Amount Funded"] >= min_amount_funded) & (df["Amount Funded"] <= max_amount_funded) &
    (df["Total Giving"] >= min_total_giving) & (df["Total Giving"] <= max_total_giving)]

st.write(f"{len(filtered_df)} grantmakers found")
st.dataframe(filtered_df)

