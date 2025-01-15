import streamlit as st
import home
import about
import contact
import project
st.set_page_config(page_icon="img/icon.png",page_title="theritikbarnwal",layout="wide")

st.sidebar.title("Navigation")
option = st.sidebar.radio("Explore", ["**Home**","**About**", "**Project**","**Contact**"])


if option == "**Home**":
    home.homeshow()
elif option == "**About**":
    about.amshow()
elif option == "**Project**":
    project.projshow()
elif option == "**Contact**":
    contact.contshow()

  

st.divider()
# Footer
st.write("© 2025 theritikbarnwal")
