# Employer API Documentation

**Base URL:** `https://jobs-api-s4o6.onrender.com`

The Employer API provides endpoints for managing job postings and job applications. This API serves as the backend for the Employee Portal.

---

## Table of Contents

- [Authentication](#authentication)
- [Endpoints](#endpoints)
  - [Health Check](#health-check)
  - [Jobs](#jobs)
  - [Applications](#applications)
- [Error Handling](#error-handling)
- [Examples](#examples)

---

## Authentication

Some endpoints require API key authentication. Include your API key in the request header:

```
x-api-key: your-api-key-here
```

**Note:** The API key is set via the `EMPLOYER_API_KEY` environment variable.

---

## Endpoints

### Health Check

#### `GET /health`

Check if the API is running and healthy.

**Authentication:** Not required

**Response:**
```json
{
  "status": "healthy",
  "service": "Employer API"
}
```

**Status Code:** `200 OK`

---

### Jobs

#### `GET /jobs`

Retrieve all available job postings.

**Authentication:** Not required

**Response:**
```json
[
  {
    "id": 1001,
    "title": "Sous Chef",
    "role": "Chef",
    "company": "Culinary Collective",
    "location": "New York, NY",
    "description": "Support lead chef with daily kitchen operations and menu execution. Responsible for food preparation, maintaining kitchen standards, and coordinating with kitchen staff.",
    "required_skills": ["Cooking", "Food Safety", "Inventory Management"],
    "required_certifications": ["Food Handler Certification"],
    "posted_at": "2025-11-11T10:30:00"
  },
  ...
]
```

**Status Code:** `200 OK`

**Example:**
```bash
curl https://jobs-api-s4o6.onrender.com/jobs
```

---

#### `POST /jobs`

Create a new job posting.

**Authentication:** Required (API key)

**Request Headers:**
```
Content-Type: application/json
x-api-key: your-api-key-here
```

**Request Body:**
```json
{
  "title": "Software Engineer",
  "role": "Engineering",
  "company": "Tech Corp",
  "location": "Remote",
  "description": "Build amazing software applications...",
  "required_skills": ["Python", "Flask", "PostgreSQL"],
  "required_certifications": []
}
```

**Response:**
```json
{
  "success": true,
  "job": {
    "id": 1016,
    "title": "Software Engineer",
    "role": "Engineering",
    "company": "Tech Corp",
    "location": "Remote",
    "description": "Build amazing software applications...",
    "required_skills": ["Python", "Flask", "PostgreSQL"],
    "required_certifications": [],
    "posted_at": "2025-11-13T23:30:00"
  }
}
```

**Status Codes:**
- `201 Created` - Job created successfully
- `400 Bad Request` - Invalid input data
- `401 Unauthorized` - Missing or invalid API key

**Example:**
```bash
curl -X POST https://jobs-api-s4o6.onrender.com/jobs \
  -H "Content-Type: application/json" \
  -H "x-api-key: your-api-key-here" \
  -d '{
    "title": "Software Engineer",
    "role": "Engineering",
    "company": "Tech Corp",
    "location": "Remote",
    "description": "Build amazing software applications...",
    "required_skills": ["Python", "Flask"],
    "required_certifications": []
  }'
```

---

### Applications

#### `POST /applications`

Submit a job application from an employee.

**Authentication:** Not required

**Request Headers:**
```
Content-Type: application/json
```

**Request Body:**
```json
{
  "job_id": 1001,
  "user_id": 5,
  "resume_link": "https://example.com/resumes/user5_resume.pdf",
  "skills": ["Cooking", "Food Safety", "Inventory Management"],
  "certifications": ["Food Handler Certification"],
  "cover_letter": "I am very interested in this position..."
}
```

**Response (Success):**
```json
{
  "success": true,
  "application_id": 98765
}
```

**Response (Error):**
```json
{
  "success": false,
  "error": "Job posting no longer available"
}
```

**Status Codes:**
- `201 Created` - Application submitted successfully
- `400 Bad Request` - Invalid input data
- `404 Not Found` - Job not found

**Example:**
```bash
curl -X POST https://jobs-api-s4o6.onrender.com/applications \
  -H "Content-Type: application/json" \
  -d '{
    "job_id": 1001,
    "user_id": 5,
    "resume_link": "https://example.com/resumes/user5_resume.pdf",
    "skills": ["Cooking", "Food Safety"],
    "certifications": ["Food Handler Certification"],
    "cover_letter": "I am very interested in this position..."
  }'
```

---

#### `GET /applications`

Retrieve all job applications.

**Authentication:** Required (API key)

**Request Headers:**
```
x-api-key: your-api-key-here
```

**Query Parameters (Optional):**
- `job_id` (integer) - Filter applications by job ID
- `user_id` (integer) - Filter applications by user ID

**Response:**
```json
[
  {
    "id": 1,
    "job_id": 1001,
    "user_id": 5,
    "resume_link": "https://example.com/resumes/user5_resume.pdf",
    "skills": ["Cooking", "Food Safety"],
    "certifications": ["Food Handler Certification"],
    "cover_letter": "I am very interested in this position...",
    "created_at": "2025-11-13T16:19:43"
  },
  ...
]
```

**Status Codes:**
- `200 OK` - Success
- `401 Unauthorized` - Missing or invalid API key

**Examples:**
```bash
# Get all applications
curl -H "x-api-key: your-api-key-here" \
  https://jobs-api-s4o6.onrender.com/applications

# Filter by job_id
curl -H "x-api-key: your-api-key-here" \
  "https://jobs-api-s4o6.onrender.com/applications?job_id=1001"

# Filter by user_id
curl -H "x-api-key: your-api-key-here" \
  "https://jobs-api-s4o6.onrender.com/applications?user_id=5"
```

---

## Error Handling

All errors are returned in JSON format with a consistent structure:

```json
{
  "success": false,
  "error": "Error message describing what went wrong"
}
```

### Common Error Responses

#### 400 Bad Request
```json
{
  "success": false,
  "error": "Missing required field: job_id"
}
```

#### 401 Unauthorized
```json
{
  "success": false,
  "error": "Missing API key. Please provide x-api-key header."
}
```

or

```json
{
  "success": false,
  "error": "Invalid API key."
}
```

#### 404 Not Found
```json
{
  "success": false,
  "error": "Job posting no longer available"
}
```

or

```json
{
  "success": false,
  "error": "Endpoint not found"
}
```

#### 500 Internal Server Error
```json
{
  "success": false,
  "error": "Internal server error"
}
```

---

## Examples

### Complete Workflow Example

#### 1. Check API Health
```bash
curl https://jobs-api-s4o6.onrender.com/health
```

#### 2. Get All Jobs
```bash
curl https://jobs-api-s4o6.onrender.com/jobs
```

#### 3. Submit an Application
```bash
curl -X POST https://jobs-api-s4o6.onrender.com/applications \
  -H "Content-Type: application/json" \
  -d '{
    "job_id": 1001,
    "user_id": 5,
    "resume_link": "https://example.com/resumes/user5_resume.pdf",
    "skills": ["Cooking", "Food Safety"],
    "certifications": ["Food Handler Certification"],
    "cover_letter": "I am interested in this position."
  }'
```

#### 4. View Applications (Employer)
```bash
curl -H "x-api-key: your-api-key-here" \
  https://jobs-api-s4o6.onrender.com/applications
```

#### 5. Create a New Job (Employer)
```bash
curl -X POST https://jobs-api-s4o6.onrender.com/jobs \
  -H "Content-Type: application/json" \
  -H "x-api-key: your-api-key-here" \
  -d '{
    "title": "Senior Chef",
    "role": "Chef",
    "company": "Fine Dining Restaurant",
    "location": "San Francisco, CA",
    "description": "Lead kitchen operations and manage culinary team.",
    "required_skills": ["Cooking", "Leadership", "Menu Planning"],
    "required_certifications": ["Culinary Degree", "Food Handler Certification"]
  }'
```

---

## Data Models

### Job Object
```typescript
{
  id: number;                    // Auto-generated unique identifier
  title: string;                  // Job title
  role: string;                   // Job role/category
  company: string;                // Company name
  location: string;               // Job location
  description: string;            // Job description
  required_skills: string[];       // Array of required skills
  required_certifications: string[]; // Array of required certifications
  posted_at: string;              // ISO 8601 datetime string
}
```

### Application Object
```typescript
{
  id: number;                     // Auto-generated unique identifier
  job_id: number;                 // Foreign key to job
  user_id: number;                // User ID from Employee Portal
  resume_link: string;            // URL to resume
  skills: string[];              // Array of applicant skills
  certifications: string[];       // Array of applicant certifications
  cover_letter: string;           // Cover letter text (optional)
  created_at: string;             // ISO 8601 datetime string
}
```

---

## Rate Limiting

Currently, there are no rate limits implemented. However, please use the API responsibly.

---

## Support

For issues or questions, please contact the development team or check the repository documentation.

---

## Version

**API Version:** 1.0.0  
**Last Updated:** November 2025

---

## Changelog

### v1.0.0 (November 2025)
- Initial release
- GET /jobs endpoint
- POST /applications endpoint
- POST /jobs endpoint (protected)
- GET /applications endpoint (protected)
- Health check endpoint

