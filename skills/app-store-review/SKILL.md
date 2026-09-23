---
name: app-store-review
description: Prepare, audit, submit, and repair an Apple App Store submission for iOS or iPadOS apps built with Xcode, Expo/EAS, Xcode Cloud, CI, or another supported upload pipeline. Covers App Store Connect metadata, privacy, permissions, subscriptions, Sign in with Apple, export compliance, reviewer access, rejection responses, and rebuild decisions. Use when the user mentions App Store Connect, App Review, TestFlight, submitting or uploading an iOS build, an App Review message or information request, a rejection or a guideline number such as Guideline 2.1 or 4.8, "was rejected", "do I need a new build", or IAP and subscriptions not working in review.
license: MIT
metadata:
  author: rege-ontop89
  version: "2.1.0"
---

# App Store Review

Help the user move an iOS or iPadOS app from its codebase or uploaded build through App Store review. Treat App Store Connect labels, Apple policy, upload tooling, and build requirements as changeable: verify current requirements against official Apple documentation and the relevant build-tool documentation before giving exact UI steps.

## Start with the actual app

Inspect the repository before drafting disclosures or review notes. Read the Xcode project or workspace, Info.plist values, entitlements, privacy manifests, package/dependency files, build configuration, authentication, account deletion, purchases, analytics, uploads, permissions, legal links, and product documentation. For cross-platform projects, also inspect framework configuration such as Expo/EAS, Flutter, React Native, or the selected CI service. Search for third-party SDKs and server services. Do not infer data collection only from visible screens.

Build a private working inventory of:

- app purpose, audience, supported devices, regions, and currencies;
- bundle identifier, marketing version, build number, signing setup, and upload path;
- account creation, login methods, demo access, and in-app deletion;
- free and paid features, product identifiers, restore and subscription-management paths;
- collected data, its purpose, whether it is linked to identity, and whether it is used for tracking;
- protected resources and the exact purpose strings shown by the operating system;
- external services, public user content, regulated activity, and third-party rights.

Never place passwords, API keys, signing material, private identifiers, or live review credentials in the skill, repository, commit history, or public artifacts. Put reviewer credentials only in App Store Connect.

## Route the work

- For the complete first-submission or update sequence, read [references/submission-workflow.md](references/submission-workflow.md).
- For Xcode, EAS, CI, uploads, versioning, and rebuild decisions, read [references/builds-and-updates.md](references/builds-and-updates.md).
- For listing copy, keywords, screenshots, and review information, read [references/metadata-and-review-notes.md](references/metadata-and-review-notes.md).
- For privacy labels and system permission prompts, read [references/privacy-and-permissions.md](references/privacy-and-permissions.md).
- For In-App Purchase or auto-renewable subscriptions, including App Review's sandbox purchases against a production backend, read [references/subscriptions.md](references/subscriptions.md).
- For Sign in with Apple and other login-service requirements, or the encryption and export compliance declaration, read [references/login-and-export-compliance.md](references/login-and-export-compliance.md).
- For a rejection, information request, or unresolved submission, read [references/rejections.md](references/rejections.md).

Load only the references needed for the current request.

## Working rules

1. Separate four distinct actions in every explanation:
   - creating the release archive or binary with Xcode, EAS, Xcode Cloud, CI, or another build system;
   - uploading that binary to App Store Connect with Xcode, Transporter/altool, EAS Submit, or another supported uploader;
   - testing or distributing the processed build through TestFlight;
   - selecting the build and submitting the app version to App Review in App Store Connect.
2. State that uploading a binary does not by itself submit the App Store version for public review.
3. Recommend a new build only when the binary, bundled code/assets, entitlements, permissions, native configuration, or runtime behavior must change. Metadata-only fixes can normally reuse the same build when App Store Connect allows editing.
4. Base privacy answers on real code and every integrated SDK. Distinguish collection from on-device access and tracking from ordinary analytics.
5. Give reviewer instructions as reproducible steps. Use a permanent review account when login is required and keep it usable throughout review.
6. For first-time In-App Purchases, verify that each product and its group have complete metadata and are included with the app version submission.
7. Test the exact submitted build on supported physical devices. A simulator run is useful development evidence but does not replace physical-device review testing.
8. Preserve the project’s selected framework, SDK, deployment target, and signing approach. Do not introduce an Xcode, framework, or SDK upgrade as incidental submission cleanup unless it is required or the user explicitly chooses it.
9. Cite primary sources near claims that may change. Prefer Apple Developer and App Store Connect Help, plus official documentation for the project’s build system.

## Finish with a concrete checklist

Report:

- which version and build are being submitted and how the binary was produced;
- what was verified in code versus what the user must verify in App Store Connect;
- any metadata or legal URLs still missing;
- whether subscriptions or IAPs are attached to the submission;
- the physical-device flows to record and test;
- whether a rebuild is required and the exact reason;
- the precise next build-tool or App Store Connect action.

When drafting text for Apple, keep it factual, reviewer-oriented, and free of marketing language. Validate text limits with `scripts/check_text_limit.py --field <field>`; keywords and review notes are measured in bytes, not characters.
