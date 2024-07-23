# LANG: A Lesson Plan Generation Framework via Multi-Form Interaction with Large Language Models

## Dataset Examples

### Access

Our dataset samples are in JSON format and can be accessed in the following way:

```python
import json
samples = json.load(open('dataset/en-samples-10.json', encoding='utf-8'))
```

### Dataset Details

Our dataset samples can be found in the [dataset](dataset) directory. Each data entry includes `input` and `output`. The `input` is the prompt provided to LLMs, and the `output` is a complete lesson plan.

```python
[
    {
        "input": "...",
        "output": "..."
    },
    ...
]
```

### Lesson Plan Showcase

<div style="text-align: center;">
  <img src="imgs/show.png">
</div>

## Baseline
