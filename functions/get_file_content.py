import os

def get_file_content(working_directory, file_path):


    working_dir_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
    # Will be True or False
    valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
    if not valid_target_file:
        return (f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
    
    valid_file = os.path.isfile(target_file)
    if not valid_file:
        return (f'Error: File not found or is not a regular file: "{file_path}"')
    
    max_content_size = 10000  # characters
    
    content = ""
    
    try:
        with open(target_file, 'r') as f:
            content += f.read(max_content_size)
            extra_content = f.read(1) 
            if extra_content != "":
                content += f'[...File "{file_path}" truncated at {max_content_size} characters]'
    except Exception as e:
        return f"Error: {str(e)}"
    
    return content