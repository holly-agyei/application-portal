# Jobs API - Quick Reference

**Base URL:** `https://jobs-api-zbgf.onrender.com`

---

## Authentication

Admin endpoints require API key in header:
```
x-api-key: myemployerkey123
```

---

## Endpoints

### Jobs

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| `GET` | `/jobs` | No | Get all jobs |
| `GET` | `/jobs/{id}` | No | Get job by ID |
| `POST` | `/jobs` | Yes | Create job |
| `DELETE` | `/jobs/{id}` | Yes | Delete job |
| `DELETE` | `/jobs` | Yes | Delete all jobs |

### Applications

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| `POST` | `/applications` | No | Submit application |
| `GET` | `/applications` | Yes | Get all applications |
| `GET` | `/applications?job_id={id}` | Yes | Get applications for job |
| `GET` | `/applications?user_id={id}` | Yes | Get applications by user |

### Health

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| `GET` | `/health` | No | Check API status |

---

## Examples

### Create Job
```bash
curl -X POST https://jobs-api-zbgf.onrender.com/jobs \
  -H "Content-Type: application/json" \
  -H "x-api-key: myemployerkey123" \
  -d '{
    "title": "Software Engineer",
    "role": "Software Engineer",
    "company": "Tech Corp",
    "location": "San Francisco, CA",
    "description": "Job description here",
    "required_skills": ["Python", "Flask"],
    "required_certifications": []
  }'
```

### Get All Jobs
```bash
curl https://jobs-api-zbgf.onrender.com/jobs
```

### Submit Application
```bash
curl -X POST https://jobs-api-zbgf.onrender.com/applications \
  -H "Content-Type: application/json" \
  -d '{
    "job_id": 1,
    "user_id": 12345,
    "resume_link": "https://example.com/resume.pdf",
    "skills": ["Python", "Flask"],
    "certifications": ["AWS Certified"]
  }'
```

### Get All Applications
```bash
curl -H "x-api-key: myemployerkey123" \
  https://jobs-api-zbgf.onrender.com/applications
```


```

### Delete Job
```bash
curl -X DELETE https://jobs-api-zbgf.onrender.com/jobs/1 \
  -H "x-api-key: myemployerkey123"
```

---

## Response Codes

- `200` - Success
- `201` - Created
- `400` - Bad Request
- `401` - Unauthorized
- `404` - Not Found
- `500` - Server Error

