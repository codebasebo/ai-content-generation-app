import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper

# Set OpenAI API key
os.environ['OPENAI_API_KEY'] = apikey

# App Framework
st.title('🎬 Content Generation App')

# Input prompt
prompt = st.text_input('Enter your prompt here:', placeholder="e.g., Artificial Intelligence")

# Validate prompt
if not prompt or len(prompt.strip()) < 3:
    st.warning("Please enter a valid prompt with at least 3 characters.")
    st.stop()

# Allow user to adjust temperature
temperature = st.slider("Adjust creativity (temperature):", min_value=0.1, max_value=1.0, value=0.7)

# Essay Template
essay_template = PromptTemplate(
    input_variables=['topic'],
    template="""
    Write a detailed and well-structured essay about the topic: {topic}.
    """
)

# Script Template
script_template = PromptTemplate(
    input_variables=['title', 'wikipedia_research'],
    template="""
    You are a professional scriptwriter. Write a detailed, engaging, and well-structured script based on the following title: **{title}**.

    **Research Context:**
    {wikipedia_research}

    **Instructions:**
    1. **Introduction:**
       - Set the scene clearly and introduce the main characters or central ideas.
       - Establish the tone (e.g., dramatic, comedic, suspenseful) and setting (time and place).
       - Hook the audience with an intriguing opening.

    2. **Body:**
       - Develop at least three key scenes or sections.
       - Each scene should include:
         - Dialogue: Natural and character-driven conversations.
         - Action: Clear descriptions of character actions and events.
         - Conflict or tension: Keep the audience engaged with challenges or obstacles.
       - Ensure smooth transitions between scenes.

    3. **Conclusion:**
       - Resolve the main conflict or story arc.
       - Leave the audience with a memorable ending or thought-provoking message.

    **Additional Guidelines:**
    - Incorporate the Wikipedia research naturally into the script to add depth and authenticity.
    - Ensure the script is creative, engaging, and easy to follow.
    - Use proper script formatting (e.g., character names in uppercase for dialogue, scene descriptions in present tense).

    **Output:**
    Write the script in proper screenplay format, adhering to industry standards.
    """
)

# Memory for the essay chain
essay_memory = ConversationBufferMemory(input_key='topic', memory_key='essay_history')

# Memory for the script chain
script_memory = ConversationBufferMemory(input_key='title', memory_key='script_history')

# Initialize the OpenAI LLM
llm = OpenAI(temperature=temperature)

# Create LLM chains
essay_chain = LLMChain(llm=llm, prompt=essay_template, verbose=True, output_key="essay", memory=essay_memory)
script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True, output_key="script", memory=script_memory)

# Initialize Wikipedia API wrapper
wiki = WikipediaAPIWrapper()

# Show results if prompt is not empty
if prompt:
    try:
        # Run the essay chain to generate a title
        with st.spinner("Generating essay..."):
            title = essay_chain.run(prompt)
        
        # Fetch Wikipedia research based on the prompt
        with st.spinner("Fetching Wikipedia research..."):
            wikipedia_research = wiki.run(prompt)
            if not wikipedia_research:
                st.warning("No Wikipedia research found for the given prompt. Proceeding without research.")
                wikipedia_research = "No additional research available."
        
        # Run the script chain to generate the script
        with st.spinner("Generating script..."):
            script = script_chain.run(title=title, wikipedia_research=wikipedia_research)
        
        # Display the generated title and script
        st.write("### Generated Title:")
        st.write(title)
        
        st.write("### Generated Script:")
        st.write(script)
         
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.warning("Please enter a prompt to generate content.")

# Display memory and research history
with st.expander("Essay Conversation History"):
    st.info(essay_memory.buffer)

with st.expander("Script Conversation History"):
    st.info(script_memory.buffer)

with st.expander("Wikipedia Research"):
    if wikipedia_research:
        st.info(wikipedia_research)
    else:
        st.info("No research available yet.")