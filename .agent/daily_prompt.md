Read .agent/policy.md and .agent/backlog.yaml before editing any files.

Choose the highest-priority incomplete backlog task that can be completed as one
small, reviewable pull request. Complete only that task.

Follow every rule in .agent/policy.md.

Use the acceptance criteria in the backlog as the definition of done. Add or
update focused tests when the task changes code behavior.

After completing the task:
1. Change its status from todo to done in .agent/backlog.yaml.
2. Write .agent/latest-report.md with:
   - selected task ID
   - selected task title
   - files changed
   - concise summary
   - test coverage added or updated
   - any review notes

Do not write a report-only change. If you cannot produce a useful project change,
leave the repository unchanged.

Before finishing, remove trailing spaces and trailing tabs from every modified
text file. Do not leave whitespace-only lines containing spaces or tabs.
