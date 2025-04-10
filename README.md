# 🚀 DocGenie - AI Code Documentation Generator

DocGenie is a classy, responsive, and intuitive web-based tool that automatically generates documentation for code using AI. Whether you're working with Python, JavaScript, Java, C++, or C#, DocGenie will analyze your code and return clean, structured documentation — ready for export as a PDF.

---

## 🌟 Features

- 🧒 **AI-powered Documentation**: Auto-generates code documentation using a backend language model.
- 💾 **Download as PDF**: Export your documentation with a single click.
- 🌐 **Responsive Design**: Works beautifully across desktop, tablet, and mobile devices.
- 🎯 **Multi-language Support**: Supports Python, JavaScript, Java, C++, and C#.
- 🎨 **Elegant UI**: Minimalist white theme with modern components and animated loaders.

---

## 📁 Project Structure

```
DocGenie/
├── static/
│   └── main.html          # Frontend interface
├── docgenie.py            # Backend Flask server
└── README.md              # This file
```

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/docgenie.git
cd docgenie
```

### 2. Install Dependencies

Make sure Python 3.7+ is installed.

```bash
pip install flask openai
```

> ✅ Optionally, add your OpenAI key to `docgenie.py` if it's using GPT for doc generation.

### 3. Run the Flask App

```bash
python docgenie.py
```

### 4. Open in Browser

Navigate to:

```
http://localhost:5000
```

You’ll see the DocGenie UI where you can paste code, generate documentation, and download it as a PDF.

---

## 💻 Technologies Used

| Frontend                | Backend              |
|------------------------|----------------------|
| HTML5, CSS3, JavaScript | Python (Flask)       |
| Highlight.js (syntax)  | OpenAI API (optional)|
| html2pdf.js (PDF export)|                      |
| Marked.js (Markdown)   |                      |

---

## 🗈️ Preview

![DocGenie Screenshot](https://via.placeholder.com/800x400.png?text=DocGenie+Preview)

---

## 📅 How It Works

1. **Paste code** into the textarea.
2. Choose the **language** from the dropdown.
3. Click **Generate Documentation**.
4. View the AI-generated documentation instantly.
5. Click **Download 💽** to save it as a PDF.

---

## 📌 Notes

- You can customize the backend (`docgenie.py`) to connect with any AI model or local NLP engine.
- PDF files are named as `DocGenie_Documentation.pdf` by default.

---

## 🙌 Acknowledgments

- [OpenAI](https://openai.com) for AI documentation generation.
- [html2pdf.js](https://github.com/eKoopmans/html2pdf) for client-side PDF conversion.
- [Highlight.js](https://highlightjs.org/) for syntax highlighting.

---

## 📃 License

This project is licensed under the MIT License. Feel free to use and modify for personal or commercial projects.

---

## 💡 Future Improvements

- Add support for uploading code files.
- Store PDF history per session.
- Support dark/light theme toggle.
- Include diagrams for class structures or flow.

---

### Made with 💙 by Uday

