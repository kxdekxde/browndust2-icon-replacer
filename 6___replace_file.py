import os
import shutil

def find_and_replace_data_files():
    # Get the current script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define paths
    repacked_path = os.path.join(script_dir, "Repacked")
    gamfs_path = os.path.join(os.path.expanduser("~"), "AppData", "LocalLow", "Unity", "Gamfs_BrownDust II")
    
    # Check if Repacked folder exists
    if not os.path.exists(repacked_path):
        print(f"Error: Repacked folder not found at {repacked_path}")
        return
    
    # Check if destination exists
    if not os.path.exists(gamfs_path):
        print(f"Error: Gamfs_BrownDust II folder not found at {gamfs_path}")
        return
    
    print(f"Searching for __data files in {repacked_path} to replace in {gamfs_path}...\n")
    
    # Walk through all directories in Repacked to find __data files
    for root, dirs, files in os.walk(repacked_path):
        if "__data" in files:
            # Get relative path from Repacked folder
            relative_path = os.path.relpath(root, repacked_path)
            
            # Construct corresponding Gamfs path
            gamfs_root = os.path.join(gamfs_path, relative_path)
            
            # Check if corresponding path exists in Gamfs
            if os.path.exists(gamfs_root):
                src_data = os.path.join(root, "__data")
                dst_data = os.path.join(gamfs_root, "__data")
                
                try:
                    # Check if destination __data exists
                    if os.path.exists(dst_data):
                        # Backup the original file (optional)
                        # backup_path = dst_data + ".bak"
                        # shutil.copy2(dst_data, backup_path)
                        
                        # Replace the file
                        shutil.copy2(src_data, dst_data)
                        print(f"Replaced: {os.path.join(relative_path, '__data')}")
                    else:
                        # Create directory if it doesn't exist
                        os.makedirs(gamfs_root, exist_ok=True)
                        shutil.copy2(src_data, dst_data)
                        print(f"Added new: {os.path.join(relative_path, '__data')}")
                except Exception as e:
                    print(f"Error processing {relative_path}: {e}")
            else:
                print(f"No matching path in Gamfs for: {relative_path} - skipping")

    print("\n__data file replacement completed!")

if __name__ == "__main__":
    find_and_replace_data_files()