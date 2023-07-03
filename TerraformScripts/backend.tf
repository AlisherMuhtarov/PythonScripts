terraform {
  backend "s3" {
    bucket = "terraform-testing-backend-alisher"
    key    = "session-10/terraform.tfstate"  # Where does terraform need to store your file. Path Or Prefix
    region = "us-east-1"
    dynamodb_table = "terraform-testing-state-lock"  # Lock Table
  }
}
