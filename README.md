# PyDICOM Storage Server

PyDICOM Storage Server is a Python-based application for receiving and storing DICOM (Digital Imaging and Communications in Medicine) files. It provides a simple server interface that accepts DICOM files from medical imaging devices and saves them to a specified directory.

## Features

- Receive DICOM files over the network using the DICOM protocol.
- Store received DICOM files in a specified directory.
- Supports handling of C-STORE requests.

## Usage

1. Clone the repository:

```bash
git clone https://github.com/jx0c/pydicom-storage-server.git
```
2. Install the required dependencies:

```bash
pip install pydicom pynetdicom
```
   
3.  Configure your DICOM devices to send files to the server's IP address and port <em>(default: 127.0.0.1:11112).</em>


4. Run the server:

  ```bash
   python server.py
   ```

## License

This project is licensed under the GNU General Public License version 2.0 (GPL-2.0). See the LICENSE file for details.



