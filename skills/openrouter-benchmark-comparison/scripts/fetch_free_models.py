#!/usr/bin/env python3
"""
Fetch list of free models from OpenRouter API
"""
import json
import os
import sys
import urllib.request
import urllib.error

def fetch_free_models():
    """Fetch free models from OpenRouter API"""
    api_key = os.environ.get('OPENROUTER_API_KEY')
    if not api_key:
        print("Error: OPENROUTER_API_KEY not set", file=sys.stderr)
        return []
    
    url = "https://openrouter.ai/api/v1/models"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "https://openclaw.ai",
        "X-Title": "OpenClaw Benchmark Comparison"
    }
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as response:
            data = json.loads(response.read().decode())
            
        models = data.get('data', [])
        free_models = []
        
        for model in models:
            # Check if model is free (pricing contains :free or is 0)
            pricing = model.get('pricing', {})
            prompt_cost = pricing.get('prompt', '0')
            completion_cost = pricing.get('completion', '0')
            
            # Consider free if both costs are 0 or contain :free
            is_free = (
                prompt_cost == '0' and completion_cost == '0' or
                ':free' in str(prompt_cost) or ':free' in str(completion_cost)
            )
            
            if is_free:
                free_models.append({
                    'id': model.get('id'),
                    'name': model.get('name', model.get('id')),
                    'description': model.get('description', ''),
                    'context_length': model.get('context_length', 0),
                    'pricing': pricing,
                    'top_provider': model.get('top_provider', {}),
                    'provider': model.get('top_provider', {}).get('name', 'Unknown') if model.get('top_provider') else 'Unknown'
                })
        
        return free_models
        
    except urllib.error.URLError as e:
        print(f"Error fetching models: {e}", file=sys.stderr)
        return []
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return []

if __name__ == "__main__":
    models = fetch_free_models()
    print(json.dumps(models, indent=2))