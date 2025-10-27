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

├── src/
│   ├── deploy_model.py                # Deployment script         
├── config/
│   └── model_config.json              # Model configuration
├── requirements.txt                   # Python dependencies
└── README.md                          # This file
```

## 🤖 Supported Models

This project demonstrates Question-Answering, but can be adapted for:

- **Text Generation**: GPT-2, GPT-Neo
- **Sentiment Analysis**: BERT, RoBERTa
- **Text Summarization**: BART, T5
- **Named Entity Recognition**: BERT-NER
- **Translation**: MarianMT, T5

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



---

**⚠️ Important**: Remember to delete SageMaker endpoints when not in use to avoid unexpected charges!

**Made with ❤️ using Amazon SageMaker and Hugging Face**

