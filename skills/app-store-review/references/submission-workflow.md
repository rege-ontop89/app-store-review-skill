# Submission workflow

Use this for a first release or later App Store update. Verify the current App Store Connect and build-tool interfaces before naming buttons.

## 1. Audit the product and release configuration

- Confirm the bundle identifier, marketing version, build number, supported device families, signing, entitlements, encryption declaration, privacy manifest, and release configuration.
- Identify the actual build and upload path: Xcode, EAS, Xcode Cloud, CI, Transporter, or another supported workflow.
- Inventory authentication, account deletion, subscriptions, restore purchases, uploads, protected resources, analytics, crash reporting, email, feedback, and backend services.
- If the app offers a third-party or social login, confirm it also offers an option that satisfies Guideline 4.8, usually Sign in with Apple, and that the export compliance key is declared. See [login-and-export-compliance.md](login-and-export-compliance.md).
- If paid features are unlocked server-side, confirm the backend accepts App Review's sandbox purchases from the production build. See [subscriptions.md](subscriptions.md).
- Confirm public legal URLs load without authentication.
- Test production behavior on every supported device platform. If iPad is enabled, test iPad. Do not assume an iPhone-oriented design disables iPad support; inspect the project configuration.

## 2. Produce and upload the build

Use the project’s established path.

### Xcode

Create a release archive, then use Xcode Organizer’s TestFlight & App Store or App Store Connect distribution workflow to validate and upload it.

### Expo/EAS

Typical commands are:

```bash
eas build --platform ios --profile production
eas submit --platform ios
```

### Xcode Cloud, CI, or an exported package

Confirm the exact commit and release configuration. Deliver with the configured App Store Connect integration or a currently supported Apple upload tool such as Transporter.

Every upload path ends at App Store Connect processing. Uploading does not by itself submit the public App Store version for review.

## 3. Complete the App Store record

Check at minimum:

- name, subtitle, description, keywords, category, and copyright;
- actual in-app screenshots for every required device size;
- support URL, privacy-policy URL, and marketing URL if used;
- age rating, content rights, pricing, availability, and release method;
- App Privacy responses, including third-party SDK collection;
- App Review contact details, sign-in information, review notes, and attachments;
- selected build and export-compliance answers;
- IAP or subscription items that must accompany the version.

## 4. Test the exact submitted build

Install the processed build with TestFlight on supported physical devices. Exercise fresh install, registration and login, permission denial and grant, core create/edit/delete flows, purchase and restore, legal links, account deletion, offline and error handling, document exports, and long or empty input states relevant to the app.

For a first app from a new developer account, prepare a concise physical-device screen recording that starts at launch and follows the normal user journey. Include access to paid features, subscription title, duration and price, legal links, registration, and account deletion when applicable. Use a separate disposable account for demonstrating deletion; do not delete the permanent reviewer account.

## 5. Submit in App Store Connect

Select the processed build on the version page, save, add required IAPs or subscriptions, add the app version to the review submission, and submit. Track the status in the App Review section.

## 6. Release

The configured release method controls what happens after approval: automatic release, manual developer release, release no earlier than a chosen date, or phased release when applicable. Processing and storefront propagation can take time after release.

## Official sources

- Apple upload methods: https://developer.apple.com/help/app-store-connect/manage-builds/upload-builds
- Apple build selection: https://developer.apple.com/help/app-store-connect/manage-builds/choose-a-build-to-submit
- Apple App Store Connect workflow: https://developer.apple.com/help/app-store-connect/get-started/app-store-connect-workflow
- Apple submission overview: https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/overview-of-submitting-for-review
- Expo EAS Submit for iOS: https://docs.expo.dev/submit/ios/
