resource "google_compute_instance" "backend_instance" {
  name         = var.backend
  machine_type = var.machine_type
  zone         = var.zone

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network    = google_compute_network.vpc.name
    subnetwork = google_compute_subnetwork.app_subnet.name
    access_config {} # Enable external access
  }

  metadata_startup_script = <<-EOT
    #! /bin/bash
    sudo apt-get update
    sudo apt-get install -y python3 python3-pip
    pip3 install flask mysql-connector-python
  EOT
}
