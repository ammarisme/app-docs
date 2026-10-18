# Evidence and reference sources

Reviewed 10 October 2026. Recheck Apple's live pages and App Store Connect at submission because accepted formats and questionnaire fields can change.

## Product truth

Adjacent source checkout: `/Users/ammar/Desktop/mindful-lock`.

- `README.md`: documented user flows, scheduling semantics, Release durations, temporary reflection text, revised-suite execution limits.
- `MindfulLock/ContentView.swift`: Stone palette, actual labels, activity UI, audio credits, lack of privacy-policy link.
- `MindfulLock/LockModel.swift` and `Core/LockSession.swift`: completion and explicit unlock, activity definitions, snapshot semantics.
- `MindfulLock/Services/AppServices.swift`, `SharedConfiguration.swift`, `KeychainSessionStorage.swift`, `ScreenTimeService.swift`: local preferences/files, device-only Keychain, authorization, shields, monitor callbacks.
- `MindfulLock.xcodeproj/project.pbxproj` and target entitlements: version 1.0/build 1, iOS 17, iPhone+iPad, placeholder bundle/group identifiers.
- `Resources/MeditationAudio/ATTRIBUTION.md`: Geoff Bremner source, CC BY 4.0, loops, fades, 128 kbps shipping encodes.
- `MindfulLock/Assets.xcassets/AppIcon.appiconset/AppIcon.png`: copied without redesign.

## Repository inspiration

app-docs clone starts at commit `48faa24` (`Redesign landing page for Finnish Pro with App Store link.`).

- `README.md`: GitHub Pages branch `main`, source `/docs`.
- `docs/index.html`: standalone responsive landing, metadata, footer links.
- `docs/learn-finnish/index.html`: public privacy/use documentation pattern.
- `docs/learn-finnish/support.html`: established support email `ammar.ofc@gmail.com`.

Finnish Pro's servers, accounts, analytics/crash collection, remote config, and App Store ID do not describe HabitFlip and were not copied.

## Apple primary sources

- [Product page guidance](https://developer.apple.com/app-store/product-page/): positioning and field presentation.
- [App information](https://developer.apple.com/help/app-store-connect/reference/app-information/app-information/): name/subtitle and identity fields.
- [Platform version information](https://developer.apple.com/help/app-store-connect/reference/app-information/platform-version-information/): description, promotional text, keywords, support URL. Validation uses 30-character name/subtitle, 170-character promo, 100-byte keywords, and 4,000-character description limits.
- [Screenshot specifications](https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications/): device-family sizes and upload requirements.
- [App Privacy Details](https://developer.apple.com/app-store/app-privacy-details/): collection definition, on-device-only processing, and optional support disclosure criteria.
- [Review Guidelines](https://developer.apple.com/app-store/review/guidelines/): accurate metadata and accessible in-app/public privacy policies.
- [Configuring Family Controls](https://developer.apple.com/documentation/xcode/configuring-family-controls): development vs distribution entitlements.
- [Family Controls entitlement request](https://developer.apple.com/documentation/familycontrols/requesting-the-family-controls-entitlement): distribution request guidance.
- [Required-reason APIs](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_use_of_required_reason_api): privacy-manifest audit reference; no guessed reason codes supplied.
- [Standard EULA](https://www.apple.com/legal/internet-services/itunes/dev/stdeula/): linked standard license; the site terms page is a product-use summary.

## Media and hosting

- [Gentle Relaxing Stream 2](https://freesound.org/people/Geoff-Bremner-Audio/sounds/697496/), Geoff Bremner.
- [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
- [GitHub privacy statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement): website-hosting disclosure.

No claims of live deployment, actual store approval, price, test execution, or final screenshot delivery are inferred from these sources.
