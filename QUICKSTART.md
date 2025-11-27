# Quick Start Guide

## Step 1: Push to GitHub

1. Initialize a git repository:
   ```bash
   cd add-two-numbers-toolkit
   git init
   git add .
   git commit -m "Initial commit: Add Two Numbers Toolkit"
   ```

2. Create a new repository on GitHub (make it public)

3. Push your code:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git branch -M main
   git push -u origin main
   ```

## Step 2: Test Locally

Before registering in the marketplace, test that your toolkit works:

```bash
# Test the add capability
echo '{"capability": "add", "args": {"a": 5, "b": 3}}' | python main.py
```

Expected output:
```json
{
  "result": 8,
  "capability": "add"
}
```

## Step 3: Register in the Marketplace

1. Open your AI Agent Platform application
2. Navigate to **Settings → Toolkit** (or go directly to **Settings → Toolkit Marketplace**)
3. Click **"Add Toolkit"**
4. Select **"Remote (GitHub)"** tab
5. Fill in the form:
   - **GitHub Repository URL**: `https://github.com/YOUR_USERNAME/YOUR_REPO_NAME`
   - **Homepage** (optional): Same as repository URL or your website
   - **Author** (optional): Your name
   - **Tags** (optional): `math, calculator, utility`
6. In the **Toolkit JSON Config** field, paste the entire contents of `toolkit.json`
7. Click **"Create Toolkit"**
8. Once created, click **"Publish"** to make it available to agents

## Step 4: Use in an Agent

After publishing, your toolkit will be available in the marketplace. Agents can discover and use it through the toolkit selection interface.

## Troubleshooting

- **"Invalid JSON config"**: Make sure you copied the entire `toolkit.json` file correctly
- **"Slug already exists"**: Choose a different slug in your `toolkit.json`
- **Toolkit not loading**: Check that your GitHub repository is public or you have proper access tokens configured

## Next Steps

- Add more capabilities to your toolkit
- Add error handling and validation
- Add unit tests
- Create documentation for your specific toolkit
- Share your toolkit with the community!

