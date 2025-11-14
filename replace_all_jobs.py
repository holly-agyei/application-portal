"""Script to delete all existing jobs and post new jobs to the API."""
import requests
import json
from datetime import datetime

# API Configuration
API_URL = "https://jobs-api-sone.onrender.com"
API_KEY = "myemployerkey123"

# New jobs to post (removing id and posted_at as they're auto-generated)
new_jobs = [
    {
        "title": "Sous Chef",
        "role": "Chef",
        "company": "Culinary Collective",
        "location": "New York, NY",
        "description": "Support lead chef with daily kitchen operations and menu execution. Responsible for food preparation, maintaining kitchen standards, and coordinating with kitchen staff.",
        "required_skills": ["Cooking", "Food Safety", "Inventory Management"],
        "required_certifications": ["Food Handler Certification"]
    },
    {
        "title": "Front Desk Cashier",
        "role": "Cashier",
        "company": "Gourmet Market",
        "location": "Chicago, IL",
        "description": "Assist guests with purchases, manage the register, and maintain customer satisfaction. Handle cash transactions, process payments, and provide excellent customer service.",
        "required_skills": ["Customer Service", "Cash Handling", "Food Safety"],
        "required_certifications": ["Food Handler Certification"]
    },
    {
        "title": "Delivery Driver",
        "role": "Driver",
        "company": "FastBite",
        "location": "Los Angeles, CA",
        "description": "Deliver gourmet meals across the metro area ensuring safety and quality. Maintain delivery vehicle, follow traffic regulations, and provide friendly customer interactions.",
        "required_skills": ["Driving", "Customer Service", "Food Safety"],
        "required_certifications": ["Driver's License"]
    },
    {
        "title": "Regional Marketing Specialist",
        "role": "Marketing Specialist",
        "company": "TasteWave",
        "location": "Austin, TX",
        "description": "Develop campaigns and manage brand engagement initiatives. Create marketing materials, manage social media presence, and coordinate promotional events.",
        "required_skills": ["Marketing", "Customer Service", "Food Safety"],
        "required_certifications": ["Marketing Certification"]
    },
    {
        "title": "Food Safety Inspector",
        "role": "Food Safety Inspector",
        "company": "SafeServe Inc.",
        "location": "Seattle, WA",
        "description": "Inspect partner facilities to maintain compliance with safety standards. Conduct regular audits, document findings, and ensure adherence to health regulations.",
        "required_skills": ["Food Safety", "Inventory Management"],
        "required_certifications": ["Food Safety Certification"]
    },
    {
        "title": "Fire Safety Inspector",
        "role": "Fire Safety Inspector",
        "company": "SecureHeat",
        "location": "Denver, CO",
        "description": "Perform safety inspections and ensure adherence to municipal codes. Test gas systems, verify compliance with fire codes, and document inspection results.",
        "required_skills": ["Gas leak tests", "City code adherence"],
        "required_certifications": ["CGLI Inspector"]
    },
    {
        "title": "Line Cook",
        "role": "Chef",
        "company": "The Kitchen Table",
        "location": "Miami, FL",
        "description": "Prepare food items according to recipes and specifications. Work in a fast-paced kitchen environment, maintain cleanliness, and collaborate with kitchen team.",
        "required_skills": ["Cooking", "Food Safety", "Inventory Management"],
        "required_certifications": ["Food Handler Certification"]
    },
    {
        "title": "Part-Time Cashier",
        "role": "Cashier",
        "company": "QuickBite Express",
        "location": "Phoenix, AZ",
        "description": "Handle point-of-sale transactions, assist customers with orders, and maintain a clean checkout area. Part-time position with flexible scheduling.",
        "required_skills": ["Customer Service", "Cash Handling", "Food Safety"],
        "required_certifications": ["Food Handler Certification"]
    },
    {
        "title": "Food Delivery Driver",
        "role": "Driver",
        "company": "DoorDash Delights",
        "location": "Portland, OR",
        "description": "Deliver food orders to customers promptly and safely. Use navigation apps, maintain vehicle cleanliness, and ensure food temperature is maintained during transport.",
        "required_skills": ["Driving", "Customer Service", "Food Safety"],
        "required_certifications": ["Driver's License"]
    },
    {
        "title": "Digital Marketing Coordinator",
        "role": "Marketing Specialist",
        "company": "BrandBoost Agency",
        "location": "San Francisco, CA",
        "description": "Manage digital marketing campaigns for food service clients. Create content, analyze metrics, and optimize social media presence.",
        "required_skills": ["Marketing", "Customer Service", "Food Safety"],
        "required_certifications": ["Marketing Certification"]
    },
    {
        "title": "Kitchen Manager",
        "role": "Chef",
        "company": "Fine Dining Restaurant",
        "location": "Boston, MA",
        "description": "Oversee kitchen operations, manage staff, and ensure food quality standards. Coordinate with suppliers, manage inventory, and train kitchen personnel.",
        "required_skills": ["Cooking", "Food Safety", "Inventory Management"],
        "required_certifications": ["Food Handler Certification"]
    },
    {
        "title": "Food Safety Auditor",
        "role": "Food Safety Inspector",
        "company": "Quality Assurance Partners",
        "location": "Atlanta, GA",
        "description": "Conduct comprehensive food safety audits at client locations. Review procedures, test samples, and provide recommendations for improvement.",
        "required_skills": ["Food Safety", "Inventory Management"],
        "required_certifications": ["Food Safety Certification"]
    },
    {
        "title": "Restaurant Cashier",
        "role": "Cashier",
        "company": "Family Diner",
        "location": "Dallas, TX",
        "description": "Greet customers, take orders, process payments, and handle cash transactions. Maintain a friendly atmosphere and ensure customer satisfaction.",
        "required_skills": ["Customer Service", "Cash Handling", "Food Safety"],
        "required_certifications": ["Food Handler Certification"]
    },
    {
        "title": "Food Truck Driver",
        "role": "Driver",
        "company": "Mobile Meals Co.",
        "location": "Las Vegas, NV",
        "description": "Drive food truck to various locations, serve customers, and handle transactions. Maintain vehicle, ensure food safety, and provide excellent service.",
        "required_skills": ["Driving", "Customer Service", "Food Safety"],
        "required_certifications": ["Driver's License"]
    },
    {
        "title": "Compliance Inspector",
        "role": "Fire Safety Inspector",
        "company": "Safety First Services",
        "location": "Minneapolis, MN",
        "description": "Inspect commercial kitchens for fire safety compliance. Test gas equipment, verify code compliance, and issue inspection reports.",
        "required_skills": ["Gas leak tests", "City code adherence"],
        "required_certifications": ["CGLI Inspector"]
    }
]

