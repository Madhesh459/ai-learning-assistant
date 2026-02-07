"""
Database service for conversation persistence using Supabase.
IMPORTANT: Used ONLY for persistence, NOT for building prompts.
Live conversation context is maintained in Streamlit session_state.
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

# Initialize Supabase client lazily
_supabase_client = None

def get_supabase_client() -> Client:
    """Get or create Supabase client."""
    global _supabase_client
    if _supabase_client is None:
        try:
            _supabase_client = create_client(
                get_secret("SUPABASE_URL"),
                get_secret("SUPABASE_KEY")
            )
        except Exception as e:
            st.error(f"Failed to initialize Supabase: {str(e)}")
            raise
    return _supabase_client

def save_message(user_id: str, role: str, content: str):
    """
    Save a message to Supabase for persistence.
    
    Args:
        user_id: User's unique identifier
        role: 'user' or 'assistant'
        content: Message content
    """
    try:
        supabase = get_supabase_client()
        data = {
            "user_id": user_id,
            "role": role,
            "content": content
        }
        supabase.table('conversations').insert(data).execute()
    except Exception as e:
        st.error(f"Failed to save message: {str(e)}")

def load_conversation(user_id: str, limit: int = 50):
    """
    Load conversation history from Supabase for a specific user.
    This is used ONLY on login to restore session_state.
    
    Args:
        user_id: User's unique identifier
        limit: Maximum number of messages to load
        
    Returns:
        List of message dicts with 'role' and 'content' keys
    """
    try:
        supabase = get_supabase_client()
        result = supabase.table('conversations')\
            .select("role, content")\
            .eq('user_id', user_id)\
            .order('created_at')\
            .limit(limit)\
            .execute()
        
        # Convert to format expected by session_state
        messages = []
        if result.data:
            for msg in result.data:
                messages.append({
                    "role": msg["role"],
                    "content": msg["content"]
                })
        return messages
    except Exception as e:
        st.error(f"Failed to load conversation: {str(e)}")
        return []

def clear_conversation(user_id: str):
    """
    Delete all messages for a specific user.
    
    Args:
        user_id: User's unique identifier
    """
    try:
        supabase = get_supabase_client()
        supabase.table('conversations')\
            .delete()\
            .eq('user_id', user_id)\
            .execute()
        st.success("Conversation cleared!")
    except Exception as e:
        st.error(f"Failed to clear conversation: {str(e)}")
