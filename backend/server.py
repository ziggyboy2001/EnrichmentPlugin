from flask import Flask, request, jsonify
from scraper import scrape_linkedin_profile
import openai

# Set your OpenAI API key here
openai.api_key = 'sk-proj-ghd7Fwh4LU0dcuDe5tnYT3BlbkFJg9d0IlDythrcx5s0SK7t'

app = Flask(__name__)

@app.route('/enrich', methods=['POST'])
def enrich_profile():
    data = request.json
    linkedin_url = data['url']
    profile_data = scrape_linkedin_profile(linkedin_url)  # Scrape LinkedIn profile data

    # Convert the profile data to a string format suitable for ChatGPT
    profile_text = f"Name: {profile_data['name']}\nHeadline: {profile_data['headline']}\nAbout: {profile_data['about']}\nExperience: {', '.join(profile_data['experience'])}\nEducation: {', '.join(profile_data['education'])}"

    # Use ChatGPT to enhance the profile data
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert LinkedIn profile enhancer."},
            {"role": "user", "content": f"Enhance the following LinkedIn profile data:\n{profile_text}"}
        ]
    )

    enhanced_data = response.choices[0].message['content']

    # Split the enhanced data into three sections for display
    enhanced_data_sections = enhanced_data.split('\n\n')
    enriched_data = {
        'tab1': enhanced_data_sections[:3],
        'tab2': enhanced_data_sections[3:6],
        'tab3': enhanced_data_sections[6:9]
    }

    return jsonify(enriched_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)