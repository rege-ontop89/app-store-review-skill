# Metadata and review notes

## Product-page metadata

Write for accurate discovery and a quick understanding of the app. Derive claims from working features.

- **Name:** recognizable brand/product name within Apple’s current limit.
- **Subtitle:** concrete audience or benefit; do not repeat the name.
- **Description:** opening value proposition, principal workflows, paid/free boundary, and required legal link text. Avoid unverifiable superlatives.
- **Keywords:** comma-separated relevant terms without duplicating high-value words already indexed from the name/subtitle when alternatives are stronger.
- **Screenshots:** show the actual app in use, with representative data. Match the submitted UI. Do not fill the set with splash, login, or title art.
- **Support URL:** a functioning page where a customer can obtain help.
- **Privacy policy:** a public, app-specific policy matching actual data practices.

For apps with auto-renewable subscriptions, confirm that the product-page metadata includes a functional Terms of Use link. When using Apple’s standard EULA, Apple has instructed developers to place this URL in the app description:

https://www.apple.com/legal/internet-services/itunes/dev/stdeula/

Check current guidance before submission. A custom EULA is configured separately in App Store Connect.

## Review information

Review notes should help a reviewer reach every material feature without guessing. Include:

1. purpose and target audience;
2. permanent demo credentials and any special login behavior;
3. numbered navigation steps for core and less obvious features;
4. explanation of private user content and whether reporting/blocking applies;
5. external services and what each does;
6. regional differences or an explicit statement that behavior is consistent;
7. regulated activity or third-party content rights, when relevant;
8. what each IAP unlocks and exact navigation to the paywall;
9. attachment name and what the recording demonstrates;
10. concise explanation of changes made after a rejection.

Do not paste credentials into public issue trackers, source files, or GitHub. App Store Connect’s dedicated sign-in fields are the proper location.

## Review note template

```text
Hello App Review,

SUBMISSION UPDATE — BUILD [BUILD]

[One paragraph describing the issue resolved and any relevant metadata URL.]

The attached recording, “[FILE].mov,” was captured from this build on a physical [DEVICE] running [OS]. It begins at launch and demonstrates [FLOWS].

1. PURPOSE AND AUDIENCE
[Accurate description.]

2. ACCESS AND MAIN FEATURES
Permanent credentials are provided in the Sign-In Information fields.
[Numbered or bulleted navigation steps.]

3. USER CONTENT
[Privacy/visibility and moderation applicability.]

4. EXTERNAL SERVICES
[Service: purpose.]

5. REGIONAL OPERATION
[Differences or consistency.]

6. REGULATORY AND CONTENT RIGHTS
[Applicable facts.]

7. IN-APP PURCHASE
[Products, entitlements, free boundary, purchase path, restore path.]
```

Apple’s reply field has a 4,000-character limit. Keep margin for edits rather than targeting exactly 4,000.
