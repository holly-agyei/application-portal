"""Comprehensive test script for all API endpoints."""
import requests
import json
from datetime import datetime

# API Configuration
API_URL = "https://jobs-api-sone.onrender.com"
API_KEY = "myemployerkey123"  # Default API key from config

# Colors for terminal output
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def print_success(message):
    print(f"{Colors.GREEN}✓ {message}{Colors.RESET}")

def print_error(message):
    print(f"{Colors.RED}✗ {message}{Colors.RESET}")

def print_info(message):
    print(f"{Colors.BLUE}ℹ {message}{Colors.RESET}")

def print_header(message):
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}{message}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.RESET}\n")

def test_health_check():
    """Test GET /health endpoint."""
    print_header("Testing Health Check Endpoint")
    try:
        response = requests.get(f"{API_URL}/health", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print_success(f"Health check passed: {data}")
            return True
        else:
            print_error(f"Health check failed: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print_error(f"Health check error: {str(e)}")
        return False

def test_get_all_jobs():
    """Test GET /jobs endpoint."""
    print_header("Testing GET /jobs (Get All Jobs)")
    try:
        response = requests.get(f"{API_URL}/jobs", timeout=10)
        if response.status_code == 200:
            jobs = response.json()
            print_success(f"Retrieved {len(jobs)} job(s)")
            if jobs:
                print_info(f"First job: {jobs[0].get('title', 'N/A')} at {jobs[0].get('company', 'N/A')}")
            return jobs
        else:
            print_error(f"Failed to get jobs: {response.status_code} - {response.text}")
            return []
    except Exception as e:
        print_error(f"Error getting jobs: {str(e)}")
        return []

def test_get_single_job(job_id):
    """Test GET /jobs/<id> endpoint."""
    print_header(f"Testing GET /jobs/{job_id} (Get Single Job)")
    try:
        response = requests.get(f"{API_URL}/jobs/{job_id}", timeout=10)
        if response.status_code == 200:
            job = response.json()
            print_success(f"Retrieved job: {job.get('title', 'N/A')}")
            print_info(f"  Company: {job.get('company', 'N/A')}")
            print_info(f"  Location: {job.get('location', 'N/A')}")
            return job
        elif response.status_code == 404:
            print_error(f"Job {job_id} not found")
            return None
        else:
            print_error(f"Failed to get job: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print_error(f"Error getting job: {str(e)}")
        return None

def test_create_job():
    """Test POST /jobs endpoint."""
    print_header("Testing POST /jobs (Create Job)")
    test_job = {
        "title": "Test Software Engineer",
        "role": "Software Engineer",
        "company": "Test Company",
        "location": "Remote",
        "description": "This is a test job posting created by the API test script.",
        "required_skills": ["Python", "Flask", "API Development"],
        "required_certifications": []
    }
    
    headers = {
        "Content-Type": "application/json",
        "x-api-key": API_KEY
    }
    
    try:
        response = requests.post(
            f"{API_URL}/jobs",
            headers=headers,
            json=test_job,
            timeout=10
        )
        
        if response.status_code == 201:
            data = response.json()
            job_id = data.get('job', {}).get('id', 'unknown')
            print_success(f"Job created successfully (ID: {job_id})")
            return job_id
        else:
            print_error(f"Failed to create job: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print_error(f"Error creating job: {str(e)}")
        return None

def test_create_job_without_auth():
    """Test POST /jobs without API key (should fail)."""
    print_header("Testing POST /jobs without API key (Should Fail)")
    test_job = {
        "title": "Unauthorized Test",
        "role": "Test",
        "company": "Test",
        "location": "Test",
        "description": "This should fail"
    }
    
    try:
        response = requests.post(
            f"{API_URL}/jobs",
            json=test_job,
            timeout=10
        )
        
        if response.status_code == 401 or response.status_code == 403:
            print_success(f"Correctly rejected unauthorized request: {response.status_code}")
            return True
        else:
            print_error(f"Unexpected response: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print_error(f"Error: {str(e)}")
        return False

def test_create_application(job_id):
    """Test POST /applications endpoint."""
    print_header(f"Testing POST /applications (Create Application for Job {job_id})")
    test_application = {
        "job_id": job_id,
        "user_id": 12345,
        "resume_link": "https://example.com/resume.pdf",
        "skills": ["Python", "Flask", "REST APIs"],
        "certifications": ["AWS Certified"],
        "cover_letter": "I am very interested in this position."
    }
    
    try:
        response = requests.post(
            f"{API_URL}/applications",
            json=test_application,
            timeout=10
        )
        
        if response.status_code == 201:
            data = response.json()
            app_id = data.get('application_id', 'unknown')
            print_success(f"Application created successfully (ID: {app_id})")
            return app_id
        else:
            print_error(f"Failed to create application: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print_error(f"Error creating application: {str(e)}")
        return None

def test_get_applications():
    """Test GET /applications endpoint."""
    print_header("Testing GET /applications (Get All Applications)")
    headers = {
        "x-api-key": API_KEY
    }
    
    try:
        response = requests.get(
            f"{API_URL}/applications",
            headers=headers,
            timeout=10
        )
        
        if response.status_code == 200:
            applications = response.json()
            print_success(f"Retrieved {len(applications)} application(s)")
            return applications
        else:
            print_error(f"Failed to get applications: {response.status_code} - {response.text}")
            return []
    except Exception as e:
        print_error(f"Error getting applications: {str(e)}")
        return []

def test_get_applications_with_filters(job_id):
    """Test GET /applications with filters."""
    print_header(f"Testing GET /applications?job_id={job_id} (With Filter)")
    headers = {
        "x-api-key": API_KEY
    }
    
    try:
        response = requests.get(
            f"{API_URL}/applications",
            headers=headers,
            params={"job_id": job_id},
            timeout=10
        )
        
        if response.status_code == 200:
            applications = response.json()
            print_success(f"Retrieved {len(applications)} application(s) for job {job_id}")
            return applications
        else:
            print_error(f"Failed to get filtered applications: {response.status_code} - {response.text}")
            return []
    except Exception as e:
        print_error(f"Error getting filtered applications: {str(e)}")
        return []

def test_invalid_endpoint():
    """Test invalid endpoint (should return 404)."""
    print_header("Testing Invalid Endpoint (Should Return 404)")
    try:
        response = requests.get(f"{API_URL}/invalid-endpoint", timeout=10)
        if response.status_code == 404:
            print_success("Correctly returned 404 for invalid endpoint")
            return True
        else:
            print_error(f"Unexpected response: {response.status_code}")
            return False
    except Exception as e:
        print_error(f"Error: {str(e)}")
        return False

def main():
    """Run all tests."""
    print(f"\n{Colors.BOLD}{'='*60}")
    print(f"API Endpoint Test Suite")
    print(f"Testing: {API_URL}")
    print(f"{'='*60}{Colors.RESET}\n")
    
    results = {
        "passed": 0,
        "failed": 0,
        "total": 0
    }
    
    # Test 1: Health Check
    if test_health_check():
        results["passed"] += 1
    else:
        results["failed"] += 1
    results["total"] += 1
    
    # Test 2: Get All Jobs
    jobs = test_get_all_jobs()
    if jobs is not None:
        results["passed"] += 1
    else:
        results["failed"] += 1
    results["total"] += 1
    
    # Test 3: Get Single Job (if jobs exist)
    if jobs:
        job_id = jobs[0].get('id')
        if job_id:
            if test_get_single_job(job_id):
                results["passed"] += 1
            else:
                results["failed"] += 1
            results["total"] += 1
            
            # Test 4: Get Non-existent Job
            if test_get_single_job(99999) is None:
                results["passed"] += 1
            else:
                results["failed"] += 1
            results["total"] += 1
    else:
        print_info("Skipping single job tests - no jobs available")
    
    # Test 5: Create Job (with auth)
    created_job_id = test_create_job()
    if created_job_id:
        results["passed"] += 1
    else:
        results["failed"] += 1
    results["total"] += 1
    
    # Test 6: Create Job without auth (should fail)
    if test_create_job_without_auth():
        results["passed"] += 1
    else:
        results["failed"] += 1
    results["total"] += 1
    
    # Test 7: Create Application
    if created_job_id:
        app_id = test_create_application(created_job_id)
        if app_id:
            results["passed"] += 1
        else:
            results["failed"] += 1
        results["total"] += 1
    else:
        # Try with first available job
        if jobs:
            test_job_id = jobs[0].get('id')
            app_id = test_create_application(test_job_id)
            if app_id:
                results["passed"] += 1
            else:
                results["failed"] += 1
            results["total"] += 1
        else:
            print_info("Skipping application creation test - no jobs available")
    
    # Test 8: Get All Applications
    applications = test_get_applications()
    if applications is not None:
        results["passed"] += 1
    else:
        results["failed"] += 1
    results["total"] += 1
    
    # Test 9: Get Applications with Filter
    if created_job_id:
        if test_get_applications_with_filters(created_job_id) is not None:
            results["passed"] += 1
        else:
            results["failed"] += 1
        results["total"] += 1
    
    # Test 10: Invalid Endpoint
    if test_invalid_endpoint():
        results["passed"] += 1
    else:
        results["failed"] += 1
    results["total"] += 1
    
    # Print Summary
    print_header("Test Summary")
    print(f"{Colors.BOLD}Total Tests: {results['total']}{Colors.RESET}")
    print(f"{Colors.GREEN}Passed: {results['passed']}{Colors.RESET}")
    print(f"{Colors.RED}Failed: {results['failed']}{Colors.RESET}")
    
    success_rate = (results["passed"] / results["total"] * 100) if results["total"] > 0 else 0
    print(f"\n{Colors.BOLD}Success Rate: {success_rate:.1f}%{Colors.RESET}\n")
    
    if results["failed"] == 0:
        print_success("All tests passed! 🎉")
    else:
        print_error(f"{results['failed']} test(s) failed. Please review the errors above.")

if __name__ == "__main__":
    main()

