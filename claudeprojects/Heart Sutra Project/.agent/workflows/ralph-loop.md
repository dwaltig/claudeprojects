---
description: Run a Ralph Loop for iterative translation or manuscript refinement
---

# Ralph Loop Workflow

Execute an iterative "Ralph Wiggum" loop that cycles content between agents until convergence.

## Prerequisites
- Source file must exist
- Python 3.10+ available

## Steps

1. **Navigate to project directory**
```bash
cd "/Users/williamaltig/claudeprojects/Heart Sutra Project"
```

2. **Run the Ralph Loop**
// turbo
```bash
python ralph_loop.py --source [SOURCE_FILE] --type [translation|review|audit] --max-iter 5
```

3. **Review the output**
   - Check `*_converged.md` for final output
   - Check `*_ralph_log.json` for iteration history

4. **If human review was triggered**, examine the log for interrupt reasons and address manually.

## Examples

### Translation Loop
```bash
python ralph_loop.py --source T251.txt --type translation --max-iter 5
```

### Manuscript Review Loop
```bash
python ralph_loop.py --source ARTICLE.md --type review --max-iter 3 --threshold 3.0
```

### Philological Audit Loop
```bash
python ralph_loop.py --source Chapter_01_Blues.md --type audit --max-iter 4
```

## Output Files
- `{source}_converged.md` — Final converged content
- `{source}_ralph_log.json` — Complete iteration history with metrics
