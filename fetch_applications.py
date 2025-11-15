"""Script to fetch all applications from the API."""
import requests
import json
from datetime import datetime

# API Configuration
API_URL = "https://jobs-api-zbgf.onrender.com"
API_KEY = "myemployerkey123"

def fetch_applications():
    """Fetch all applications from the API."""
    headers = {
        "x-api-key": API_KEY
    }
    
    try:
        print(f"Fetching applications from {API_URL}...")
        print("=" * 60)
        
        response = requests.get(f"{API_URL}/applications", headers=headers, timeout=30)
        
        if response.status_code == 200:
            applications = response.json()
            
            print(f"\n✓ Successfully fetched {len(applications)} application(s)\n")
            print("=" * 60)
            
            if not applications:
                print("No applications found.")
                return []
            
            # Display applications
            for i, app in enumerate(applications, 1):
                print(f"\nApplication {i}/{len(applications)}:")
                print(f"  ID: {app.get('id', 'N/A')}")
                print(f"  Job ID: {app.get('job_id', 'N/A')}")
                print(f"  User ID: {app.get('user_id', 'N/A')}")
                print(f"  Resume Link: {app.get('resume_link', 'N/A')}")
                print(f"  Skills: {', '.join(app.get('skills', [])) if app.get('skills') else 'None'}")
                print(f"  Certifications: {', '.join(app.get('certifications', [])) if app.get('certifications') else 'None'}")
                print(f"  Created At: {app.get('created_at', 'N/A')}")
                cover_letter = app.get('cover_letter', '')
                if cover_letter:
                    if len(cover_letter) > 200:
                        print(f"  Cover Letter: {cover_letter[:200]}...")
                    else:
                        print(f"  Cover Letter: {cover_letter}")
                else:
                    print(f"  Cover Letter: None")
                print("-" * 60)
            
            # Save to file
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"applications_{timestamp}.json"
            
            with open(filename, 'w') as f:
                json.dump(applications, f, indent=2)
            
            print(f"\n✓ Applications saved to {filename}")
            print(f"Total applications: {len(applications)}")
            print("=" * 60)
            
            return applications
            
        else:
            print(f"✗ Failed to fetch applications - Status: {response.status_code}")
            print(f"Response: {response.text}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"✗ Error connecting to API: {str(e)}")
        return None
    except Exception as e:
        print(f"✗ Unexpected error: {str(e)}")
        return None


def fetch_applications_by_job(job_id):
    """Fetch applications for a specific job."""
    headers = {
        "x-api-key": API_KEY
    }
    
    try:
        print(f"Fetching applications for job {job_id}...")
        print("=" * 60)
        
        response = requests.get(
            f"{API_URL}/applications",
            headers=headers,
            params={"job_id": job_id},
            timeout=30
        )
        
        if response.status_code == 200:
            applications = response.json()
            print(f"\n✓ Found {len(applications)} application(s) for job {job_id}\n")
            return applications
        else:
            print(f"✗ Failed: {response.status_code} - {response.text}")
            return []
    except Exception as e:
        print(f"✗ Error: {str(e)}")
        return []


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        try:
            job_id = int(sys.argv[1])
            fetch_applications_by_job(job_id)
        except ValueError:
            print("Error: Job ID must be a number")
            print("Usage: python fetch_applications.py [job_id]")
    else:
        fetch_applications()

