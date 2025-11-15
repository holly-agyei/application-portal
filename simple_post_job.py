"""Simple script to post a job to the API."""
import requests

# API Configuration
API_URL = "https://jobs-api-zbgf.onrender.com"
API_KEY = "myemployerkey123"

# Job data to post
job_data = {
    "title": "Software Engineer",
    "role": "Software Engineer",
    "company": "Tech Corp",
    "location": "San Francisco, CA",
    "description": "We are looking for an experienced software engineer to join our team.",
    "required_skills": ["Python", "Flask", "PostgreSQL"],
    "required_certifications": []
}

# Headers with API key
headers = {
    "Content-Type": "application/json",
    "x-api-key": API_KEY
}

# Post the job
response = requests.post(f"{API_URL}/jobs", headers=headers, json=job_data)

# Check result
if response.status_code == 201:
    result = response.json()
    job_id = result['job']['id']
    print(f"✓ Job posted successfully!")
    print(f"  Job ID: {job_id}")
    print(f"  Title: {job_data['title']}")
else:
    print(f"✗ Failed to post job: {response.status_code}")
    print(f"  Error: {response.text}")

