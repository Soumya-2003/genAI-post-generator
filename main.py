import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post
import time

length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hindi", "Hinglish"]

def load_css():
    """Load CSS from external file"""
    try:
        with open('style.css', 'r') as f:
            css = f.read()
        st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("CSS file not found. Please make sure style.css is in the same directory.")
        st.markdown("""
        <style>
        .stApp { background: #5A3DAB; }
        .stButton > button { background: #000000; color: white; }
        </style>
        """, unsafe_allow_html=True)

def show_success_notification():
    """Show a temporary success notification"""
    notification_html = """
    <div class="success-notification">
        ✅ Post generated successfully!
    </div>
    """
    st.markdown(notification_html, unsafe_allow_html=True)

def main():

    load_css()
    
    # Initialize session state for notification
    if 'show_notification' not in st.session_state:
        st.session_state.show_notification = False
    
    st.markdown('<h1 class="main-title">✍️ Post Writer 📝</h1>', unsafe_allow_html=True)
    
    fs = FewShotPosts()
    tags = fs.get_tags()
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🏷️ Topic")
        selected_tag = st.selectbox("Select a topic", options=tags, key="topic", label_visibility="collapsed")

    with col2:
        st.markdown("### 📏 Length")
        selected_length = st.selectbox("Select length", options=length_options, key="length", label_visibility="collapsed")

    with col3:
        st.markdown("### 🌍 Language")
        selected_language = st.selectbox("Select language", options=language_options, key="language", label_visibility="collapsed")
    
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    col_left, col_center, col_right = st.columns([1, 2, 1])
    
    with col_center:
        if st.button("Generate Post", key="generate", use_container_width=True):
            with st.spinner("Generating post..."):
                post = generate_post(selected_length, selected_language, selected_tag)
            
            st.session_state.show_notification = True
            st.session_state.generated_post = post
            
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Show notification if flag is set
    if st.session_state.get('show_notification', False):
        show_success_notification()
        # Reset the flag
        st.session_state.show_notification = False
        
        # Display the generated post with light text color
        if 'generated_post' in st.session_state:
            st.markdown("### Your Generated Post:")
            st.markdown(f'<div class="generated-post-content">{st.session_state.generated_post}</div>', unsafe_allow_html=True)
          
if __name__ == "__main__":
    main()