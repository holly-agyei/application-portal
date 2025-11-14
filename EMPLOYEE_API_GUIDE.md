# Employee & Admin API User Guide

**API Base URL:** `https://jobs-api-sone.onrender.com`

This guide will help you use the Jobs API to view job postings and submit applications.

---

## Quick Start

### 1. Check if API is Running
```bash
curl https://jobs-api-sone.onrender.com/health
```

**Response:**
```json
{
  "status": "healthy",
  "service": "Employer API"
}
```

---

## For Employees (Job Seekers)

### View All Available Jobs

**Endpoint:** `GET /jobs`

**No authentication required**

**Example using curl:**
```bash
curl https://jobs-api-sone.onrender.com/jobs
```

**Example using Python:**
```python
import requests

response = requests.get('https://jobs-api-sone.onrender.com/jobs')
jobs = response.json()

for job in jobs:
    print(f"{job['title']} at {job['company']}")
    print(f"Location: {job['location']}")
    print(f"Required Skills: {', '.join(job['required_skills'])}")
    print("---")
```

**Response:**
```json
[
  {
    "id": 1,
    "title": "Sous Chef",
    "role": "Chef",
    "company": "Culinary Collective",
    "location": "New York, NY",
    "description": "Support lead chef with daily kitchen operations...",
    "required_skills": ["Cooking", "Food Safety", "Inventory Management"],
    "required_certifications": ["Food Handler Certification"],
    "posted_at": "2025-11-11T10:30:00"
  },
  ...
]
```

---

### View a Specific Job

**Endpoint:** `GET /jobs/{job_id}`

**No authentication required**

**Example:**
```bash
curl https://jobs-api-sone.onrender.com/jobs/1
```

**Python example:**
```python
import requests

job_id = 1
response = requests.get(f'https://jobs-api-sone.onrender.com/jobs/{job_id}')
job = response.json()

print(f"Title: {job['title']}")
print(f"Company: {job['company']}")
print(f"Description: {job['description']}")
```

---

### Submit a Job Application

**Endpoint:** `POST /applications`

**No authentication required**

**Request Body:**
```json
{
  "job_id": 1,
  "user_id": 12345,
  "resume_link": "https://example.com/resume.pdf",
  "skills": ["Python", "Flask", "REST APIs"],
  "certifications": ["AWS Certified"],
  "cover_letter": "I am very interested in this position."
}
```

**Example using curl:**
```bash
curl -X POST https://jobs-api-sone.onrender.com/applications \
  -H "Content-Type: application/json" \
  -d '{
    "job_id": 1,
    "user_id": 12345,
    "resume_link": "https://example.com/resume.pdf",
    "skills": ["Python", "Flask"],
    "certifications": ["AWS Certified"],
    "cover_letter": "I am interested in this position."
  }'
```

**Example using Python:**
```python
import requests

application_data = {
    "job_id": 1,
    "user_id": 12345,
    "resume_link": "https://example.com/resume.pdf",
    "skills": ["Python", "Flask", "REST APIs"],
    "certifications": ["AWS Certified"],
    "cover_letter": "I am very interested in this position."
}

response = requests.post(
    'https://jobs-api-sone.onrender.com/applications',
    json=application_data
)

if response.status_code == 201:
    result = response.json()
    print(f"Application submitted! ID: {result['application_id']}")
else:
    print(f"Error: {response.status_code} - {response.text}")
```

**Response (Success):**
```json
{
  "success": true,
  "application_id": 1
}
```

**Required Fields:**
- `job_id` - The ID of the job you're applying for
- `user_id` - Your user ID
- `resume_link` - URL to your resume

**Optional Fields:**
- `skills` - Array of your skills
- `certifications` - Array of your certifications
- `cover_letter` - Your cover letter text

---

## For Admins (Employers)

### Authentication

Admin endpoints require an API key. Include it in the request header:

```
x-api-key: your-api-key-here
```

**Default API Key:** `myemployerkey123`

---

### Create a New Job Posting

**Endpoint:** `POST /jobs`

**Authentication:** Required (API key)

**Request Body:**
```json
{
  "title": "Software Engineer",
  "role": "Software Engineer",
  "company": "Tech Corp",
  "location": "San Francisco, CA",
  "description": "We are looking for an experienced software engineer...",
  "required_skills": ["Python", "Flask", "PostgreSQL"],
  "required_certifications": []
}
```

**Example using curl:**
```bash
curl -X POST https://jobs-api-sone.onrender.com/jobs \
  -H "Content-Type: application/json" \
  -H "x-api-key: myemployerkey123" \
  -d '{
    "title": "Software Engineer",
    "role": "Software Engineer",
    "company": "Tech Corp",
    "location": "San Francisco, CA",
    "description": "We are looking for an experienced software engineer...",
    "required_skills": ["Python", "Flask", "PostgreSQL"],
    "required_certifications": []
  }'
```

**Example using Python:**
```python
import requests

headers = {
    "Content-Type": "application/json",
    "x-api-key": "myemployerkey123"
}

job_data = {
    "title": "Software Engineer",
    "role": "Software Engineer",
    "company": "Tech Corp",
    "location": "San Francisco, CA",
    "description": "We are looking for an experienced software engineer...",
    "required_skills": ["Python", "Flask", "PostgreSQL"],
    "required_certifications": []
}

response = requests.post(
    'https://jobs-api-sone.onrender.com/jobs',
    headers=headers,
    json=job_data
)

if response.status_code == 201:
    result = response.json()
    print(f"Job created! ID: {result['job']['id']}")
else:
    print(f"Error: {response.status_code} - {response.text}")
```

