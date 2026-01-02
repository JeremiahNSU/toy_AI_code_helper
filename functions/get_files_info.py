
import os
from builtins import Error
def get_files_info(working_directory, directory="."):
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
    # Will be True or False
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    if not valid_target_dir:
        return Error(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    
    valid_directory = os.path.isdir(target_dir)
    if not valid_directory:
        return Error(f'Error: "{directory}" is not a directory.')
    
    all_entries = os.listdir(target_dir)
    files_info = [] 
    all_file_info = ""
    try:
        for entry in all_entries:
            entry_path = os.path.join(target_dir, entry)
            
            file_size = os.path.getsize(entry_path) 
            files_info.append({
                "name": entry,
                "size": file_size,
                "is_dir": os.path.isdir(entry_path)
            })

    except Exception as e:
        return Error(f"Error accessing directory contents: {str(e)}")

    for file_info in files_info:
        all_file_info += f"- {file_info['name']}: file_size={file_info['size']} bytes, is_dir={file_info['is_dir']}\n"
    return all_file_info

    