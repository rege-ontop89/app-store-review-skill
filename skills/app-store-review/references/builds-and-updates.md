# Builds, uploads, versions, and updates

Use the build path already established by the project. Do not migrate a working Xcode project to EAS or a working EAS project to a manual Xcode workflow merely to submit it.

## Terms that developers often conflate

- **Source-control commit:** a recorded codebase state in Git.
- **Marketing version:** the customer-facing App Store version, such as `1.0.1`.
- **Build number:** an increasing identifier for uploaded binaries under a marketing version.
- **Archive or release binary:** the signed app produced by Xcode, EAS, Xcode Cloud, CI, or another build system.
- **Uploaded build:** a binary processed by App Store Connect and available for TestFlight or version selection.
- **TestFlight build:** an uploaded build enabled for testing.
- **App Store version submission:** the App Store Connect record that selects one build and goes through review.
- **Over-the-air update:** a framework-specific compatible code or asset update. It does not replace App Review when changes require a new binary or materially change reviewed behavior.

## Xcode archive and upload

For a native Xcode project, confirm the Release configuration, signing team, bundle identifier, version, build number, capabilities, supported destinations, and archive scheme. Test the release behavior on physical devices.

The current graphical workflow is generally:

1. Open the correct project or workspace in Xcode.
2. Select the app scheme and an eligible generic or physical-device destination.
3. Choose Product → Archive.
4. In Organizer, select the archive and choose Distribute App.
5. Select TestFlight & App Store, or use the custom App Store Connect upload path when needed.
6. Validate, resolve signing or capability errors, and upload.
7. Wait for App Store Connect processing, then test in TestFlight and select the build on the app version.

Apple can change Xcode labels and minimum supported Xcode versions. Verify the live Xcode distribution documentation before giving exact clicks.

## Expo/EAS build and upload

For a project that already uses Expo Application Services, inspect `app.json` or app config, `eas.json`, the version source, credentials, and production profile. Typical commands are:

```bash
eas build --platform ios --profile production
eas submit --platform ios
```

EAS Submit uploads the selected binary to App Store Connect. It does not submit the App Store version to App Review. After processing, test the build and select it in App Store Connect.

## Xcode Cloud, CI, Transporter, and command-line uploads

Projects may build and deliver with Xcode Cloud or another CI provider. Confirm which commit, scheme, configuration, signing identity, export method, version, and build number produced the artifact. Preserve delivery logs.

Apple also supports upload paths including Transporter and command-line tools. When the user has an exported package, choose an uploader that supports that artifact and the team’s authentication method. Verify current Apple requirements rather than copying stale altool or Transporter commands.

## Rebuild decision

Create a new release build when changing executable code or bundled assets, native dependencies, entitlements, privacy manifests, Info.plist purpose strings, signing-sensitive configuration, icons or launch assets, supported devices, purchase behavior, or another runtime behavior App Review will test.

A new binary is usually unnecessary for editable App Store metadata such as description text, reviewer notes, demo credentials, a missing standard-EULA link, privacy-questionnaire corrections, pricing or availability configuration, or a reply to App Review. App Store Connect state can limit which fields are editable, so verify the current status.

## Future updates

1. Make and test changes in source control.
2. Decide whether the change requires a store binary or qualifies for a framework-supported compatible update.
3. For a store update, set the intended marketing version and increment the build number according to the project’s version source.
4. Produce and upload the release build using the project’s established Xcode, EAS, Xcode Cloud, or CI workflow.
5. Test the processed build in TestFlight on supported physical devices.
6. Create or select the App Store version, update metadata and privacy answers, select the build, attach changed IAP items if needed, and submit to review.

An existing TestFlight build remains available until it expires or is removed; uploading a newer build does not rewrite it. Reviewers receive the build selected on the App Store version.

## Official sources

- Apple upload methods: https://developer.apple.com/help/app-store-connect/manage-builds/upload-builds
- Apple Xcode distribution: https://developer.apple.com/documentation/xcode/distributing-your-app-for-beta-testing-and-releases
- Apple build selection: https://developer.apple.com/help/app-store-connect/manage-builds/choose-a-build-to-submit
- Expo iOS submission: https://docs.expo.dev/submit/ios/
