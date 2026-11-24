# Build notes — The One-Line Exit

- Read the kit RULES.txt / competition.yaml first. Key gate: entry.txt must
  be UTF-8, 1-140 characters, not whitespace only (stricter than the
  1-200 range in the task brief, so the entry targets <= 140).
- Judge criteria followed: a real one-line resignation letter, surprise
  punchline, specific voice (sole IT guy), quotable, no padding.
- v1: "I resign — after five years as the office's only IT guy, I've
  finally fixed my biggest bug: this job." — local test passed (101 chars).
- v2 (revision): changed the opening to "I hereby resign" so it reads more
  like a formal letter someone could actually send. Re-ran local test:
  108 chars, 1 line, 0 newlines, 110 UTF-8 bytes — within the gate.
- Local test: `mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py`,
  then checked out/entry.txt length/content. Test output dir removed
  afterwards; entry dir contains only main.py, README.md, prompt.txt,
  BUILD-NOTES.md.
- Not submitted; no repo created; no contact with make.fun.
