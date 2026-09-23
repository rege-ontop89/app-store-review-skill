# Privacy labels and permission prompts

## Audit before answering

Trace data from collection through storage and third parties. Inspect source code, installed SDKs, server calls, authentication providers, analytics, crash reporting, payment systems, uploads, email, advertising, and feedback tools.

For each data type, determine:

- whether it leaves the device;
- whether the developer or a third party retains it beyond immediate servicing;
- its purpose under Apple’s categories;
- whether it is linked to the user’s identity/account/device;
- whether it is used to track the user across other companies’ apps or websites.

Do not select a category merely because a feature discusses money. “Financial information” depends on the actual data collected and Apple’s current definition. Likewise, a user-entered receipt or note is not automatically “purchases”; determine what the app collects and why.

Include SDK practices. If a vendor’s documentation is ambiguous, state the uncertainty and verify the SDK configuration rather than guessing.

Publish completed privacy responses. Saving an unfinished questionnaire is insufficient. Keep the answers current after analytics, authentication, advertising, crash reporting, or storage changes.

## Permission prompts

Audit the final native configuration, including permissions introduced by libraries. Remove unused permission declarations when the framework supports doing so.

Each purpose string should say:

1. the protected resource requested;
2. the feature that uses it;
3. what the user receives from granting access.

Example pattern:

```text
[App] uses the photo you choose as your business logo on receipts and statements.
```

Avoid vague text such as “This app needs access” or generic framework defaults. Request access immediately before the related user action and handle denial without trapping or crashing the user.

Notifications use the system authorization alert and typically do not use an Info.plist purpose string. Still provide enough in-app context before requesting them when the benefit is not obvious.

## Official sources

- Apple App Privacy management: https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-privacy
- Apple user privacy and data use: https://developer.apple.com/app-store/user-privacy-and-data-use/
- Apple protected-resource purpose strings: https://developer.apple.com/documentation/uikit/requesting-access-to-protected-resources
