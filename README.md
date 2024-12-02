# User Demo

# <h4>Prerequisites</h4>
<ul>Google Cloud Account</ul>
<ul>Download Google cloud cli</ul>
<ul>Download Python3</ul>

# <h4>Download python dependencies and libraries<h4>
<ul>pip3 install flask google-cloud-storage cloud-sql-python-connector mysql-connector-python python-dotenv</ul>

# <h4>Create Project ID in GCP CLoud Account</h4>
Console > New Project

# <h4>Create Service Account attach below policy</h4>
<ul>Compute Admin</ul>
<ul>Cloud Storage Admin</ul>
<ul>IAM admin</ul>
<ul>Cloud SQL Admin</ul>

# <h4>Enable API's</h4>
<ul>Compute Engine API</ul>
<ul>Cloud Storage API</ul>
<ul>IAM API</ul>
<ul>Cloud SQL Admin API</ul>

# <h4>Authenticate Using gcloud</h4>
<ul> gcloud auth login </ul>

# <h4>Clone the Source Code</h4>
<br>git clone https://github.com/ragnarlegacy/atlys.git</br>


# <h4>Go to Terraform Folder to provision infrastructure over GCP Cloud and execute below commands</h4>
<ul>cd Terraform</ul>
<ul>terraform init</ul>
<ul>terraform plan</ul>
<ul>terraform apply</ul>

# <h4>Upload the static content to provisioned storage bucket</h4>

# <h4>Clone the Source Code on backend instance</h4>
git clone https://github.com/ragnarlegacy/atlys.git

# Go back to root folder 
cd ../
python3 app.py

# The python server starts
Open http://machine_ip:5000 in your browser to see the frontend served from Google Cloud Storage.


