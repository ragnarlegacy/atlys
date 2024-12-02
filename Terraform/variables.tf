variable "PROJECT_ID" {
    type = string
    default = "ragnar-07"
}
variable "vpc" {
    default = "atlys-vpc" 
}

variable "region" {
    type = string
    default = "us-central1"
}

variable "zone" {
    type = string
    default = "us-central1-c"
  
}

variable "frontend" {
    default = "atlys-bucket-077"
  
}

variable "backend" {
    default = "backend-instance"
  
}

variable "machine_type" {
    default = "e2-medium"
  
}

variable "db" {
    default = "atlysdb" 
}

variable "app_subnet_cidr" {
  description = "CIDR range for the application subnet"
  default     = "10.0.1.0/24"
}

variable "db_subnet_cidr" {
  description = "CIDR range for the database subnet"
  default     = "10.0.2.0/24"
}