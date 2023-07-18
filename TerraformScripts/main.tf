resource "aws_iam_role" "lambda_role" {
 name   = "lambda_function_role"
 assume_role_policy = jsonencode(
{
 "Version": "2012-10-17",
 "Statement": [
   {
     "Action": "sts:AssumeRole",
     "Principal": {
       "Service": "lambda.amazonaws.com"
     },
     "Effect": "Allow",
     "Sid": ""
   }
 ]
}
)
}

resource "aws_iam_policy" "iam_policy_for_lambda" {
 
 name         = "aws_iam_policy_for_terraform_aws_lambda_role"
 path         = "/"
 description  = "AWS IAM Policy for managing aws lambda role"

policy = jsonencode({
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "ec2:*"
      ],
      "Resource": "*"
    }
  ]
})
}

resource "aws_iam_role_policy_attachment" "attach_iam_policy_to_iam_role" {
 role        = aws_iam_role.lambda_role.name
 policy_arn  = aws_iam_policy.iam_policy_for_lambda.arn
}

data "archive_file" "zip_the_python_code" {
 type        = "zip"
 source_dir  = "/home/ec2-user/PythonScripts/TerraformScripts/lambda_function/"
 output_path = "/home/ec2-user/PythonScripts/TerraformScripts/lambda_function/lambda_function.zip"
}

resource "aws_lambda_function" "terraform_lambda_func" {
 filename                       = data.archive_file.zip_the_python_code.output_path
 function_name                  = "ec2_create_function"
 role                           = aws_iam_role.lambda_role.arn
 handler                        = "lambda_function.lambda_handler"
 runtime                        = "python3.9"
 timeout                        = "15"
 depends_on                     = [aws_iam_role_policy_attachment.attach_iam_policy_to_iam_role]

resource "aws_lambda_invocation" "event" {
  function_name = aws_lambda_function.terraform_lambda_func.function_name

  input = jsonencode({
    key1 = "value1"
    key2 = "value2"
  })
}
output "result_entry" {
  value = jsondecode(aws_lambda_invocation.event.result)["key1"]
}
#  provisioner "local-exec" {
#   command = <<-EOT
#     sudo yum install -y python3-pip
#     sudo pip3 install boto3 -t /home/ec2-user/PythonScripts/TerraformScripts/lambda_function/
#   EOT
# }
}