import os
from google.genai import types
def write_file(working_directory, file_path, content):
    """
    Writes content to a file located at file_path within the working_directory.
    Creates any necessary directories if they do not exist.

    Parameters:
    working_directory (str): The base directory where the file will be written.
    file_path (str): The relative path to the file from the working_directory.
    content (str): The content to write to the file.
    """
    # Combine working directory and file path
    full_path = os.path.abspath(os.path.join(working_directory, file_path))
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.dirname(full_path)
    valid_target_dir = os.path.commonpath([working_dir_abs, full_path]) == working_dir_abs
    
    if not valid_target_dir:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    if os.path.isdir(full_path):
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    
   
    
    # Write content to the file
    try:
        os.makedirs(target_dir, exist_ok=True)
        with open(full_path, 'w') as file:
            file.write(content)
    except Exception as e:
        return f'Error: {str(e)}'
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file located at `file_path`, ensuring it is within `working_directory`",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory",
                
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file",
            ),
        },required=["file_path", "content"]
    ),
    )