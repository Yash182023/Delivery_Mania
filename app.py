import streamlit as st  

style = """
<style>
    @import 'https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap';
    
    .main{
        background: rgb(255,243,0);
        background: radial-gradient(circle, rgba(255,243,0,1) 0%, rgba(77,251,78,1) 44%, rgba(255,218,0,1) 100%);
    }
    
    h1{
        font-family: "Poppins", sans-serif;
        font-weight: 700;
        font-style: normal;
        color: #054707;
    }
    
    h3{
        font-family: "Poppins", sans-serif;
        font-weight: 500;
        font-style: normal;
        color: #054707;
    }
    p{
        font-family: "Poppins", sans-serif;
        font-weight: 400;
        font-style: normal;
        color: #054707;
    }
    
    .st-emotion-cache-13k62yr{
        font-family: "Poppins", sans-serif;
        font-weight: 400;
        font-style: normal;
        color: #054707;
    }
    
</style>
"""

st.markdown(style,unsafe_allow_html=True)

st.title("Welcome to Delivery Mania!")

content ="""
### Introduction

Welcome to Delivery Mania! In today's fast-paced world, efficient delivery systems are essential for businesses to thrive and customers to receive their goods promptly. Delivery Mania is a project aimed at optimizing delivery routes, ensuring timely deliveries, and maximizing customer satisfaction.

### Key Features

- **Route Optimization:** Delivery Mania utilizes advanced algorithms to optimize delivery routes, minimizing travel time and fuel consumption.
- **Real-time Tracking:** Track delivery vehicles in real-time to monitor their progress and ensure timely arrivals.
- **Customizable Solutions:** Tailor our delivery management system to fit the unique needs of your business, whether you're a small local shop or a large-scale logistics company.
- **Data Analytics:** Gain valuable insights into delivery patterns, customer preferences, and operational efficiency through powerful analytics tools.
- **User-friendly Interface:** Our intuitive interface makes it easy for drivers, dispatchers, and managers to interact with the system seamlessly.

### How It Works

1. **Input Delivery Requests:** Enter delivery requests, including pickup and drop-off locations, along with any special instructions or requirements.
2. **Route Optimization:** Delivery Mania automatically calculates the most efficient delivery routes based on factors such as distance, traffic conditions, and delivery priorities.
3. **Dispatch & Tracking:** Dispatch delivery vehicles and track their progress in real-time using our tracking system. Receive alerts and notifications for any delays or issues.
4. **Analytics & Optimization:** Analyze delivery data to identify areas for improvement, optimize routes, and enhance overall delivery performance.

### Get Started

Ready to revolutionize your delivery operations? Sign up for Delivery Mania today and experience the future of delivery management!

"""

st.markdown(content,unsafe_allow_html=True)
