#!/bin/bash
# Auto-push extraction results to GitHub every hour
# Usage: nohup bash auto_push.sh > generated/auto_push.log 2>&1 &

cd "$(dirname "$0")"

while true; do
    # Count new JSON files
    NEW=$(git status --porcelain generated/*_data_*.json generated/corpus_state.json 2>/dev/null | wc -l)

    if [ "$NEW" -gt 0 ]; then
        TIMESTAMP=$(date '+%Y-%m-%d %H:%M')
        # Stage extraction data + state
        git add generated/*_data_*.json generated/corpus_state.json generated/*_quarantined_*.json .gitignore 2>/dev/null
        git commit -m "Auto-backup: extraction results as of ${TIMESTAMP}"
        git push origin main
        echo "[${TIMESTAMP}] Pushed ${NEW} changed files"
    else
        echo "[$(date '+%Y-%m-%d %H:%M')] No new files to push"
    fi

    sleep 3600
done