**Response (Success):**
```json
{
  "success": true,
  "job": {
    "id": 1,
    "title": "Software Engineer",
    "role": "Software Engineer",
    "company": "Tech Corp",
    "location": "San Francisco, CA",
    "description": "We are looking for an experienced software engineer...",
    "required_skills": ["Python", "Flask", "PostgreSQL"],
    "required_certifications": [],
    "posted_at": "2025-11-14T10:30:00"
  }
}
```

**Required Fields:**
- `title` - Job title
- `role` - Job role/category
- `company` - Company name
- `location` - Job location
- `description` - Job description

**Optional Fields:**
- `required_skills` - Array of required skills (default: empty array)
- `required_certifications` - Array of required certifications (default: empty array)

---

### View All Applications

**Endpoint:** `GET /applications`

**Authentication:** Required (API key)

**Query Parameters (optional):**
- `job_id` - Filter by job ID
- `user_id` - Filter by user ID

**Example:**
```bash
# Get all applications
curl -H "x-api-key: myemployerkey123" \
  https://jobs-api-sone.onrender.com/applications

# Get applications for a specific job
curl -H "x-api-key: myemployerkey123" \
  "https://jobs-api-sone.onrender.com/applications?job_id=1"

# Get applications from a specific user
curl -H "x-api-key: myemployerkey123" \
  "https://jobs-api-sone.onrender.com/applications?user_id=12345"
```

**Python example:**
```python
import requests

headers = {"x-api-key": "myemployerkey123"}

# Get all applications
response = requests.get(
    'https://jobs-api-sone.onrender.com/applications',
    headers=headers
)
applications = response.json()

# Get applications for a specific job
response = requests.get(
    'https://jobs-api-sone.onrender.com/applications',
    headers=headers,
    params={"job_id": 1}
)
job_applications = response.json()
```

**Response:**
```json
[
  {
    "id": 1,
    "job_id": 1,
    "user_id": 12345,
    "resume_link": "https://example.com/resume.pdf",
    "skills": ["Python", "Flask", "REST APIs"],
    "certifications": ["AWS Certified"],
    "cover_letter": "I am very interested in this position.",
    "created_at": "2025-11-14T10:30:00"
  },
  ...
]
```

---

### Delete a Job

**Endpoint:** `DELETE /jobs/{job_id}`

**Authentication:** Required (API key)

**Example:**
```bash
curl -X DELETE \
  -H "x-api-key: myemployerkey123" \
  https://jobs-api-sone.onrender.com/jobs/1
```

**Python example:**
```python
import requests

headers = {"x-api-key": "myemployerkey123"}

response = requests.delete(
    'https://jobs-api-sone.onrender.com/jobs/1',
    headers=headers
)

if response.status_code == 200:
    print("Job deleted successfully")
```

---

### Delete All Jobs

**Endpoint:** `DELETE /jobs`

**Authentication:** Required (API key)

**Example:**
```bash
curl -X DELETE \
  -H "x-api-key: myemployerkey123" \
  https://jobs-api-sone.onrender.com/jobs
```

**Python example:**
```python
import requests

headers = {"x-api-key": "myemployerkey123"}

response = requests.delete(
    'https://jobs-api-sone.onrender.com/jobs',
    headers=headers
)

if response.status_code == 200:
    result = response.json()
    print(result['message'])  # e.g., "16 job(s) deleted successfully"
```

---

## Error Responses

All endpoints may return error responses in this format:

```json
{
  "success": false,
  "error": "Error message here"
}
```

**Common HTTP Status Codes:**
- `200` - Success
- `201` - Created successfully
- `400` - Bad request (missing or invalid data)
- `401` - Unauthorized (missing or invalid API key)
- `404` - Not found
- `500` - Internal server error

---

## Complete Python Example

Here's a complete example showing how to use the API:

```python
import requests

API_URL = "https://jobs-api-sone.onrender.com"
API_KEY = "myemployerkey123"  # For admin endpoints

# 1. Check API health
response = requests.get(f"{API_URL}/health")
print("API Status:", response.json())

# 2. Get all jobs (no auth needed)
response = requests.get(f"{API_URL}/jobs")
jobs = response.json()
print(f"\nFound {len(jobs)} jobs")

# 3. View a specific job
if jobs:
    job_id = jobs[0]['id']
    response = requests.get(f"{API_URL}/jobs/{job_id}")
    job = response.json()
    print(f"\nJob Details: {job['title']} at {job['company']}")

# 4. Submit an application (no auth needed)
application = {
    "job_id": job_id,
    "user_id": 12345,
    "resume_link": "https://example.com/resume.pdf",
    "skills": ["Python", "Flask"],
    "certifications": ["AWS Certified"],
    "cover_letter": "I'm interested in this position."
}

response = requests.post(f"{API_URL}/applications", json=application)
if response.status_code == 201:
    print(f"\nApplication submitted! ID: {response.json()['application_id']}")

# 5. View applications (admin only - requires API key)
headers = {"x-api-key": API_KEY}
response = requests.get(f"{API_URL}/applications", headers=headers)
applications = response.json()
print(f"\nTotal applications: {len(applications)}")
```

---

## Need Help?

- **API Base URL:** `https://jobs-api-sone.onrender.com`
- **Health Check:** `GET /health`
- **All endpoints support CORS** - you can call them from any web application

---

## Quick Reference

| Endpoint | Method | Auth | Description |
|----------|--------|------|-------------|
| `/health` | GET | No | Check API status |
| `/jobs` | GET | No | Get all jobs |
| `/jobs/{id}` | GET | No | Get specific job |
| `/jobs` | POST | Yes | Create job (admin) |
| `/jobs/{id}` | DELETE | Yes | Delete job (admin) |
| `/jobs` | DELETE | Yes | Delete all jobs (admin) |
| `/applications` | POST | No | Submit application |
| `/applications` | GET | Yes | Get applications (admin) |

---

**Last Updated:** November 2025

