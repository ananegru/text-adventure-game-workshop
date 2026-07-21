# Prerequisites & Setup

Complete this setup **before** running the labs — ideally the day before. The
slow, easy-to-forget items are installing the Squad CLI and authenticating with
GitHub and Copilot. Front-loading them is the difference between a smooth
session and watching an install bar.

> **Time budget:** with setup done beforehand, the two labs run in **~60 min**
> (Plan ~20, Implement ~30, Score ~10). A first-time install of every tool adds
> ~30–45 min — do it the day before.

> **Shell note:** command blocks below are labeled `bash`, but they run the same
> in **PowerShell 7+** — only where they differ (like the pre-flight script) is a
> separate Windows block shown.

---

## 1. Accounts & Access

| Requirement | Notes |
|---|---|
| **GitHub account with Copilot** | Required for every station. Squad runs on GitHub Copilot. |
| **Copilot in the CLI or VS Code** | You drive the Squad from a terminal (`squad`) or from Copilot Chat in VS Code. |

---

## 2. Tools to Install

`scripts/preflight.sh` (macOS/Linux) or `scripts/preflight.ps1` (Windows
PowerShell) checks for all of these. Install anything it flags.

| Tool | Why | Install |
|---|---|---|
| **Node.js ≥ 22.5 + npm** | Runtime for the Squad CLI | [nodejs.org](https://nodejs.org/) |
| **Python ≥ 3.11** | Runs the text-adventure game and Spec Kit | [python.org](https://www.python.org/) |
| **uv** | Python env + test runner; also runs Spec Kit via `uvx` | [astral.sh/uv](https://docs.astral.sh/uv/) |
| **Squad CLI** | The 8-role Squad (Lab 02) | `npm install -g @bradygaster/squad-cli` |
| **GitHub Copilot CLI** | Runs the Squad from the terminal | `npm install -g @github/copilot` (or use Copilot in VS Code) |
| **GitHub CLI (`gh`)** | Auth for Squad (Issues/PRs) | [cli.github.com](https://cli.github.com/) |
| **Spec Kit** | Spec-driven workflow (Lab 01) | No install needed — run on demand with `uvx` (see Lab 01) |

> **Squad is experimental (alpha).** These materials were validated against
> **squad v0.9.6** (`@bradygaster/squad-cli`). Commands and output may drift in
> newer releases — if something looks different, trust the live tool over the
> docs. See the [Squad repo](https://github.com/bradygaster/squad) for breaking
> changes.

### Install checks

```bash
node --version      # >= 22.5
python3 --version   # >= 3.11
uv --version
squad --version
gh --version
```

If any command fails, install the missing tool before continuing.

---

## 3. Authenticate

Squad uses the GitHub CLI **and** drives GitHub Copilot — sign in to both:

```bash
gh auth login
gh auth status      # should report: Logged in to github.com

copilot             # launch once; run /login if prompted, then /exit
```

Using VS Code instead of the terminal? Just sign in to Copilot there — the
`copilot` step above is only needed for the terminal `squad` workflow.

---

## 4. Run the Pre-flight Check

From the workshop root, run the script for your platform — both run the
identical set of checks:

**macOS / Linux (bash):**

```bash
./scripts/preflight.sh
```

**Windows (PowerShell 7+):**

```powershell
./scripts/preflight.ps1
```

This one script validates the whole environment so there are no surprises. It
checks your local tools (`node`, `npm`, `python3`, `uv`, `squad`, `gh`), GitHub
auth, the game workspace tests in `app/`, and Squad's own health via
`squad doctor`. A clean run ends with `==> Preflight complete`.

> Two Squad info lines about `vscode-jsonrpc` and `@github/copilot-sdk` are
> **normal and harmless** for global installs.

---

## 5. Repository Checks

From `squadsdd-workshop/`, verify these exist:

- `labs/`
- `specs/speckit/`
- `.squad/`
- `app/` (the game workspace you'll build in during Lab 02)

Confirm the baseline game workspace runs:

```bash
cd app && uv run pytest      # baseline: 2 passed, 8 skipped
cd ..
```

---

## 6. Lab Readiness

You are ready when you can:

1. Open `specs/speckit/spec.md`.
2. Run `squad doctor` successfully (9 checks pass).
3. Start a Squad session with `squad` (an interactive shell — type `quit` to
   exit) **or** select the **Squad** agent in Copilot Chat in VS Code.

---

## Notes

- Participant materials intentionally avoid timestamped execution plans. Use the
  [facilitator guide](facilitator/run-of-show.md) for sequence, not minute-by-minute scheduling.
- Model availability varies by Copilot plan. If `.squad/config.json` pins a
  model you can't access (e.g. `MAI-Code-1-Flash` on some plans), Squad falls
  back to a fast model and the labs still work — see Lab 02, Feature 3.
