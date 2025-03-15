# Fitness Tracker

This is a simple FitnessTracker app. Below is a guide on how to fork the project, install PyInstaller, and package the application.

## Fork the Project

1. **Fork the Repository**:
   - Go to the repository page on GitHub.
   - Click the "Fork" button in the top right corner to create a personal copy of the repository.

2. **Clone the Repository**:
   - Clone the repository to your local machine using the following command:
     ```bash
     git clone https://github.com/your-username/HealthTrackerV2.git
     ```

3. **Navigate to the Project Folder**:
   ```bash
   cd HealthTrackerV2

4. **Install Pyinstaller**
   ```bash
   pip install pyinstaller

5. **Package the app**
   Run this command to package to <code>dist</code>:
   ```bash
   pyinstaller --onefile --icon=favicon.ico --windowed main.py

6. **Run the app**
   Open <code>dist</code>, then just double click main.exe
   ! You can rename the file to Health Tracker or Fitness Tracker or something else.


   **PyInstaller's compatibility may vary between operating systems; particularly Unix-like OSs.**
