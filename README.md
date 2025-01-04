# AI Content Generation App 🎬

Welcome to the **AI Content Generation App**! This Streamlit-based application leverages the power of **LangChain** and **OpenAI** to generate essays and scripts based on user prompts. It also integrates **Wikipedia research** to add depth and authenticity to the generated content.

---

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Project Structure](#project-structure)
5. [Dependencies](#dependencies)
6. [Contributing](#contributing)
7. [License](#license)

---

## Features ✨

- **Essay Generation**: Generate detailed and well-structured essays on any topic.
- **Script Generation**: Create engaging and professional scripts with proper formatting.
- **Wikipedia Integration**: Automatically fetch relevant Wikipedia research to enhance the content.
- **Conversation Memory**: Track and display the history of generated content for both essays and scripts.
- **User-Friendly Interface**: Built with **Streamlit** for an intuitive and interactive experience.

---

## Installation 🛠️

### Prerequisites
- Python 3.8 or higher
- An OpenAI API key (get it from [OpenAI](https://platform.openai.com/))

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/codebasebo/ai-content-generation-app.git

   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:
   - Create a file named `apikey.py` in the root directory.
   - Add your OpenAI API key to the file:
     ```python
     apikey = "your-openai-api-key-here"
     ```

4. Run the app:
   ```bash
   streamlit run app/main.py
   ```

5. Open your browser and navigate to `http://localhost:8501` to access the app.

---

## Usage 🚀

1. **Enter a Prompt**:
   - Type a topic or idea into the input box (e.g., "Artificial Intelligence").

2. **Generate Content**:
   - The app will:
     - Generate an essay title.
     - Fetch relevant Wikipedia research.
     - Create a detailed script based on the title and research.

3. **View Results**:
   - The generated title and script will be displayed on the screen.
   - You can expand sections to view:
     - Conversation history for essays and scripts.
     - Wikipedia research used in the script.

---


## Dependencies 📦

The project relies on the following Python libraries:
- **Streamlit**: For building the web app.
- **LangChain**: For chaining prompts and generating content.
- **OpenAI**: For accessing the GPT models.
- **Wikipedia-API**: For fetching Wikipedia research.

You can install all dependencies using:
```bash
pip install -r requirements.txt
```

---

## Contributing 🤝

We welcome contributions! Here’s how you can help:
1. Fork the repository.
2. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

---

## Acknowledgments 🙏

- **OpenAI** for providing the powerful GPT models.
- **LangChain** for simplifying prompt chaining and memory management.
- **Streamlit** for making it easy to build interactive web apps.

---

Enjoy using the **Content Generation App**! If you have any questions or feedback, feel free to open an issue or reach out to the maintainers. 🚀