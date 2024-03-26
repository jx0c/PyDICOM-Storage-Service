import os
from pydicom import dcmread
from pynetdicom import AE, evt, StoragePresentationContexts

# Define the directory where you want to save the DICOM files
save_directory = "C:/burner/dicom/files"

# Ensure the save directory exists, create it if it doesn't
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

def handle_store(event):
    """Handle incoming C-STORE requests."""
    # Extract the dataset from the event
    ds = event.dataset
    # Specify the file path using the SOP Instance UID to create a unique filename
    file_path = os.path.join(save_directory, f"{ds.SOPInstanceUID}.dcm")
    # Save the dataset to file
    ds.save_as(file_path, write_like_original=False)
    # TESTING
    print(f"Saved DICOM file {file_path}")
    # Return a 'Success' status
    return 0x0000

# Create an Application Entity (AE) and set the AE Title
ae = AE(ae_title='AETITLEHERE')
# Support all storage SOP Classes
ae.supported_contexts = StoragePresentationContexts
# Add the handler for C-STORE requests
handlers = [(evt.EVT_C_STORE, handle_store)]

# Start the server on a specified IP address, and port
ae.start_server(('127.0.0.1', XXXXX), evt_handlers=handlers)
