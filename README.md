AI Virtual Mouse
AI Virtual Mouse is a Python project that allows you to control your computer mouse using hand gestures detected by a webcam. With this project, you can move the mouse cursor, perform left-clicks, and right-clicks without actually touching the mouse.

Features
Hand Tracking: Utilizes computer vision to detect and track the movement of your hand in real-time.
Gesture Recognition: Recognizes hand gestures to perform mouse movements and clicks.
Smooth Cursor Movement: Implements algorithms to ensure smooth and accurate movement of the mouse cursor.
Adjustable Parameters: Allows customization of webcam resolution, frame rate, and other parameters for optimal performance.
Requirements
Python 3.x
OpenCV
NumPy
Mediapipe
Autopy
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/ai-virtual-mouse.git
Install the required dependencies:
Copy code
pip install opencv-python numpy mediapipe autopy
Usage
Run the main.py script:
css
Copy code
python main.py
Position your hand in front of the webcam.
Use the following gestures to control the mouse:
Moving Mode: Extend your index finger to move the mouse cursor.
Clicking Mode: Extend both your index and middle fingers to perform a left-click.
Right-click Mode: (Currently commented out in the code) Extend your thumb and index finger to perform a right-click.
Configuration
You can adjust the following parameters in the main.py file to suit your preferences:

wCam and hCam: Webcam resolution.
frameR: Frame reduction.
smoothening: Smoothening factor for cursor movement.
lastClickTime: Delay between consecutive clicks.
(Optional) Right-click Mode: Uncomment the corresponding code block in main.py to enable right-click functionality.
Contributing
Contributions are welcome! If you have any ideas for improvements or new features, feel free to submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Enjoy controlling your computer with gestures using the AI Virtual Mouse! If you encounter any issues or have questions, don't hesitate to reach out to us.
