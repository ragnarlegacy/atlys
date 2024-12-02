# Deployment Architecture and Design
1. Architecture Overview
The application consists of three main components deployed on Google Cloud Platform (GCP):
The entire infrastructure is provisioned using IaaC tool i.e., Terraform. It helps to reduce the infrastructure complexity of manual changes and provides traceable versioned changes using Github.

Frontend:

1. Hosted in a GCP Storage bucket configured for static website hosting.
2. The frontend interacts with the backend API over HTTP to perform CRUD operations on user data.

Backend:

1. A Python Flask API deployed on Google Cloud Instance
2. The backend connects to a Cloud SQL MySQL instance for persistent storage.
3. Implements RESTful endpoints for creating and retrieving user data.

Database:

1. A Cloud SQL MySQL instance for storing user information securely and reliably.
2. The backend accesses the database using a private IP connection within the same VPC for enhanced security.

# Key Design Decisions

Decouple Architecture:

The frontend, backend, and database are decoupled, enabling scalability and independent updates.

Use of GCP Services:

1. GCP Storage for simple and cost-effective hosting of the frontend.
2. Cloud SQL for a managed database solution, reducing operational overhead.

Security and Authentication:

1. Backend service is authenticated with a GCP service account using json key that has limited permissions (Compute Admin, SQL Admin).

# Challenges and Solutions

SSL Certificate Verification Errors Issue:
Encountered SSL errors while connecting the backend to database
Solution: Installed and configured certificates using the certifi package to enable secure communication. Download the mysql client certificate nd trying to create ssl handshake with it.

Integration Between Backend and Cloud SQL:

Authentication and authorization issue using service account while provisioning the infrastructure with Terraform
Solution: Use Service Account with compute admin, storage admin, iam admin and cloud sql admin permissions

Bucket URL: https://storage.googleapis.com/atlys-bucket-077/index.html