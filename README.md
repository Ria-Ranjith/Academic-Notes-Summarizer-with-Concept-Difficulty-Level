# 📚 Academic Notes Summarizer with Concept Difficulty Level

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Gemini](https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

An AI-powered application that summarizes academic notes and assesses concept difficulty levels using Google's Gemini API.

## ✨ Features

- **Smart Summarization**: Condenses lengthy notes into key points
- **Difficulty Assessment**: Rates concepts as Easy/Medium/Hard
- **Flashcard Generation**: Creates Q&A pairs for study
- **File Support**: Processes PDFs and DOCX files
- **Privacy Focused**: Runs locally with your API key

## 🚀 Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/Ria-Ranjith/Academic-Notes-Summarizer-with-Concept-Difficulty-Level.git
Set up environment

bash
Copy
cd Academic-Notes-Summarizer-with-Concept-Difficulty-Level
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
pip install -r requirements.txt
Configure API

Get your Google API key from Google AI Studio

Create .env file:

bash
Copy
echo "GOOGLE_API_KEY=your_key_here" > .env
Run the app

bash
Copy
streamlit run app.py
🛠️ Project Structure
Copy
Academic-Notes-Summarizer/
│
├── app.py              # Main application logic
├── utils.py            # File parsing and processing
├── requirements.txt    # Python dependencies
└── .gitignore          # Sensitive files exclusion
📝 Example Output
Input Notes:

Copy
The mitochondria is the powerhouse of the cell. It generates ATP through cellular respiration..."
Output:

Copy
SUMMARY:
- Mitochondria are cell organelles that produce energy (ATP)
- ATP generation occurs through cellular respiration

FLASHCARDS:
1. Q: What is the function of mitochondria?
   A: To produce ATP (cellular energy)

DIFFICULTY LEVEL: Easy

🤝 Contributing
Fork the project

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some amazing feature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

📜 License
Distributed under the MIT License. See LICENSE for more information.

📧 Contact
Ria Ranjith - riaranjith25@gmail.com

Project Link: https://github.com/Ria-Ranjith/Academic-Notes-Summarizer-with-Concept-Difficulty-Level


### Key Features of This README:
1. **Visual Badges**: Shows technologies used at a glance
2. **Clear Installation Steps**: With copy-paste ready commands
3. **Project Structure**: Visual tree of important files
4. **Example I/O**: Demonstrates the app's value
5. **Contributing Guide**: Encourages collaboration
6. **Responsive Formatting**: Looks good on GitHub mobile and desktop

