import os 
import subprocess
import sys
from google.genai import types
def run_python_file(working_directory, file_path, args=None):
    """Executes a Python file located at `file_path`, ensuring it is within `working_directory`."""
    working_dir_abs = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(working_dir_abs, file_path))
    target_file = os.path.basename(full_path)
    valid_target_dir = os.path.commonpath([working_dir_abs, full_path]) == working_dir_abs

    if not valid_target_dir:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(full_path):
        return f'Error: "{file_path}" does not exist or is not a regular file'
    
    if not target_file.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file'
    
    try:
        command = [sys.executable, full_path] 
        if not (args == None):
            command.extend(args)
        

        completed_process = subprocess.run(command, capture_output=True, text=True,cwd=working_dir_abs , timeout=30)
        output_string =""
        if completed_process.returncode != 0:
            output_string += f"Process exited with code {completed_process.returncode}\n"
        if completed_process.stdout :
            output_string += f"STDOUT: {completed_process.stdout}"
        if completed_process.stdout and completed_process.stderr:
            output_string += "\n"
        if completed_process.stderr:
            output_string += f"STDERR: {completed_process.stderr}"
        if not completed_process.stdout and not completed_process.stderr:
            output_string += "No output produced"

        return output_string
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file located at `file_path`, ensuring it is within `working_directory`",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to read, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="List of arguments to pass to the Python script",
                items=types.Schema(type=types.Type.STRING),
            ),
        },required=["file_path"]
    ),
)