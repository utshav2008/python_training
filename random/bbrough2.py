process_list = [
    {"id": 15, "children": [1, 2]},
    {"id": 1, "children": []},
    {"id": 2, "children": []},
    {"id": 9, "children": [4]},
    {"id": 10, "children": [15, 9]},
    {"id": 4, "children": []}
]


def find_root_crash(process_list):
    parent_map = {}  # Maps child -> parent
    all_processes = set()  # Stores all process IDs
    
    # Step 1: Build Parent Map & Process Set
    for process in process_list:
        parent_id = process["id"]
        all_processes.add(parent_id)
        
        for child in process.get("children", []):
            parent_map[child] = parent_id
            all_processes.add(child)
    
    # Step 2: Find the Root Cause (Process Without a Parent)
    for process in all_processes:
        if process not in parent_map:  # No parent means it's the first one that crashed
            return process
    
    return None  # Just in case input is empty



