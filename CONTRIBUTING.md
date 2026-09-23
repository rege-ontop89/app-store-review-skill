# Contributing

Contributions that make App Store submissions clearer, more accurate, or easier to reproduce are welcome.

## Good contributions

- corrections based on current Apple Developer or App Store Connect documentation;
- support for established build and upload pipelines;
- repeatable App Review rejection patterns and their verified resolution;
- clearer privacy, permission, subscription, or reviewer-access guidance;
- improvements to the bundled validation script.

## Requirements

- Use primary sources where possible, especially Apple and the relevant build-tool documentation.
- Keep the skill framework-neutral. Pipeline-specific instructions belong in a clearly named section or reference.
- Do not commit reviewer credentials, signing certificates, provisioning profiles, API keys, private app identifiers, customer data, or unpublished review correspondence containing sensitive information.
- Keep `SKILL.md` focused and place detailed conditional guidance in `references/`.
- Preserve the Agent Skills directory name and frontmatter name: `app-store-review`.

## Before opening a pull request

1. Review the changed instructions for claims that may have become outdated.
2. Run `gh skill publish --dry-run` when GitHub CLI is available.
3. Test discovery with `npx skills add . --list`.
4. Run `git diff --check`.
5. Describe the real submission scenario or official documentation that supports the change.
