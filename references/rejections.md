# Information requests and rejections

## Classify the issue before changing code

1. **Information request:** Apple needs evidence, credentials, a recording, explanation, or documentation. Reply and update durable review notes. A new build is unnecessary unless the request reveals a binary defect.
2. **Metadata issue:** Fix the editable App Store Connect field and usually reuse the same binary. Examples include a missing EULA URL, incomplete review notes, or incorrect screenshots when editing is allowed.
3. **Binary or runtime issue:** Fix code/configuration, increment the build number, build, upload, test, select the new build, and resubmit.
4. **IAP configuration issue:** Complete the product/group metadata and submission association. Rebuild only if the app’s purchase UI or behavior also changes.

Quote the relevant rejection point in the working notes, identify the exact artifact that resolves it, and avoid unrelated changes during a review repair.

## Guideline 2.1 information request

For requests from accounts with limited review history, prepare:

- a physical-device recording from the exact submitted build, beginning at launch;
- registration, login, account deletion, core flow, private user content, subscription/paywall, legal links, and restore as applicable;
- purpose, audience, problem solved, and value;
- reproducible access steps and permanent demo credentials;
- external services and their roles;
- regional differences;
- regulated-industry or protected-content authorization, or a factual explanation that neither applies;
- IAP benefits and navigation.

Place durable facts in App Review Information notes for future submissions and reply to the message with a concise summary plus the attachment.

## Unresolved Issues flow

Use App Review → unresolved issues → Resolve. Reply to Apple as needed. For a rejected item, choose Edit, make the correction, and add it for review again. Once every rejected item is edited or removed, resubmit the submission. Accepted items can remain in the submission.

Apple states that metadata-only issues can be resubmitted with the same build after correction. Do not rebuild just to change App Store Connect text.

## Response template

```text
Hello App Review,

We addressed the reported [GUIDELINE/ISSUE].

[Exact change and where it appears. Include the functional URL when relevant.]

Build [BUILD] was tested on a physical [DEVICE] running [OS]. The attached recording begins at launch and demonstrates [FLOWS]. Permanent review credentials are provided in App Review Information.

[If applicable: The app version, subscription group, and subscription products are included together in this submission.]

Thank you.
```

## Official sources

- Reply to App Review: https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/reply-to-app-review-messages
- Manage unresolved issues: https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/manage-a-submission-with-unresolved-issues
- App and submission statuses: https://developer.apple.com/help/app-store-connect/reference/app-information/app-and-submission-statuses
