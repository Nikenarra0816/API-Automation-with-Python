import tkinter as tk
import subprocess

# Function to run tests using pytest
def run_tests():
    # Jalankan pytest di terminal dan dapatkan hasilnya
    result = subprocess.run(['pytest', '--maxfail=1', '--disable-warnings', '-q'], capture_output=True, text=True)
    
    # Run pytest in terminal and get the result
    output_text.set(result.stdout)
    error_text.set(result.stderr)

# Creating the main window of a Tkinter application
root = tk.Tk()
root.title("API Test Automation - Niken Arra")

# Add labels to display test results
output_text = tk.StringVar()
output_label = tk.Label(root, textvariable=output_text, justify=tk.LEFT, wraplength=400)
output_label.pack(pady=20)

error_text = tk.StringVar()
error_label = tk.Label(root, textvariable=error_text, justify=tk.LEFT, wraplength=400, fg="red")
error_label.pack(pady=20)

# Add a button to run the test
run_button = tk.Button(root, text="Run API Tests - Niken", command=run_tests)
run_button.pack(pady=10)

# Running a Tkinter application
root.mainloop()
