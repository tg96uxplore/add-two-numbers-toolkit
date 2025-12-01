#!/usr/bin/env python3
"""
Add Two Numbers Toolkit
A simple example toolkit that demonstrates how to create a toolkit for the marketplace.
"""

import json
import sys
from typing import Dict, Any


def add(a: float, b: float) -> float:
    """
    Add two numbers and return the result.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of a and b
    """
    return a + b


def handle_request(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Handle a toolkit request by routing to the appropriate capability.
    
    Args:
        payload: JSON payload containing the capability name and arguments
    
    Returns:
        JSON response with the result
    """
    capability = payload.get("capability")
    args = payload.get("args", {})
    
    if capability == "add":
        if "a" not in args or "b" not in args:
            return {
                "error": "Missing required arguments: 'a' and 'b' are required"
            }
        try:
            result = add(float(args["a"]), float(args["b"]))
            return {
                "result": result,
                "capability": capability
            }
        except (ValueError, TypeError) as e:
            return {
                "error": f"Invalid arguments: {str(e)}"
            }
    else:
        return {
            "error": f"Unknown capability: {capability}"
        }


if __name__ == "__main__":
    try:
        # Read JSON from stdin
        input_data = sys.stdin.read()
        payload = json.loads(input_data)
        
        # Process the request
        response = handle_request(payload)
        
        # Output JSON to stdout
        print(json.dumps(response, indent=2))
        
    except json.JSONDecodeError as e:
        error_response = {
            "error": f"Invalid JSON input: {str(e)}"
        }
        print(json.dumps(error_response, indent=2))
        sys.exit(1)
    except Exception as e:
        error_response = {
            "error": f"Unexpected error: {str(e)}"
        }
        print(json.dumps(error_response, indent=2))
        sys.exit(1)

