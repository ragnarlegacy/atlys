terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "6.12.0"
    }
  }
}

provider "google" {
  credentials = file("ragnar-07-8f816f54d8e2.json")
  project = var.PROJECT_ID
  region  = var.region
  zone    = var.zone
}