# Auto-renewable subscriptions and IAP

Use this when the app sells digital features or content.

## Product setup

For every subscription group and product, verify:

- reference name and product identifier;
- duration and level within the group;
- localized display name and description;
- price and storefront availability;
- review screenshot showing the purchase context;
- review notes that explain how to find and test the purchase flow;
- tax, banking, and paid-app agreements;
- matching identifiers in the app and entitlement provider;
- functional purchase, cancellation guidance, and Restore Purchases.

Test with Apple’s sandbox or TestFlight. Confirm successful purchase, entitlement activation, relaunch persistence, restore, expiry/revocation handling, and server/webhook behavior if used.

## App Review purchases run in the sandbox

App Review tests the submitted production build, but its purchases go through Apple's sandbox environment. A backend that unlocks paid features must therefore accept sandbox transactions from the production build while the app is in review, or the reviewer pays, sees nothing unlock, and the submission fails under Guideline 2.1.

Check, before submitting:

- receipt or transaction validation that tries production first and falls back to sandbox (for the legacy `verifyReceipt` endpoint, retry against sandbox on status `21007`);
- server-side rules that ignore or restrict sandbox events, such as an allowlist of sandbox tester accounts, a webhook filter that drops `SANDBOX` events, or an environment check in the entitlement logic. Any of these can block the reviewer's account, which will not be on your list;
- the entitlement provider's own configuration. For example, RevenueCat's test store key must be replaced with the platform-specific API key before submitting to App Review, and any provider setting that limits sandbox access applies to the reviewer too.

If the team wants to stop real users claiming entitlements through sandbox purchases, decide how the reviewer is let through before tightening it, and keep that rule in place through the whole review. Mention the purchase path in the review notes so the reviewer tries it deliberately.

## First IAP submission

Apple currently requires the first In-App Purchase to be submitted with a new app version. For auto-renewable subscriptions, include the relevant subscription products and group in the same review submission as the app version. Confirm their states on the submission page rather than assuming EAS attached them.

## Customer-facing subscription information

The paywall should clearly show the subscription title, duration, localized price, renewal terms, restore action, Privacy Policy, and Terms of Use. The App Store product-page metadata must also contain the required functional Terms of Use link. Account deletion guidance should explain that deleting an app account does not automatically cancel an Apple subscription and should provide a path to manage it.

Do not hard-code a price that can disagree with the App Store storefront. Display StoreKit/provider package pricing where possible.

## Official sources

- Apple IAP configuration overview: https://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/overview-for-configuring-in-app-purchases
- Apple submission overview: https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/overview-of-submitting-for-review
- Apple auto-renewable subscription information: https://developer.apple.com/help/app-store-connect/reference/in-app-purchases-and-subscriptions/auto-renewable-subscription-information
- Apple receipt validation, including the sandbox during App Review: https://developer.apple.com/documentation/storekit/validating-receipts-with-the-app-store
- RevenueCat sandbox testing: https://www.revenuecat.com/docs/test-and-launch/sandbox
