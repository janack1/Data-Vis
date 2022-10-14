import streamlit as st
st.set_page_config(
    page_title="Data Science Career",
    page_icon="📊",
    layout='wide',
    )
#The needed packages for visualization are installed
#The following packages are include those needed for plotly
import pandas as pd
import numpy as np 
import chart_studio.plotly as py
import cufflinks as cf
import seaborn as sns 
import plotly.express as px 
import plotly.figure_factory as ff
import country_converter as coco
import pycountry_convert as pc
from PIL import Image
import plotly.graph_objects as go
def country_to_continent(country_name):
    country_continent_code = pc.country_alpha2_to_continent_code(country_name)
    country_continent_name = pc.convert_continent_code_to_continent_name(country_continent_code)
    return country_continent_name
st.text("")
st.markdown(f'<h1 style="color:#494949;font-size:50px;">{"📊  Data Science Career"}</h1>', unsafe_allow_html=True)
st.text("")
st.header('Are you wondering if the data science field is a good career path?')
st.text("")
#st.markdown(f'<h1 style="color:#000000;font-size:25px;">{"Take a tour in my website to get some facts and tips that will help you take your career decision."}</h1>', unsafe_allow_html=True)
option1 = st.selectbox('Take a tour in my website to get some facts and tips that will help you take your career decision.',('Home Page','What Are The Most Popular Jobs In The Data Science Market?','Where Should You Go?', 'Will data science be the future?','What type of contract should you sign?', 'Can you work remotely?','How much will you get paid?'))
df=pd.read_csv("https://raw.githubusercontent.com/janack1/Data-Vis/main/ds_salaries.csv")
df.drop("Unnamed: 0", axis=1, inplace=True)
df['Continent'] = df['company_location'].apply(country_to_continent)
#col1, col2, col3 = st.columns([5,8,3])
if option1=='Home Page':
   image = "https://s27389.pcdn.co/wp-content/uploads/2021/07/data-science-predictions-for-near-future-1024x440.jpeg.optimal.jpeg"
   st.image(image, width= 1200)
#with col2:
if option1 == "What Are The Most Popular Jobs In The Data Science Market?":
   col1,col2,col3=st.columns([1,2,1])
   with col2:
       top_titles=df.groupby(['job_title'],as_index=False).size().sort_values('size',ascending=True).tail(10)
       fig = px.bar(top_titles, y="job_title",
                    x="size", 
                    #color ='#5d006f',
                    #color_discrete_sequence=px.colors.qualitative.Bold,
                    text="size",
                    orientation='h',
                    template= 'plotly_dark')
       fig.update_layout(
                    xaxis_title="Frequency",
                    yaxis_title="Job Titles",
                    font = dict(size=15),
                    width=1100,
                    height=800)
       fig.update_yaxes(showgrid=False)
       fig.update_xaxes(showgrid=False)
       fig.update_traces(marker_color='#5d006f')
       st.plotly_chart(fig)
       st.subheader("Data scientist, data engineer and data analyst are recently the most popular jobs in this field!")

