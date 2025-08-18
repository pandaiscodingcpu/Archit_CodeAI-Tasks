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

# Top batting performance
st.subheader("Top Batting performance")
batsmen_performance = df.groupby(['batsman','batting_team'])['batsman_runs'].sum()
top_10_batsmen = batsmen_performance.sort_values(ascending=False).head(10)
top_10_batsmen = top_10_batsmen.reset_index() # resetting index positions
top_10_batsmen.columns = ['Batsman', 'Batting Team', 'Total Runs']
st.bar_chart(data=top_10_batsmen.set_index('Batsman')['Total Runs'].sort_values(ascending=False))

# Death Overs performances
st.subheader("Death Overs Performances (Team wise)")
death_over = df.groupby(['over','batting_team'])['total_runs'].sum()
death_over_runs = df.groupby(['over', 'batting_team'])['total_runs'].sum().reset_index()
temp = death_over_runs.groupby(['batting_team'])['total_runs'].sum().reset_index()
temp_sorted = temp.sort_values(by='total_runs',ascending=False)
st.bar_chart(data=temp_sorted.set_index('batting_team'))

# Top 10 least economical bowlers
st.subheader("Top 10 most economical bowlers")
bowler_wkt = df.groupby(['bowler'])['total_runs'].sum().reset_index()
top_10_most_eco_bowler = bowler_wkt.sort_values(by='total_runs',ascending=False)
most_eco = top_10_most_eco_bowler.head(10)
st.bar_chart(data=most_eco.set_index('bowler'))


st.subheader("Top 10 Most Wicket Taking Bowlers")
valid_wickets = [
    "bowled", "caught", "lbw", "stumped", "caught and bowled", "hit wicket"
]
wkt_cnt = df[df['dismissal_kind'].isin(valid_wickets)]
most_wkt = wkt_cnt.groupby('bowler')['dismissal_kind'].count().reset_index().sort_values(by='dismissal_kind', ascending=False)
top_wkt_bowler = most_wkt.head(10).rename(columns={'dismissal_kind': 'wicket_count'})
st.bar_chart(data=top_wkt_bowler.set_index('bowler')['wicket_count'])
