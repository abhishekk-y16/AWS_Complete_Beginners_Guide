# Lambda Layers 📦

Reuse code across multiple Lambda functions with layers.

## What is a Lambda Layer?

A **Lambda Layer** is a package of libraries, custom code, or other dependencies that you can use with Lambda functions.

```
Without Layers:
├─ Function A: 50MB (30MB code + 20MB libraries)
├─ Function B: 50MB (30MB code + 20MB libraries)
└─ Function C: 50MB (30MB code + 20MB libraries)
Total: 150MB (duplicated dependencies!)

With Layers:
├─ Shared Layer: 20MB (shared libraries)
├─ Function A: 30MB (just code) + Layer
├─ Function B: 30MB (just code) + Layer
└─ Function C: 30MB (just code) + Layer
Total: 110MB (saved 40MB!)
```

## Why Use Layers?

### 1. Code Reuse

```
Scenario: 10 Lambda functions need same libraries

Without layers:
├─ Each function: zip code + dependencies
├─ Each function package: 50MB
└─ Total: 500MB duplicated

With layers:
├─ Shared layer: dependencies (20MB)
├─ Each function: just code (5MB)
└─ Total: 20MB + 50MB = 70MB

Savings: 430MB (86% reduction!)
```

### 2. Faster Deployment

```
Without layers:
├─ Change library
├─ Update all 10 functions
└─ Deploy all 10 (time-consuming)

With layers:
├─ Change library
├─ Update 1 layer
├─ All 10 functions automatically use new version
└─ Much faster!
```

### 3. Organized Code

```
Typical structure:
├─ Shared Layer: Database, logging, utils
├─ Function A Layer: boto3 AWS SDK
├─ Function B Layer: requests HTTP lib
└─ Function code: Just business logic
```

## Layer Architecture

```
Layer Structure:
layer/
├─ python/          (for Python)
│  ├─ __pycache__/
│  └─ lib/
│     └─ python3.x/
│        └─ site-packages/
│           ├─ requests/
│           ├─ numpy/
│           └─ pandas/
└─ nodejs/ (for Node.js)
   └─ node_modules/
      ├─ express
      ├─ axios
      └─ lodash
```

## Creating a Python Layer

### Step 1: Create Layer Directory

```bash
mkdir -p python/lib/python3.x/site-packages
cd python
```

### Step 2: Install Dependencies

```bash
pip install requests pandas -t ./lib/python3.x/site-packages
```

Result:
```
python/
└─ lib/
   └─ python3.x/
      └─ site-packages/
         ├─ requests/
         └─ pandas/
```

### Step 3: Create ZIP

```bash
zip -r layer.zip python/
# Result: layer.zip (5MB)
```

### Step 4: Upload to Lambda

```python
import boto3

lambda_client = boto3.client('lambda')

with open('layer.zip', 'rb') as f:
    response = lambda_client.publish_layer_version(
        LayerName='my-requests-layer',
        Description='Requests HTTP library',
        ZipFile=f.read(),
        CompatibleRuntimes=['python3.9', 'python3.10']
    )

print(f"Layer ARN: {response['LayerVersionArn']}")
```

## Attaching Layers to Functions

### Method 1: AWS Console

```
Lambda function → Layers → Add layer
├─ Choose "Custom layers"
├─ Select "my-requests-layer"
└─ Click "Add"
```

### Method 2: Python Code

```python
lambda_client.update_function_configuration(
    FunctionName='my-function',
    Layers=['arn:aws:lambda:region:account:layer:my-requests-layer:1']
)
```

### Method 3: CloudFormation

```yaml
MyFunction:
  Type: AWS::Lambda::Function
  Properties:
    FunctionName: my-function
    Layers:
      - !Sub arn:aws:lambda:${AWS::Region}:${AWS::AccountId}:layer:my-requests-layer:1
```

## Layer Limitations

```
Size Limits:
├─ Unzipped layer: 262 MB max
├─ 250 MB max per function (with code)
└─ Multiple layers: Combined max 250 MB

Implications:
├─ Can't include video files
├─ Can't include datasets (use S3)
├─ Large ML models better in container
```

## Common Layer Use Cases

### Use Case 1: Shared Utilities

```python
# shared_utils.py (in layer)
def log_event(event):
    print(f"Event: {event}")

def parse_json(text):
    import json
    return json.loads(text)

# Function A (uses layer)
from shared_utils import log_event
def handler(event, context):
    log_event(event)
    return {"status": "ok"}
```

### Use Case 2: Database Connectors

```python
# Layer: mysql-connector

# Function A
import mysql.connector

def handler(event, context):
    conn = mysql.connector.connect(
        host="rds.amazonaws.com",
        user="admin",
        password="..."
    )
    # Query database
```

### Use Case 3: AWS SDK Extensions

```python
# Layer: enhanced-boto3

# Function A: Uses enhanced layer
from enhanced_boto3 import S3Helper

def handler(event, context):
    s3 = S3Helper()
    s3.upload_with_retry(bucket, key, data)
```

