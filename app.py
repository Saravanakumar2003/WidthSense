import os
import pandas as pd
import numpy as np
from flask import Flask, render_template, request, send_file
from scipy.interpolate import interp1d
from datetime import datetime

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_FOLDER'] = 'outputs'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

def calculate_widths(filepath):
    df = pd.read_excel(filepath)
    x = df['x'].values
    y = df['y'].values

    sorted_indices = np.argsort(x)
    x = x[sorted_indices]
    y = y[sorted_indices]

    y_min = np.floor(min(y) * 10) / 10
    y_max = np.ceil(max(y) * 10) / 10
    y_levels = np.arange(y_min, y_max + 0.1, 0.1)

    results = []

    for level in y_levels:
        crossings = []
        for i in range(len(y) - 1):
            if (y[i] - level) * (y[i+1] - level) <= 0 and y[i] != y[i+1]:
                x_interp = x[i] + (level - y[i]) * (x[i+1] - x[i]) / (y[i+1] - y[i])
                crossings.append(x_interp)
        if len(crossings) >= 2:
            width = max(crossings) - min(crossings)
        else:
            width = None
        results.append({"y_level": round(level, 1), "width": width})

    output_df = pd.DataFrame(results)
    output_file = os.path.join(app.config['OUTPUT_FOLDER'], f"width_vs_y_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx")
    output_df.to_excel(output_file, index=False)
    return output_file

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('file')
        if file and file.filename.endswith('.xlsx'):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            output_path = calculate_widths(filepath)
            return send_file(output_path, as_attachment=True)
        else:
            return "Invalid file format. Upload an Excel (.xlsx) file.", 400
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    