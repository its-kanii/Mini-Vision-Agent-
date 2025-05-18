# 🧠 Mini Vision Agent — Real-Time Object Detection with Voice Feedback

A simple but powerful Python-based AI agent that uses YOLOv8 for real-time object detection and provides audio feedback using text-to-speech (TTS). Designed as part of my Data Science learning journey, this project demonstrates how computer vision can assist in real-world accessibility use cases like blind assistance.

## 📸 Demo

→ Real-time detection through webcam
→ Object labels are spoken aloud using TTS
→ Ideal for educational, accessibility, and computer vision projects

---

## 🧰 Tech Stack

* 🧠 YOLOv8 (Ultralytics)
* 📸 OpenCV (video capture and visualization)
* 🗣️ pyttsx3 (offline TTS engine)
* 🐍 Python 3.x

---

## 🛠️ Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/its-kanii/mini-vision-agent.git
cd mini-vision-agent
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Download the YOLOv8 model:
   Place the yolov8n.pt model file in the project directory.
   Download from: [https://github.com/ultralytics/ultralytics#models](https://github.com/ultralytics/ultralytics#models)

4. Run the agent:

```bash
python vision_agent.py
```

---

## 📂 File Structure

```
mini-vision-agent/
├── vision_agent.py        # Main script to run the mini vision agent
├── yolov8n.pt             # YOLOv8 model (download separately)
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

---

## ✅ Features

* Real-time object detection using webcam
* Works offline (no cloud API)
* Gives audio feedback for every detected object
* Lightweight and beginner-friendly

---

## 🎯 Use Cases

* Accessibility assistance for the visually impaired
* Educational demos for computer vision beginners
* IoT or surveillance applications (customizable)

---

## 📌 Example Output

```bash
Detected: person
Detected: chair
Speaking: I see a person
Speaking: I see a chair
```

---

## 🤝 Contributions

Pull requests are welcome! If you have ideas for improving this mini agent (e.g., multilingual TTS, image logging, object tracking), feel free to open an issue or PR.

---

## 📜 License

This project is licensed under the MIT License.
