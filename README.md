# App Store Review - Agent Skill for AI Coding Assistants

An agent skill that helps developers prepare, submit, and repair iOS App Store submissions, whether the app is built with Xcode, Expo/EAS, Xcode Cloud, CI, or another supported pipeline. Built by [rege-ontop89](https://github.com/rege-ontop89) from the process of shipping Kobo Profit Tracker through its first App Store approval.

AI coding assistants are good at building features, but App Store review spans much more than code: signing, builds, App Store Connect metadata, privacy labels, permission prompts, subscriptions, reviewer access, physical-device evidence, and rejection responses. This skill helps an agent inspect the whole submission instead of guessing from one screen or treating every rejection as a reason to rebuild.

## Background

This skill was built from a real first App Store launch. The process included an EAS production build, TestFlight testing, auto-renewable subscriptions, privacy questionnaires, content-rights declarations, permission-copy fixes, account-deletion guidance, reviewer credentials, a physical-device recording, a Guideline 2.1 information request, and a metadata rejection for a missing Terms of Use link.

Those lessons apply beyond Expo. Apple accepts builds uploaded through Xcode, Xcode Cloud, Transporter, command-line tooling, CI systems, and managed services such as EAS. The skill starts by identifying the project’s real build path, then keeps build creation, binary upload, TestFlight, and App Review submission as separate steps.

It uses the [Agent Skills](https://agentskills.io/home) format, so it works with Claude Code, OpenAI Codex, Cursor, GitHub Copilot, Gemini CLI, OpenCode, and other compatible agents.

The guidance is organized into focused reference files that the agent loads only when needed. A metadata rejection loads the rejection workflow. A subscription submission loads the IAP checklist. An Xcode or EAS build question loads the build reference. No wasted context on unrelated parts of the submission.

## Installing App Store Review

### Claude Code

```bash
npx skills add https://github.com/rege-ontop89/app-store-review-skill --skill app-store-review
```

Select **Claude Code** when prompted for the agent platform.

If `npx` is unavailable, install Node.js first with `brew install node` on macOS or download it from [nodejs.org](https://nodejs.org/).

### OpenAI Codex

```bash
npx skills add https://github.com/rege-ontop89/app-store-review-skill --skill app-store-review
```

Select **Codex** when prompted for the agent platform.

### Cursor, GitHub Copilot, Gemini CLI, OpenCode, and others

Use the same command and select your coding agent when prompted:

```bash
npx skills add https://github.com/rege-ontop89/app-store-review-skill --skill app-store-review
```

Install globally and non-interactively for several agents at once:

```bash
npx skills add https://github.com/rege-ontop89/app-store-review-skill \
  --skill app-store-review \
  --global \
  --agent claude-code \
  --agent codex \
  --agent cursor \
  --yes
```

### Manual Installation for Claude Code

Clone this repository and copy the `skills/app-store-review/` folder to a project or global skills directory:

```bash
# Project level: applies to one repository
cp -r skills/app-store-review/ .claude/skills/app-store-review/

# Global: applies to all projects
cp -r skills/app-store-review/ ~/.claude/skills/app-store-review/
```

Other compatible agents use the same skill directory with their supported skills location, such as `.agents/skills/`, `.cursor/skills/`, `.github/skills/`, or `.opencode/skills/`.

## Using App Store Review

**Claude Code:** Use `/app-store-review`, or ask naturally: “audit this app before I submit it to Apple,” “help me answer this rejection,” or “do I need a new build?”

**OpenAI Codex:** Use `$app-store-review`, or ask naturally: “check everything required for App Store submission,” “audit my privacy answers,” or “walk me through submitting this Xcode archive.”

**Other agents:** Invoke `app-store-review` through the agent’s skill or slash-command interface, or describe the App Store task normally. Compatible agents can also activate the skill automatically when its description matches the request.

## What It Covers

| Category | What It Handles |
| --- | --- |
| **Builds and uploads** | Xcode archives, Xcode Organizer, Xcode Cloud, CI, Transporter/altool, Expo/EAS Build and Submit, build processing, and build selection |
| **Versioning** | Marketing versions, build numbers, Git commits, TestFlight builds, store versions, later updates, and rebuild decisions |
| **App Store metadata** | Name, subtitle, description, keywords, screenshots, support URL, privacy policy, EULA, content rights, pricing, availability, release method, and per-field length checks in characters or bytes |
| **Privacy** | Data-type inventory, SDK collection, purposes, linked data, tracking, privacy labels, and keeping disclosures current |
| **Permissions** | Photo, camera, location, notifications, and other protected-resource prompts; specific purpose strings and unused permission removal |
| **Subscriptions and IAP** | Subscription groups, product metadata, localized pricing, review screenshots, paywall requirements, restore purchases, first-IAP submission, and backends that must accept App Review's sandbox purchases |
| **Login and export compliance** | Guideline 4.8 login services, Sign in with Apple across code, the developer portal and the auth provider, and the encryption declaration |
| **Reviewer access** | Permanent demo accounts, navigation instructions, physical-device recordings, sample data, regional differences, and external services |
| **Rejections** | Guideline 2.1 information requests, metadata-only fixes, binary defects, unresolved submissions, reviewer replies, and resubmission steps |
| **Quality assurance** | Testing the exact processed build on supported physical devices, account deletion, purchase flows, legal links, exports, and edge cases |

## Contributing

Contributions, corrections, and improvements are very welcome. App Store Connect screens and review requirements change, and build pipelines vary across native and cross-platform projects. If you encounter a repeatable submission issue or rejection pattern, please add it with an official source where possible.

See [CONTRIBUTING.md](https://github.com/rege-ontop89/app-store-review-skill/blob/main/CONTRIBUTING.md) for guidelines.

## License

App Store Review is available under the MIT License. See [LICENSE](https://github.com/rege-ontop89/app-store-review-skill/blob/main/LICENSE) for details.

Created by [rege-ontop89](https://github.com/rege-ontop89) from the experience of taking Kobo Profit Tracker through its first App Store review and approval.
