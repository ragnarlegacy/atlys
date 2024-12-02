resource "google_sql_database_instance" "cloud_sql" {
  name             = var.db
  database_version = "MYSQL_8_0"
  settings {
    tier = "db-f1-micro"
  }
  deletion_protection  = true
}

resource "google_sql_database" "user_db" {
  name     = "user_db"
  instance = google_sql_database_instance.cloud_sql.name
}

resource "google_sql_user" "db_user" {
  instance   = google_sql_database_instance.cloud_sql.name
  name       = "admin"
  password   = "password123"
}

# resource "google_sql_user" "iam_service_account_user" {
#   # Note: for Postgres only, GCP requires omitting the ".gserviceaccount.com" suffix
#   # from the service account email due to length limits on database usernames.
#   name     = "109888480994-compute@developer.gserviceaccount.com"
#   instance = google_sql_database_instance.cloud_sql.name
#   type     = "CLOUD_IAM_SERVICE_ACCOUNT"
# }
