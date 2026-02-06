"""
Prompt builder for AI explanations.
Builds prompts using session_state messages (NOT Supabase).
"""

def build_system_prompt(mode: str) -> str:
    """
    Build system prompt based on response mode.
    
    Args:
        mode: 'simple' or 'detailed'
        
    Returns:
        System prompt string
    """
    base_prompt = """You are a patient coding tutor helping developers learn and understand code.

Guidelines:
- Explain concepts in simple, clear terms
- Avoid unnecessary jargon
- Use bullet points and step-by-step breakdowns
- Provide actionable next steps
- Be encouraging and supportive
- When explaining code, describe what it does before how it works
"""
    
    if mode == "simple":
        return base_prompt + "\n- Keep explanations concise (max 500 words)\n- Focus on high-level concepts"
    else:  # detailed
        return base_prompt + "\n- Provide comprehensive explanations (max 1500 words)\n- Include code examples and best practices"

def build_user_message(question: str, code: str = None) -> str:
    """
    Build user message with question and optional code.
    
    Args:
        question: User's question
        code: Optional code snippet
        
    Returns:
        Formatted user message
    """
    if code:
        return f"{question}\n\n```\n{code}\n```"
    return question

def format_messages_for_api(history: list, system_prompt: str) -> list:
    """
    Format messages from session_state for OpenAI API.
    
    Args:
        history: List of message dicts from session_state
        system_prompt: System prompt string
        
    Returns:
        List of messages formatted for OpenAI API
    """
    messages = [{"role": "system", "content": system_prompt}]
    
    # Add conversation history (last 5 exchanges to stay within token limits)
    recent_history = history[-10:] if len(history) > 10 else history
    
    for msg in recent_history:
        messages.append({
            "role": msg["role"],
            "content": msg["content"]
        })
    
    return messages
