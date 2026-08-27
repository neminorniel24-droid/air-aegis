#!/usr/bin/env bash

set -u

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT" || exit 1

LOG_FILE=".air-aegis-progress.log"

run_checks() {
    echo
    echo "=== Python syntax check ==="

    python -m compileall -q \
        simulation \
        sensors \
        tracking \
        perception \
        fusion \
        risk \
        dashboard

    if [ $? -ne 0 ]; then
        echo "Syntax check failed."
        return 1
    fi

    echo "=== Tests ==="
    pytest -q

    if [ $? -ne 0 ]; then
        echo "Tests failed."
        return 1
    fi

    echo "=== Git diff check ==="
    git diff --check

    if [ $? -ne 0 ]; then
        echo "Git diff check failed."
        return 1
    fi

    return 0
}

commit_if_changed() {
    if [ -z "$(git status --porcelain)" ]; then
        echo "No changes detected."
        return 0
    fi

    git add .

    COMMIT_MESSAGE="$1"

    git commit -m "$COMMIT_MESSAGE"

    if [ $? -ne 0 ]; then
        echo "Commit failed."
        return 1
    fi

    git push origin main

    if [ $? -ne 0 ]; then
        echo "Push failed."
        return 1
    fi

    echo "$(date '+%Y-%m-%d %H:%M:%S') | $COMMIT_MESSAGE" >> "$LOG_FILE"

    echo
    echo "=== COMMITTED AND PUSHED ==="
    git log --oneline -1

    return 0
}

task_number=1

while true; do
    echo
    echo "=============================================="
    echo "        AIR AEGIS DEVELOPMENT LOOP"
    echo "=============================================="
    echo "Repository: $ROOT"
    echo

    echo "Current HEAD:"
    git log --oneline -1

    echo
    echo "Working tree:"
    git status --short

    echo
    echo "This script will NOT invent empty commits."
    echo "Implement one real development task, then run checks."
    echo

    read -r -p "Press ENTER to run checks, or type q to quit: " choice

    if [ "$choice" = "q" ]; then
        break
    fi

    if ! run_checks; then
        echo
        echo "=============================================="
        echo "STOPPED: fix the failure before continuing."
        echo "=============================================="
        exit 1
    fi

    echo
    read -r -p "Commit message: " message

    if [ -z "$message" ]; then
        echo "Commit message cannot be empty."
        continue
    fi

    if ! commit_if_changed "$message"; then
        exit 1
    fi

    task_number=$((task_number + 1))

    echo
    echo "Ready for the next real task."
done
