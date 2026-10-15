# Counsel review, 2026-10-15, private Studio project

The user asked to start developing so Studio could be learned, and then said not to publish anything.

## Checked against the creation response

- `POST /admin/studio/newproject.html` returned "Done!".
- The response named `ImperialTwoThousandThirty (imperialtwothousandthirty)` and SVN revision 340706.
- HAL's lines said all good for images, PHP, SQL, JS, and CSS. The same log had two `cp` lines for missing png and jpg files in `emptygame`.
- Managed games then listed one game, `prod-version` `-not deployed-`, `prod-status` null.
- The projects list had no row named `imperialtwothousandthirty`.
- The downloaded `gameinfos.jsonc` has `bgg_id` 54138 and the template name "My Great Game".
- No alpha or deploy call was made. The request included `visibility=private`. The managed-games object has no visibility field, so privacy is the value that was sent plus the absence of a projects-list row, not a separate confirmation field.

## Left unchanged

The downloaded skeleton was not edited. Copyright placeholders and the template title remain. Imperial 2030 rules were not added.

## Limit

The historical note `grok/counsel/2026-10-15-license-email.md` still says the project stays uncreated. That sentence described the review at the time of the email. Step 5 is the later decision.
