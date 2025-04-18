import streamlit as st
from pages.home_page import home
from pages.about_page import about
from pages.service_page import services
from pages.contact_page import contact

def load_main_css():
    st.markdown("""
        <style>
        /* Main styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Inter', sans-serif;
        }
        
        body {
            background: #f8f5ff;
            font-size: 1.1rem;
        }
        
        /* Navigation styles */
        .nav {
            padding: 1rem 2rem;
            background: rgba(255, 255, 255, 0.95);
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            margin-bottom: 2rem;
        }
        
        .stButton > button {
            background: rgb(109, 40, 217);
            color: white;
            padding: 0.75rem 1.5rem;
            border-radius: 4px;
            border: none;
            font-size: 1rem;
            transition: background 0.3s ease;
        }
        
        .stButton > button:hover {
            background: rgb(91, 33, 182);
        }
        </style>
    """, unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="SpeechSmith", layout="wide")
    load_main_css()
    
    # Initialize session state
    if 'page' not in st.session_state:
        st.session_state.page = 'home'
    
    # Navigation
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("Home"):
            st.session_state.page = 'home'
    with col2:
        if st.button("About"):
            st.session_state.page = 'about'
    # with col3:
    #     if st.button("Why Choose Us"):
    #         st.session_state.page = 'why_choose_us'
    with col3:
        if st.button("Services"):
            st.session_state.page = 'services'
    with col4:
        if st.button("Contact Us"):
            st.session_state.page = 'contact'
    
    # Display the selected page
    if st.session_state.page == 'home':
        home()
    elif st.session_state.page == 'about':
        about()
    elif st.session_state.page == 'services':
        services()
    elif st.session_state.page == 'contact':
        contact()

if __name__ == "__main__":
    main()