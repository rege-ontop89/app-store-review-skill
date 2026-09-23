# EAS builds, versions, and updates

## Terms that developers often conflate

- **Source control commit:** a recorded codebase state in Git.
- **Marketing version:** the customer-facing App Store version, such as `1.0.1`.
- **Build number:** an increasing identifier for uploaded binaries under a marketing version.
- **EAS build profile:** configuration such as `production` that controls how the binary is built and distributed.
- **TestFlight build:** an uploaded and processed binary available for testing.
- **App Store version submission:** the App Store Connect record that selects a build and goes through review.
- **EAS Update:** an over-the-air update to compatible JavaScript/assets; it is not a replacement for App Review when changes require a new binary or materially change reviewed behavior.

## Rebuild decision

Create a new production build when changing code or bundled assets included in the binary, native dependencies, entitlements, Info.plist permission text, Expo app configuration that affects native output, icons/splash, supported devices, purchase behavior, or another runtime behavior App Review will test.

A new binary is usually unnecessary for editable App Store metadata such as description text, reviewer notes, demo credentials, a missing standard-EULA link, privacy questionnaire corrections, pricing/availability configuration, or a reply to App Review. App Store Connect state can limit which fields are editable; verify the current status.

## Future updates

1. Make and test changes in source control.
2. Decide whether the release is an over-the-air compatible update or a store binary update.
3. For a store update, set the intended marketing version and increment the iOS build number according to the project’s version source.
4. Run the production EAS build and upload it.
5. Test the processed build in TestFlight on physical supported devices.
6. Create/select the new App Store version, update metadata and privacy answers, select the build, attach changed IAP items if needed, and submit to review.

An existing TestFlight build remains available until it expires or is removed; uploading a newer build does not rewrite it. Reviewers receive the build selected on the App Store version.

## Official sources

- Expo iOS submission: https://docs.expo.dev/submit/ios/
- Expo production iOS build: https://docs.expo.dev/tutorial/eas/ios-production-build/
