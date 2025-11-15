"""Simple script to delete a job from the API."""
import requests

# API Configuration
API_URL = "https://jobs-api-zbgf.onrender.com"
API_KEY = "myemployerkey123"

# Job ID to delete
job_id = 1  # Change this to the job ID you want to delete

# Headers with API key
headers = {
    "x-api-key": API_KEY
}

# Delete the job
response = requests.delete(f"{API_URL}/jobs/{job_id}", headers=headers)

# Check result
if response.status_code == 200:
    result = response.json()
    print(f"✓ Job deleted successfully!")
    print(f"  {result['message']}")
else:
    print(f"✗ Failed to delete job: {response.status_code}")
    print(f"  Error: {response.text}")

