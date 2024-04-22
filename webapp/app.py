import streamlit as st
import streamlit_scrollable_textbox as stx 
from utils import text_preprocessing, getResults
import re

# Set page config
st.set_page_config(
    page_title="S^2",
    page_icon='🧐',
)

# Title and description
st.title("🧐 Subtitle Search Engine")
st.markdown("""
    This tool helps you find subtitles based on characters or Incidents from a show or movie. 
    Enter character names or Incidents separated by commas in the text area below.
""")

# Take query
query = st.text_area("Enter character names separated by commas", height=100)  # Increase text area height
submit = st.button("Search")

# Initialize session state
if 'search_state' not in st.session_state:
    st.session_state['search_state'] = False

if (submit or st.session_state['search_state']) and re.search(r'\w+', query):
    st.session_state.search_state = True
    
    # Preprocess the query
    text = text_preprocessing(query, 'stemming')
    
    # Get results
    names = getResults(text, 'stemming')
    
    # Display results as a list
    st.header("Matching Names")
    st.write(names)
    
    # Select a name from the list
    selected_name = st.selectbox(label="Select a Name", options=names, index=0)
    
    # Button to show subtitles
    flag = st.button('Show Subtitles')
    
    if flag:
        st.header(f"Subtitles for {selected_name}")
        if re.search(r'\w+', selected_name):
            with open(r'M:\innomatics\project4\Project\transcripts\{}.srt'.format(selected_name), 'r', encoding='utf-8') as file:
                content = file.read()

            stx.scrollableTextbox(content, height=500)
            
            # Download button for the transcript
            st.download_button(
                label="⬇️ Download Transcript", data=content, file_name=f"{selected_name}_transcript.txt", mime="text/plain",
                help='Click on this button to download the transcript'
            )