def delete_all_jobs():
    """Delete all existing jobs from the API."""
    headers = {
        "x-api-key": API_KEY
    }
    
    try:
        print("Deleting all existing jobs...")
        response = requests.delete(f"{API_URL}/jobs", headers=headers, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            count = result.get('message', '').split()[0] if 'message' in result else '0'
            print(f"✓ {result.get('message', 'Jobs deleted successfully')}")
            return True
        else:
            print(f"✗ Failed to delete jobs: {response.status_code} - {response.text}")
            return False
            
    except Exception as e:
        print(f"✗ Error deleting jobs: {str(e)}")
        return False

def post_jobs():
    """Post all new jobs to the API."""
    headers = {
        "Content-Type": "application/json",
        "x-api-key": API_KEY
    }
    
    success_count = 0
    error_count = 0
    
    print(f"\nPosting {len(new_jobs)} new jobs...")
    print("=" * 60)
    
    for i, job in enumerate(new_jobs, 1):
        try:
            response = requests.post(
                f"{API_URL}/jobs",
                headers=headers,
                json=job,
                timeout=30
            )
            
            if response.status_code == 201:
                result = response.json()
                job_id = result.get('job', {}).get('id', 'unknown')
                print(f"✓ Job {i}/{len(new_jobs)}: '{job['title']}' created (ID: {job_id})")
                success_count += 1
            else:
                print(f"✗ Job {i}/{len(new_jobs)}: '{job['title']}' failed - {response.status_code}: {response.text}")
                error_count += 1
                
        except Exception as e:
            print(f"✗ Job {i}/{len(new_jobs)}: '{job['title']}' error - {str(e)}")
            error_count += 1
    
    print("=" * 60)
    print(f"\nSummary: {success_count} successful, {error_count} failed")
    
    return success_count, error_count

def main():
    """Main function to replace all jobs."""
    print("=" * 60)
    print("Replace All Jobs Script")
    print(f"API URL: {API_URL}")
    print("=" * 60)
    
    # Step 1: Delete all existing jobs
    if not delete_all_jobs():
        print("\n⚠ Warning: Failed to delete existing jobs. Continuing anyway...")
    
    # Step 2: Post new jobs
    success_count, error_count = post_jobs()
    
    # Final summary
    print("\n" + "=" * 60)
    if error_count == 0:
        print("✓ All jobs replaced successfully!")
    else:
        print(f"⚠ Completed with {error_count} error(s)")
    print("=" * 60)

if __name__ == "__main__":
    main()