if option1 == 'Where Should You Go?':
    col1,col2,col3=st.columns([1,2,1])
    with col1:
        continents=st.radio("Select a Continent", ["All","Asia","Europe","North America","South America","Africa"])
    with col2:
        if continents=="All":

            companies_locations_name = coco.convert(names=df['company_location'], to="name")
            companies_locations_ISO = coco.convert(names=df['company_location'], to="ISO3")
            df["company's location name"] = companies_locations_name
            df["company's location ISO"] = companies_locations_ISO
            comp_loc_name = df["company's location name"].value_counts()
            comp_loc_iso = df["company's location ISO"].value_counts()
            fig = px.choropleth(df,locations=comp_loc_iso.index,
                            color=comp_loc_iso.values,
                            color_continuous_scale=px.colors.sequential.RdPu,
                            template='simple_white')

            fig.update_layout(font = dict(size= 20),width=1100,height=800,coloraxis_colorbar=dict(title="Number of Companies"))
            st.plotly_chart(fig)
            st.subheader('''USA is your best destination! More than 335 data science companies are located there!''')
        elif continents=="Asia":
            df1=df[df["Continent"]=="Asia"]
            companies_locations_name = coco.convert(names=df1['company_location'], to="name")
            companies_locations_ISO = coco.convert(names=df1['company_location'], to="ISO3")
            df1["company's location name"] = companies_locations_name
            df1["company's location ISO"] = companies_locations_ISO
            comp_loc_name = df1["company's location name"].value_counts()
            comp_loc_iso = df1["company's location ISO"].value_counts()
            fig = px.choropleth(df1,locations=comp_loc_iso.index,
                            color=comp_loc_iso.values,
                            color_continuous_scale=px.colors.sequential.RdPu,
                            template='simple_white', scope="asia")

            fig.update_layout(font = dict(size= 20),width=1100,height=800,coloraxis_colorbar=dict(title="Number of Companies"))
            st.plotly_chart(fig)
            st.subheader('''India is your best destination in Asia! More than 24 data science companies are located there!''')

        elif continents=="Europe":
            df1=df[df["Continent"]=="Europe"]
            companies_locations_name = coco.convert(names=df1['company_location'], to="name")
            companies_locations_ISO = coco.convert(names=df1['company_location'], to="ISO3")
            df1["company's location name"] = companies_locations_name
            df1["company's location ISO"] = companies_locations_ISO
            comp_loc_name = df1["company's location name"].value_counts()
            comp_loc_iso = df1["company's location ISO"].value_counts()
            fig = px.choropleth(df1,locations=comp_loc_iso.index,
                            color=comp_loc_iso.values,
                            color_continuous_scale=px.colors.sequential.RdPu,
                            template='simple_white', scope="europe")

            fig.update_layout(font = dict(size= 20),width=1100,height=800,coloraxis_colorbar=dict(title="Number of Companies"))
            st.plotly_chart(fig)
            st.subheader('''UK is your best destination in Europe! More than 47 data science companies are located there!''')

        elif continents=="Africa":
            df1=df[df["Continent"]=="Africa"]
            companies_locations_name = coco.convert(names=df1['company_location'], to="name")
            companies_locations_ISO = coco.convert(names=df1['company_location'], to="ISO3")
            df1["company's location name"] = companies_locations_name
            df1["company's location ISO"] = companies_locations_ISO
            comp_loc_name = df1["company's location name"].value_counts()
            comp_loc_iso = df1["company's location ISO"].value_counts()
            fig = px.choropleth(df1,locations=comp_loc_iso.index,
                            color=comp_loc_iso.values,
                            color_continuous_scale=px.colors.sequential.RdPu,
                            template='simple_white', scope="africa")

            fig.update_layout(font = dict(size= 20),width=1100,height=800,coloraxis_colorbar=dict(title="Number of Companies"))
            st.plotly_chart(fig)
            st.subheader('''Nigeria is your best destination. 2 data science companies are located there.''')
                

        elif continents=="North America":
            df1=df[df["Continent"]=="North America"]
            companies_locations_name = coco.convert(names=df1['company_location'], to="name")
            companies_locations_ISO = coco.convert(names=df1['company_location'], to="ISO3")
            df1["company's location name"] = companies_locations_name
            df1["company's location ISO"] = companies_locations_ISO
            comp_loc_name = df1["company's location name"].value_counts()
            comp_loc_iso = df1["company's location ISO"].value_counts()
            fig = px.choropleth(df1,locations=comp_loc_iso.index,
                            color=comp_loc_iso.values,
                            color_continuous_scale=px.colors.sequential.RdPu,
                            template='simple_white', scope="north america")

            fig.update_layout(font = dict(size= 20),width=1100,height=800,coloraxis_colorbar=dict(title="Number of Companies"))
            st.plotly_chart(fig)
            st.subheader('''USA is your best destination! 335 data science companies are located there!''')

        elif continents=="South America":
            df1=df[df["Continent"]=="South America"]
            companies_locations_name = coco.convert(names=df1['company_location'], to="name")
            companies_locations_ISO = coco.convert(names=df1['company_location'], to="ISO3")
            df1["company's location name"] = companies_locations_name
            df1["company's location ISO"] = companies_locations_ISO
            comp_loc_name = df1["company's location name"].value_counts()
            comp_loc_iso = df1["company's location ISO"].value_counts()
            fig = px.choropleth(df1,locations=comp_loc_iso.index,
                            color=comp_loc_iso.values,
                            color_continuous_scale=px.colors.sequential.RdPu,
                            template='simple_white', scope="south america")

            fig.update_layout(font = dict(size= 20),width=1100,height=800,coloraxis_colorbar=dict(title="Number of Companies"))
            st.plotly_chart(fig)
            st.subheader('''Brazil is your best destination. 3 data science companies are located there.''')

