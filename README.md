# Web Automation & Computer Vision Toolkit 🛠️

A collection of utility scripts designed for web automation, DOM manipulation, accessibility testing, and optical character recognition (OCR). This repository serves as an educational toolkit to understand how automated browsers interact with web elements and how computer vision processes visual text data.

## 📁 Repository Structure

```text
├── web_modifier.py        # Automates browsers and manipulates DOM elements via JS injection
├── image_ocr_reader.py    # Processes images and extracts text using OpenCV and Tesseract OCR
└── requirements.txt       # Python library dependencies
```

---

## 🚀 Features

### 1. Web Modifier & Browser Automation (`web_modifier.py`)
* **Dynamic JS Injection:** Demonstrates how to programmatically interact with and modify the Document Object Model (DOM) in real-time.
* **Accessibility Simulation:** Simulates user-agent overrides and removes obstructive web overlays (like persistent banners or modals) to restore clean reading layouts.
* **Automated Scraper Base:** Uses Selenium to handle dynamic rendering smoothly.

### 2. Image Processing & OCR (`image_ocr_reader.py`)
* **Image Pre-processing:** Converts images to grayscale and applies thresholding matrices via OpenCV to eliminate background noise.
* **Text Extraction:** Utilizes Tesseract OCR engine to read characters from processed local images.
* **Security & Testing:** Can be used to benchmark the readability of internal captchas, anti-spam mechanisms, or to digitize physical text documents.

---

## 🛠️ Installation & Setup

### Prerequisites
1. **Python 3.8+** installed on your system.
2. **Tesseract OCR Engine** installed locally (required for the OCR script).
   * *Ubuntu/Debian:* `sudo apt install tesseract-ocr`
   * *macOS:* `brew install tesseract`
   * *Windows:* Download the installer from the official GitHub binaries.

### Step-by-Step Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com
   cd YOUR-REPO-NAME
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 How to Use

### Running the Web Modifier
To execute the automated browser session and DOM cleanup script:
```bash
python web_modifier.py
```

### Running the OCR Reader
To test image processing and character recognition, uncomment the usage lines at the bottom of the script and provide a valid image path, then run:
```bash
python image_ocr_reader.py
```

---

## ⚖️ Disclaimer & Ethical Use

This repository is strictly intended for **educational, research, and legal testing purposes**. The scripts provided demonstrate foundational engineering concepts behind web automation and computer vision. 

The author does not condone, support, or encourage the use of these tools to bypass commercial paywalls, disrupt active security mechanisms, scrape data in violation of platform Terms of Service, or perform any unauthorized activities. Always ensure you have explicit permission before running automation scripts against external infrastructure.
