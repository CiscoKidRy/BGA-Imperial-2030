# Code counsel before the playtest commit

Date: 2026-10-15. Repository: the local Imperial 2030 tree whose origin is https://github.com/CiscoKidRy/BGA-Imperial-2030.git. I read playtest/engine.py, playtest/server.py, playtest/index.html, playtest/test_engine.py, and .gitignore. I did not re-read the booklet. I did not commit, push, merge, stage, or edit the game files.

## 1. Excluded material

The four playtest files do not contain reference/, grok/source-docs/, source-email/, a keys folder, rule PDFs, publisher art, passwords, private keys, pem data, sftp.json, or Python bytecode. index.html is a schematic page and has no image files. engine.py comments name BGG file 50631 and board photo 574713. Those are public file and image numbers, not copies of the PDF or the photo.

.gitignore is the exclusion list. It is not a copy of the excluded material. It ignores source-email/, *.pem, *password*, *secret*, sftp.json, reference/, grok/source-docs/, __pycache__/, and *.pyc. A comment says passwords from the BGA welcome email live in a keys folder outside this repository, and that rulebooks and art stay in this Dropbox folder and are not committed. That comment does not contain a password. There is no keys/ ignore line. A keys directory copied into the repo later would not be ignored by that name.

__pycache__ and *.pyc are ignored. git check-ignore attributes playtest/__pycache__/engine.cpython-314.pyc to the __pycache__/ line, and a sample .pyc path to the *.pyc line. git status --ignored shows playtest/__pycache__/ as ignored. The bytecode files on disk are engine.cpython-314.pyc and test_engine.cpython-314.pyc. They are not inside the four source files. git check-ignore also ignores the publisher rules PDF and image 574713 under reference/, a PDF under grok/source-docs/, and source-email/_index.json.

## 2. Server

server.py does not upload to Board Game Arena. The module docstring says it serves the schematic page and one in-memory game and does not upload anything to Board Game Arena. main() binds ThreadingHTTPServer to 127.0.0.1 on port 8765 and prints http://127.0.0.1:8765/. The handler reads local index.html and answers /api/game JSON. I found no outbound request and no Board Game Arena host.

The engine hides another seat's cash inside one view. The local server still returns whichever seat the request names, and the page uses that for "View as." That stays on localhost.

## 3. The limit note

engine.py sets limit_note to these sentences: this is a local test of the experienced setup, not the published board; fleet and army moves are only offered across borders named in the booklet or the Quick Intro; Panama's west mouth is not drawn; convoy, factory destruction, the 15-flag replacement choice, and both variants are not in this test; a peace offer ends the battle without asking each defender; if the government cannot cover interest from personal cash, the unpaid part remains; the booklet does not name who leads India, Brazil, the United States, or Europe, and this test rotates that lead.

I am not confirming the booklet. I am comparing the note with the code. The note does name each of those gaps.

Named borders: army moves use the LAND pairs, plus rail between that nation's own cities when the rail is open. Fleet moves use the SEA pairs, and a fleet in a home city may also use the HARBOR pairs. A move outside those sets is rejected as not on a named border. The file also defines four COAST pairs and builds COAST_ADJ, and nothing reads COAST_ADJ, so those coast links are not offered. The note does not claim that every named border is implemented.

Panama: the engine has no Panama region. index.html also says "No north-south wrap. Panama's west mouth is not drawn." The canal table only has Colombia between the Caribbean Sea and the North Pacific, and North Africa between the Mediterranean Sea and the Indian Ocean.

Convoy: the word appears only in the note. There is no convoy action.

Factory destruction: factories are added at setup and when a city is built. I found no code that removes a factory. A hostile army blocks a new factory and blocks production in that city. It does not destroy the factory.

15 flags: each nation starts with 15 flags. If none are left, placement is refused and there is no replacement choice. If at least one remains, placing a flag writes that nation onto the region even when another nation already had the flag, and the previous nation's supply is not increased. The note names the missing replacement choice. It does not mention that overwrite.

