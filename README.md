
# 🛰️ Smart CCTV — Tkinter-based Camera Suite

A lightweight **desktop GUI** that turns any webcam into a _smart_ CCTV system.  
Built with **Python & Tkinter**, the app offers multiple real-time monitoring modes powered by **OpenCV**.



---

## ✨ Key Features

| Mode | What it does | Where to look in code |
|------|--------------|-----------------------|
| **Noise** | Global motion detection with “MOTION / NO-MOTION” overlay | `motion.py` :contentReference[oaicite:0]{index=0} |
| **Rectangle** | Select a custom region with the mouse and monitor that area only | `rect_noise.py` :contentReference[oaicite:1]{index=1} |
| **In / Out** | Tracks movement direction to log **visitors entering / leaving**; saves snapshots in `visitors/` | `in_out.py` :contentReference[oaicite:2]{index=2} |
| **Record** | One-click video capture with date-time stamp overlay; files saved in `recordings/` | `record.py` :contentReference[oaicite:3]{index=3} |
| **Face Cascade** | Haar cascade (`haarcascade_frontalface_default.xml`) included for future face-detection features | repo tree |

The main launcher (`main.py`) ties everything together in a dark-themed Tkinter window with big icon buttons.:contentReference[oaicite:4]{index=4}

---

## 🖥️ Demo

*Live walk-through*: [YouTube Video](https://youtu.be/vNeaJacy99s)

---

## 📂 Project Layout

```text
smart_cctv/
├─ icons/                 # Button icons (PNG)
├─ visitors/
│  ├─ in/                 # Auto-saved snapshots for entries
│  └─ out/                # Auto-saved snapshots for exits
├─ recordings/            # Saved .avi clips (created at runtime)
├─ haarcascade_frontalface_default.xml
├─ main.py                # Tkinter dashboard
├─ motion.py              # Noise (global motion) detector
├─ rect_noise.py          # Region-of-interest motion detector
├─ in_out.py              # Directional people counter
├─ record.py              # Video recorder
├─ requirements.txt       # (create this – see below)
└─ README.md
````

---

## ⚙️ Installation

> **Tested on Python 3.9+**

```bash
# 1. Clone
git clone https://github.com/zeeshanaf02/smart_cctv.git
cd smart_cctv

# 2. (Optional) create a venv
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 3. Install deps
pip install opencv-python pillow
```

Add any extra packages you use to **`requirements.txt`** so others can do
`pip install -r requirements.txt`.

---

## 🚀 Running the App

```bash
python main.py
```

*The webcam feed will open in a new window; use the big icon buttons to switch modes.*

---

## 📸 Screenshots

Put screenshots (PNG/JPG) into `docs/screenshots/` and reference them like this:

```markdown
![Noise mode](docs/screenshots/noise.png)
```

---

## 🛠️ Built With

* **Python 3**
* **OpenCV** – real-time image processing
* **Tkinter** – native GUI
* **Pillow** – icon & image handling

---

## 🤝 Contributing

1. **Fork** the repo
2. Create your feature branch: `git checkout -b feat/awesome-feature`
3. Commit your changes: `git commit -m "feat: add awesome feature"`
4. **Open a pull request**

---

## 📜 License

Choose a license (e.g. MIT) and add a `LICENSE` file — open source loves clarity!

---

> *Made with ☕  by **Zeeshan***


