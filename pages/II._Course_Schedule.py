import streamlit as st
import requests

# Create tabs for different sections of the course
tabs = st.tabs(["🍐 Weekly", "📕 Readings", "🍏 Assignment details", "🐾 Padlet","👫 Github IDs"])
                
# Content for the Schedule tab
with tabs[0]:
    st.caption("Spring 2025")
    # URL of the raw markdown file on GitHub
    markdown_url = "https://raw.githubusercontent.com/MK316/Acoustics/refs/heads/main/README.md"
    
    try:
        response = requests.get(markdown_url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        markdown_content = response.text
        st.markdown(markdown_content, unsafe_allow_html=True)
    except requests.exceptions.HTTPError as err:
        st.error(f"Failed to retrieve Markdown content: {err}")
    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")

with tabs[1]:
  st.markdown("""
  #### Acoustic analysis of English sounds

  - [Clopper et al. (2005)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3432912/) Acoustic characteristics of the vowel systems of six regional varieties of American English
  - [Maniwa & Jongman (2009)](https://kuppl.ku.edu/sites/kuppl/files/documents/publications/Maniwa_et_al_JASA2009.pdf) Acoustic characteristics of clearly spoken English fricatives
  - [Best et al. (2009)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2777975/) Discrimination of non-native consonant contrasts varying in perceptual assimilation to the listener’s native phonological system
  - [Kim (2011)](https://linguistics.stonybrook.edu/_pdf/dissertation/Mi-ran_Kim_2011_dissertation.pdf) The phonetics of stress manifestation: Segmental variation, syllable constituency and rhythm
  """)
  
with tabs[2]:
  st.write("When necessary, assignments will be detailed in this section.")

with tabs[3]:
    st.header("🐾 Files to share: on Padlet")
    st.write("This Padlet serves as a dynamic hub for our Acoustics course. Here, you'll find additional course materials, additional reading resources, and online tools. It's also a space for sharing files and submitting assignments.")
    st.components.v1.iframe("https://padlet.com/mirankim316/acoustics", width=700, height=800)

with tabs[4]:
    st.markdown("#### Github IDs")

    st.markdown("""
    +[MK316](https://github.com/mk316)  
    +[WC Jung](https://github.com/Alexwcjung)  
    +[SJ Kwon](https://github.com/kwonsungja)  
    +JH Choi
    """)
  


