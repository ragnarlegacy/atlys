
resource "google_compute_network" "vpc" {
  name = var.vpc
}

resource "google_compute_subnetwork" "app_subnet" {
  name          = "app-subnet"
  ip_cidr_range = var.app_subnet_cidr
  network       = google_compute_network.vpc.name
  region        = var.region
}

resource "google_compute_subnetwork" "db_subnet" {
  name          = "db-subnet"
  ip_cidr_range = var.db_subnet_cidr
  network       = google_compute_network.vpc.name
  region        = var.region
}

resource "google_compute_firewall" "allow_http_https" {
  name    = "allow-http-https"
  network = google_compute_network.vpc.name

  allow {
    protocol = "tcp"
    ports    = ["80", "443"]
  }

  source_ranges = ["0.0.0.0/0"]
}

resource "google_compute_firewall" "allow_mysql" {
  name    = "allow-mysql"
  network = google_compute_network.vpc.name

  allow {
    protocol = "tcp"
    ports    = ["3306"]
  }

  source_ranges = ["10.0.0.0/16"]
}

