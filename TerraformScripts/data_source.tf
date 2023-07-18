data "aws_lambda_invocation" "event" {
  function_name = aws_lambda_function.terraform_lambda_func.function_name

  input = <<JSON
{
  "key1": "value1",
  "key2": "value2"
}
JSON
}

output "result_entry" {
  value = jsondecode(data.aws_lambda_invocation.event.result)["key1"]
}