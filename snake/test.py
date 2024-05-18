import h5py

# Open the H5 file in read-only mode
file_path = "keras_model.h5"
with h5py.File(file_path, "r") as file:
    # List all groups and datasets in the file
    print("Groups and datasets in the H5 file:")
    for name in file:
        print(name)

    # Access a specific group or dataset
    group_or_dataset = file["your_group_or_dataset_name"]

    # Access data from the group or dataset
    data = group_or_dataset[:]
    print("Data from the H5 file:")
    print(data)
