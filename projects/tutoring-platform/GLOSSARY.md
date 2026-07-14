# Tutoring Platform Glossary

- **Tutor** — the single business owner operating the tutoring platform.
- **Prospect** — a visitor evaluating the tutor who has not yet established an ongoing
  student relationship.
- **Invitee** — a known prospect with a tutor-created personal invitation who has not
  yet claimed it or created a student account.
- **Student** — a person with a tutoring relationship who can manage sessions and
  access lesson material shared with them.
- **Invitation** — a revocable, expirable pre-account record reached through an opaque
  personal link. It can carry client-facing setup context and one-time discount
  eligibility, then be claimed by an authenticated student account.
- **Private Tutor Note** — invitation or lesson context visible only to the tutor and
  excluded from all invitee and student responses.
- **Shared Personal Message** — tutor-authored context intentionally shown to an
  invitee on their personalized setup page.
- **Invitation Claim** — the one-time association of an active invitation with a
  verified student account. Claiming does not itself consume a discount.
- **Discount Redemption** — consumption of invitation-bound discount eligibility by
  the first successful payment, not by a checkout attempt.
- **Student Session** — a revocable server-side authentication record referenced by an
  opaque, HTTPS-only `Secure` and `HttpOnly` host cookie. It has both inactivity and
  absolute expiration limits.
- **Booking** — the platform-owned record of a tutoring session, including its student,
  service, scheduled time, payment relationship, and lifecycle state.
- **Calendar Projection** — the external calendar event mirroring a platform booking.
  It is an availability and convenience integration, not the booking source of truth.
- **Sync Drift** — a detected mismatch between a platform booking and its calendar
  projection that must be surfaced and reconciled rather than silently accepted.
