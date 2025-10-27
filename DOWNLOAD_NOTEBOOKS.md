# 📥 Download Your Notebooks from SageMaker

## Quick Steps

### Method 1: Direct Download from JupyterLab (Recommended)

1. **Open your SageMaker Unified Studio project**
   - Go to: https://studio.us-east-1.sagemaker.aws/
   - Navigate to your `Huggingface_model` project
   - Click on the notebook to open JupyterLab

2. **Download each notebook:**
   - In JupyterLab, look at the **left sidebar** (file browser)
   - Find your notebook file (e.g., `getting_started.ipynb`)
   - **Right-click** on the file
   - Select **"Download"**
   - Save to: `/Users/omkarthakur/Desktop/sagemaker_LLMops/notebooks/`

3. **Repeat for all files:**
   - Download all `.ipynb` files
   - Also download any `.py` scripts you created
   - Download any data files (if small enough for GitHub)

---

### Method 2: Using AWS CLI (Advanced)

```bash
# Navigate to project directory
cd /Users/omkarthakur/Desktop/sagemaker_LLMops

# List files in your S3 bucket
aws s3 ls s3://amazon-sagemaker-307369429660-us-east-1-fa531a10d914/

# Download all notebooks from your project folder
# Replace 'Huggingface_model' with your actual project folder name
aws s3 cp s3://amazon-sagemaker-307369429660-us-east-1-fa531a10d914/Huggingface_model/ ./notebooks/ --recursive --include "*.ipynb"

# Download Python files
aws s3 cp s3://amazon-sagemaker-307369429660-us-east-1-fa531a10d914/Huggingface_model/ ./src/ --recursive --include "*.py"
```

---

### Method 3: From SageMaker Console

1. **Go to S3 Console:**
   - Navigate to: https://s3.console.aws.amazon.com/s3/
   - Find bucket: `amazon-sagemaker-307369429660-us-east-1-fa531a10d914`
   - Browse to your project folder
   - Select files and click **"Download"**

---

## Files to Download

Make sure you download:

- ✅ `getting_started.ipynb` (if you modified it)
- ✅ Any custom notebooks you created for model deployment
- ✅ Any Python scripts (`.py` files)
- ✅ Configuration files
- ❌ Don't download: checkpoints, large model files, temp files

---

## After Downloading

1. **Organize files:**
   ```
   sagemaker_LLMops/
   ├── notebooks/
   │   ├── getting_started.ipynb         ← Put here
   │   ├── huggingface_deployment.ipynb  ← Put here
   │   └── model_testing.ipynb           ← Put here
   ```

2. **Clean up notebooks** (optional):
   - Clear output cells to reduce file size
   - Remove sensitive data (AWS credentials, account IDs)
   - Add comments for clarity

3. **Test notebooks locally** (optional):
   ```bash
   cd /Users/omkarthakur/Desktop/sagemaker_LLMops
   jupyter notebook
   # Open and verify notebooks work
   ```

---

## If You Can't Download

If you're having trouble downloading, you can:

1. **Copy-paste code** from SageMaker notebooks into new local notebooks
2. **Take screenshots** of important outputs
3. **Recreate notebooks** using the code structure you remember

---

## Important Notes

⚠️ **Before pushing to GitHub:**
- Remove AWS account IDs
- Remove S3 bucket names (or use placeholders)
- Remove IAM role ARNs
- Clear all output cells with sensitive data

✅ **Safe to include:**
- Code snippets
- Model configurations
- Example inputs/outputs (non-sensitive)
- Comments and markdown cells

---

## Next Step

After downloading notebooks, continue with `SETUP_GITHUB.md` to push everything to GitHub! 🚀

