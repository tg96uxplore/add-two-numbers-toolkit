# Add Two Numbers Toolkit

A simple example toolkit for the AI Agent Platform marketplace that demonstrates how to create and publish a toolkit.

## Overview

This toolkit provides a basic `add` capability that takes two numbers and returns their sum. It serves as a minimal example to help you understand the toolkit structure and how to create your own toolkits.

## Toolkit Structure

```
add-two-numbers-toolkit/
├── toolkit.json      # Toolkit manifest with metadata and capabilities
├── main.py           # Implementation of the toolkit logic
└── README.md         # This file
```

## Toolkit Manifest (`toolkit.json`)

The `toolkit.json` file defines:
- **slug**: Unique identifier (`add-two-numbers`)
- **display_name**: Human-readable name
- **description**: What the toolkit does
- **version**: Semantic version
- **entrypoint**: How to run the toolkit (Python command)
- **capabilities**: List of available tools with their schemas

## Capabilities

### `add`

Adds two numbers together.

**Input Schema:**
```json
{
  "type": "object",
  "properties": {
    "a": {"type": "number"},
    "b": {"type": "number"}
  },
  "required": ["a", "b"]
}
```

**Example Request:**
```json
{
  "capability": "add",
  "args": {
    "a": 5,
    "b": 3
  }
}
```

**Example Response:**
```json
{
  "result": 8,
  "capability": "add"
}
```

## How to Use

1. **Clone or download this repository**
   ```bash
   git clone https://github.com/yourusername/add-two-numbers-toolkit.git
   cd add-two-numbers-toolkit
   ```

2. **Test locally**
   ```bash
   echo '{"capability": "add", "args": {"a": 5, "b": 3}}' | python main.py
   ```
   Expected output: `{"result": 8, "capability": "add"}`

3. **Publish to GitHub**
   - Create a new repository on GitHub
   - Push this code to your repository
   - Make sure the repository is public (or you have a personal access token)

4. **Register in the Marketplace**
   - Go to Settings → Toolkit Marketplace
   - Click "Add Toolkit"
   - Select "Remote (GitHub)"
   - Paste your GitHub repository URL
   - Paste the contents of `toolkit.json` in the config field
   - Click "Create Toolkit"
   - Click "Publish" to make it available to agents

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Creating Your Own Toolkit

To create your own toolkit:

1. **Create a repository** with your toolkit code
2. **Add a `toolkit.json`** manifest file following this structure
3. **Implement your capabilities** in your chosen language (Python, Node.js, etc.)
4. **Test locally** before publishing
5. **Push to GitHub** and register in the marketplace

## Toolkit Manifest Schema

```json
{
  "slug": "your-toolkit-slug",
  "display_name": "Your Toolkit Name",
  "description": "What your toolkit does",
  "version": "0.1.0",
  "entrypoint": {
    "type": "python|node|bash|...",
    "command": "command to run"
  },
  "capabilities": [
    {
      "name": "capability_name",
      "description": "What this capability does",
      "schema": {
        "type": "object",
        "properties": {
          "param1": {"type": "string"},
          "param2": {"type": "number"}
        },
        "required": ["param1", "param2"]
      }
    }
  ],
  "author": "Your Name",
  "homepage": "https://github.com/yourusername/your-toolkit",
  "tags": ["tag1", "tag2"]
}
```

## License

MIT License - feel free to use this as a template for your own toolkits!

## Contributing

This is an example toolkit. Feel free to fork it and modify it for your needs!

