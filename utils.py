def write_to_file(text: str, filename: str) -> None:
    """
    Writes the given text to a specified file.

    Parameters:
    text (str): The content to write to the file.
    filename (str): The name of the file where the content will be written.

    Raises:
    IOError: If the file cannot be opened or written to.
    ValueError: If the text or filename is empty.
    """
    if not text or not filename:
        raise ValueError("Text and filename must not be empty.")
    
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

    