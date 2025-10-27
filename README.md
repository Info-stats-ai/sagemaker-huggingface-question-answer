# SageMaker LLMOps - Hugging Face Model Deployment

This project demonstrates how to deploy and use Hugging Face models on Amazon SageMaker for real-time inference.

## 🎯 Project Overview

This repository contains code for deploying a Hugging Face Question-Answering model (`distilbert-base-uncased-distilled-squad`) on Amazon SageMaker and performing real-time inference.

## 🚀 Features

- ✅ SageMaker Unified Studio setup with SSO authentication
- ✅ Hugging Face model deployment on SageMaker endpoints
- ✅ Real-time question-answering inference
- ✅ Extractive QA from context passages
- ✅ Cost-optimized instance management

## 📋 Prerequisites

- AWS Account with appropriate permissions
- IAM Identity Center (AWS SSO) configured
- SageMaker Unified Studio domain created
- Python 3.9+
- Required AWS services access:
  - Amazon SageMaker
  - Amazon S3
  - IAM roles

## 🏗️ Architecture

```
User Query → SageMaker Endpoint → Hugging Face Model → Answer Extraction
                ↓
            S3 Bucket (Model Artifacts)
```

## 📦 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/sagemaker_LLMops.git
cd sagemaker_LLMops
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure AWS Credentials

```bash
aws configure
# Or use SSO:
aws configure sso
```

## 🔧 Project Structure

```
sagemaker_LLMops/
├── notebooks/
│   ├── getting_started.ipynb          # Introduction to SageMaker
│   ├── huggingface_deployment.ipynb   # Model deployment code
│   └── model_inference.ipynb          # Testing and inference
├── src/
│   ├── deploy_model.py                # Deployment script
│   └── test_endpoint.py               # Testing utilities
├── config/
│   └── model_config.json              # Model configuration
├── requirements.txt                   # Python dependencies
└── README.md                          # This file
```

## 💻 Usage

### Deploy Hugging Face Model

```python
from sagemaker.huggingface.model import HuggingFaceModel

# Model configuration
hub = {
    "HF_MODEL_ID": "distilbert-base-uncased-distilled-squad",
    "HF_TASK": "question-answering"
}

# Create and deploy model
huggingface_model = HuggingFaceModel(
    env=hub,
    role=role,
    transformers_version="4.26",
    pytorch_version="1.13",
    py_version="py39"
)

predictor = huggingface_model.deploy(
    initial_instance_count=1,
    instance_type="ml.m5.xlarge"
)
```

### Run Inference

```python
# Prepare input data
data = {
    "inputs": {
        "question": "What is Amazon SageMaker?",
        "context": "Amazon SageMaker is a fully managed machine learning service. With SageMaker, data scientists and developers can quickly build and train machine learning models, and then deploy them into a production-ready hosted environment."
    }
}

# Get prediction
response = predictor.predict(data)
print(f"Answer: {response['answer']}")
print(f"Confidence: {response['score']:.2%}")
```

### Clean Up Resources

```python
# Delete endpoint to stop charges
predictor.delete_endpoint(delete_endpoint_config=False)
```

## 🤖 Supported Models

This project demonstrates Question-Answering, but can be adapted for:

- **Text Generation**: GPT-2, GPT-Neo
- **Sentiment Analysis**: BERT, RoBERTa
- **Text Summarization**: BART, T5
- **Named Entity Recognition**: BERT-NER
- **Translation**: MarianMT, T5

## 💰 Cost Optimization

### Instance Pricing (us-east-1)

| Instance Type | vCPU | Memory | Cost/Hour | Best For |
|---------------|------|--------|-----------|----------|
| ml.t3.medium  | 2    | 4 GB   | $0.05     | Testing/Development |
| ml.m5.large   | 2    | 8 GB   | $0.115    | Light production |
| ml.m5.xlarge  | 4    | 16 GB  | $0.23     | Production workloads |
| ml.g4dn.xlarge| 4    | 16 GB  | $0.74     | GPU inference |

### Cost Saving Tips

✅ **Always delete endpoints** when not in use  
✅ **Use smaller instances** for testing (ml.t3.medium)  
✅ **Enable auto-scaling** for variable traffic  
✅ **Use batch transform** for large datasets instead of real-time endpoints  
✅ **Monitor CloudWatch** for endpoint utilization  

## 🔐 Security & IAM

### Required IAM Permissions

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sagemaker:*",
                "s3:GetObject",
                "s3:PutObject",
                "s3:ListBucket",
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "*"
        }
    ]
}
```

## 📊 Model Performance

### DistilBERT Question Answering

- **Model Size**: 66M parameters
- **Inference Latency**: ~50-100ms (ml.m5.xlarge)
- **Accuracy**: 86.9 F1 on SQuAD v1.1
- **Context Length**: Up to 512 tokens

## 🐛 Troubleshooting

### Common Issues

**1. Permission Denied Errors**
```bash
# Solution: Add SageMaker execution permissions to your IAM role
# Navigate to IAM → Roles → Add AmazonSageMakerFullAccess policy
```

**2. Endpoint Creation Timeout**
```bash
# Solution: Check CloudWatch logs for detailed error messages
# Ensure instance limits are not exceeded in your AWS account
```

**3. Out of Memory Errors**
```bash
# Solution: Use a larger instance type (e.g., ml.m5.2xlarge)
# Or reduce batch size in inference requests
```

## 📚 Resources

- [Amazon SageMaker Documentation](https://docs.aws.amazon.com/sagemaker/)
- [Hugging Face Models](https://huggingface.co/models)
- [SageMaker Python SDK](https://sagemaker.readthedocs.io/)
- [AWS Machine Learning Blog](https://aws.amazon.com/blogs/machine-learning/)

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Omkarnath Thakur**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: othakur@umd.edu

## 🙏 Acknowledgments

- Amazon Web Services for SageMaker platform
- Hugging Face for pre-trained models
- The open-source ML community

## 📈 Future Enhancements

- [ ] Add CI/CD pipeline with GitHub Actions
- [ ] Implement A/B testing for model versions
- [ ] Add model monitoring and drift detection
- [ ] Create REST API wrapper with FastAPI
- [ ] Add support for multi-model endpoints
- [ ] Implement caching for frequently asked questions
- [ ] Add Gradio/Streamlit UI for demo

## 📞 Support

For questions or issues, please:
1. Check the [Troubleshooting](#-troubleshooting) section
2. Open an [Issue](https://github.com/yourusername/sagemaker_LLMops/issues)
3. Refer to [AWS Support](https://aws.amazon.com/support/)

---

**⚠️ Important**: Remember to delete SageMaker endpoints when not in use to avoid unexpected charges!

**Made with ❤️ using Amazon SageMaker and Hugging Face**

