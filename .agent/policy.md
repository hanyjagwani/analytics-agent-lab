# Daily Project Agent Policy

The agent must follow these rules:

1. Complete no more than one backlog task per run.
2. Choose the highest-priority incomplete task that can be delivered safely.
3. Make a small, reviewable change.
4. Never create filler commits solely to produce GitHub activity.
5. Never push code or create commits directly.
6. Never modify GitHub Actions workflows.
7. Never modify scripts/guard-agent-changes.sh.
8. Never modify scripts/verify.sh.
9. Never modify this policy file.
10. Never modify .agent/daily_prompt.md.
11. Never create or modify secrets, credentials, .env files, key files, or tokens.
12. Do not attempt to deploy the application.
13. Do not change unrelated files.
14. Do not add dependencies unless the selected task genuinely requires them.
15. When a task is completed, update its backlog status to done.
16. When a task is completed, write a brief report to .agent/latest-report.md.
17. When no safe and meaningful task can be completed, leave the repository unchanged.

A trusted workflow will run tests after the edits are complete.
Do not attempt to execute terminal commands.

18. Remove trailing spaces and trailing tabs from modified text files before finishing.
19. Do not leave whitespace-only lines containing spaces or tabs.
