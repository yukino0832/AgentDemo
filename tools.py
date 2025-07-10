import os
import socket
import platform
import psutil
from pathlib import Path

base_dir = Path("./files")

def read_file(name: str) -> str:
    """
    Reads the content of a file and returns it as a string.
    
    Args:
        file_path (str): The path to the file to be read.
        
    Returns:
        str: The content of the file.
    """
    print(f"Reading file: {name}")
    try:
        with open(base_dir / name, 'r') as file:
            content = file.read()
        return content
    except Exception as e:
        return f"Error reading file {name}: {e}"
    

def list_files()->list[str]:
    print("(list_file)")
    file_list = []
    for item in base_dir.rglob('*'):
        if item.is_file():
            file_list.append(str(item.relative_to(base_dir)))
    return file_list

def rename_file(name: str, new_name: str) -> str:
    print(f"Renaming file {name} to {new_name}")
    try:
        new_path = base_dir / new_name
        if not str(new_path).startswith(str(base_dir)):
            return "Error: New file name must be within the base directory."
        # os.makedirs(new_path, exist_ok=True)
        os.rename(base_dir / name, new_path)
        return f"File {name} renamed to {new_name} successfully."
    except Exception as e:
        return f"Error renaming file {name}: {e}"

def get_host_info() -> str:
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        system = platform.system()
        release = platform.release()
        version = platform.version()
        processor = platform.processor()
        cpu_count = psutil.cpu_count(logical=True)
        mem = psutil.virtual_memory()

        info = (
            f"Hostname: {hostname}\n"
            f"IP Address: {ip_address}\n"
            f"CPU: {processor} ({cpu_count} cores)\n"
            f"Memory: {mem.total / (1024**3):.2f} GB\n"
            f"OS: {system} {release} ({version})"
        )
        return info

    except Exception as e:
        return f"Failed to get host info: {e}"