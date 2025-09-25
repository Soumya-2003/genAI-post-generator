## Post Writer - AI-Powered LinkedIn Post Generator
### Overview
Post Writer is an intelligent content generation tool that helps LinkedIn influencers maintain their unique writing style while creating new posts. 
By analyzing an influencer's past LinkedIn posts, the tool extracts key topics and uses few-shot learning to generate new content that matches their distinctive 
voice and style.

### Features
- Style Analysis: Analyzes past LinkedIn posts to understand writing style

- Topic Extraction: Automatically identifies key topics from existing content

- AI-Powered Generation: Creates new posts using few-shot learning

- Customizable Output: Control post length and language (English, Hindi, Hinglish)

- Responsive Design: Works seamlessly across desktop and mobile devices

### Technical Architecture
#### Stage 1: Content Analysis
- Collect and process LinkedIn posts from the influencer

- Extract key topics, writing patterns, and style characteristics

- Analyze language preferences and post length variations

#### Stage 2: AI-Powered Generation
- Use selected topic, language, and length parameters

- Apply few-shot learning with relevant past posts as examples

- Generate new content that matches the influencer's unique writing style

- Ensure consistency in tone, vocabulary, and structure

### Prerequisites
- Python 3.8 or higher

- Groq API account (Get API key here)

### Installation
- Clone the repository

`
git clone <repository-url>
cd project-genai-post-generator
Set up environment variables
`

- Create a .env file in the root directory
`echo "GROQ_API_KEY=your_groq_api_key_here" > .env`

- Install dependencies

`pip install -r requirements.txt`

### Usage
- Prepare your LinkedIn posts data

- Export your LinkedIn posts to a compatible format

- Place the data file in the appropriate directory

### Run the application

`
streamlit run main.py
Generate new posts
`

- Select your desired topic from the extracted list

- Choose post length (Short, Medium, Long)

- Select language (English, Hindi, Hinglish)

- Click "Generate Post" to create content in your style


<img width="1712" height="936" alt="Screenshot 2025-09-25 231954" src="https://github.com/user-attachments/assets/015638d4-ecb8-4962-b75e-c91d24e4c04e" />
