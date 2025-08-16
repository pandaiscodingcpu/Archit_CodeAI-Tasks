import streamlit as st
import pandas as pd

st.header("IPL DASHBOARD")

file = "cleaned_dataset.csv"
df = pd.read_csv(file)
st.write("### Preview of Data")
st.dataframe(df.head())

st.write("### Dataset Shape")
st.write(df.shape)
st.write("### Column Types")
st.write(df.dtypes)
st.write("### Summary Stats")
st.write(df.describe())

st.write("### Numeric Column Distribution")

# Select a column
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

if len(numeric_cols) > 0:
    col = st.selectbox("Choose a numeric column", numeric_cols)
    st.bar_chart(df[col].value_counts())
else:
    st.info("No numeric columns found.")


# Pick a column to filter
cat_cols = df.select_dtypes(include=['object']).columns

if len(cat_cols) > 0:
    filter_col = st.sidebar.selectbox("Choose a categorical column to filter", cat_cols)

    if filter_col:
        options = df[filter_col].unique().tolist()
        selected = st.sidebar.multiselect(f"Select values for {filter_col}", options, default=options)
        df = df[df[filter_col].isin(selected)]



runs_per_match = df.groupby('matchId')['total_runs'].sum()
# runs_per_match_per_innings
runs_per_match_per_innings = df.groupby(['matchId','inning','year','batting_team'])['total_runs'].sum()
# print(type(runs_per_match_per_innings.index)) <class 'pandas.core.indexes.multi.MultiIndex'>
idx = runs_per_match_per_innings.groupby(level='year').idxmax()
max_runs_per_year = runs_per_match_per_innings.loc[idx].reset_index()


# Maximum runs per year
st.subheader("Maximum Runs per Year")
st.line_chart(max_runs_per_year, x="year", y="total_runs")

# Displaying team wise bowlers
bowlers = df.groupby('bowling_team')['bowler'].unique()
team = st.selectbox("Choose the team:", bowlers.index.tolist())
st.write("Bowlers for", team, ":")
st.write(bowlers[team].tolist())

# Top batting performance
st.subheader("Top Batting performance")
batsmen_performance = df.groupby(['batsman','batting_team'])['batsman_runs'].sum()
top_10_batsmen = batsmen_performance.sort_values(ascending=False).head(10)
top_10_batsmen = top_10_batsmen.reset_index() # resetting index positions
top_10_batsmen.columns = ['Batsman', 'Batting Team', 'Total Runs']
st.bar_chart(data=top_10_batsmen.set_index('Batsman')['Total Runs'].sort_values(ascending=True))