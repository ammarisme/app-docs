# Privacy and submission answers

Assessment date: 10 October 2026. Source inspection supports the recommendations below; final answers must match the actual submitted archive and current Apple questionnaire.

## App Privacy label

Recommended answer for the inspected app: **Data Not Collected**, if the final build retains the current on-device-only behavior. No app-owned server, analytics SDK, advertising SDK, login, HealthKit, contacts, location, photos, microphone collection, or user-data upload was found. Audio playback is local. Opening source/license links hands the visit to external websites.

Apple defines collection around off-device transmission accessible beyond real-time request handling. On-device processing alone is not collection. Voluntary support email is described separately in the policy; assess it against Apple's optional-disclosure criteria rather than assuming every support workflow is exempt. Website hosting logs belong to GitHub's hosting context, not an invented app telemetry pipeline. If any SDK, remote crash reporting, or support upload is added, reassess the label.

Do not request App Tracking Transparency authorization: the inspected app does not implement tracking. Do not label local medication confirmation as uploaded Health Data.

Reference: https://developer.apple.com/app-store/app-privacy-details/

## Evidence in the adjacent app checkout

| Behavior | Source |
| --- | --- |
| Local onboarding and authorization preferences via UserDefaults | `MindfulLock/Services/AppServices.swift` |
| Shared local files, file protection, scheduled-occurrence records | `MindfulLock/Services/SharedConfiguration.swift` |
| Device-only Keychain active pause, deleted on successful unlock | `MindfulLock/Services/KeychainSessionStorage.swift`, `MindfulLock/LockModel.swift` |
| Temporary reflection/checklist state, bundled audio source/license links | `MindfulLock/ContentView.swift` |
| Opaque selections, website token discard | `MindfulLock/Services/ScreenTimeService.swift`, `MindfulLock/LockModel.swift` |
| Static network/analytics source guard | `qa/audit-local-privacy.py` |
| Audio source and modifications | `Resources/MeditationAudio/ATTRIBUTION.md` |

Do not promise complete deletion on uninstall: Keychain state can survive removal. Ordinary App Group files are not explicitly excluded from device backup in the inspected code. Do not promise that every app file is excluded from iCloud backup; only the active pause Keychain item is explicitly device-only. There is no erase-all control in the inspected UI.

## Privacy manifest: open implementation work

No `PrivacyInfo.xcprivacy` was found in the app source. The shipping app uses UserDefaults and filesystem APIs. Review Apple's current required-reason API list against all targets and linked code, choose reasons justified by actual use, add manifest files to the correct app/extension resources, and inspect the archived privacy report. A Data Not Collected label does not remove required-reason manifest obligations. Do not copy a guessed reason code from this document.

Reference: https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_use_of_required_reason_api

## In-app policy access: open implementation work

The inspected UI links audio credits but has no easily accessible privacy-policy link. Add the public privacy URL to an accessible app surface before submission and verify it in Release. Apple requires a policy link in the app as well as the store metadata.

Reference: https://developer.apple.com/app-store/review/guidelines/#privacy

## Other questionnaire decisions

- **Age rating:** complete the current questionnaire truthfully. The medicine confirmation means health-related questions need attention; do not assign a rating from this package.
- **Medical status:** the app is a general personal-routine tool, not presented as a medical device; answer the current regulated-medical-device question according to actual intended use and seller circumstances.
- **Encryption/export compliance:** inspect Apple's current questionnaire and the archive. The source uses Apple Keychain and contains no custom encryption implementation. Do not assume a legal export classification from source inspection alone.
- **Advertising ID/tracking:** no IDFA or tracking implementation found.
- **Content rights:** preserve Geoff Bremner's CC BY 4.0 attribution and modification notice in-app and on the credits page; confirm rights to the app icon separately.
- **Accessibility labels:** only claim capabilities tested against Apple's current criteria. Existing narrow UI checks do not establish universal VoiceOver, text scaling, or device-size support.
