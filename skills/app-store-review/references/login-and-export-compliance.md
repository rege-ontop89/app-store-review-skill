# Login services and export compliance

Two configuration checks that are easy to miss because nothing fails until review or upload.

## Login services (Guideline 4.8)

If the app uses a third-party or social login (Google Sign-In, Facebook Login and similar) to set up or authenticate the user's primary account, Guideline 4.8 requires an equivalent login option that:

- limits data collection to the user's name and email address;
- lets users keep their email address private while setting up the account;
- does not collect interactions with the app for advertising without consent.

Sign in with Apple meets all three and is the usual way to comply. Check the guideline's current exceptions before concluding it does not apply: apps that use only the company's own account system, education or enterprise apps requiring an existing organisational account, government or industry-backed electronic ID, clients for a specific third-party service, and alternative marketplace logins.

When Sign in with Apple is used, check each layer separately, because each one fails silently on its own:

1. **Code:** the button is offered wherever the other login options are, on both sign-up and sign-in screens.
2. **Apple Developer portal:** the Sign in with Apple capability is enabled on the App ID that matches the bundle identifier, and the build's entitlements include it. For Expo/EAS, confirm the config plugin or `ios.usesAppleSignIn` produced the entitlement, and regenerate native folders if the project keeps an `ios/` directory.
3. **Auth provider:** a native identity token's audience is normally the app's bundle identifier, not a web Services ID. For providers that validate against an allowed audience list, register the native bundle identifier. Supabase, for example, accepts a native `signInWithIdToken` token only when its audience appears in the configured Client IDs. Other providers use their own app and Apple-provider configuration, so follow that provider's native iOS instructions instead of assuming a web Services ID covers native tokens.

Test on a physical device with the release build, including a first sign-in that uses Hide My Email. Account deletion must also work for an account created this way.

## Export compliance (encryption)

Every uploaded build asks whether the app uses encryption. Declaring the answer in the binary avoids the question on each build and stops builds waiting in TestFlight for it.

- Set `ITSAppUsesNonExemptEncryption` in Info.plist. `NO` (false) declares that the app, including linked third-party libraries, uses no encryption or only encryption that is exempt from export compliance requirements.
- Standard HTTPS through the operating system is typically exempt, but the answer depends on the app's actual use of cryptography. Do not declare `NO` without checking the app and its SDKs against Apple's guidance.
- If the app uses non-exempt encryption, set the key to `YES` and provide the export compliance documentation Apple requests; after approval Apple supplies a code for `ITSEncryptionExportComplianceCode`.
- For Expo, set `ios.config.usesNonExemptEncryption` in app config, which writes the Info.plist key during the build.

Changing this key changes the binary, so it needs a new build.

## Official sources

- Apple App Review Guidelines, 4.8 Login Services: https://developer.apple.com/app-store/review/guidelines/#login-services
- Supabase, Login with Apple (native client IDs): https://supabase.com/docs/guides/auth/social-login/auth-apple
- Apple `ITSAppUsesNonExemptEncryption`: https://developer.apple.com/documentation/bundleresources/information-property-list/itsappusesnonexemptencryption
- Apple export compliance overview: https://developer.apple.com/help/app-store-connect/manage-app-information/overview-of-export-compliance
- Expo app config (`ios.config.usesNonExemptEncryption`, `ios.usesAppleSignIn`): https://docs.expo.dev/versions/latest/config/app/