if option1 == 'Will data science be the future?':
    col1,col2=st.columns(2)
    with col1:
        df2=df.groupby(['employee_residence',"work_year"],as_index=False).size().sort_values("work_year")
        employees_locations_name = coco.convert(names=df2['employee_residence'], to="name")
        employees_locations_ISO = coco.convert(names=df2['employee_residence'], to="ISO3")
        df2["employee's location name"] = employees_locations_name
        df2["employee's location ISO"] = employees_locations_ISO
        emp_loc_name = df2["employee's location name"].value_counts()
        fig = px.choropleth(locations=df2["employee's location ISO"],
                        color=df2["size"],
                        color_continuous_scale=px.colors.sequential.RdPu,
                        animation_frame=df2["work_year"],
                        hover_name=df2["employee's location ISO"],
                        template='simple_white')

        fig.update_layout(font = dict(size= 20),width=1100,height=800,coloraxis_colorbar=dict(title="Number of employees"))
        st.plotly_chart(fig)
        st.subheader(''' Data Science Employees are spreading across the world!''')
    with col2:
        work_year = df['work_year'].value_counts(sort=False)
        fig = px.pie(values=work_year.values, 
                 names=work_year.index, 
                 color_discrete_sequence=['#fff3ef','#ef589e','#5d006f'],
                 template='simple_white')
        fig.update_traces(textinfo='label+percent+value', textfont_size=16,
                      marker=dict(line=dict(color='#100000', width=0.3)))
        fig.data[0].marker.line.width = 2
        fig.data[0].marker.line.color='gray'
        fig.update_layout(title="Number of employees",width=1100,height=800,font=dict(size=20))
        st.plotly_chart(fig)
        st.subheader('''Job opportunies are increasing VERY QUICKLY each year!''')
        st.write("The Job opportunities for the data science field have increased in the market by 40% within 2 years!")

if option1 == 'What type of contract should you sign?':
    col1,col2,col3=st.columns([1,2,1])
    with col2:
        fig = px.box(x=df['salary_in_usd'],y=df["employment_type"],color=df["employment_type"],color_discrete_sequence=px.colors.qualitative.Bold,template= 'plotly_dark')
        fig.update_layout(font = dict(size=18),width=1100,height=800,title="Salary range per contract type",xaxis_title="Salary",yaxis_title="Contract Type")
        fig.update_yaxes(showgrid=False)
        fig.update_xaxes(showgrid=False)
        st.plotly_chart(fig)
        st.subheader(''' The Contract Employee Gets The Highest Salaries! 50% of them get a salary between 105k and 306k''')
        
if option1 == 'Can you work remotely?':
    col1,col2,col3=st.columns([1,2,1])
    with col2:
        remote_year = df.groupby(['work_year','remote_ratio']).size()
        ratio_2020 = np.round(remote_year[2020].values/remote_year[2020].values.sum(),2)
        ratio_2021 = np.round(remote_year[2021].values/remote_year[2021].values.sum(),2)
        ratio_2022 = np.round(remote_year[2022].values/remote_year[2022].values.sum(),2)
        fig = go.Figure()
        categories = ['No Remote Work', 'Partially Remote', 'Fully Remote']
        fig.add_trace(go.Scatterpolar(
                 r = ratio_2020, 
                 theta = categories,
                 fill = 'toself',
                 name = '2020 remote ratio'
                 ))
        fig.add_trace(go.Scatterpolar(
                 r = ratio_2021, 
                 theta = categories,
                 fill = 'toself',
                 name = '2021 remote ratio',
                fillcolor ='#fff3ef'
                 ))
        fig.add_trace(go.Scatterpolar(
                 r = ratio_2022, 
                 theta = categories,
                 fill = 'toself',
                 name = '2022 remote ratio',
                 fillcolor = '#ef589e'
                 ))

        fig.update_layout(
             polar=dict(
             radialaxis=dict(
             #visible=True,
             range=[0, 0.75]
             )),
             font = dict(size=17), width=1100,height=800,
             showlegend=True
             )
        fig.layout.template = 'seaborn'
        st.plotly_chart(fig)
        st.subheader(''' You Can Have The Chance to Work From Your Comfortable Home!''')

