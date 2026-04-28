def lambda_handler(event, context):
 password = "12345" # Vulnerability
 return {
 'statusCode': 200,
 'body': 'Hello from Secure CI/CD Pipeline!'
 }