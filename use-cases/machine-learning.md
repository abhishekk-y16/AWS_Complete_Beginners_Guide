# Machine Learning

What it is
- Train and deploy ML models using managed infrastructure.

Recommended stack
- Data in S3; labeling with Ground Truth; training/hosting on SageMaker; monitoring with Model Monitor.

Quick start
1. Prepare data in S3; use built-in algorithms or custom containers.
2. Train in SageMaker (spot where possible); evaluate metrics.
3. Deploy endpoint or Batch Transform; add auto-scaling and monitoring.

Cost snapshot
- Training/hosting instances dominate; shut down endpoints when idle.

Success metrics
- Model accuracy/latency, cost per 1k predictions, drift alerts.