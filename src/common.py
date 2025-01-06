
def snake_to_title(snake_case_string):
    """Converts a snake_case string to a Title Case string."""
    words = snake_case_string.split('_')
    return ' '.join(word.capitalize() for word in words)
