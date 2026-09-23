---
name: expo-app-store-review
description: Prepare, audit, submit, and repair an Expo/EAS iOS App Store submission, including App Store Connect metadata, privacy disclosures, permissions, subscriptions, reviewer access, rejection responses, and deciding whether a new native build is required.
license: MIT
metadata:
  author: rege-ontop89
  version: "1.0.0"
---

# Expo App Store Review

Help the user move an Expo/EAS iOS app from a codebase or TestFlight build through App Store review. Treat App Store Connect labels and Apple policy as changeable: verify current requirements against official Apple and Expo documentation before giving exact UI steps.

## Start with the actual app

Inspect the repository before drafting disclosures or review notes. Read the Expo config, `eas.json`, package manifest, authentication, account deletion, purchases, analytics, uploads, permissions, legal links, and any product brief. Search for third-party SDKs and server services. Do not infer data collection only from visible screens.

Build a private working inventory of:

- app purpose, audience, supported devices, regions, and currencies;
- account creation, login methods, demo access, and in-app deletion;
- free and paid features, product identifiers, restore/manage-subscription paths;
- collected data, its purpose, whether it is linked to identity, and whether it is used for tracking;
- protected resources and the exact purpose strings shown by iOS;
- external services, public user content, regulated activity, and third-party rights;
- version, build number, bundle identifier, and release profile.

Never place passwords, API keys, private identifiers, or live review credentials in the skill, repository, commit history, or public artifacts. Put reviewer credentials only in App Store Connect.

## Route the work

- For the complete first-submission or update sequence, read [references/submission-workflow.md](references/submission-workflow.md).
- For listing copy, keywords, screenshots, and review information, read [references/metadata-and-review-notes.md](references/metadata-and-review-notes.md).
- For privacy labels and system permission prompts, read [references/privacy-and-permissions.md](references/privacy-and-permissions.md).
- For In-App Purchase or auto-renewable subscriptions, read [references/subscriptions.md](references/subscriptions.md).
- For a rejection, information request, or unresolved submission, read [references/rejections.md](references/rejections.md).
- For Expo build/version behavior and the rebuild decision, read [references/eas-builds-and-updates.md](references/eas-builds-and-updates.md).

Load only the references needed for the current request.

## Working rules

1. Separate four distinct actions in every explanation:
   - building the `.ipa` with EAS Build;
   - uploading it to App Store Connect with EAS Submit;
   - testing/distributing it through TestFlight;
   - selecting it and submitting the version to App Review in App Store Connect.
2. Say explicitly that `eas submit` uploads a binary; it does not by itself submit the App Store version for public review.
3. Recommend a new build only when the binary, bundled JavaScript/assets, entitlements, permissions, native configuration, or runtime behavior must change. Metadata-only fixes can normally reuse the same build when App Store Connect allows editing.
4. Base privacy answers on real code and every integrated SDK. Distinguish collection from on-device access and tracking from ordinary analytics.
5. Give reviewer instructions as reproducible steps. Use a permanent review account when login is required and keep it usable throughout review.
6. For first-time In-App Purchases, verify that each product and its group have complete metadata and are included with the app version submission.
7. Test the exact submitted build on supported physical devices. A simulator run is useful development evidence but does not replace physical-device review testing.
8. Preserve the user’s selected Expo SDK and native setup. Do not introduce an SDK upgrade as part of submission cleanup unless the user explicitly chooses it.
9. Cite primary sources near claims that may change. Prefer Apple Developer/App Store Connect Help and the version-matched Expo documentation.

## Finish with a concrete checklist

Report:

- which build and version are being submitted;
- what was verified in code versus what the user must verify in App Store Connect;
- any metadata or legal URLs still missing;
- whether subscriptions/IAPs are attached to the submission;
- the physical-device flows to record and test;
- whether a rebuild is required and the exact reason;
- the precise next App Store Connect action.

When drafting text for Apple, keep it factual, reviewer-oriented, and free of marketing language. Validate text limits with `scripts/check_text_limit.py`.
