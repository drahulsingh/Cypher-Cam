# Cypher-Cam

![ViewCount](https://views.whatilearened.today/views/github/drahulsingh/Cypher-Cam.svg)

![Cypher-Cam](mn.png)

## Description

Cypher-Cam is a Python GUI application designed for surveillance using a webcam or surveillance camera. It includes features such as motion detection, noise detection, in/out tracking, and recording functionalities. The application has a user-friendly interface and supports a dark mode for better visibility in low-light conditions.

## Features

- Anti-theft alarming system
- Face and motion detection
- Visitor recognition
- Video surveillance
- Dark mode toggle for the GUI

## Tech Stack

- **Programming Language**: Python
- **Algorithms**: LBPH and Haar-based algorithms
- **Python Packages**: OpenCV, Skimage, Numpy, Tkinter, simpleaudio

## Screenshots
![Screenshot]()

## Real-world Applications

- Industrial warehouses
- Banking systems
- Jewelry shops
- Any setting requiring enhanced surveillance

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/drahulsingh/Cypher-Cam.git
   cd Cypher-Cam
   ```

2. Install the required packages:
   ```bash
   pip install opencv-python-headless numpy scikit-image simpleaudio
   ```

## Usage
- To run the application, execute the following command:

```bash
python main.py
```

## Dark Mode
The application includes a dark mode feature that can be toggled using the button at the top-right corner of the main window. When dark mode is activated, the UI colors switch to a darker theme, and the toggle button text changes to "Light Mode". Deactivating dark mode reverts to the light theme, and the button text changes back to "Dark Mode".

## Acknowledgements

This project was made possible thanks to the following resources and contributions:
- OpenCV for image processing and motion detection.
- NumPy for numerical operations.
- Scikit-Image for advanced image processing techniques.
- SimpleAudio for audio handling.
- The contributors and maintainers of the Python libraries used in this project.
- Special thanks to the open-source community for providing tools and frameworks that facilitated the development of Cypher-Cam.

## Files and Folders
- `find_motion.py`: Handles motion detection.
- `haarcascade_frontalface_default.xml`: XML file for Haar Cascade face detection.
- `identify.py`: Implements the main functionality for identification.
- `in_out.py`: Manages in/out tracking.
- `just_for_test.py`: Contains test functions.
- `main.py`: Main application script.
- `mn.png`: Application icon.
- `model.yml`: YAML file for model configuration.
- `motion.py`: Handles noise detection.
- `record.py`: Manages recording functionality.
- `rect_noise.py`: Handles rectangular noise detection.
- `spot_diff.py`: Spot difference functionality.

## Contributing
- Feel free to contribute to this project by opening issues or submitting pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For any inquiries or issues, please contact [drahulsingh](https://github.com/drahulsingh).
