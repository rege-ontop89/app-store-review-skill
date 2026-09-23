# Expo App Store Review skill

A Codex skill for taking an Expo/EAS iOS app through App Store Connect, App Review, subscription review, and rejection repair.

It grew from a real first-launch workflow involving EAS Build, TestFlight, auto-renewable subscriptions, privacy disclosures, permission copy, reviewer recordings, metadata rejection, and a successful App Store approval. The repository contains no application credentials or private customer data.

## Install

Clone or copy this repository into your Codex skills directory:

```bash
git clone https://github.com/rege-ontop89/expo-app-store-review-skill.git ~/.codex/skills/expo-app-store-review
```

Restart or reload Codex so it discovers the skill. Invoke it with `$expo-app-store-review`, or let Codex select it when working on an Expo iOS App Store submission.

## What it covers

- EAS production builds, TestFlight, and App Store submission boundaries
- App Store metadata and reviewer notes
- privacy labels and protected-resource purpose strings
- first-time In-App Purchase and subscription submissions
- physical-device QA and reviewer recordings
- information requests, metadata rejections, and binary rejections
- rebuild decisions and future version/build updates

The skill directs agents to verify current requirements against official Apple and Expo documentation because policies and App Store Connect screens change.
