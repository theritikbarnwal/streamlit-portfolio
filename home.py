import streamlit as st

def homeshow():
    st.title("Welcome to My Portfolio")

    # Adjusted column ratios to prioritize text
    col1, col2 = st.columns([3, 1])
    
    with col2:
        # Image with adjusted path and resized width
        st.image("img/home.jpg", caption="Ritik Barnwal", use_column_width=True, width=150)  # Slightly larger image for better visibility
    
    with col1:
        # Introductory text with emphasis on key skills
        st.write("""
        Hello! I'm **Ritik Barnwal**, a passionate **Data Scientist** and **Web Developer** with a strong foundation in **data analytics**, **machine learning**, and **web development**.
        """)
        
        # Updated section title and description
        st.write("""
        #### My Journey
        I am currently pursuing a **Bachelor of Computer Applications (BCA)** in **Data Science**. Over the years, I’ve developed a strong interest in using data to solve real-world problems. Here’s a glimpse of what I’ve been working on:
        - **Data Cleaning**: Ensuring high-quality, structured data for accurate analysis.
        - **Machine Learning**: Building predictive models to provide actionable insights.
        
        I’m well-versed in **Python**, **SQL**, **Power BI**, and machine learning frameworks. I'm always excited to take on new challenges and work on impactful projects.

        Explore my work below, and feel free to reach out if you’d like to collaborate!
        """)
