import pandas as pd
import streamlit as st

# Load the CSV file using the absolute path
df = pd.read_csv('/Users/mac/Desktop/Projects /Python Project from Carrer Ada/4274725-Python_Mini_Project_-_Social_Media_Combat/data-science-project/data/Students Social Media Addiction (1) copy.csv')

# Data cleaning
# Remove duplicates
df = df.drop_duplicates()
# Fill missing numeric values with column mean
num_cols = df.select_dtypes(include=['float64', 'int64']).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].mean())
# Fill missing categorical values with mode
cat_cols = df.select_dtypes(include=['object']).columns
for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

st.title('Social Media Addiction Data Analysis')
st.write('## Data Preview')
st.dataframe(df.head())

# --- FILTERS ---
countries = df['Country'].unique().tolist()
ages = sorted(df['Age'].unique().tolist())
platforms = df['Most_Used_Platform'].unique().tolist()
genders = df['Gender'].unique().tolist()

selected_country = st.selectbox('Filter by Country', ['All'] + countries)
selected_age = st.selectbox('Filter by Age', ['All'] + ages)
selected_platform = st.selectbox('Filter by Most Used Platform', ['All'] + platforms)
selected_gender = st.selectbox('Filter by Gender', ['All'] + genders)

# Apply filters
df_filtered = df.copy()
if selected_country != 'All':
    df_filtered = df_filtered[df_filtered['Country'] == selected_country]
if selected_age != 'All':
    df_filtered = df_filtered[df_filtered['Age'] == selected_age]
if selected_platform != 'All':
    df_filtered = df_filtered[df_filtered['Most_Used_Platform'] == selected_platform]
if selected_gender != 'All':
    df_filtered = df_filtered[df_filtered['Gender'] == selected_gender]

st.write('## Filtered Data Preview')
st.dataframe(df_filtered)

# Visualizations with filtered data
st.write('### Average Daily Usage by Academic Level')
df_avg_usage_academic = df_filtered.groupby('Academic_Level')['Avg_Daily_Usage_Hours'].mean().reset_index()
st.bar_chart(df_avg_usage_academic.set_index('Academic_Level'))

# Average Daily Usage by Gender
st.write('### Average Daily Usage by Gender')
df_avg_usage_gender = df_filtered.groupby('Gender')['Avg_Daily_Usage_Hours'].mean().reset_index()
st.bar_chart(df_avg_usage_gender.set_index('Gender'))

# Average Daily Usage by Age
st.write('### Average Daily Usage by Age')
df_avg_usage_age = df_filtered.groupby('Age')['Avg_Daily_Usage_Hours'].mean().reset_index()
st.line_chart(df_avg_usage_age.set_index('Age'))

# Average Daily Usage by Country
st.write('### Average Daily Usage by Country')
df_avg_usage_country = df_filtered.groupby('Country')['Avg_Daily_Usage_Hours'].mean().reset_index()
st.bar_chart(df_avg_usage_country.set_index('Country'))

# Relationship Status Analysis
st.write('### Average Usage by Relationship Status')
df_relationship_usage = df_filtered.groupby('Relationship_Status')['Avg_Daily_Usage_Hours'].mean().reset_index()
st.bar_chart(df_relationship_usage.set_index('Relationship_Status'))

st.write('### Average Addiction Score by Relationship Status')
df_relationship_addiction = df_filtered.groupby('Relationship_Status')['Addicted_Score'].mean().reset_index()
st.bar_chart(df_relationship_addiction.set_index('Relationship_Status'))

# Conflicts Over Social Media
st.write('### Conflicts Over Social Media (Frequency)')
df_conflicts = df_filtered.groupby('Conflicts_Over_Social_Media').size().reset_index(name='Count')
st.bar_chart(df_conflicts.set_index('Conflicts_Over_Social_Media'))

# Platform Popularity
st.write('### Platform Popularity')
df_platform_counts = df_filtered['Most_Used_Platform'].value_counts().reset_index()
df_platform_counts.columns = ['Platform', 'Count']
st.bar_chart(df_platform_counts.set_index('Platform'))

# Addiction Score by Platform
st.write('### Average Addiction Score by Platform')
df_addiction_platform = df_filtered.groupby('Most_Used_Platform')['Addicted_Score'].mean().reset_index()
st.bar_chart(df_addiction_platform.set_index('Most_Used_Platform'))

# Correlation between Addiction Score and Sleep Hours
st.write('### Correlation between Addiction Score and Sleep Hours')
st.write(df_filtered['Addicted_Score'].corr(df_filtered['Sleep_Hours_Per_Night']))

# Average Mental Health Score by Country
st.write('### Average Mental Health Score by Country')
df_avg_mental_health = df_filtered.groupby('Country')['Mental_Health_Score'].mean().reset_index()
st.bar_chart(df_avg_mental_health.set_index('Country'))

# Platform Popularity by Gender
st.write('### Platform Popularity by Gender')
df_platform_gender = df_filtered.groupby(['Gender', 'Most_Used_Platform']).size().reset_index(name='Count')
for gender in df_platform_gender['Gender'].unique():
    st.write(f'#### {gender}')
    st.bar_chart(df_platform_gender[df_platform_gender['Gender'] == gender].set_index('Most_Used_Platform')['Count'])
