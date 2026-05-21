"""Text preprocessing utilities."""

import re

def clean_text(text):
    """Clean and normalize text for ML model.
    
    Args:
        text: Raw text to clean
        
    Returns:
        str: Cleaned and normalized text
    """
    # Convert to lowercase
    text = str(text).lower()
    
    # Remove special characters and numbers, keep only letters and spaces
    text = re.sub(r'[^a-z\s]', '', text)
    
    # Remove extra whitespace
    text = ' '.join(text.split())
    
    return text