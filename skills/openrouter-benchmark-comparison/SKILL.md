---
name: openrouter-benchmark-comparison
description: Compare free AI models on OpenRouter by researching benchmarks from multiple sources (general web search and OpenRouter's own benchmark data) and generating a ranked comparison table. Use when you need to select the best free model for a task based on quality, speed, and cost.
---

# OpenRouter Free Model Benchmark Comparison

## Overview

This skill helps you compare free AI models available on OpenRouter by:
1. Searching the web for recent benchmark results and reviews
2. Checking OpenRouter's own model pages for performance metrics
3. Creating a structured comparison table with scores for quality, speed, and cost (all free)
4. Providing recommendations based on your use case (reasoning, coding, general chat, etc.)

Use this skill when you want to:
- Select the best free model for a specific task
- Understand trade-offs between different free models
- Stay updated on the performance of newly released free models
- Generate a quick reference table for model selection

## Workflow

### Step 1: Gather Model List
- Fetch the current list of free models from OpenRouter (using `freeride list` or API)
- Filter for models with `:free` tag

### Step 2: Web Research for Benchmarks
- Search for each model name + "benchmark" or "performance review"
- Extract key metrics: MMLU, HumanEval, GSM8K, speed (tokens/sec), latency
- Use multiple sources to cross-verify

### Step 3: Check OpenRouter Model Pages
- Visit each model's OpenRouter page for official benchmark data
- Look for "Benchmark" section or provider-provided metrics

### Step 4: Normalize and Score
- Convert different benchmarks to a 0-100 scale where possible
- Weight quality (70%) and speed (30%) for overall score
- Note any special strengths (coding, reasoning, multilingual)

### Step 5: Generate Comparison Table
- Output as markdown table with columns:
  - Model Name
  - Provider
  - Context Length
  - Quality Score (0-100)
  - Speed Score (0-100)
  - Overall Score
  - Best For (use case)
  - Notes

### Step 6: Provide Recommendations
- Suggest top picks for different categories:
  - Best overall free model
  - Best for reasoning/complex tasks
  - Best for coding
  - Best for long context
  - Fastest response time

## Usage

Run this skill when you need to compare free models. It will:
1. Perform web searches (using available search skills)
2. Access OpenRouter model information
3. Generate a comparison report in the current directory
4. Optionally save results to a file

You can then use the results to:
- Update your `freeride` configuration
- Choose a model for a specific task
- Share findings with teammates

## Example Request

"Compare the free models on OpenRouter and tell me which is best for coding tasks."

## Output Example

| Model | Provider | Context | Quality | Speed | Overall | Best For | Notes |
|-------|----------|---------|---------|-------|---------|----------|-------|
| nemotron-3-super-120b-a12b:free | nvidia | 262K | 85 | 70 | 80 | General | Strong reasoning, good for long context |
| qwen3-next-80b-a3b-instruct:free | qwen | 32K | 90 | 60 | 78 | Coding | Excellent HumanEval, multilingual |
| ... | ... | ... | ... | ... | ... | ... | ... |

## Resources

### scripts/
- `fetch_free_models.py` - Get list of free models from OpenRouter API
- `search_model_benchmark.py` - Search web for model benchmarks
- `parse_openrouter_page.py` - Extract benchmark data from model pages
- `generate_comparison_table.py` - Create markdown table from collected data

### references/
- `benchmark_sources.md` - List of trusted benchmark websites and methodologies
- `model_providers.md` - Information about each provider's strengths
- `scoring_methodology.md` - Details on how scores are calculated

### assets/
- `template_comparison.md` - Starter template for the comparison table
- `icons/` - Provider icons for visual enhancement (optional)