from flask import Flask, request, jsonify, Response
from google.cloud import storage
import os
from db import create_user, get_all_users

# from google.auth.transport.requests import AuthorizedSession
# from google.oauth2 import service_account

# Path to your service account key
# service_account_path = "/Users/ragnarlothbrok/Desktop/atlys/Terraform/ragnar-07-8f816f54d8e2.json"

# # Authenticate
# credentials = service_account.Credentials.from_service_account_file(service_account_path)
# authed_session = AuthorizedSession(credentials)

# # Use the session to make requests
# response = authed_session.get("https://www.googleapis.com/auth/cloud-platform")


class UserApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.bucket_name = os.getenv("GCS_BUCKET_NAME", "atlys-bucket-077")
        self.setup_routes()

    def setup_routes(self):
        self.app.add_url_rule("/", "serve_frontend", self.serve_frontend, methods=["GET"])
        self.app.add_url_rule("/users", "add_user", self.add_user, methods=["POST"])
        self.app.add_url_rule("/users", "get_users", self.get_users, methods=["GET"])

    def get_gcs_client(self):
        """
        Initialize and return a Google Cloud Storage client.
        """
        return storage.Client()

    def fetch_file_from_gcs(self, file_name):
        """
        Fetch a file from the Google Cloud Storage bucket.
        """
        try:
            client = self.get_gcs_client()
            bucket = client.bucket(self.bucket_name)
            blob = bucket.blob(file_name)
            if not blob.exists():
                return None, f"File {file_name} not found in bucket {self.bucket_name}."
            return blob.download_as_bytes(), None
        except Exception as e:
            return None, str(e)

    def serve_frontend(self):
        """
        Serve the `index.html` file from the GCS bucket.
        """
        file_name = "index.html"
        file_content, error = self.fetch_file_from_gcs(file_name)
        if error:
            return jsonify({"error": error}), 500
        return Response(file_content, content_type="text/html")

    def add_user(self):
        """
        Add a new user to the database from the request JSON.
        """
        data = request.json
        if not data or not data.get("name") or not data.get("email"):
            return jsonify({"error": "Invalid input"}), 400

        try:
            create_user(data["name"], data["email"])
            return jsonify({"message": "User added successfully!"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def get_users(self):
        """
        Retrieve all users from the database.
        """
        try:
            users = get_all_users()
            return jsonify(users), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def run(self, host="0.0.0.0", port=9000):
        self.app.run(host=host, port=port)


if __name__ == "__main__":
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/ragnarlothbrok/Desktop/atlys/Terraform/ragnar-07-8f816f54d8e2.json"
    app = UserApp()
    app.run()
