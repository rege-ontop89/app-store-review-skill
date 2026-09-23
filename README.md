# Expo App Store Review Agent Skill

A portable, open-source [Agent Skill](https://agentskills.io/) for taking an Expo/EAS iOS app through App Store Connect, App Review, subscription review, and rejection repair.

It grew from a real first-launch workflow involving EAS Build, TestFlight, auto-renewable subscriptions, privacy disclosures, permission copy, reviewer recordings, metadata rejection, and a successful App Store approval. The repository contains no application credentials or private customer data.

## Install with GitHub CLI

GitHub CLI 2.90 or later can preview, install, update, and publish Agent Skills for many coding agents.

Preview the skill before installing it:

```bash
gh skill preview rege-ontop89/expo-app-store-review-skill expo-app-store-review
```

Install it for one coding agent across all of your projects:

```bash
gh skill install rege-ontop89/expo-app-store-review-skill expo-app-store-review --agent AGENT --scope user
```

Replace `AGENT` with one of these common host identifiers:

| Coding agent | `--agent` value |
| --- | --- |
| Claude Code | `claude-code` |
| Cursor | `cursor` |
| GitHub Copilot | `github-copilot` |
| Gemini CLI | `gemini-cli` |
| OpenAI Codex | `codex` |
| OpenCode | `opencode` |
| Universal Agent Skills location | `universal` |

For example:

```bash
gh skill install rege-ontop89/expo-app-store-review-skill expo-app-store-review --agent claude-code --scope user

gh skill install rege-ontop89/expo-app-store-review-skill expo-app-store-review --agent cursor --scope user
```

Run the command once for each coding agent you use. Omit `--scope user` or pass `--scope project` from inside a repository to install it only for that project.

Update an installed copy later with:

```bash
gh skill update expo-app-store-review
```

## Manual installation

Copy the complete [`skills/expo-app-store-review`](skills/expo-app-store-review) directory into a skill location supported by your agent. Keep the directory name `expo-app-store-review` because the Agent Skills specification requires it to match the `name` in `SKILL.md`.

Common project locations include:

- `.agents/skills/expo-app-store-review/` for the shared Agent Skills convention
- `.claude/skills/expo-app-store-review/` for Claude Code
- `.cursor/skills/expo-app-store-review/` for Cursor
- `.github/skills/expo-app-store-review/` for GitHub Copilot
- `.opencode/skills/expo-app-store-review/` for OpenCode

Prefer `gh skill install` when possible because it selects the correct user or project directory for the requested host.

## Use

Ask the agent to use `expo-app-store-review`, or invoke it with the skill/slash-command interface provided by your coding agent. Example:

```text
Use expo-app-store-review to audit this Expo iOS app and give me the exact steps to submit it to App Review.
```

The description also lets compatible agents select the skill automatically when the request clearly concerns Expo/EAS App Store submission or rejection handling.

## What it covers

- EAS production builds, TestFlight, and App Store submission boundaries
- App Store metadata, ASO, reviewer access, and review notes
- privacy labels and protected-resource purpose strings
- first-time In-App Purchase and subscription submissions
- physical-device QA and reviewer recordings
- information requests, metadata rejections, and binary rejections
- rebuild decisions, source control, and future version/build updates

The skill directs agents to verify current requirements against official Apple and Expo documentation because policies and App Store Connect screens change.

## Repository structure

```text
skills/expo-app-store-review/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── eas-builds-and-updates.md
│   ├── metadata-and-review-notes.md
│   ├── privacy-and-permissions.md
│   ├── rejections.md
│   ├── submission-workflow.md
│   └── subscriptions.md
└── scripts/check_text_limit.py
```

`SKILL.md`, `references/`, and `scripts/` follow the open Agent Skills format. `agents/openai.yaml` adds optional Codex display metadata and is ignored by other hosts.

## Contributing

Issues and pull requests are welcome. Keep guidance grounded in official Apple, Expo, or coding-agent documentation, and never commit reviewer credentials, API keys, signing material, or private application data.

## License

MIT
