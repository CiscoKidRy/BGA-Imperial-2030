# BGA Imperial 2030

Working copy for adapting Imperial 2030 on Board Game Arena Studio.

The game page is https://boardgamegeek.com/boardgame/54138/imperial-2030/.

This repository is public. The BGA walkthrough says not to commit a file that contains an SFTP password, and not to commit original publisher graphics. Those files stay in the Dropbox folder and are listed in `.gitignore`.

Revisions are stored on GitHub and in the local working copy below. No GitLab remote is used.

## Where the files live

Local working copy:

`C:\Users\ryanh\Dropbox\Ryan\AI-SI-Grok-Tools\BoardGameAreana - Imperial 2030`

GitHub:

https://github.com/CiscoKidRy/BGA-Imperial-2030

SSH keys and the BGA Studio connection note are not in this repository. They are in:

`C:\Users\ryanh\Dropbox\Ryan\Key SSH API Private Public Security RSA`

The public key file is `bga-development-rsa-key.pub`. The private key is `bga-development-rsa-key`.

## How a change is published

Use this sequence for every change after the repository exists.

1. Do the work on a new branch in the local folder above.
2. Have a counsel of agents read the change and the sources it relies on. The counsel writes its findings under `grok/counsel/`. A claim about Board Game Arena or about Imperial 2030 stays out of the branch unless a retrieved source states it.
3. Commit the branch. The message says what changed and why.
4. Push the branch to GitHub.
5. Open a pull request. The description uses `.github/pull_request_template.md`: what changed, why, sources, counsel review, how it was checked, and limits.
6. Merge the pull request.

BGA Studio also has its own commit button at Control Panel / Manage Games / the game / Commit my modifications now. The First steps page says that commit does not work until an admin has committed the project once, and it says to keep another copy in git or GitHub. Use both once a Studio project exists. Do not put the SFTP password or publisher art in the GitHub commit.

## What is not in git

- `source-email/` — the BGA Studio emails, including passwords and a one-time password link
- `reference/` — local rule and art downloads, when a download succeeds
- `grok/source-docs/` — saved API responses, the walkthrough text, and the five BGA presentation PDFs

## Pickup

Read `grok/RESUME.md` and `grok/SDLC-PLAN.md` before changing the game.
