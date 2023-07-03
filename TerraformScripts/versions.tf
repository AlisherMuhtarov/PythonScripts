terraform {
  required_version = "~> 1.3.7" # Terraform Version
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.53.0" # AWS Provider
    }
  }
}