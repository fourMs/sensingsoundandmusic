#!/bin/bash

echo "Word counts for week documents:"
echo "================================"

# Function to count words in ipynb files
count_ipynb_words() {
    python3 -c "
import json
import re
try:
    with open('$1', 'r') as f:
        nb = json.load(f)
    
    text = ''
    for cell in nb.get('cells', []):
        if cell.get('cell_type') == 'markdown':
            text += ' '.join(cell.get('source', []))
    
    # Remove markdown formatting and count words
    text = re.sub(r'[#*\`\[\]()]', ' ', text)
    words = len([w for w in text.split() if w.strip()])
    print(words)
except Exception as e:
    print(0)
"
}

# Collect all results first, then sort
{
    # Count words in markdown files
    for file in ../book/week*.md; do
        if [ -f "$file" ]; then
            word_count=$(wc -w < "$file")
            printf "%-15s: %6d words\n" "$(basename "$file")" "$word_count"
        fi
    done

    # Count words in Jupyter notebooks (excluding code)
    for file in ../book/week*.ipynb; do
        if [ -f "$file" ]; then
            word_count=$(count_ipynb_words "$file")
            printf "%-15s: %6d words\n" "$(basename "$file")" "$word_count"
        fi
    done
} | sort -V

echo "================================"
# Calculate total (only show the number)
total=$(
    {
        for file in ../book/week*.md; do
            if [ -f "$file" ]; then
                wc -w < "$file"
            fi
        done
        for file in ../book/week*.ipynb; do
            if [ -f "$file" ]; then
                count_ipynb_words "$file"
            fi
        done
    } | awk '{sum += $1} END {print sum}'
)

echo "Total words: $total"