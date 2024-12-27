import streamlit as st


def contshow():
    st.title("Get in Touch")
    st.subheader("Feel free to reach out to me via:")
    st.write("""
    - <img src="https://img.icons8.com/ios-filled/50/000000/new-post.png" width="20"/> **Email**: [theritikbarnwal@gmail.com](https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox?compose=GTvVlcSGKnRBkrldmTGDnWDkJdGtsmVmBvhVLXxCvrNwpwBKXzvKgBLrjflpjTPzxHsqZqGcFDfMR)
    - <img src="https://img.icons8.com/ios-filled/50/000000/github.png" width="20"/> **GitHub**: [Ritik Barnwal](https://github.com/theritikbarnwal)
    - <img src="https://img.icons8.com/ios-filled/50/000000/linkedin.png" width="20"/> **LinkedIn**: [Ritik Barnwal](https://www.linkedin.com/in/theritikbarnwal/)
    """, unsafe_allow_html=True)

    st.write("\n\n")

# Initialize session state to manage the form's visibility
    if "show_form" not in st.session_state:
        st.session_state["show_form"] = False

# Button to toggle the form
    if st.button("✉️ Reach Out"):
        st.session_state["show_form"] = not st.session_state["show_form"]

# Display the form only if the button has been clicked
    if st.session_state["show_form"]:
        contact_form = """
        <style>
            .contact-form-container {
                max-width: 500px;
                margin: 20px auto;
                padding: 20px;
                background-color: #f9f9f9;
                border-radius: 8px;
                box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
            }
            .contact-form-container input, .contact-form-container textarea {
                width: 100%;
                padding: 10px;
                margin: 10px 0;
                border: 1px solid #ccc;
                border-radius: 5px;
                font-size: 16px;
                resize: vertical;
            }
            .contact-form-container button {
                width: 100%;
                padding: 10px;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                font-size: 18px;
                cursor: pointer;
            }
            .contact-form-container button:hover {
                background-color: #45a049;
            }
        </style>
        <div class="contact-form-container">
            <form action="https://formsubmit.co/theritikbarnwal@gmail.com" method="POST">
                <input type="text" name="name" placeholder="Name" required>
                <input type="email" name="email" placeholder="mail@gmail.com" required>
                <input type="tel" name="phone" placeholder="Contact Number" pattern="[0-9]{10}" required>
                <textarea name="message" placeholder="Message..." required></textarea>
                <button type="submit">Submit</button>
            </form>
        </div>
        """
        # Display the styled form using st.markdown with unsafe HTML allowed
        st.markdown(contact_form, unsafe_allow_html=True)