Variants: I found no variant switch. Starting cash is the experienced table only. The page says the basic deal is not on this screen. The note says both variants are absent.

Peace: the attacker is asked to fight or not fight. Choosing peace logs that peace is offered, leaves the units together, and returns to maneuver. Defenders are not asked. The button detail says the same thing.

Unpaid interest: the treasury pays other bondholders first. The government then pays from personal cash up to what it has. Any remainder is logged as unpaid in this test. It is not stored as a balance and it is not collected later. The government's own shortfall is logged as forgone, not as a payment that remains due to someone else. That matches the note's sentence about a shortfall personal cash cannot cover.

Draft lead: the leader seat stays 0. Each nation's lead is that seat plus the nation index, wrapping by the player count. Russia starts at the start player. China starts one seat later. India, Brazil, the United States, and Europe each start one seat further. For those later nations the banner adds that the booklet does not name the leader and that this test rotates the lead. The limit note says the same.

## 4. Tests

I ran python -m unittest test_engine.py from the playtest directory. The result lines were:

Ran 10 tests in 0.008s

OK

Cash privacy is tested. test_opening_leaves_two_million_false_for_experienced checks that the other seat's cash is None, that the acting seat sees 11, and that 11 is not in the log. test_china_rondel_sentence_cost_and_hidden_cash checks that the other seat's cash is None and that the other seat does not see the personal "cannot pay" block. test_interest_shortfall_does_not_print_remaining_cash checks that the interest log does not contain "cannot cover" or "empty".

The China factor-2 sentence is tested. test_china_rondel_sentence_cost_and_hidden_cash asserts "On Investor, factor 2, choosing Taxation (4 spaces, cost 3) or Factory (5 spaces, cost 6)." The engine uses that same sentence when the marker is on Investor and the factor is 2.

Swiss force repricing is tested. test_swiss_force_reprices_the_shorter_move stops a passing move on Investor, checks that the marker lands on Investor, checks that the payer's cash stays 10, and checks that the log contains "forces". The force action recalculates the destination and the cost for that shorter stop.

Tax to 25 is tested. test_taxation_to_25_skips_investor_steps commits taxation from power 24 with flags on Mexico and Turkey, expects power 25, expects the game to be over, expects the phase not to be investor-buy, and expects the sentence "Game over: Russia reached 25."

New Orleans to Mexico is tested. test_named_border_and_blocked_invented_border moves an army from New Orleans to Mexico and expects a move to Canada to raise ValueError. The land list includes the New Orleans to Mexico pair.

## 5. Secrets

I found no password, private key, pem block, sftp credential, BGG numeric user id, or Studio table number in the four playtest files or in .gitignore. The word token in index.html is a request serial. It increments so a late response cannot overwrite a newer one. It is not a credential. The numbers 50631 and 574713 in engine.py are the BGG file number and the board-photo number. They are not a user id and not a Studio table number.

## 6. Commit answer

Yes. These four playtest files, plus the gitignore lines, are safe to commit to the public repo.

What must stay unstaged is playtest/__pycache__/ and the .pyc files; reference/, including the rule PDFs and publisher images; grok/source-docs/; source-email/; sftp.json; *.pem; files whose names match *password* or *secret*; and any keys folder if one is ever placed inside the repo. Do not force-add ignored paths.

This working tree also has other changes that are not those four files. I did not review their contents for this question, so they should stay out of this commit: the modified grok/RESUME.md and grok/SESSION-INSTRUCTIONS.md, and the untracked grok counsel notes and grok/ui-design-2026-10-15.md. This review file is a counsel note, not part of the playtest commit.

git status currently shows .gitignore as modified and playtest/engine.py, playtest/server.py, playtest/index.html, and playtest/test_engine.py as untracked. The bytecode directory is ignored. I did not stage anything.

## After this review

A second counsel read the notes and the interface plan and wrote `2026-10-15-commit-review-notes.md`. That review says those files are safe to commit with this change. They go in the same commit because the working agreement commits the counsel notes with the change they review. The excluded paths in section 6 stay unstaged.
