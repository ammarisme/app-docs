# Screenshot production guide

The storyboard and final overlay copy are ready in [screenshots.csv](screenshots.csv). Final App Store screenshot PNGs and a review video are **not included**: they require genuine captures from the release candidate, especially real Screen Time selection/shield behavior. Existing QA screenshots are development evidence, not automatically store-ready. No mockups have been passed off as app captures.

## Capture requirements

1. Use the final Release candidate with genuine durations and no `DEBUG`, `DEVICE_TEST_SUPPORT`, or `LEGACY_TEST_SEED` behavior. Do not use UI fixtures or remove their banners to disguise them.
2. Obtain Screen Time permission on a compatible physical device for real picker/shield material. Use only nonessential apps and non-sensitive sample custom activities. Do not include personal reflections, medication details, Apple Account details, notifications, or app-selection information without consent.
3. Capture the six scenes in the CSV. Use readable, actual UI. App Store screenshots should show the app in use; the welcome-only screen can be moved later if the first screenshot benefits from demonstrating core behavior.
4. Export device-native PNGs and inspect at actual size. Use the same order and messaging on each supported device family. Keep all essential UI within the frame; no stretched iPhone screenshots labeled as iPad.
5. Confirm current upload slots and accepted dimensions in App Store Connect. Apple currently lists **1320 × 2868** portrait among accepted large iPhone sizes and **2064 × 2752** or **2048 × 2732** portrait for the required 13-inch iPad set when the app supports iPad. The project currently targets both device families.
6. Verify every screenshot matches the submitted build and English localization. Recheck image dimensions, color profile, readability, privacy, and absence of development controls before upload. A preview video is optional unless review requests it.

## Visual direction

Use the app's Stone palette: paper `#f2eadd`, ink `#594b3d`, clay `#ae725b`, panel `#e9decd`. For small website text and buttons, the website darkens clay to `#875440` for stronger contrast. Keep copy short, serif headlines, generous spacing, and actual screenshots dominant. Avoid invented testimonials, productivity scores, medical claims, or promises of unbreakable blocking.

## Icon

The original 1024 × 1024 app icon is copied unchanged to `mindful-lock/public/assets/app-icon-1024.png`. Web sizes are derived from that original. Xcode supplies the App Store icon through the asset catalog; verify the archive contains the expected icon and that the original meets Apple's current opacity/asset requirements. Confirm artwork rights with the owner.

## Acceptance record

Record the build/version, device, OS, image dimensions, capture date, and reviewer for each final asset. Keep raw captures and upload files together in a dedicated release-assets folder when ready. Final captures are a release gate in [release-checklist.md](release-checklist.md).

Apple reference: https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications/
Metadata accuracy: https://developer.apple.com/app-store/review/guidelines/#accurate-metadata
