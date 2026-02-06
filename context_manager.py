"""
Context manager for code chunking and token estimation.
Handles large code inputs by splitting them into processable segments.
"""

def count_tokens(text: str) -> int:
    """
    Rough estimate of token count.
    Rule of thumb: 1 token ≈ 4 characters
    
    Args:
        text: Input text
        
    Returns:
        Estimated token count
    """
    return len(text) // 4

def chunk_code(code: str, max_chars: int = 4000) -> list[str]:
    """
    Split code into chunks if it exceeds max size.
    
    Args:
        code: Code to chunk
        max_chars: Maximum characters per chunk
        
    Returns:
        List of code chunks
    """
    if len(code) <= max_chars:
        return [code]
    
    # Simple chunking by splitting at newlines
    chunks = []
    current_chunk = ""
    
    for line in code.split('\n'):
        if len(current_chunk) + len(line) + 1 <= max_chars:
            current_chunk += line + '\n'
        else:
            if current_chunk:
                chunks.append(current_chunk)
            current_chunk = line + '\n'
    
    if current_chunk:
        chunks.append(current_chunk)
    
    return chunks

def process_code_input(code: str) -> str:
    """
    Process code input and return first chunk if too large.
    
    Args:
        code: Input code
        
    Returns:
        Processed code (first chunk if too large)
    """
    if len(code) > 4000:
        chunks = chunk_code(code, max_chars=3000)
        return chunks[0] + "\n\n[... code truncated for length ...]"
    return code
