# 🧮 Linear Regression GUI App

A sleek, educational desktop app to **train your own Linear Regression model from scratch** — using nothing but Python, Tkinter, and NumPy. Perfect for learning how gradient descent actually works under the hood 🚀

---

## ✨ Features

✅ Load CSV datasets with ease  
✅ Choose your own target column  
✅ Run training with customizable epochs  
✅ View live training loss updates  
✅ Save model weights and bias automatically  
✅ Experience the retro vibes of a Tkinter interface

---

## 🧠 Tech Stack

- **Python 3.x**
- **Tkinter** – for GUI
- **NumPy** – matrix ops and math magic
- **scikit-learn** – just for scaling (`StandardScaler`)

---

## 🗂️ File Structure

📦 root/ ├── app.py # GUI logic ├── main.py # Entry point ├── model.py # Linear Regression from scratch ├── util_func.py # Utility functions (timing, saving) ├── Data/ │ └── data.py # (You need to create this) ├── weights/ │ └── weights.txt # Saved weights and bias


---

## 🚀 Getting Started

1. **Clone this repo**  
   ```bash
   git clone https://github.com/your-username/linear-regression-gui.git
   cd linear-regression-gui



## 🧪 How It Works
- **Enter the path to your CSV file (e.g., data.csv)**

- **Input the name of the target column (e.g., Revenue)**

- **Set the number of training epochs**

- **Hit “Start Training” and watch the magic happen in the console**

- **Model weights will be saved in /weights/weights.txt**

## Example
- **Dataset path**: coffee_shop.csv
- **Target column**: Daily_Revenue
- **Epochs**: 100

## 🧃 Credits
- **Open-sourced under the MIT License.**
- **Feel free to fork, star ⭐, or contribute!**