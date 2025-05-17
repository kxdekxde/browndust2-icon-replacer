import os
import shutil

def copy_backup_to_modded():
    # Get the current script's directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define the source and destination paths
    backup_folder = os.path.join(current_dir, "Backup")
    modded_bundles_folder = os.path.join(current_dir, "Modded Bundles")
    
    # Check if Backup folder exists
    if not os.path.exists(backup_folder):
        print(f"Error: Backup folder not found at {backup_folder}")
        return
    
    # Create Modded Bundles folder if it doesn't exist
    if not os.path.exists(modded_bundles_folder):
        os.makedirs(modded_bundles_folder)
    
    # Walk through the Backup folder and copy all files
    for root, dirs, files in os.walk(backup_folder):
        # Calculate relative path from Backup folder
        relative_path = os.path.relpath(root, backup_folder)
        
        # Create corresponding directory in Modded Bundles
        dest_dir = os.path.join(modded_bundles_folder, relative_path)
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        
        # Copy each file
        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_dir, file)
            
            # Skip if file already exists and is the same
            if os.path.exists(dest_file):
                src_size = os.path.getsize(src_file)
                dest_size = os.path.getsize(dest_file)
                if src_size == dest_size:
                    continue
            
            shutil.copy2(src_file, dest_dir)
            print(f"Copied: {os.path.join(relative_path, file)}")
    
    print("\nCopy operation completed successfully!")

if __name__ == "__main__":
    copy_backup_to_modded()