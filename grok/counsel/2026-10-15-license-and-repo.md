# Counsel review, 2026-10-15, license check and repository decisions

Two reviewers read the documentation diff. They did not open Credential Manager, `source-email/`, the keys folder, or temporary session files.

## Kept

- The notes say not to create a Reversi project or another tutorial project. The Studio, First steps, and walkthrough sentences stay as retrieved text.
- The repository is described as public. GitLab is not a remote. `git remote -v` shows only `origin` at `https://github.com/CiscoKidRy/BGA-Imperial-2030.git`.
- Imperial 2030 and BoardGameGeek id 54138 are absent from the retrieved licensing and project arrays. The notes do not say that BGA holds no license beyond that list.
- These figures agree across the plan and the resume: licensing `games` 2265, `licenses-available` 1175, `licenses-published` 925, `licenses-refused` 140, projects 2662, managed games empty, `userConfirmedBeingDev` false, login `username` CiscoKidRyan0, licensing `developer-username` CiscoKidRyan.
- Concordia 124361, Imperial Settlers 154203, Imperial Steam 338760, and project `imperialminers` are other titles.
- No password, request token, private-key block, or street address is in the diff. A scan of the diff against the Credential Manager secret reported absent. Three password prefixes from the welcome email are absent from the markdown.
- The gate line "about 63%" matches (75+85+55+60+80+25+60)/7.
- Step 2 says "These retrieved instructions" and then four bullets.

## Corrected

One reviewer flagged this sentence: "Request Art Files was not available for Imperial 2030. The title is not in the list, so the page had no row on which to offer it."

Replacement now in step 2: the licensing `games` array has no Imperial 2030 entry. Request Art Files was not checked as its own control. Unavailability is only an inference from that missing entry.

The second reviewer found no sentence to replace in the five files as they stood before the FileZilla lines below.

## FileZilla lines added after that review

Those lines were checked against `%APPDATA%\FileZilla\sitemanager.xml`, which this session did not modify. The `BGA Studio` element stores the host, port 2022, user CiscoKidRyan, Protocol 1, Logontype 5, the `bga-development-rsa-key` path, and this Dropbox folder as LocalDir. Its comment says the remote home is `/`. RemoteDir is stored as `1 0`. The user said FileZilla connected with the key, did not ask for the Credential Manager password, and listed `/` empty. A second element named MacMini is in the file. Its host and user are not in this repository.

The trusted-host file `%APPDATA%\FileZilla\hostkeys.xml` contains the string `1.studio.boardgamearena.com`. The key material in that file is not copied here.
