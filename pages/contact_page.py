# pages/contact_page.py
import streamlit as st
from PIL import Image
import pandas as pd
import os

def load_contact_css():
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(255, 255, 255, 0.2)),
                        url("https://github.com/user-attachments/assets/bc0cf4c2-5598-4dbf-8aa3-a2029a516f8e") no-repeat center center fixed;
            background-size: cover;
        }
        
        .contact-container {
            max-width: 1200px;
            width: 100%;
            padding: 3rem;
            background: rgba(255, 255, 255, 0.3);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
            position: relative;
        }
        .image-container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 600px;  /* Increased height */
            background: none;  /* Removed white background */
            border-radius: 20px;
            margin-bottom: 1.5rem;
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.3);  /* Stronger shadow for a modern feel */
            overflow: hidden;
        }

        .image-container img {
            border-radius: 16px;
            width: 100%;
            height: 100%;
            object-fit: cover;  /* Ensures the image covers the entire container without distortion */
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .image-container img:hover {
            transform: scale(1.05);  /* Subtle zoom effect on hover */
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.5);  /* Enhanced shadow on hover */
        }
            
        .gradient-text {
            background: linear-gradient(45deg, #6C63FF, #FF6B9B);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            font-size: 2.5rem;
            margin-bottom: 2rem;
            text-align: center;
        }
        
        .form-group {
            margin-bottom: 1.5rem;
        }
        
        .contact-footer {
            background: #f8f9fa;
            padding: 1.5rem;
            border-radius: 10px;
            margin-top: 2rem;
            display: flex;
            justify-content: space-around;
            align-items: center;
            flex-wrap: wrap;
        }
        .contact-info-item {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            color: #4a5568;
            margin: 0.5rem;
        }
        .contact-info-item svg {
            width: 24px;
            height: 24px;
        }
        @media (max-width: 768px) {
            .contact-footer {
                flex-direction: column;
                gap: 1rem;
            }
        }
        
        .success-message {
            background: #4CAF50;
            color: white;
            padding: 1rem;
            border-radius: 4px;
            margin-bottom: 1rem;
            text-align: center;
        }
        .stTextInput, .stTextArea {
            background: rgba(255, 255, 255, 0.8);
            backdrop-filter: blur(12px);
            border-radius: 16px;
            padding: 1rem;
            margin-bottom: 1.5rem;
            color: #334155;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        
        /* Custom styling for Streamlit elements */
        /*.stTextInput > div > div > input {
            background: rgba(199, 180, 252, 0.3);
            border: none;
            padding: 0.75rem;
            border-radius: 4px;
        }
        
        .stTextArea > div > div > textarea {
            background: rgba(199, 180, 252, 0.3);
            border: none;
            padding: 0.75rem;
            border-radius: 4px;
        } */
        
        </style>
    """, unsafe_allow_html=True)

def contact():
    load_contact_css()
    
    # Container for the entire contact section
    st.markdown('<h2 class="gradient-text">Contact Us</h2>', unsafe_allow_html=True)
    
    # Create two columns: one for the form and one for the image
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Contact Form
        with st.form("contact_form"):
            name = st.text_input("Name", key="name", placeholder="Your name")
            email = st.text_input("Email ID", key="email", placeholder="Your email")
            comments = st.text_area("Comments", key="comments", placeholder="Your message", height=150)
            
            submitted = st.form_submit_button("Send Message")
            
            if submitted:
                # Collect form data
                form_data = {
                    'Name': name,
                    'Email': email,
                    'Comments': comments
                }
                
                # Convert form data to DataFrame
                df = pd.DataFrame([form_data])
                
                # Append to CSV file
                csv_file_path = "contact_form_data.csv"
                if os.path.exists(csv_file_path):
                    df.to_csv(csv_file_path, mode='a', index=False, header=False)
                else:
                    df.to_csv(csv_file_path, mode='w', index=False, header=True)
                
                # Display success message
                st.markdown('<div class="success-message">Form submitted successfully!</div>', 
                          unsafe_allow_html=True)
    
    with col2:
        # Try to load and display the contact image
        html_code = """
        <div class="image-container">
            <img src="https://github.com/user-attachments/assets/03d06851-6c6e-48d6-b977-22c58cbd6922" alt="Image not found">
        </div>
        """

        # Rendering the image with the specified HTML and CSS
        st.markdown(html_code, unsafe_allow_html=True)
        
    
    # Footer with contact information
    st.markdown("""
        <div class="contact-footer">
            <div class="contact-info-item">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" 
                     stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
                    <polyline points="22,6 12,13 2,6"/>
                </svg>
                <span>contact@example.com</span>
            </div>
            <div class="contact-info-item">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" 
                     stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
                    <circle cx="12" cy="10" r="3"/>
                </svg>
                <span>123 Business Street, City, Country</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    contact()
