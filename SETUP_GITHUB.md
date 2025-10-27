# How to Download Your SageMaker Notebooks and Push to GitHub

## Step 1: Download Notebooks from SageMaker Unified Studio

### Option A: Download via Jupyter Interface (Easiest)

1. **Open your project in SageMaker Unified Studio**
   - Navigate to your `Huggingface_model` project
   - Click on the notebook you want to download

2. **In JupyterLab:**
   - Right-click on the notebook file in the file browser (left sidebar)
   - Select **"Download"**
   - Save to your local folder: `/Users/omkarthakur/Desktop/sagemaker_LLMops/notebooks/`

3. **Repeat for all notebooks:**
   - `getting_started.ipynb`
   - Any other notebooks you created

### Option B: Download via AWS CLI

```bash
# Navigate to your project directory
cd /Users/omkarthakur/Desktop/sagemaker_LLMops

# Create notebooks directory
mkdir -p notebooks

# Use AWS S3 to download from your SageMaker bucket
aws s3 cp s3://amazon-sagemaker-307369429660-us-east-1-fa531a10d914/Huggingface_model/ ./notebooks/ --recursive --exclude "*" --include "*.ipynb"
```

### Option C: Download from Project Files

1. Go to your SageMaker Unified Studio project
2. Click on **"Project files"** section
3. For each notebook:
   - Click the three dots (⋮) next to the file
   - Select **"Download"**
   - Save to `notebooks/` folder

---

## Step 2: Create GitHub Repository

### On GitHub Website:

1. **Go to**: https://github.com
2. **Click**: "+" icon (top right) → "New repository"
3. **Repository name**: `sagemaker_LLMops`
4. **Description**: "Hugging Face model deployment on Amazon SageMaker"
5. **Visibility**: Public (or Private if you prefer)
6. **DO NOT** initialize with README (we already have one)
7. **Click**: "Create repository"

---

## Step 3: Initialize Git and Push to GitHub

### Open Terminal and Run:

```bash
# Navigate to your project
cd /Users/omkarthakur/Desktop/sagemaker_LLMops

# Initialize Git repository
git init

# Add all files
git add .

# Commit with message
git commit -m "Initial commit: SageMaker Hugging Face deployment project"

# Add your GitHub repository as remote (replace 'yourusername' with your GitHub username)
git remote add origin https://github.com/yourusername/sagemaker_LLMops.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### If You Get Authentication Error:

GitHub requires a Personal Access Token (PAT) instead of password.

**Create PAT:**
1. Go to: https://github.com/settings/tokens
2. Click "Generate new token" → "Generate new token (classic)"
3. Give it a name: "SageMaker Project"
4. Select scopes: ✓ `repo` (full control)
5. Click "Generate token"
6. **Copy the token** (you won't see it again!)

**Use PAT when pushing:**
```bash
# When prompted for password, paste your PAT instead
git push -u origin main
```

**Or configure Git to remember credentials:**
```bash
git config --global credential.helper store
git push -u origin main
# Enter username and PAT (will be saved)
```

---

## Step 4: Verify on GitHub

1. Go to: `https://github.com/yourusername/sagemaker_LLMops`
2. You should see:
   - ✅ README.md (with nice formatting)
   - ✅ requirements.txt
   - ✅ .gitignore
   - ✅ notebooks/ folder (if you downloaded them)

---

## Step 5: Create Python Scripts (Optional)

If you want to create standalone Python scripts from your notebooks:

### Create `src/deploy_model.py`:

```bash
mkdir -p src
```

Then manually create the deployment script by extracting code from your notebooks.

---

## Future Updates

When you make changes in SageMaker:

```bash
# 1. Download updated notebooks from SageMaker
# 2. Navigate to project
cd /Users/omkarthakur/Desktop/sagemaker_LLMops

# 3. Check what changed
git status

# 4. Add changes
git add .

# 5. Commit with descriptive message
git commit -m "Update: Added sentiment analysis model deployment"

# 6. Push to GitHub
git push
```

---

## Quick Reference Commands

```bash
# Check status
git status

# Add specific file
git add notebooks/my_notebook.ipynb

# Add all files
git add .

# Commit changes
git commit -m "Your message here"

# Push to GitHub
git push

# Pull latest changes (if collaborating)
git pull

# View commit history
git log --oneline

# Create new branch
git checkout -b feature/new-model

# Switch branch
git checkout main
```

---

## Troubleshooting

### Problem: "Repository not found"
**Solution**: Double-check your GitHub username and repository name in the remote URL

### Problem: "Permission denied"
**Solution**: Use Personal Access Token instead of password

### Problem: "Files too large"
**Solution**: 
- Add large files to .gitignore
- Or use Git LFS: `git lfs install`

### Problem: "Nothing to commit"
**Solution**: Make sure files are in the directory (`ls -la` to check)

---

## Best Practices

✅ **Commit often** with descriptive messages  
✅ **Never commit AWS credentials** (.gitignore prevents this)  
✅ **Update README** when adding new features  
✅ **Use branches** for experiments  
✅ **Add comments** in notebooks for clarity  
✅ **Test code** before committing  

---

## Need Help?

- Git Documentation: https://git-scm.com/doc
- GitHub Guides: https://guides.github.com/
- Git Cheat Sheet: https://training.github.com/downloads/github-git-cheat-sheet/

Good luck with your project! 🚀

