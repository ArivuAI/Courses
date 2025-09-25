# Python Environment Setup Guide for Deep Learning

This guide will help you set up a proper Python development environment for deep learning experiments using Python 3.12 and Visual Studio Code.

## Setting Up a Virtual Environment with Python 3.12 for Deep Learning Experiments

To ensure a clean and manageable workspace for your deep learning projects, it is recommended to use a virtual environment. This allows you to isolate dependencies and avoid conflicts with other Python projects.

### Steps to Install Python 3.12

1. **Download Python 3.12:**
   - Visit the [official Python downloads page](https://www.python.org/downloads/) and select Python 3.12 for your operating system.

2. **Install Python 3.12:**
   - **Windows:** Run the installer and follow the prompts. Make sure to check "Add Python to PATH" during installation.
   - **macOS:** Download the macOS installer and run it, or use Homebrew:
     ```bash
     brew install python@3.12
     ```
   - **Linux (Ubuntu/Debian):**
     ```bash
     sudo apt update
     sudo apt install python3.12 python3.12-venv python3.12-dev
     ```

3. **If `python3.12` is not recognized:**
   - Check the installation path:
     ```bash
     which python3.12
     ```
   - If the path is not in your `PATH` environment variable, add it (replace `/opt/homebrew/bin` with your actual path if different):
     ```bash
     export PATH="/opt/homebrew/bin:$PATH"
     ```
   - On Windows, ensure the Python installation directory is added to your system's PATH environment variable (replace `C:\Python312;C:\Python312\Scripts` with your actual path if different):
     ```bash
     setx PATH "%PATH%;C:\Python312;C:\Python312\Scripts" /M
     ```

4. **Verify the installation:**
   ```bash
   python3.12 --version
   ```

### Steps to Create a Virtual Environment with Python 3.12

1. **Install `virtualenv` (if not already installed):**
   ```bash
   pip install virtualenv
   ```

2. **Create a new virtual environment using Python 3.12:**
   ```bash
   virtualenv -p python3.12 module1_dl_env
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     module1_dl_env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source module1_dl_env/bin/activate
     ```

4. **Install required packages (e.g., TensorFlow, Keras, scikit-learn):**
   ```bash
   pip install tensorflow==2.17.0 scikit-learn==1.5.0 matplotlib==3.9.0 torch==2.4.0 torchvision==0.19.0 torchaudio==2.4.0
   ```
   
   Note: Keras is now included with TensorFlow 2.17.0, so no separate installation is needed.

5. **Deactivate the environment when done with all the experiments:**
   ```bash
   deactivate
   ```

Using a virtual environment with Python 3.12 helps you manage dependencies and ensures reproducibility for your deep learning experiments.

## Using Python Notebooks in VS Code with a Custom Virtual Environment

To work with Jupyter Notebooks in Visual Studio Code and use your custom Python 3.12 virtual environment, follow these steps:

### 1. Install VS Code and Extensions

- Download and install [Visual Studio Code](https://code.visualstudio.com/).
- Open VS Code and go to the Extensions view (`Ctrl+Shift+X`).
- Search for and install the **Python** extension (by Microsoft).
- Search for and install the **Jupyter** extension (by Microsoft).

### 2. Open Your Project Folder

- Open the folder containing your Jupyter Notebook (`.ipynb`) and virtual environment.

### 3. Select the Python Interpreter

- Press `Ctrl+Shift+P` to open the Command Palette.
- Type `Python: Select Interpreter` and select it.
- Choose the interpreter from your virtual environment (e.g., `./module1_dl_env/bin/python` or `.\module1_dl_env\Scripts\python.exe`).

### 4. Enable and Use Jupyter Notebooks

- Open or create a `.ipynb` notebook file in VS Code.
- At the top right of the notebook, click on the **kernel selector** (shows the current Python version).
- Select your virtual environment as the Jupyter kernel.

### 5. Install Jupyter in the Virtual Environment (if needed)

If you haven't already installed Jupyter in your virtual environment, activate the environment and run:

```bash
pip install jupyter
```

### 6. Start Coding

- You can now run notebook cells using your selected virtual environment and installed packages.

---

**Tip:**  
If your virtual environment does not appear in the kernel list, restart VS Code after activating the environment and installing the Jupyter extension. Make sure the environment is properly set up and recognized by VS Code.

## Steps to Install Git and Download a Repository

1. **Install Git:**
    - **Windows:** Download and run the installer from [git-scm.com](https://git-scm.com/download/win).
    - **macOS:**
      ```bash
      brew install git
      ```
    - **Linux (Ubuntu/Debian):**
      ```bash
      sudo apt update
      sudo apt install git
      ```

2. **Verify Git Installation:**
    ```bash
    git --version
    ```

3. **Clone the Repository (including all subfolders):**
    ```bash
    git clone https://github.com/<reponame>/DeepLearningCourse.git
    ```

    This command will download the entire repository and its subfolders into a local directory named `DeepLearningCourse`.

4. **Navigate into the Downloaded Repository:**
    ```bash
    cd DeepLearningCourse
    ```

You can now access all files and subfolders from the repository on your local machine.

## Troubleshooting Common Issues

### Issue 1: `python3.12` command not found
- Ensure Python 3.12 is properly installed and added to your system PATH
- Try using the full path to the Python executable

### Issue 2: Virtual environment not showing in VS Code kernel selector
- Restart VS Code after creating the virtual environment
- Ensure the Python and Jupyter extensions are installed
- Try manually selecting the interpreter using `Ctrl+Shift+P` → `Python: Select Interpreter`

### Issue 3: Package installation errors
- Make sure your virtual environment is activated before installing packages
- Use `pip install --upgrade pip` to update pip to the latest version
- For permission issues on Windows, run the command prompt as Administrator

### Issue 4: Jupyter kernel not starting
- Install Jupyter in your virtual environment: `pip install jupyter ipykernel`
- Register the kernel: `python -m ipykernel install --user --name=module1_dl_env`

## Summary

Following this guide will set up a clean, isolated Python 3.12 environment for your deep learning projects with all necessary packages and VS Code integration. This setup ensures reproducibility and prevents conflicts between different projects.