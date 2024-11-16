import streamlit as st

def amshow():
    st.title("About")
    
    col1, col2 = st.columns([3, 1])  # Adjusted column ratios to prioritize text
    
    
    with col2:
        st.image("img/about.jpg", caption="Ritik Barnwal", use_column_width=True, width=150)  # Adjusted width for a smaller image
    
    with col1:
        st.write("""
        Hello! I'm **Ritik Barnwal**, a passionate Data Scientist with a focus on machine learning and data analytics. 
        I have completed my **Bachelor of Computer Applications (BCA)** with a specialization in **Data Science**. 
        Currently, I am deepening my knowledge and skills to pursue a career in data science, aiming to apply data-driven solutions in real-world scenarios.
        
        Throughout my career, I've worked on projects involving:
        - **Data Cleaning**: Ensuring data quality for better insights.
        - **Machine Learning**: Building models to predict and analyze data patterns.
       
        I am proficient in technologies like **Python**, **SQL**, **Power BI**, and machine learning libraries such as **Pandas**, **NumPy**, and **Scikit-learn**.

        Feel free to explore my portfolio to see my work and learn more about my projects.
        """)
