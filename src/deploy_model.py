"""
SageMaker Hugging Face Model Deployment Script
Author: Omkarnath Thakur
Description: Deploy Hugging Face models to SageMaker endpoints
"""

import sagemaker
import boto3
from sagemaker.huggingface.model import HuggingFaceModel


def get_sagemaker_session():
    """
    Initialize and return SageMaker session with proper configuration
    
    Returns:
        tuple: (session, role, bucket)
    """
    session = sagemaker.Session()
    
    # Get default S3 bucket
    sagemaker_session_bucket = session.default_bucket()
    
    # Get execution role
    try:
        role = sagemaker.get_execution_role()
    except ValueError:
        iam = boto3.client("iam")
        role = iam.get_role(RoleName="sagemaker_execution_role")["Role"]["Arn"]
    
    print(f"✅ SageMaker Role ARN: {role}")
    print(f"✅ SageMaker Region: {session.boto_region_name}")
    print(f"✅ S3 Bucket: {sagemaker_session_bucket}")
    
    return session, role, sagemaker_session_bucket


def deploy_huggingface_model(
    model_id="distilbert-base-uncased-distilled-squad",
    task="question-answering",
    instance_type="ml.m5.xlarge",
    instance_count=1,
    transformers_version="4.26",
    pytorch_version="1.13",
    python_version="py39"
):
    """
    Deploy a Hugging Face model to SageMaker endpoint
    
    Args:
        model_id (str): Hugging Face model ID from hub
        task (str): NLP task type
        instance_type (str): EC2 instance type for endpoint
        instance_count (int): Number of instances
        transformers_version (str): Transformers library version
        pytorch_version (str): PyTorch version
        python_version (str): Python version
    
    Returns:
        predictor: SageMaker predictor object for inference
    """
    # Get SageMaker session and role
    session, role, bucket = get_sagemaker_session()
    
    # Model configuration
    hub_config = {
        "HF_MODEL_ID": model_id,
        "HF_TASK": task
    }
    
    print(f"\n🚀 Deploying model: {model_id}")
    print(f"📋 Task: {task}")
    print(f"💻 Instance: {instance_type} × {instance_count}")
    
    # Create Hugging Face Model
    huggingface_model = HuggingFaceModel(
        env=hub_config,
        role=role,
        transformers_version=transformers_version,
        pytorch_version=pytorch_version,
        py_version=python_version
    )
    
    # Deploy to endpoint
    print("\n⏳ Deploying endpoint (this takes 5-10 minutes)...")
    predictor = huggingface_model.deploy(
        initial_instance_count=instance_count,
        instance_type=instance_type
    )
    
    print(f"\n✅ Endpoint deployed successfully!")
    print(f"📍 Endpoint name: {predictor.endpoint_name}")
    
    return predictor


def test_question_answering(predictor, question, context):
    """
    Test the deployed Q&A model
    
    Args:
        predictor: SageMaker predictor object
        question (str): Question to ask
        context (str): Context passage containing the answer
    
    Returns:
        dict: Prediction result with answer and score
    """
    data = {
        "inputs": {
            "question": question,
            "context": context
        }
    }
    
    print(f"\n❓ Question: {question}")
    print(f"📝 Context: {context[:100]}...")
    
    response = predictor.predict(data)
    
    print(f"\n✅ Answer: {response['answer']}")
    print(f"📊 Confidence: {response['score']:.2%}")
    
    return response


def delete_endpoint(predictor):
    """
    Delete SageMaker endpoint to stop charges
    
    Args:
        predictor: SageMaker predictor object
    """
    endpoint_name = predictor.endpoint_name
    print(f"\n🗑️  Deleting endpoint: {endpoint_name}")
    
    try:
        predictor.delete_endpoint(delete_endpoint_config=False)
        print("✅ Endpoint deleted successfully!")
        print("💰 Charges stopped")
    except Exception as e:
        print(f"⚠️  Error deleting endpoint: {e}")
        print("💡 Try deleting from AWS Console instead")


def main():
    """
    Main execution function
    """
    print("="*70)
    print("🤗 SageMaker Hugging Face Model Deployment")
    print("="*70)
    
    # Deploy model
    predictor = deploy_huggingface_model(
        model_id="distilbert-base-uncased-distilled-squad",
        task="question-answering",
        instance_type="ml.m5.xlarge"
    )
    
    # Test the model
    test_question_answering(
        predictor,
        question="What is Amazon SageMaker?",
        context="Amazon SageMaker is a fully managed machine learning service. "
                "With SageMaker, data scientists and developers can quickly build "
                "and train machine learning models, and then deploy them into a "
                "production-ready hosted environment."
    )
    
    # Ask user if they want to delete endpoint
    print("\n" + "="*70)
    user_input = input("Do you want to delete the endpoint? (yes/no): ")
    
    if user_input.lower() in ['yes', 'y']:
        delete_endpoint(predictor)
    else:
        print(f"\n⚠️  Endpoint still running: {predictor.endpoint_name}")
        print("💰 Remember to delete it later to avoid charges!")
        print(f"   Run: predictor.delete_endpoint()")


if __name__ == "__main__":
    main()

