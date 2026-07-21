# 🤟 SignTalk AI – Real-Time Sign Language Translator

## Project Overview

SignTalk AI is an AI-powered real-time sign language translation project that uses computer vision and machine learning to recognize hand gestures through a webcam and convert recognized signs into speech.

The system uses MediaPipe Hands to detect and track hand landmarks in real time. The extracted hand landmark coordinates are processed by a trained Random Forest machine learning model to classify the detected hand gesture.

Once a sign is recognized, the system displays the predicted result on the screen and uses text-to-speech technology to provide audio output.

The project demonstrates the integration of:

- Artificial Intelligence
- Machine Learning
- Computer Vision
- Hand Landmark Detection
- Real-Time Gesture Recognition
- Text-to-Speech

## ✨ Features

- Real-time hand detection using a webcam
- Hand landmark tracking using MediaPipe
- Machine learning-based gesture classification
- Random Forest classification model
- Real-time prediction of recognized signs
- Text-to-speech output
- Visual display of recognized signs
- Custom dataset collection
- Custom machine learning model training
- Live webcam processing
- Speech output cooldown to prevent repeated announcements

## 🧠 How the AI System Works

The project follows a three-stage machine learning pipeline:

```text
Webcam
   │
   ▼
Hand Detection
   │
   ▼
MediaPipe Hand Landmarks
   │
   ▼
Extract X, Y, Z Coordinates
   │
   ▼
Random Forest Model
   │
   ▼
Recognized Sign
   │
   ▼
Text-to-Speech
   │
   ▼
Audio Output
```

## 📊 Machine Learning Pipeline

### 1. Data Collection

The `collect.py` script captures hand landmark data using the computer's webcam.

MediaPipe detects the hand and extracts the 3D coordinates of the hand landmarks.

The collected data is stored in:

```text
hand_data.csv
```

Each data sample contains the hand landmark coordinates along with the corresponding sign label.

### 2. Model Training

The `train.py` script loads the collected dataset and trains a Random Forest Classifier.

The process includes:

1. Loading the hand landmark dataset.
2. Separating features and labels.
3. Splitting the data into training and testing sets.
4. Training the Random Forest model.
5. Evaluating the model using accuracy.
6. Saving the trained model.

The trained model is saved as:

```text
model.p
```

### 3. Real-Time Recognition

The `main.py` script loads the trained machine learning model.

The webcam captures live video frames.

MediaPipe detects the user's hand and extracts the hand landmark coordinates.

These coordinates are passed to the trained Random Forest model for prediction.

The predicted sign is displayed on the screen and converted into speech using the text-to-speech engine.

## 📂 Project Structure

```text
SignTalk-AI-Real-Time-Sign-Language-Translator/
│
├── main.py
├── train.py
├── collect.py
├── model.p
├── hand_data.csv
├── requirements.txt
└── README.md
```

## 🛠️ Technologies Used

- Python
- OpenCV
- MediaPipe
- NumPy
- Pandas
- Scikit-learn
- Random Forest Classifier
- Pyttsx3
- Machine Learning
- Computer Vision
- Artificial Intelligence

## 📦 Installation

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the Project Folder

```bash
cd SignTalk-AI-Real-Time-Sign-Language-Translator
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

## ▶️ How to Run the Project

### Option 1: Use the Existing Trained Model

If you already have:

```text
model.p
```

and:

```text
hand_data.csv
```

you can directly run:

```bash
python main.py
```

Make sure your computer has a working webcam.

The application will open the camera and begin detecting hand gestures.

## 🧪 Creating a New Dataset

If you want to add new gesture classes or create a new dataset, run:

```bash
python collect.py
```

The program will ask you to enter the name of the sign you want to record.

The webcam will then open.

Press:

```text
s
```

to save a hand landmark sample.

Press:

```text
q
```

to stop data collection.

The collected data will be saved to:

```text
hand_data.csv
```

## 🧠 Training the AI Model

After collecting the required training data, run:

```bash
python train.py
```

The training script will:

1. Load `hand_data.csv`.
2. Split the data into training and testing sets.
3. Train a Random Forest Classifier.
4. Calculate the model accuracy.
5. Save the trained model as `model.p`.

After training is complete, run:

```bash
python main.py
```

to start real-time sign recognition.

## 🔊 Text-to-Speech

When the AI recognizes a sign, the predicted result is sent to the text-to-speech engine.

The system then produces audio output using:

```text
pyttsx3
```

A cooldown mechanism is implemented to reduce repeated speech output when the same sign remains visible in front of the camera.

## 🎮 Controls

While running `main.py`:

### Press `c`

Resets the current recognized sign and allows the system to recognize a new sign.

### Press `q`

Closes the application and stops the webcam.

## 🔄 Complete Workflow

```text
1. Collect Hand Data
        │
        ▼
   collect.py
        │
        ▼
  hand_data.csv
        │
        ▼
2. Train AI Model
        │
        ▼
    train.py
        │
        ▼
     model.p
        │
        ▼
3. Real-Time Recognition
        │
        ▼
     main.py
        │
        ▼
    Webcam Input
        │
        ▼
 MediaPipe Hand Detection
        │
        ▼
 Landmark Extraction
        │
        ▼
 Random Forest Prediction
        │
        ▼
 Recognized Sign
        │
        ▼
 Text-to-Speech Output
```

## 🚀 Future Improvements

- Support for a larger sign vocabulary
- Continuous sentence formation
- Word prediction and language processing
- Improved gesture classification
- Support for multiple hands
- Improved model accuracy
- Real-time translation into complete sentences
- Graphical user interface
- Mobile application integration
- Cloud-based AI processing
- Support for additional sign languages

## ⚠️ Project Scope

SignTalk AI is an educational AI and computer vision project demonstrating real-time hand gesture recognition and speech output.

The current system recognizes gestures based on the custom dataset used to train the machine learning model. The recognition capabilities depend on the quality and variety of the training data.

## 👨‍💻 Author

**Rizwa Hassan**

Computer Science Student
