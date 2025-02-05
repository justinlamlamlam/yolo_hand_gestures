import os
import random
import shutil

def split_data(images_dir, labels_dir, split_ratio=0.9):
    """Splits files in images and labels directories into train and val sets, ensuring matching pairs."""
    
    # Get all filenames (assuming the same structure for images and labels)
    image_files = [f for f in os.listdir(images_dir) if os.path.isfile(os.path.join(images_dir, f))]
    label_files = [f for f in os.listdir(labels_dir) if os.path.isfile(os.path.join(labels_dir, f))]
    
    # Check that image and label counts are the same
    if len(image_files) != len(label_files):
        print(f"Found {len(image_files)} image files and {len(label_files)} label files.")
        raise ValueError("The number of image files and label files must be the same.")
    
    # Create dictionaries for easy lookup (mapping filename without extension to its corresponding full filename)
    image_dict = {os.path.splitext(f)[0]: f for f in image_files}
    label_dict = {os.path.splitext(f)[0]: f for f in label_files}
    
    # Ensure that every image has a corresponding label (based on the base filename)
    common_files = list(image_dict.keys() & label_dict.keys())  # Files with matching base names
    
    # Shuffle the filenames randomly
    random.shuffle(common_files)
    
    # Calculate the split index
    split_index = int(len(common_files) * split_ratio)
    
    # Split into train and val sets
    train_files = common_files[:split_index]
    val_files = common_files[split_index:]
    
    # Create train and val directories inside both images and labels
    train_images_dir = os.path.join(images_dir, "train")
    val_images_dir = os.path.join(images_dir, "val")
    train_labels_dir = os.path.join(labels_dir, "train")
    val_labels_dir = os.path.join(labels_dir, "val")
    
    # Create the directories if they don't exist
    os.makedirs(train_images_dir, exist_ok=True)
    os.makedirs(val_images_dir, exist_ok=True)
    os.makedirs(train_labels_dir, exist_ok=True)
    os.makedirs(val_labels_dir, exist_ok=True)

    # Move files to train/val directories
    for base_filename in train_files:
        # Move corresponding image and label files to train
        image_filename = image_dict[base_filename]
        label_filename = label_dict[base_filename]
        
        shutil.copy(os.path.join(images_dir, image_filename), os.path.join(train_images_dir, image_filename))
        shutil.copy(os.path.join(labels_dir, label_filename), os.path.join(train_labels_dir, label_filename))

    for base_filename in val_files:
        # Move corresponding image and label files to val
        image_filename = image_dict[base_filename]
        label_filename = label_dict[base_filename]
        
        shutil.copy(os.path.join(images_dir, image_filename), os.path.join(val_images_dir, image_filename))
        shutil.copy(os.path.join(labels_dir, label_filename), os.path.join(val_labels_dir, label_filename))
    
    print(f"Train-Val split completed: {len(train_files)} files for training, {len(val_files)} files for validation.")

if __name__ == "__main__":
    images_dir = "full_dataset/images"  # Path to images directory
    labels_dir = "full_dataset/labels"  # Path to labels directory
    
    # Perform the data split
    split_data(images_dir, labels_dir)
