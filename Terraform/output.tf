
output "vpc_name" {
  value = google_compute_network.vpc.name
}

output "app_subnet" {
  value = google_compute_subnetwork.app_subnet.self_link
}

output "db_subnet" {
  value = google_compute_subnetwork.db_subnet.self_link
}

# Outputs
output "frontend_url" {
  value = "http://${google_storage_bucket.frontend.name}.storage.googleapis.com"
}

output "backend_ip" {
  value = google_compute_instance.backend_instance.network_interface[0].access_config[0].nat_ip
}

output "cloud_sql_connection" {
  value = google_sql_database_instance.cloud_sql.connection_name
}