# Bedrock Chatbot

TL;DR
- Build a serverless chatbot using Amazon Bedrock (or generative models) and API Gateway.
- Use Lambda to proxy user messages to model endpoints and store transcripts in DynamoDB.
- Keep prompts simple, sanitize user input, and manage tokens/quotas.
- Use Cognito or API keys for authentication.
- Log interactions and sample responses to tune prompts.
- Start with a small model and iterate on prompt engineering.

Prerequisites
- AWS account with Bedrock access (or a supported foundation model service).
- AWS CLI configured, IAM role for Lambda with Bedrock/DynamoDB permissions.
- Basic knowledge of Lambda, API Gateway, and DynamoDB.

Steps
1. Create a DynamoDB table for sessions:
```
aws dynamodb create-table --table-name ChatSessions --attribute-definitions AttributeName=sessionId,AttributeType=S --key-schema AttributeName=sessionId,KeyType=HASH --billing-mode PAY_PER_REQUEST
```
2. Create a Lambda function (Node/Python) that accepts a message, calls Bedrock, and saves the transcript.
3. In Lambda, call the model endpoint (pseudo):
```
response = bedrock_client.invoke_model(ModelId='model-name', InputText=user_input)
```
4. Create API Gateway HTTP API and a POST /chat route integrated with the Lambda.
5. Secure the API with API keys, Cognito, or IAM authorizers.
6. Deploy, test with curl or Postman, and refine prompt templates.

Cost notes
- Costs include Bedrock model inference, Lambda compute, API Gateway requests, and DynamoDB storage. Model inference is the main variable.

Quick troubleshooting
- No model response: check Bedrock quotas and Lambda execution role.
- Slow responses: increase Lambda timeout and monitor model latency.
- Authentication errors: verify API Gateway authorizer and IAM role policies.

Checklist
- API Gateway + Lambda integrated and secured.
- DynamoDB stores transcripts properly.
- Model calls succeed and response quality is acceptable.
# Tutorials

AWS Tutorials service