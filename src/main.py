#Import required libraries
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio

pio.templates.default = "plotly_white"

#Read the dataset
data = pd.read_csv("../data/customer_acquisition_data.csv")
print(data.head())

#Exploratory Data Analysis

#Distribution of Acquisition cost
fig = px.histogram(data, x = "cost", nbins = 20,
                   labels={"cost": "Acquisition cost"}, title = "Distribution of Acquisition cost")

fig.show()

#Distribution of Revenue
fig = px.histogram(data, x = "revenue", nbins = 20,
                   labels={"revenue": "Revenue"}, title = "Distribution of Revenue")

fig.show()

#Customer Acquisition Cost (CAC) based on Channel
cost_by_channel = data.groupby('channel')['cost'].mean().reset_index()

fig = px.bar(cost_by_channel,
            x = "channel",
            y = "cost",
            color = "channel",
            title = "Customer Acquisition Cost by Channel",
            labels = {"cost": "Acquisition cost", "channel": "Channel"})

fig.show()

#Conversion Rates based on Channel
cost_by_channel = data.groupby('channel')['conversion_rate'].mean().reset_index()

fig = px.bar(cost_by_channel,
            x = "channel",
            y = "conversion_rate",
            color = "channel",
            title = "Conversion Rate by Channel",
            labels = {"conversion_rate": "Conversion rate", "channel": "Channel"})

fig.show()

# Cost per Conversion by Channel

data['cost_per_conversion'] = data['cost'] / (data['conversion_rate'] * data['cost'])

cost_per_conversion_by_channel = data.groupby('channel')['cost_per_conversion'].mean().reset_index()

fig = px.bar(cost_per_conversion_by_channel,
             x = "channel",
             y = "cost_per_conversion",
             color = "channel",
             title = "Cost per Conversion by Channel",
             labels = {"cost_per_conversion": "Cost per Conversion", "channel": "Channel"})

fig.show()

#Revenue generated by Channel
revenue_by_channel = data.groupby('channel')['revenue'].sum().reset_index()

fig = px.pie(revenue_by_channel,
            names = "channel",
            values = "revenue",
            title = "Total Revenue by Channel",
            hole = 0.6, color_discrete_sequence=px.colors.qualitative.Pastel)

fig.show()

# Revenue per Conversion by Channel

data['revenue_per_conversion'] = data['revenue'] / (data['conversion_rate'] * data['cost'])

revenue_per_conversion_by_channel = data.groupby('channel')['revenue_per_conversion'].mean().reset_index()

fig = px.bar(revenue_per_conversion_by_channel,
             x = "channel",
             y = "revenue_per_conversion",
             color = "channel",
             title = "Revenue per Conversion by Channel",
             labels = {"revenue_per_conversion": "Revenue per Conversion", "channel": "Channel"})

fig.show()

#ROI by Channel
data['roi'] = data['revenue'] / data['cost']

roi_by_channel = data.groupby('channel')['roi'].mean().reset_index()

fig = px.bar(roi_by_channel,
             x = "channel",
             y = "roi",
             color = "channel",
             title = "Return on Investment (ROI) by Channel",
             labels = {"roi": "Return on Investment", "channel": "Channel"})

fig.show()

#Customer Lifetime Value by Channel

data['cltv'] = (data['revenue'] - data['cost']) * (data['conversion_rate'] / data['cost'])

cltv_by_channel = data.groupby('channel')['cltv'].mean().reset_index()

fig = px.bar(cltv_by_channel,
             x = "channel",
             y = "cltv",
             color='channel',
             title = "Customer Lifetime Value by Channel",
             labels = {"cltv": "Customer Lifetime Value", "channel": "Channel"})

fig.show()

#CLTV distribution

subset = data.loc[data['channel'].isin(['social media', 'referral'])]

fig = px.box(subset,
             x = "channel",
             y = "cltv",
             title = "CLTV Distribution by Channel",
             labels = {"channel": "Channel", "cltv": "CLTV"})

fig.update_xaxes(title='Channel')
fig.update_yaxes(title='CLTV')
fig.update_layout(legend_title='Channel')

fig.show()