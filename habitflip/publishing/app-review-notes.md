# App Review notes

Paste the walkthrough below into App Store Connect after the release checklist passes. Provide the account holder's actual name, email, and phone in the separate review-contact fields. No credentials are needed: the app has no account or login.

## Reviewer walkthrough

HabitFlip is a voluntary self-control app using individual Screen Time authorization through Family Controls. Please test on a physical iPhone or iPad running iOS/iPadOS 17 or later. Simulator UI does not demonstrate real Screen Time shields or Device Activity callbacks.

1. On first launch, tap **Start small**, then **Allow Screen Time access** and approve the system authorization request. Device authentication may be requested by iOS.
2. In **Choose apps**, use Apple's Family Activity picker to choose a nonessential app or category, then confirm. Website selections are not supported.
3. Tap **Choose activities**. For a short review path, deselect Meditation and select only Water, then tap **Block now**.
4. Open the selected app to see the system shield. Return to HabitFlip, open the Water activity, and confirm the water break.
5. Return to the activities screen and tap **Unlock apps**. Open the selected app again to verify the shield has been removed. Completing an activity alone does not unlock apps.
6. To review timers, start another pause with Meditation. Choose 5, 10, or 15 minutes and start. The shipping build uses the full selected duration. Leaving the screen, backgrounding, an audio interruption, or disconnected headphones resets an unfinished session.
7. To review scheduling, set up apps and activities while unlocked, tap **Schedule**, select today and a time at least two minutes ahead, and save. Leave the app and check the selected app after the time. iOS controls callback delivery. The 15-minute monitor interval is a start trigger, not an automatic unlock timer.
8. Optional: create a custom timer, confirmation, or checklist activity. Custom timers allow 1–180 minutes; checklists allow 1–10 steps. Changes to reusable definitions do not alter an already-active pause.

The app and relevant extensions need Apple's Family Controls distribution entitlement. Confirm the approved, signed distribution build before submission; this note does not claim approval has been granted.

No PIN, login, subscription, in-app purchase, web filtering, VPN, MDM, or remote service is required. Activities are timed or self-reported, and users retain control of Screen Time access. The medicine activity only confirms an existing routine dose and gives no dosing or medical advice.

Reflection text is temporary in-memory input, cleared on leaving or finishing the activity. Other preferences and activity progress are local. Meditation audio is bundled and attributed in the app.

Privacy: https://ammarisme.github.io/app-docs/habitflip/privacy.html
Support: https://ammarisme.github.io/app-docs/habitflip/support.html

## Before pasting

- Verify every label and flow against the final Release build.
- Replace missing review-contact fields in App Store Connect.
- Attach a real-device screen recording of authorization → shield → water completion → explicit unlock if needed to clarify the Screen Time flow. It is not included in this package.
- Verify public URLs work without authentication after GitHub Pages deployment.
