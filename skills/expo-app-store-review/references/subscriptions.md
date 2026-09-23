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

## First IAP submission

Apple currently requires the first In-App Purchase to be submitted with a new app version. For auto-renewable subscriptions, include the relevant subscription products and group in the same review submission as the app version. Confirm their states on the submission page rather than assuming EAS attached them.

## Customer-facing subscription information

The paywall should clearly show the subscription title, duration, localized price, renewal terms, restore action, Privacy Policy, and Terms of Use. The App Store product-page metadata must also contain the required functional Terms of Use link. Account deletion guidance should explain that deleting an app account does not automatically cancel an Apple subscription and should provide a path to manage it.

Do not hard-code a price that can disagree with the App Store storefront. Display StoreKit/provider package pricing where possible.

## Official sources

- Apple IAP configuration overview: https://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/overview-for-configuring-in-app-purchases
- Apple submission overview: https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/overview-of-submitting-for-review
- Apple auto-renewable subscription information: https://developer.apple.com/help/app-store-connect/reference/in-app-purchases-and-subscriptions/auto-renewable-subscription-information