if option1 == 'How much will you get paid?':
    col1,col2=st.columns(2)
    with col1:
        wy2020 = df.loc[(df['work_year'] == 2020)]
        wy2021 = df.loc[(df['work_year'] == 2021)]
        wy2022 = df.loc[(df['work_year'] == 2022)]
        hist_data = [wy2020['salary_in_usd'],wy2021['salary_in_usd'],wy2022['salary_in_usd']]
        group_labels = ['2020 salary','2021 salary','2022 salary']
        colors = ['#edcbc0','#ef589e','#5d006f']

        year_salary = pd.DataFrame(columns=['2020','2021','2022'])
        year_salary['2020'] = wy2020.groupby('work_year').mean('salary_in_usd')['salary_in_usd'].values
        year_salary['2021'] = wy2021.groupby('work_year').mean('salary_in_usd')['salary_in_usd'].values
        year_salary['2022'] = wy2022.groupby('work_year').mean('salary_in_usd')['salary_in_usd'].values

        fig1 = ff.create_distplot(hist_data, group_labels,show_hist=False,colors=colors)
        fig1.layout.template = 'plotly_dark'
        fig1.update_layout(title='Distribution of Salary per year',font = dict(size=17),width=1100,height=800,coloraxis_colorbar=dict(title="Mean Salary"))
        fig1.update_yaxes(showgrid=False)
        fig1.update_xaxes(showgrid=False)
        st.plotly_chart(fig1)
        st.subheader(''' Better Career Rewards Are On Their Way! Salaries increased a lot last year!''')
    with col2:
        fig2 = go.Figure(data=px.bar(x= year_salary.columns, 
                                y=year_salary.values.tolist()[0],
                                color = year_salary.columns,
                                color_discrete_sequence=['#fff3ef','#ef589e','#5d006f'],
                                title='Mean Salary by Work Year',
                                text = np.round([num/1000 for num in year_salary.values.tolist()[0]],2),
                                template = 'plotly_dark',
                                height=500))
    
        fig2.update_traces(width=0.3)
        fig2.update_layout(
             xaxis_title="Work Year",
             yaxis_title="Mean Salary in USD (k)",
             font = dict(size=17),width=1100,height=800,coloraxis_colorbar=dict(title="Mean Salary"))
   
        fig2.update_yaxes(showgrid=False)
        fig2.update_xaxes(showgrid=False)
    
        st.plotly_chart(fig2)
        st.subheader('''The average salary in USD for year 2022 attained 125k!''')
    col1,col2,col3=st.columns([1,2,1])
    with col2:
        df3=df.groupby(['job_title'],as_index=False).mean().sort_values('salary_in_usd',ascending=True)
        #salary_job = df.groupby(['salary_in_usd','job_title'],as_index=False).size().sort_values("size",ascending=False)
        df3['salary_in_usd'] = df3['salary_in_usd'].apply(lambda x: round(x,2))
        salary_job = df3[-20:]
        fig = px.bar(y=salary_job['job_title'],x=salary_job['salary_in_usd'],text = salary_job['salary_in_usd'], 
                       color = salary_job['salary_in_usd'], color_continuous_scale=px.colors.sequential.RdPu)

        fig.update_layout(
            yaxis_title="Job Title",
            xaxis_title="Salaries ")
        fig.update_layout(barmode = 'relative',xaxis_tickangle=-60, width=1100,height=800,template='plotly_white',font = dict(size=15),coloraxis_colorbar=dict(title="Average Salary"))
        fig.update_yaxes(showgrid=False)
        fig.update_xaxes(showgrid=False)
        st.plotly_chart(fig)
        st.subheader('''These Are The Top 20 Highest Salary by Job Title!
                        Principal Data Engineer is the most well paid job in the market (600k USD).''')
    
