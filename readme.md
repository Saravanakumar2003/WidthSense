# WidthSense WebApp

This Flask-based web application allows users to upload a 2D profile dataset (`x`, `y` coordinates in Excel format) and calculates the **horizontal width** of the profile at evenly spaced **Y-levels** using linear interpolation. It outputs a downloadable `.xlsx` file containing width values for each Y-level.

![Python](https://img.shields.io/badge/Built%20With-Python-blue)  
![Flask](https://img.shields.io/badge/Framework-Flask-red)  
![Excel](https://img.shields.io/badge/Input-Excel%20(.xlsx)-green)  

## 🚀 Features

- 📁 Upload `.xlsx` file containing 2D curve data (`x` and `y` columns).
- ⚙️ Automatically calculates width at every 0.1 unit step in Y-levels.
- 📤 Download the result as an Excel file: `width_vs_y_TIMESTAMP.xlsx`.
- 🧠 Smart Y-range detection and interpolation using `SciPy`.
- 🖥️ Minimal, clean frontend using `Flask` and `HTML`.

---
## 🖼️ Demo Screenshot

> **Note:** The web app is designed to be simple and user-friendly. Below is a screenshot of the interface.

![Web Interface](/static/assets/img/web_1.png)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/width-y-webapp.git
cd width-y-webapp
```

### 2. Install Required Packages

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## ⚙️ Usage

### 1. Start the Flask Server

```bash
python app.py
```

The app will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000)

### 2. Upload and Process

- Upload your `.xlsx` file with `x` and `y` columns.
- The tool processes it, computes widths, and downloads the output file.

## Deployment

The deployment is configured for **PythonAnywhere**. You can deploy it easily by following the instructions on the Pythonanywhere platform.

#### Deployed URL: [https://widthsense.pythonanywhere.com](https://widthsense.pythonanywhere.com)

---

# Widthsense GUI

A simple yet powerful Python desktop application that calculates the **horizontal widths of a 2D curve** at multiple vertical (Y) levels from an Excel dataset. Designed with a user-friendly GUI using Tkinter, this tool is ideal for engineers, scientists, and researchers working with geometric profiles, sensor data, or topographic curves.

![Python](https://img.shields.io/badge/Built%20With-Python-blue)  
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)  
![GUI](https://img.shields.io/badge/GUI-Tkinter-orange)  

## 🚀 Features

- 📁 **Input**: Upload `.xlsx` Excel files with `x` and `y` columns representing a 2D shape or curve.
- 📐 **Computation**: Calculates horizontal width at evenly spaced `Y-levels` using linear interpolation.
- 📊 **Output**: Exports the results as an Excel file with `Y-level` vs `Width` data.
- 💡 **Error Handling**: Displays clean error messages and logs issues in a `app.log` file.
- 🖥️ **GUI**: Clean and responsive user interface using `Tkinter`.


## 📦 Installation For Exe App

> 💡 Requires Python 3.7 or higher.

1. **Clone this repository:**

```bash
git clone https://github.com/Saravanakumar2003/Widthsense.git
cd widthsense
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

## ⚙️ Run the Application

```bash
cd app
python main.py
```

A GUI will pop up for file selection and processing.

3. **Create Executable (Optional):**
4. If you want to create an executable file for distribution, you can use `PyInstaller`:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --add-data "python38.dll;." main.py
```

This will create a standalone executable in the `dist` folder. You can run this executable without needing Python installed on the target machine.

## Download Executable

Go to [Github Releases](https://github.com/Saravanakumar2003/WidthSense/releases) and download the latest version of the executable file. 

Windows may flag the executable as unrecognized. You can ignore this warning and run the file. The executable is safe to use.

## 🖼️ Screenshots

> **Note:** The GUI is designed to be simple and user-friendly. Below are some screenshots of the interface.

![GUI ScreenShot](/static/assets/img/gui_1.png)
---

## 🌐 Folder Structure

```plaintext
Widthsense/
├── app.py                # Main Flask app
├── app/                 # GUI app folder
│   ├── main.py           # Main Tkinter app
│   ├── python38.dll      # Python DLL for Tkinter (Used for making exe file)
│   ├── app.log           # Log file for errors and exceptions
├── templates/
│   └── index.html        # HTML form for upload
├── uploads/              # Uploaded Excel files
├── outputs/              # Output Excel files
├── requirements.txt      # Dependencies
├── static/               # Static files
│   ├── assets/           # Assets folder
├── vercel.json          # Vercel deployment config
└── README.md             # This file
```

## 🔧 How It Works

Given a set of 2D coordinates (x, y) representing a closed or open profile:

1. The tool sorts the data by X-axis.
2. It calculates evenly spaced horizontal slices across the Y-axis.
3. For each Y-level:
   - It finds where the curve intersects that level (by interpolation).
   - Calculates the distance between the leftmost and rightmost X-crossings — this is the **width**.
4. The results are stored in a new Excel sheet.
5. The user can download the output file.

## 📂 Input Format

- Input must be an **Excel file (.xlsx)**.
- It should contain two columns named exactly:
  - `x` – X-coordinates (float)
  - `y` – Y-coordinates (float)

Example:

| x     | y     |
|-------|-------|
| 1.0   | 2.3   |
| 1.5   | 2.5   |
| 2.0   | 2.1   |
| ...   | ...   |

## ✅ Output Format

- An Excel file named `output.xlsx` containing:

| y_level | width  |
|---------|--------|
| 1.0     | 2.45   |
| 1.1     | 2.38   |
| ...     | ...    |

If no valid width exists at a particular level, `width` is left blank.

## 📂 Log Files

- Errors and exceptions are logged to a file named `app.log` in the working directory.
- This file can be useful for debugging and understanding any issues that arise during execution.

## 🧠 Use Cases

- Civil Engineering: River cross-sections, channel widths.
- Environmental Science: Sediment profiles or terrain analysis.
- Medical Imaging: Analyzing anatomical cross-sections.
- Sensor-Based IoT: Shape profiling from scanning data.
- Geometry Education: Teaching curve behavior and properties.

## 📜 License

This project is licensed under the **MIT License**.  See the [LICENSE](LICENSE) file for more details.

## 🤝 Contributions

Pull requests are welcome! For major changes, please open an issue first  to discuss what you would like to change.

## 🙋‍♂️ Need Help?

Open an [Issue](https://github.com/your-username/width-calculation-tool/issues)  or reach out via [GitHub Discussions](https://github.com/your-username/width-calculation-tool/discussions).
