# Mindful Lock release checklist

Prepared 10 October 2026. Checked items reflect artifact preparation only. Unchecked items are real release gates or account-holder decisions, not verified completion.

## Prepared here

- [x] Clone app-docs locally; preserve the existing Finnish Pro landing and docs.
- [x] Add responsive landing, support, privacy, terms-summary, and audio-credit pages under `mindful-lock/public/`.
- [x] Reuse the existing 1024px icon and produce web sizes.
- [x] Draft App Store English metadata, reviewer walkthrough, entitlement context, beta copy, and launch copy.
- [x] Provide screenshot storyboard, capture requirements, source references, and static package validation.

## Owner/account decisions

- [ ] Confirm support inbox `ammar.ofc@gmail.com` is appropriate for Mindful Lock and monitored.
- [ ] Confirm full seller/legal/copyright name; draft uses “Ammar” internally and the app name in the website footer.
- [ ] Choose pricing, territories, availability date, and release mode; no payment implementation exists in the inspected app.
- [ ] Supply review contact name, email, and phone in App Store Connect.
- [ ] Create the app record and record its actual Apple App ID; recommended category Health & Fitness / Productivity.
- [ ] Complete current age rating, content rights, medical-device status, encryption/export, DSA/trader, and other applicable account questionnaires.

## App implementation and signing blockers observed

- [ ] Replace `com.example.MindfulLock` and both extension bundle IDs with registered final IDs; keep the required extension prefixes.
- [ ] Replace `group.com.example.MindfulLock` consistently in app/monitor entitlements and `SharedConfiguration.group`; register and provision the group, including shared Keychain access.
- [ ] Verify developer team selection and request/obtain Family Controls **distribution** approval for all relevant App IDs. Recreate distribution profiles and inspect archive entitlements.
- [ ] Add an easily accessible **in-app privacy-policy link** to the final public URL. The inspected UI only exposes audio source/license links.
- [ ] Audit required-reason APIs (including UserDefaults and filesystem use), add justified `PrivacyInfo.xcprivacy` manifests where required, and inspect the archive privacy report. No manifest was found in source.
- [ ] Build a clean standard **Release** archive, not a QA DeviceReleaseTests or legacy-seed configuration. Confirm no fixture controls or accelerated activity durations.
- [ ] Verify icon validity, opacity, rights, bundle versions, extension embedding, deployment target, and app/extension signing.
- [ ] Decide and validate iPad support: current `TARGETED_DEVICE_FAMILY = "1,2"` advertises it. If retained, test iPad and prepare its screenshots.

## Device and acceptance evidence

The adjacent README explicitly says the revised suite was compiled but not executed; historical results do not establish this revision's readiness.

- [ ] Run the latest core and Release-duration suite on the signed development device; retain build/commit and results.
- [ ] Run the separate interactive Face ID group with the owner present.
- [ ] Run long/overnight calendar cases separately; capture actual scheduling evidence, including midnight, next-day, time-zone, daylight-saving, and post-restart behavior appropriate to launch.
- [ ] Complete fault/recovery/privacy and uninstall/upgrade acceptance. Confirm Keychain persistence is accurately described.
- [ ] Manually validate accessibility, small/large devices, iPad layout/orientation, audio interruptions, headphones, and foreground timer resets.
- [ ] Validate the distribution build through TestFlight on real hardware, including selection → actual shield → completion → explicit unlock.
- [ ] Capture final App Store screenshots per `screenshots.csv`; inspect privacy, dimensions, fidelity, and device-family coverage. Capture a real review walkthrough if needed.

## Publish docs and submit

- [ ] Review privacy/terms against the final build and actual seller/support practices.
- [ ] Run `python3 mindful-lock/publishing/validate.py`; inspect responsive pages in a browser.
- [ ] Configure deployment for `mindful-lock/public/` without placing it inside the existing app’s `/docs`. Preserve Finnish Pro hosting, exclude `mindful-lock/publishing/`, and update proposed URLs if the final host or route differs. Commit, push, and verify the deployment.
- [ ] Open all intended public URLs unauthenticated; confirm privacy and support links in-app and App Store metadata resolve.
- [ ] Confirm App Privacy answers against final archive and SDK inventory; current recommendation is Data Not Collected conditional on unchanged behavior.
- [ ] Enter English listing copy, pricing, screenshots, copyright, legal/account information, and actual review contact.
- [ ] Upload the correct Release archive, resolve validation warnings, and select the processed build.
- [ ] Paste verified review notes and submit. Track approval separately; preparation is not submission or approval.
- [ ] After approval, update the landing page with the actual App Store link/badge and confirmed availability; deploy and verify it.

Apple source links and verification date: [sources.md](sources.md).