### Use Case 4: Monitoring & Logging

```python
# Layer: monitoring

# Function A
from monitoring import CloudWatch, trace

@trace()  # Decorator from layer
def handler(event, context):
    CloudWatch.log_event(event)
    return {"status": "ok"}
```

## Versioning Layers

```
Create new layer:
├─ Layer: my-lib v1 (first version)
├─ Layer: my-lib v2 (update)
└─ Layer: my-lib v3 (latest)

Functions can use:
├─ Function A: v1 (old version, stable)
├─ Function B: v2 (middle version)
└─ Function C: v3 (latest features)

Benefit: Gradual rollout, easy rollback
```

## Layer Organization Best Practices

### Small, Focused Layers

```
Bad:
└─ mega-layer (100MB)
   ├─ requests
   ├─ pandas
   ├─ numpy
   ├─ boto3
   └─ django

Good:
├─ requests-layer (2MB)
├─ data-science-layer (50MB)
│  ├─ pandas
│  └─ numpy
├─ aws-utils-layer (5MB)
└─ web-layer (20MB)
   └─ django
```

### Environment-Based Layers

```
Development:
├─ dev-layer (includes testing, debug tools)
└─ 15MB

Production:
├─ prod-layer (optimized, minimal)
└─ 8MB

Deploy different layer per environment
```

## Performance Considerations

```
Layer Loading Time:
├─ First invocation: Extract layer (100-500ms)
├─ Subsequent invocations: Cached (5-10ms)
└─ Total overhead: Usually minimal

Multiple Layers:
├─ 1 layer: ~100ms overhead
├─ 3 layers: ~150ms overhead
├─ 5 layers: ~250ms overhead
└─ Recommendation: Keep under 5 layers
```

## Cost Implications

```
Layer Storage:
├─ Layer: 50MB
├─ Storage: $0.50 per 1GB/month
├─ Cost: ~$0.025/month (negligible)
└─ No additional deployment cost

Benefit: Reduced code size = faster deployment
```

## Common Mistakes

### ✗ Mistake 1: Wrong Directory Structure

```
Wrong:
└─ layer.zip
   ├─ requests/
   ├─ pandas/
   └─ numpy/

Right:
└─ layer.zip
   └─ python/
      └─ lib/
         └─ python3.x/
            └─ site-packages/
               ├─ requests/
               ├─ pandas/
               └─ numpy/
```

### ✗ Mistake 2: Mixing Runtime Types

```
Wrong:
└─ Layer with both Python + Node.js
   ├─ python/lib/requests
   └─ nodejs/node_modules/express

Right:
└─ Layer (Python only)
   └─ python/lib/requests

OR:
└─ Layer (Node.js only)
   └─ nodejs/node_modules/express
```

### ✗ Mistake 3: Layer Too Large

```
Wrong:
└─ mega-layer (200MB)
   └─ Everything including datasets

Problem: Exceeds size limits
Solution: Use S3 for large files, layer for libraries

Right:
├─ Layer (50MB): Libraries only
└─ Function fetches data from S3
```

### ✗ Mistake 4: Not Versioning Layers

```
Wrong:
└─ Always overwrite existing layer version

Problem: Can't rollback, hard to debug

Right:
├─ Layer v1
├─ Layer v2
└─ Layer v3
└─ Functions explicitly choose version
```

## Sharing Layers Across Accounts

```
Share read-only:
├─ Create layer in Account A
├─ Add resource policy
└─ Grant Account B read permission

Account B can:
├─ Use layer ARN: arn:aws:lambda:region:ACCOUNT_A:layer:name:version
└─ No copy needed (reference only)
```

## Monitoring Layers

```
Track layer usage:
└─ CloudWatch Logs
   ├─ See which functions use which layer
   ├─ Monitor layer performance
   └─ Alert on layer errors
```

## Migration to Layers

### If Currently Using Package

```
Before:
├─ Function 1: 50MB (code + deps)
├─ Function 2: 50MB (code + deps)
└─ Function 3: 50MB (code + deps)

After:
├─ Layer: 20MB (deps)
├─ Function 1: 30MB (code only)
├─ Function 2: 30MB (code only)
└─ Function 3: 30MB (code only)

Savings: 50MB, deployment faster
```

## Best Practices

✅ Create focused, single-purpose layers
✅ Keep layer size under 50MB
✅ Version all layers
✅ Document layer dependencies
✅ Test layer compatibility
✅ Use descriptive layer names
✅ Remove unused layers
✅ Monitor layer usage
✅ Automate layer creation with CI/CD
✅ Share common layers across org

## Next Steps

→ [What is Lambda](./what-is-lambda.md) - Lambda basics
→ [Triggers](./triggers.md) - Lambda event sources
→ [Use Cases](./use-cases.md) - Real-world examples
→ [Pricing](./pricing.md) - Cost optimization