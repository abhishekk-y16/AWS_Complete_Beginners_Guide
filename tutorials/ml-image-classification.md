# ML Image Classification (SageMaker)

TL;DR
- Train a simple image classifier using SageMaker built-in algorithms or a prebuilt notebook, then deploy an endpoint.

Prerequisites
- Labeled images in S3, IAM role for SageMaker with S3 access, notebook or Studio.

Steps
1. Upload data: `s3://bucket/train/` and `s3://bucket/validation/` with class folders.
2. Start SageMaker Studio/Notebook; use the Image Classification algorithm or a PyTorch/TensorFlow script.
3. Create Training Job: set input channels to S3 paths, instance type (e.g., `ml.p3.2xlarge` for GPU), and output S3 path.
4. Monitor training logs in CloudWatch; tune hyperparameters (learning rate, epochs).
5. Deploy Model: create endpoint with `ml.m5`/`ml.g4` instance; test with sample images using `invoke-endpoint`.

Cost notes
- Training/hosting instance hours dominate; shut down endpoints when idle or use Serverless Inference/Batch Transform.

Troubleshooting
- Training fails: verify channel paths and IAM role; check image dimensions; reduce batch size for OOM.
- Slow inference: enable model optimizations (TorchScript/ONNX) and right-size instance.

Checklist
- Data in S3, training job completes, endpoint returns predictions, endpoint autoscaling configured (optional).