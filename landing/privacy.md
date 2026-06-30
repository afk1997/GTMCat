# Privacy Policy

**Last updated: June 30, 2026**

GTMCat ("GTMCat", "we", "us") helps you find and engage high-intent conversations on Reddit for
your product. This policy explains what we collect, why, who processes it, and the controls you
have. It covers both the **GTMCat web app** (gtmcat.xyz / app.gtmcat.xyz) and the **GTMCat Capture**
Chrome extension.

> Plain-English summary: We capture the **public** Reddit content your own logged-in session can
> already see, and use it to score buyer intent for your product. We **never** store your Reddit
> password, we **never** post or act on your behalf, we **don't sell your data**, and you can
> export or delete everything at any time.

## Who we are
GTMCat, San Francisco, CA, USA. Contact: **[support@gtmcat.xyz]**.

## What we collect

**Account data** — your email, name, and authentication records when you sign up. Passwords are
stored only as salted hashes (via our auth provider); we never see them in plaintext.

**Product context you provide** — the description of your product, value props, competitors,
keywords, target subreddits, and similar inputs you enter to tune scoring.

**Reddit content captured through your session** — when you run capture, the GTMCat Capture
extension reads **public** Reddit threads, comments, and public author details (handle, karma, account
age) that **your own logged-in reddit.com session** can see, and uploads them to your GTMCat account.
There is no Reddit API and no server-side scraping — if your session can't see it, we don't fetch it.
Restricted/private subreddits stay scoped to you and are never added to the shared content pool.

**Reddit posting identity** — if you choose to engage, we store your Reddit **username only**, never
your Reddit credentials. You post by hand, from your own account.

**Device & capture data** — a device pairing token that links a browser to your account, capture
run logs, and sync events.

**Usage & billing** — product usage (for metering allowances), and subscription state. Payments are
processed by our merchant of record (Dodo Payments); **we do not receive or store your full card
number** — Dodo handles card data.

**Diagnostics** — error reports and logs to keep the service reliable.

**What we do NOT collect:** your Reddit or GTMCat password/credentials; your browsing activity
outside reddit.com; any Reddit content your own session cannot see.

## How we use it
- To provide the product: score captured threads by buyer intent, organize your inbox, draft
  replies you review, and produce research/mentions reports.
- To operate your account, meter plan allowances, send transactional and (if enabled) digest emails.
- To secure, debug, and improve the service.

We do **not** use your data for advertising, and we do **not** sell or rent it.

## AI processing
To score threads, generate reply drafts, and create embeddings, captured thread content and your
product context are sent to our AI provider (**OpenAI**) for processing. This content is used to
return results to you; it is not used to train third-party models under our configuration.

## Subprocessors
We share data only with vendors that process it on our behalf to run GTMCat:

| Subprocessor | Purpose |
|---|---|
| Vercel | Application hosting |
| Neon (PostgreSQL) | Primary database |
| Upstash (Redis / queue) | Caching & background job scheduling |
| OpenAI | Intent scoring, reply drafting, embeddings |
| AutoSend | Transactional & digest email |
| Dodo Payments | Subscription billing (merchant of record; card data) |
| Sentry | Error monitoring |

## Data sharing
Beyond the subprocessors above, we disclose data only: (a) with your consent; (b) to comply with
law or valid legal process; (c) to protect rights, safety, or the integrity of the service; or
(d) in a business transfer (merger/acquisition), under this policy. **We never sell personal data.**

## The global content pool
Public Reddit threads are stored once and shared across GTMCat accounts keyed by Reddit IDs, so the
same public thread isn't re-fetched per user. Your **scoring, triage, drafts, notes, and product
context remain private to your account.** Restricted/private-sub content is never pooled.

## Retention & deletion
- We keep your data while your account is active.
- If your trial ends without upgrading, we keep your archive for **30 days** so you don't lose your
  work, then it may be removed.
- **Export:** you can export your data (signals, engagements, notes, targets, context) one-click from
  the app.
- **Delete everything:** you can purge all your account data from the app at any time. This removes
  your private data and tombstones it; shared public-pool threads (other users' captures) remain.
- If a thread is deleted on Reddit, we honor that deletion on re-check (purge + tombstone).

## Your rights
Depending on where you live (e.g., GDPR/UK GDPR, CCPA/CPRA), you may have rights to access, correct,
export, delete, or restrict processing of your personal data, and to object to certain processing.
You can exercise most of these in-app (export / delete-everything) or email **[support@gtmcat.xyz]**.
We do not sell personal information or use it for cross-context behavioral advertising.

## Cookies
We use a small number of strictly-necessary cookies (e.g., your login session). We don't use
advertising or cross-site tracking cookies.

## Security
Data is encrypted in transit (HTTPS). Passwords are hashed; secrets and tokens are stored securely.
The capture extension stores only a pairing token and a local outbox.

## Children
GTMCat is a business tool not directed to children and is not intended for anyone under 18.

## International transfers
We're based in the United States and process data there and in our subprocessors' regions. Where
required, transfers rely on appropriate safeguards.

## Changes
We'll update this page and the "Last updated" date for material changes, and notify you in-app or by
email where appropriate.

## Contact
Questions or requests: **[support@gtmcat.xyz]** · GTMCat, San Francisco, CA, USA.
