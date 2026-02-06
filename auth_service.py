"""
Authentication service using Supabase Auth.
Handles signup, login, logout, and session management.
"""

from supabase import create_client, Client
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_secret(key: str) -> str:
    """Get secret from environment or Streamlit secrets."""
    # Try environment variable first
    value = os.getenv(key)
    if value:
        return value
    # Try Streamlit secrets
    try:
        return st.secrets[key]
    except:
        raise ValueError(f"Missing required secret: {key}")

# Initialize Supabase client
supabase: Client = create_client(
    get_secret("SUPABASE_URL"),
    get_secret("SUPABASE_KEY")
)

def signup(email: str, password: str):
    """
    Sign up a new user with email and password.
    
    Args:
        email: User's email address
        password: User's password
        
    Returns:
        User object if successful, None otherwise
    """
    try:
        response = supabase.auth.sign_up({
            "email": email,
            "password": password
        })
        if response.user:
            st.success("Account created successfully!")
            return response.user
        return None
    except Exception as e:
        st.error(f"Signup failed: {str(e)}")
        return None

def login(email: str, password: str):
    """
    Log in an existing user with email and password.
    
    Args:
        email: User's email address
        password: User's password
        
    Returns:
        User object if successful, None otherwise
    """
    try:
        response = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })
        if response.user:
            st.success("Logged in successfully!")
            return response.user
        return None
    except Exception as e:
        st.error(f"Login failed: {str(e)}")
        return None

def logout():
    """Log out the current user and clear session state."""
    try:
        supabase.auth.sign_out()
        st.session_state.clear()
        st.success("Logged out successfully!")
    except Exception as e:
        st.error(f"Logout failed: {str(e)}")

def get_current_user():
    """
    Get the currently authenticated user.
    
    Returns:
        User object if authenticated, None otherwise
    """
    try:
        user = supabase.auth.get_user()
        return user.user if user else None
    except:
        return None
