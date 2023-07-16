import plotly.express as px
import streamlit as st 
import pandas as pd 
import numpy as np 

map_user = pd.read_csv(r"C:\Users\Welcome\OneDrive\Documents\phonepe\pulse\data\aggregated\transaction\country\india\map_user")

agg_user = pd.read_csv(r"C:\Users\Welcome\OneDrive\Documents\phonepe\pulse\data\aggregated\transaction\country\india\agg_user.csv")

with st.container():
    st.title(":green[PHONEPE PULSE DATA VISUALISATION(2018-2022)]")
    st.write(" ")
    st.subheader(
              ":red[Registered User & App Installed -> State & District Wise:]")
    split_year = st.selectbox('Select The Year:',
                              ('2018','2019','2020','2021','2022'))
    st.write(" ")
    split_state = st.selectbox('Select The State:',
                               ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
                                                         'assam', 'bihar', 'chandigarh', 'chhattisgarh',
                                                         'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
                                                         'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
                                                         'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                                                         'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
                                                         'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
                                                         'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
                                                         'uttarakhand', 'west-bengal'))
    split_year = int(split_year)
    mapuser_df = map_user[(map_user['Year'] == split_year) & (map_user['State'] == split_state)]
    scatter_mapuser = px.scatter(mapuser_df, x='District', y='Registered_user', color='District')
    st.plotly_chart(scatter_mapuser)

    st.write(" ")
    st.subheader(":red[Brand and Brand_Count -> State and Year Wise:]")
    arr_year = st.selectbox('Select The Year',
                            ('2018','2019','2020','2021','2022'))
    arr_state = st.selectbox('Select The State',
                             ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
                                                         'assam', 'bihar', 'chandigarh', 'chhattisgarh',
                                                         'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
                                                         'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
                                                         'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                                                         'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
                                                         'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
                                                         'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
                                                         'uttarakhand', 'west-bengal'))
    arr_year = int(arr_year)
    agguser_df = agg_user[(agg_user['Year'] == arr_year) & (agg_user['State'] == arr_state)]
    scatter_agguser = px.bar(agguser_df, x='Brand', y='Brand_count', color='Brand')
    st.plotly_chart(scatter_agguser)

    st.write(" ")
    agg_trans = pd.read_csv(r"C:\Users\Welcome\OneDrive\Documents\phonepe\pulse\data\aggregated\transaction\country\india\agg_trans.csv")
    st.subheader(":red[Transaction_type & Transaction_count(2018 - 2022):]")
    year_split = int(st.radio('Select The Year',
                            ('2018','2019','2020','2021','2022'), horizontal=True))
    splitted_state = st.selectbox(' Please Select The State',
                                     ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
                                                         'assam', 'bihar', 'chandigarh', 'chhattisgarh',
                                                         'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
                                                         'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
                                                         'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                                                         'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
                                                         'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
                                                         'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
                                                         'uttarakhand', 'west-bengal'))
    

    year_split = int(year_split)
    aggtrans_df = agg_trans[(agg_trans['Year'] == year_split) & (agg_trans['State'] == splitted_state)]
    scatter_aggtrans = px.bar(aggtrans_df, x='Transaction_type', y='Transaction_count', color='Transaction_type')
    st.plotly_chart(scatter_aggtrans)
    
    st.write(" ")
    st.subheader(':red[Pie Chart Of Payment_mode]')
    pie_chart = px.pie(aggtrans_df, values='Transaction_count', names='Transaction_type', hole=.5, hover_data=['Year'])
    st.plotly_chart(pie_chart)


    st.write(" ")
    state = pd.read_csv(r"C:\Users\Welcome\OneDrive\Documents\phonepe\pulse\data\aggregated\transaction\country\india\State code.csv")
    Gdistricts = pd.read_csv(r"C:\Users\Welcome\OneDrive\Documents\phonepe\pulse\data\aggregated\transaction\country\india\District code.csv")
    map_trans = pd.read_csv(r"C:\Users\Welcome\OneDrive\Documents\phonepe\pulse\data\aggregated\transaction\country\india\map_trans")
    state = state.sort_values(by='state')
    state = state.reset_index(drop=True)
    df = agg_trans.groupby(['State']).agg({'Transaction_count':'sum','Transaction_amount':'sum'})
    df = df.reset_index()

    choropleth_data = state.copy()

    for column in df.columns:
        choropleth_data[column] = df[column]
    choropleth_data = choropleth_data.drop(labels='State', axis=1)

    agg_trans.rename(columns={'State': 'state'}, inplace=True)
    sta_list = ['andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
            'assam', 'bihar', 'chandigarh', 'chhattisgarh',
            'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
            'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
            'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
            'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
            'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
            'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
            'uttarakhand', 'west-bengal']
    state['state'] = pd.Series(data=sta_list)
    state_final = pd.merge(agg_trans, state, how='outer', on='state')
    districts_final = pd.merge(map_trans, Gdistricts,
                           how='outer', on=['State', 'District'])



    st.subheader(":red[Geo Visualisation of Transaction Data]")
    st.write(' ')
    year_splits = st.selectbox('Please select the Year',
                    ['2018', '2019', '2020', '2021', '2022'], index=0)
    st.write(' ')
    Quater = st.radio('Please select the Quarter',
                       ('1', '2', '3', '4'), horizontal=True)
    st.write(' ')
    year_splits = int(year_splits)
    Quater = int(Quater)
    scat_district = districts_final[(districts_final['Year'] == year_splits) & (
        districts_final['Quater'] == Quater)]
    scat_state = state_final[(state_final['Year'] == year_splits)
                             & (state_final['Quater'] == Quater)]
    scat_state_total = scat_state.groupby(
        ['state', 'Year', 'Quater', 'Latitude', 'Longitude']).sum()
    scat_state_total = scat_state_total.reset_index()
    state_code = ['AN', 'AD', 'AR', 'AS', 'BR', 'CH', 'CG', 'DNHDD', 'DL', 'GA',
                  'GJ', 'HR', 'HP', 'JK', 'JH', 'KA', 'KL', 'LA', 'LD', 'MP', 'MH',
                  'MN', 'ML', 'MZ', 'NL', 'OD', 'PY', 'PB', 'RJ', 'SK', 'TN', 'TS',
                  'TR', 'UP', 'UK', 'WB']
    scat_state_total['code'] = pd.Series(data=state_code)


    fig1 = px.scatter_geo(scat_district,
                          lon=scat_district['Longitude'],
                          lat=scat_district['Latitude'],
                          color=scat_district['Transaction_amount'],
                          size=scat_district['Transaction_count'],
                          hover_name="District",
                          hover_data=["State", 'Transaction_amount',
                                      'Transaction_count', 'Year', 'Quater'],
                          title='District',
                          size_max=22,)
    fig1.update_traces(marker={'color': "#CC0044",
                               'line_width': 1})
    fig2 = px.scatter_geo(scat_state_total,
                          lon=scat_state_total['Longitude'],
                          lat=scat_state_total['Latitude'],
                          hover_name='state',
                          text=scat_state_total['code'],
                          hover_data=['Transaction_count',
                                      'Transaction_amount', 'Year', 'Quater'],
                          )
    fig2.update_traces(marker=dict(color="#D5FFCC", size=0.3))
    fig = px.choropleth(
        choropleth_data,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='state',
        color='Transaction_amount',
        color_continuous_scale='twilight',
        hover_data=['Transaction_count', 'Transaction_amount']
    )

    fig.update_geos(fitbounds="locations", visible=False)
    fig.add_trace(fig1.data[0])
    fig.add_trace(fig2.data[0])
    fig.update_layout(height=1000, width=1000)
    st.write(' ')
    st.write(' ')
    
#     if st.button('Click here to see map clearly'):
#         fig.show()
        
    st.plotly_chart(fig)