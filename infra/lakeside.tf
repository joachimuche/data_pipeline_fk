resource "aws_s3_bucket" "regional_data_lake" {
  bucket = "raw-data-regional"

  tags = {
    Team        = "Data Engineers"
    Manage_by_terraform = "True"
    service = "Airflow"
  }
}