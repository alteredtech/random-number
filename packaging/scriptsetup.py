import os

def get_script_list(start_path):
    script_list = []
    for root, dirs, files in os.walk(start_path):
        for file in files:
            if file.endswith(".py") and not file.startswith("__init__"):
                script_name = os.path.splitext(file)[0]
                folder_name = os.path.basename(root)
                script_list.append(f"{script_name}={folder_name}.{script_name}:main")
    return script_list

# Example usage
start_path = "src/"
result = get_script_list(start_path)
print(result)