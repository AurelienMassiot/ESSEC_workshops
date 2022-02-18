from datetime import datetime

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout='wide')
st.title('My beautiful dashboard')


@st.cache
def load_data() -> pd.DataFrame:
    df = pd.read_csv('fake_accidents.csv')
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    keep_columns = ['Date', 'Latitude', 'Longitude', 'Accident_Severity']
    df = df[keep_columns]
    df = df.dropna().reset_index(drop=True)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Date_Day_Number'] = df['Date'].dt.day
    df['Date_Day_Name'] = df['Date'].dt.day_name()
    return df


def filter_by_severity(data: pd.DataFrame, severity_list: list[str]) -> pd.DataFrame:
    return data[data['Accident_Severity'].isin(severity_list)]


def filter_by_dates(data: pd.DataFrame, min_date: datetime, max_date: datetime) -> pd.DataFrame:
    return data[(data['Date'] >= pd.to_datetime(min_date)) & (data['Date'] <= pd.to_datetime(max_date))]


# Loading
df = load_data()
df = clean_data(df)

# Filters
severity_list = ['Low', 'Medium', 'High']
selected_severities = st.sidebar.multiselect(
    label='Select severity:',
    options=severity_list,
    default=severity_list
)

selected_date_min, selected_date_max = st.sidebar.date_input(
    label='Dates',
    value=[df['Date'].min(), df['Date'].max()])

df_filtered = filter_by_severity(df, selected_severities)
df_filtered = filter_by_dates(df_filtered, selected_date_min, selected_date_max)

# Feature Engineering
df_grouped_by_accident_severity_and_date = pd.DataFrame(df_filtered.groupby(by=['Date', 'Accident_Severity']).size(),
                                                        columns=['Count']).reset_index()
df_grouped_by_accident_severity_and_dayname = pd.DataFrame(
    df_filtered.groupby(by=['Date_Day_Name', 'Accident_Severity']).size(),
    columns=['Count']).reset_index()

# Display

## Dataframe
# st.write(df)

## Map
latitude = 48.866667
longitude = 2.333333
map_graph = px.scatter_mapbox(
    df_filtered,
    lat='Latitude',
    lon='Longitude',
    color='Accident_Severity',
    hover_data={'Latitude': True,
                'Longitude': True,
                'Date': True,
                'Accident_Severity': False
                },
    color_continuous_scale=px.colors.sequential.Blackbody_r,
    size_max=15,
    zoom=12,
    opacity=1,
    center={'lat': latitude, 'lon': longitude},
    mapbox_style='carto-positron',
)
st.plotly_chart(map_graph, use_container_width=True)

## Line graph
line_graph = px.line(df_grouped_by_accident_severity_and_date,
                     x='Date',
                     y='Count',
                     color='Accident_Severity',
                     )
st.plotly_chart(line_graph, use_container_width=True)

## Histogram
day_order = {'Date_Day_Name': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']}
histogram_chart = px.histogram(df_grouped_by_accident_severity_and_dayname,
                               x='Date_Day_Name',
                               y='Count',
                               color='Accident_Severity',
                               category_orders=day_order)
st.plotly_chart(histogram_chart, use_container_width=True)

# Final word
is_button_clicked = st.sidebar.button(label='Display balloons')
if is_button_clicked:
    st.balloons()
