"""
AI Learning Assistant - Hackathon MVP
Main Streamlit application with authentication and chat interface.
"""

import streamlit as st
from auth_service import signup, login, logout, get_current_user
from db_service import save_message, load_conversation, clear_conversation
from ai_service import generate_explanation
from context_manager import process_code_input

# Page configuration
st.set_page_config(
    page_title="AI Learning Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
def init_session_state():
    """Initialize session state variables."""
    if 'user' not in st.session_state:
        st.session_state.user = None
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'response_mode' not in st.session_state:
        st.session_state.response_mode = "simple"
    if 'code_context' not in st.session_state:
        st.session_state.code_context = ""

init_session_state()

# Check authentication status on app load
if st.session_state.user is None:
    st.session_state.user = get_current_user()
    
    # Load conversation history from Supabase if user is authenticated
    if st.session_state.user and len(st.session_state.messages) == 0:
        st.session_state.messages = load_conversation(st.session_state.user.id)

# Authentication UI
if not st.session_state.user:
    st.title("🤖 AI Learning Assistant")
    st.markdown("### Your AI-powered coding tutor")
    st.markdown("Understand complex codebases in minutes, not hours.")
    
    st.markdown("---")
    
    # Login/Signup tabs
    tab1, tab2 = st.tabs(["Login", "Sign Up"])
    
    with tab1:
        st.subheader("Login to your account")
        login_email = st.text_input("Email", key="login_email", placeholder="your@email.com")
        login_password = st.text_input("Password", type="password", key="login_password", placeholder="Enter your password")
        
        if st.button("Login", type="primary", use_container_width=True):
            if login_email and login_password:
                user = login(login_email, login_password)
                if user:
                    st.session_state.user = user
                    # Load conversation history from Supabase
                    st.session_state.messages = load_conversation(user.id)
                    st.rerun()
            else:
                st.error("Please enter both email and password")
    
    with tab2:
        st.subheader("Create a new account")
        signup_email = st.text_input("Email", key="signup_email", placeholder="your@email.com")
        signup_password = st.text_input("Password", type="password", key="signup_password", placeholder="Choose a strong password")
        signup_password_confirm = st.text_input("Confirm Password", type="password", key="signup_password_confirm", placeholder="Re-enter your password")
        
        if st.button("Sign Up", type="primary", use_container_width=True):
            if signup_email and signup_password and signup_password_confirm:
                if signup_password == signup_password_confirm:
                    user = signup(signup_email, signup_password)
                    if user:
                        st.session_state.user = user
                        st.rerun()
                else:
                    st.error("Passwords do not match")
            else:
                st.error("Please fill in all fields")
    
    st.markdown("---")
    st.markdown("**Demo Features:**")
    st.markdown("✅ Code explanation (paste or upload)")
    st.markdown("✅ Follow-up questions with context")
    st.markdown("✅ Simple vs Detailed modes")
    st.markdown("✅ Conversation history persistence")

else:
    # Main application UI (authenticated users only)
    
    # Sidebar
    with st.sidebar:
        st.title("⚙️ Settings")
        
        # User info
        st.markdown(f"**Logged in as:**")
        st.markdown(f"`{st.session_state.user.email}`")
        
        st.markdown("---")
        
        # Response mode toggle
        st.markdown("**Response Mode:**")
        mode = st.radio(
            "Choose explanation depth",
            options=["simple", "detailed"],
            index=0 if st.session_state.response_mode == "simple" else 1,
            help="Simple: High-level overview\nDetailed: In-depth with examples"
        )
        st.session_state.response_mode = mode
        
        st.markdown("---")
        
        # Clear conversation button
        if st.button("🗑️ Clear Conversation", use_container_width=True):
            if st.session_state.user:
                clear_conversation(st.session_state.user.id)
                st.session_state.messages = []
                st.session_state.code_context = ""
                st.rerun()
        
        # Logout button
        if st.button("🚪 Logout", use_container_width=True):
            logout()
            st.rerun()
        
        st.markdown("---")
        st.markdown("**💡 Tips:**")
        st.markdown("• Paste code or upload a file")
        st.markdown("• Ask follow-up questions")
        st.markdown("• Switch modes anytime")
    
    # Main content area
    st.title("🤖 AI Learning Assistant")
    st.markdown("Ask me anything about code!")
    
    # Code input section
    st.markdown("### 📝 Code Input")
    
    input_method = st.radio(
        "Choose input method:",
        options=["Paste Code", "Upload File"],
        horizontal=True
    )
    
    if input_method == "Paste Code":
        code_input = st.text_area(
            "Paste your code here:",
            height=200,
            placeholder="def example():\n    return 'Hello, World!'",
            help="Paste any code snippet you want to understand"
        )
        if code_input:
            st.session_state.code_context = process_code_input(code_input)
            st.info(f"📊 Code length: {len(code_input)} characters")
    
    else:  # Upload File
        uploaded_file = st.file_uploader(
            "Upload a code file:",
            type=["py", "js", "java", "cpp", "c", "txt", "md"],
            help="Max file size: 10MB"
        )
        if uploaded_file:
            try:
                code_content = uploaded_file.read().decode("utf-8")
                st.session_state.code_context = process_code_input(code_content)
                st.success(f"✅ File uploaded: {uploaded_file.name}")
                st.info(f"📊 File size: {len(code_content)} characters")
                
                # Show preview
                with st.expander("Preview first 500 characters"):
                    st.code(code_content[:500], language="python")
            except Exception as e:
                st.error(f"Error reading file: {str(e)}")
    
    st.markdown("---")
    
    # Chat interface
    st.markdown("### 💬 Conversation")
    
    # Display chat messages
    chat_container = st.container()
    with chat_container:
        if len(st.session_state.messages) == 0:
            st.info("👋 Welcome! Paste some code above and ask me a question to get started.")
        else:
            for msg in st.session_state.messages:
                if msg["role"] == "user":
                    with st.chat_message("user"):
                        st.markdown(msg["content"])
                else:
                    with st.chat_message("assistant"):
                        st.markdown(msg["content"])
    
    # Question input
    question = st.text_input(
        "Ask a question:",
        placeholder="What does this code do?",
        help="Ask anything about the code above"
    )
    
    col1, col2 = st.columns([1, 5])
    
    with col1:
        submit_button = st.button("🚀 Ask", type="primary", use_container_width=True)
    
    if submit_button and question:
        if not st.session_state.code_context and len(st.session_state.messages) == 0:
            st.warning("⚠️ Please provide some code first!")
        else:
            # Show loading spinner
            with st.spinner("🤔 Thinking..."):
                # Generate explanation using session_state history
                explanation = generate_explanation(
                    question=question,
                    code=st.session_state.code_context,
                    mode=st.session_state.response_mode,
                    history=st.session_state.messages
                )
                
                # Add to session state (live context)
                st.session_state.messages.append({"role": "user", "content": question})
                st.session_state.messages.append({"role": "assistant", "content": explanation})
                
                # Save to Supabase (persistence only)
                save_message(st.session_state.user.id, "user", question)
                save_message(st.session_state.user.id, "assistant", explanation)
            
            # Rerun to display new messages
            st.rerun()
    
    # Footer
    st.markdown("---")
    st.markdown("**Built with Streamlit + Google Gemini (FREE) + Supabase** | Hackathon MVP 2024")
