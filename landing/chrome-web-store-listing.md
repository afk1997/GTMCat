# Chrome Web Store — listing content (paste-ready)

Everything below clears the red items in the "Unable to publish" dialog. Paste into the
**Privacy practices** tab (and Store listing tab) of the item edit page, then **Save Draft**.

---

## Single purpose description

> GTMCat Capture surfaces high-intent Reddit conversations for your product. It reads the
> public Reddit threads, comments, and author info that **your own logged-in reddit.com
> session** can already see, and sends that content to your GTMCat account for buyer-intent
> scoring and go-to-market research. It is strictly **read-only** — it never posts, comments,
> votes, messages, or takes any action on your Reddit account.

(Single, narrow purpose: capture Reddit content via the user's own session into their GTMCat account.)

---

## Permission justifications

Paste each into its matching field.

**storage**
> Stores the device pairing token (which links this browser to the user's GTMCat account) and
> a local capture outbox — the queue of thread IDs awaiting upload — so capture survives
> service-worker restarts and brief offline periods. No browsing history or personal data
> beyond the pairing token and queue is stored.

**alarms**
> Wakes the MV3 service worker on a periodic schedule so background/scheduled capture keeps
> running when the popup is closed. MV3 service workers are terminated after ~30 seconds of
> inactivity; the alarm is the standard keepalive so a capture run isn't cut off mid-sweep.

**tabs**
> Used only to detect whether the active tab is on reddit.com (to scope capture to Reddit and
> show accurate capture status) and to open the GTMCat dashboard in a tab. It does not read the
> contents of non-Reddit tabs.

**sidePanel**
> Provides the extension's main UI — the bulk-capture side panel, where the user starts/pauses
> capture, watches per-profile progress, and reviews what's being captured.

**Host permission: `*://*.reddit.com/*`**
> This is the sole capture source. There is no Reddit API; the extension reads the public
> threads/comments/authors that the user's own logged-in Reddit session can see, so it needs to
> fetch pages on reddit.com. Read-only — it never submits anything to Reddit.

**Host permission: `app.gtmcat.xyz` (the GTMCat backend)**
> So the extension's background can call the user's own GTMCat backend over HTTPS (device
> pairing, the /check de-duplication probe, /ingest upload, and a heartbeat) without CORS
> errors. It talks only to the user's own GTMCat account.

**Remote code**
> No remotely-hosted code is used or executed. All JavaScript is bundled in the package. The
> only network requests are HTTPS **data** calls to reddit.com (the user's session) and to the
> GTMCat backend, plus a Google Fonts stylesheet used for UI typography. No remote scripts are
> downloaded, injected, or evaluated; there is no eval of remote content.

> (Optional hardening — removes this question entirely: self-host the UI font instead of the
> Google Fonts `@import`. Ask and I'll bundle the font into the extension.)

---

## Data use & certifications (Privacy practices tab)

**What user data the extension handles**
- **Reddit content** (public thread titles/bodies, comments, public author handles & karma) that
  the user's logged-in session can see — uploaded to the user's GTMCat account for scoring.
- **Authentication info**: a device **pairing token** only. The extension **never** sees, stores,
  or transmits the user's Reddit (or GTMCat) **password or credentials** — it relies on the
  existing browser session.
- **Website content**: only reddit.com page content, only while capturing.

**How it's used:** solely to provide the GTMCat product (buyer-intent scoring + GTM research) for
the user's own account. Processing subprocessors (OpenAI for scoring, hosting, database, email,
payments) are disclosed in the Privacy Policy at `gtmcat.xyz/privacy`.

**Certify all three (they are true for GTMCat):**
- ☑ I do **not** sell or transfer user data to third parties outside the approved use cases.
- ☑ I do **not** use or transfer user data for purposes unrelated to the item's single purpose.
- ☑ I do **not** use or transfer user data to determine creditworthiness or for lending.

**Privacy policy URL:** `https://gtmcat.xyz/privacy`  (publish `privacy.md` first)

---

## Assets checklist (the remaining red items)

- **Icon image** — upload **`apps/extension/public/icon/128.png`** (the GTMCat cat, 128×128) as the
  store icon. (The manifest already references the 16/32/48/128 set after the latest build.)
- **Screenshot (≥1, required)** — 1280×800 or 640×400, PNG/JPEG. Best options:
  1. The **side panel** open over a reddit.com page, showing capture progress; or
  2. The **GTMCat Signals inbox** (scored threads). Take it on a real screen, crop to 1280×800.
  A short screencast of "open side panel → capture runs → signals appear" also satisfies it.
- **Support URL** — set to `https://gtmcat.xyz/support` once `support.md` is live (that resolves the
  "Support URL is not reachable" error). A `mailto:` is not accepted as the support URL.

---

## Store-listing copy (Store listing tab)

**Name:** GTMCat Capture
**Summary (≤132 chars):** Find Reddit threads ready to buy your product. Read-only capture through your own session — never posts, never votes.
**Category:** Productivity (or Developer Tools)
**Description:**
> GTMCat finds the Reddit conversations where people are looking for what you sell — and scores
> each one by buyer intent so you spend time only where it counts.
>
> GTMCat Capture is the read-only bridge: it captures Reddit through **your own logged-in
> browser session** (no Reddit API, no scraping service) and sends threads to your GTMCat
> account, where they're scored and organized. You engage **by hand, from your own account** —
> GTMCat never posts, comments, votes, or automates anything on Reddit.
>
> • Buyer-intent scoring on every captured thread
> • A compliance read of each subreddit's rules before you reply
> • Humanized reply drafts you review and post yourself
>
> Requires a GTMCat account (free trial at gtmcat.xyz). Capture profiles are throwaway,
> read-only logins; your posting identity is stored as a username only — never credentials.
