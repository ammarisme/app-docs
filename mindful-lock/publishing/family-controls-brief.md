# Family Controls distribution entitlement brief

Use as supporting product context if Apple's current request workflow asks for it. This is not an entitlement approval or a submitted request.

**App:** Mindful Lock, native SwiftUI, iOS/iPadOS 17+.

**Purpose:** Individual, voluntary app pauses that make room for a user-chosen activity before returning to distracting apps. The user explicitly grants individual Screen Time authorization and chooses apps/categories in Apple's picker. No child accounts, monitoring dashboard, remote commands, VPN, or MDM are used.

**API use:** FamilyControls for authorization and opaque app/category selections; ManagedSettings for shields in the named MindfulLock store; DeviceActivity for recurring start triggers on selected weekdays. Completing all activities enables an explicit Unlock apps action. Ending a monitor interval never removes the shields.

**Targets requiring distribution review:** main app, ShieldConfiguration extension, and ActivityMonitor extension, each with its final registered App ID. Source IDs currently use `com.example.MindfulLock` and extension suffixes; they must be replaced consistently before release.

**Data handling:** selection tokens, schedule, and custom activity definitions remain in the local App Group. Active pause and completed activity IDs use a shared device-only Keychain item. No app-operated server, analytics SDK, or transfer of selection tokens off-device.

**User control:** permission can be revoked through iOS. Activities are timed or self-reported. No claim of tamper-proof enforcement, parental supervision, or medical outcomes.

**Distribution steps:** consult Apple's current Family Controls configuration/request guidance, obtain distribution approval for the relevant App IDs, regenerate distribution provisioning profiles, archive the actual Release configuration, and inspect the signed main app and extensions. Development entitlements do not establish distribution approval.

Reference: https://developer.apple.com/documentation/xcode/configuring-family-controls
Request guidance: https://developer.apple.com/documentation/familycontrols/requesting-the-family-controls-entitlement
