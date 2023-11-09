import pandas as pd
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go


pio.templates.default = "plotly_white"

data = pd.read_csv("customer_acquisition_cost_dataset.csv")

print(data.head())

data.info()

data['CAC'] = data['Marketing_Spend'] / data['New_Customers']

print(data.head())

fig = px.bar(data, x='Marketing_Channel', y='CAC', title= 'CAC by Marketing Channel')
fig.show()

fig2 = px.scatter(data, x='New_Customers', y='CAC',
                  color='Marketing_Channel',title= "New Customers vs CAC",
                  trendline='ols')
fig2.show()


summary_stats = data.groupby('Marketing_Channel')['CAC'].describe()

print(summary_stats)

data['Conversion_Rate'] = data['New_Customers'] / data['Marketing_Spend'] * 100
print(data.head())

data['Break_Even_Customers'] = data['Marketing_Spend'] / data['CAC']

fig3 = px.bar(data, x='Marketing_Channel', y='Break_Even_Customers', 
             title='Break-Even Customers by Marketing Channel')

fig3.show()

fig = go.Figure()

#Actual Customers Acquired

fig.add_trace(go.Bar(x= data['Marketing_Channel'], y= data['New_Customers'],
                      name='Actual Customers Acquired', marker_color='royalblue'))
                      
# Break-Even Customers
fig.add_trace(go.Bar(x=data['Marketing_Channel'], y=data['Break_Even_Customers'],
                     name='Break-Even Customers', marker_color='lightcoral'))

# Update the layout
fig.update_layout(barmode='group', title='Actual vs. Break-Even Customers by Marketing Channel',
                  xaxis_title='Marketing Channel', yaxis_title='Number of Customers')

# Show the chart
fig.show()
