"""Simple script to fetch all jobs from the API."""
import requests

# API Configuration
API_URL = "https://jobs-api-zbgf.onrender.com"

# Fetch all jobs (no authentication needed)
response = requests.get(f"{API_URL}/jobs")

# Check result
if response.status_code == 200:
    jobs = response.json()
    print(f"✓ Found {len(jobs)} job(s)\n")
    
    # Display each job
    for job in jobs:
        print(f"Job ID: {job['id']}")
        print(f"  Title: {job['title']}")
        print(f"  Company: {job['company']}")
        print(f"  Location: {job['location']}")
        print(f"  Skills: {', '.join(job['required_skills'])}")
        print()
else:
    print(f"✗ Failed to fetch jobs: {response.status_code}")
    print(f"  Error: {response.text}")

