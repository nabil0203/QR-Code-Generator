# ⛆ QR Code Generator from Input File

A simple Python script that reads a **Text/URL** and a **File name** from a Text file. Then generates a QR code and saves it as an image.

---

## 📝 Input Format

The input should be placed in a file named `input.txt` with **two lines only**:

- **Line 1** – The text or URL to encode into the QR code  
- **Line 2** – The image file name (with `.png` or `.jpg` extension)

### 🔹 Example `input.txt`:
```
https://youtube.com
YT.png
```

---


## 🚀 How to Run

### 1. Clone or Download This Repository

```
git clone https://github.com/nabil0203/QR_Code_Generator.git
cd QR_Code_Generator
```

### 2. Install Required Library
```
pip install qrcode[pil]
```

### 3. Prepare Your Input
- Create or edit the `input.txt` file in the same folder.

### 4. Run the Script
```
python qrCode_generator.py
```

✅ A QR code image (like YT.png) will be generated and saved in the current directory.

---

## 📂 Project Structure
```
  ├── input.txt                   # Input with text/URL and filename 
  ├── qrCode_generator.py         # Python code to generate QR 
  └── YT.png                      # Output QR code image
```




## 📦 Requirements
- Python 3.13
- Qr Code Library:- pip install qrcode[pil]



## ⚠️ Notes
- Ensure the input file has no extra blank lines.
- The second line must end with .png or .jpg.
- The image will be saved in the current directory.



## 🙌 Contributing
- Pull requests and suggestions are welcome!
- Feel free to open issues or share ideas to improve this project.

