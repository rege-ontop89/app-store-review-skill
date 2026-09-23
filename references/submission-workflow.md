# Submission workflow

Use this for a first release or later App Store update. Verify the current App Store Connect interface before naming buttons.

## 1. Audit the product and binary

- Confirm the bundle identifier, marketing version, build number, supported device families, encryption declaration, and production EAS profile.
- Inventory authentication, account deletion, subscriptions, restore purchases, uploads, protected resources, analytics, crash reporting, email, feedback, and backend services.
- Confirm public legal URLs load without authentication.
- Test the production behavior on every supported device platform. If iPad is enabled, test iPad. Do not assume an iPhone-only design disables iPad support; inspect the native/app configuration.

## 2. Build and upload

Typical commands:

```bash
eas build --platform ios --profile production
eas submit --platform ios
```

`eas submit` uploads the chosen `.ipa` to App Store Connect. After Apple processes it, the build appears in TestFlight and can be selected for an App Store version. The developer must still complete the version record and submit it to App Review.

## 3. Complete the App Store record

Check at minimum:

- name, subtitle, description, keywords, category, copyright;
- actual in-app screenshots for every required device size;
- support URL, privacy policy URL, and marketing URL if used;
- age rating, content rights, pricing, availability, and release method;
- App Privacy responses, including third-party SDK collection;
- App Review contact details, sign-in information, review notes, and attachment;
- selected build and export-compliance answers;
- IAP/subscription items that must accompany the version.

## 4. Test the exact submitted build

Install the processed build with TestFlight on a physical supported device. Exercise fresh install, registration/login, denial and grant of permissions, core create/edit/delete flows, purchase and restore, legal links, account deletion, offline/error handling, document exports, and long/empty input states relevant to the app.

For a first app from a new developer account, prepare a concise physical-device screen recording that starts at launch and follows the normal user journey. Include access to paid features, subscription title/duration/price, legal links, registration, and account deletion when applicable. Use a separate disposable account for demonstrating deletion; do not delete the permanent reviewer account.

## 5. Submit in App Store Connect

Select the processed build on the version page, save, add required IAPs/subscriptions, add the app version to the review submission, and submit. Track the status in the App Review section.

## 6. Release

The configured release method controls what happens after approval: automatic release, manual developer release, or release no earlier than a chosen date. Processing and storefront propagation can take time after release.

## Official sources

- Apple App Store Connect workflow: https://developer.apple.com/help/app-store-connect/get-started/app-store-connect-workflow
- Apple submission overview: https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/overview-of-submitting-for-review
- Expo EAS Submit for iOS: https://docs.expo.dev/submit/ios/
