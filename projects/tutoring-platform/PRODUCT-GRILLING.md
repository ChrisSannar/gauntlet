# Product Grilling: Single-Tutor Platform (2026-07-13 through 2026-07-17)

*Product scope for a one-week build used to test the Gauntlet's adaptive
accountability loop.*

## Status

Paused on 2026-07-12. Continue these product questions during the trial week; do not
mix them into the accountability-system design session.

## Product intent

Give one independent tutor a coherent operating system for acquiring students and
running lessons. A prospective student should be able to understand the offer and
book a service and available time, pay, and receive an immediately confirmed session.
An active student should be able to manage sessions and use the lesson material the
tutor shares with them.

The reward for efficient work is more functioning product. The task backlog may remain
open-ended, while each day retains a finite required boundary (ADR 0016).

The pilot has a 40-hour envelope. Intended capabilities below are backlog candidates;
the adaptive planner must prefer thin end-to-end value over incomplete breadth.

## Actors

- **Tutor**: the single business owner. Controls services, availability, sessions,
  lesson records, resources, and payment configuration.
- **Prospect**: a person evaluating the tutor who has not established an ongoing
  student relationship.
- **Invitee**: a known prospect for whom the tutor created a personalized invitation,
  but who has not yet claimed it or created an account.
- **Student**: a person with a tutoring relationship who can manage their sessions and
  access material shared with them.
- **Calendar provider**: external source and destination for availability and session
  events.
- **Payment provider**: external system that authorizes and records payment.
- **Accountability system**: assigns daily work and grades frozen evidence; it is not a
  tutoring-platform user.

## Intended capabilities

- Public landing page for prospective students.
- Tutor admin flow for creating a personalized invitation for a known prospect.
- Opaque personal invitation link with a pre-account setup page and an optional
  invitation-bound, one-time discount.
- Invitation claim through signup/authentication, producing the student's account and
  preserving the intended booking context.
- Session scheduling with calendar synchronization.
- Rescheduling and cancellation.
- Lesson notes shared with the appropriate student.
- File and resource sharing.
- Lesson reminders.
- Payment collection and payment-state visibility.

## Day 1 deployment constraint

Day 1 establishes the project and deploys a reachable product skeleton to Chris's
DigitalOcean server under his website. Chris will supply the final URL after setup.
Later daily work must preserve a deployable main path so midnight grading can run E2E
tests and a live product check against the hosted application.

The Day 1 product may be thin, but it must be a real deployed application rather than
only infrastructure notes or a local mockup.

## Explicit pilot non-goals

- Multiple tutor organizations or tenant isolation.
- Tutor marketplace, tutor discovery, or matching.
- Platform commissions, connected-account payouts, or tutor revenue splitting.
- Architecture whose only justification is a hypothetical later SaaS conversion.

## Open product decisions

- Does an invitation expire, and may the tutor revoke or regenerate it?
- Can the invitee change the prefilled name before creating their account?
- Which lesson notes are private to the tutor versus shared with the student?
- Which critical journey must work end to end for the pilot to count as useful?

## Settled booking journey

A public prospect chooses a service and an available time, pays, and receives an
immediately confirmed session. Calendar synchronization and reminder scheduling follow
the confirmed booking.

## Invitation lifecycle

The tutor may create a personalized invitation before an account exists. The system
issues an opaque link whose token refers to server-side invitation data; personally
identifying information and discount authority do not live in URL parameters. The
invitation stores **private tutor notes** separately from a **shared personal message**.
Private notes are never returned by invitee or student endpoints; the shared message is
deliberately rendered on the setup page. This is an authorization boundary, not merely
a presentation choice. The invitation has an explicit lifecycle:

`draft -> active -> claimed`

An active invitation may also become `revoked` or `expired`. Claiming it requires
verified signup/authentication, permanently associates the invitation with that one
student account, and records the claim independently of payment.

Any invitation-bound discount remains available through failed or abandoned checkout
attempts. It is redeemed only by the first successful payment and records that payment
as evidence. A claimed invitation cannot be claimed by another account.

## Student authentication and sessions

Students verify their identity through an emailed magic link or one-time code. A
successful verification creates an opaque server-side session; subsequent visits do
not require another email while that session remains valid. Google sign-in is stretch
work. Apple and GitHub sign-in are outside the pilot's required boundary.

Production serves authentication only over HTTPS. HTTP redirects to HTTPS, and the
session identifier uses a host-only cookie with a `__Host-` name, `Secure`, `HttpOnly`,
`SameSite=Lax`, and `Path=/`; it has no `Domain` attribute. The application rotates the
session after authentication and supports logout and server-side revocation.

The session expires after 30 days without activity and has a 90-day absolute lifetime.
Normal authenticated use may extend the inactivity deadline but never the absolute
deadline.

## Booking and calendar authority

The tutoring platform is authoritative for a session's service, student, time, payment
relationship, and lifecycle state. Booking, rescheduling, and cancellation commands go
through the platform and then synchronize to the configured calendar provider.

The calendar provider contributes busy-time constraints when the platform computes
availability and stores a mirrored event for each confirmed session. Direct changes to
that mirrored event do not silently change the platform booking. The synchronization
process detects the mismatch, records it as drift, and surfaces repair work to the
tutor and maintenance backlog.

Calendar writes must be retryable and idempotent. Each booking retains the external
event identifier and synchronization status needed to reconcile failures without
creating duplicate events.

## Cancellation and rescheduling policy

- At least 24 hours before a session, a student may cancel for a full refund or use one
  self-service reschedule.
- Inside 24 hours, the platform does not automatically refund or reschedule; the
  student must contact the tutor.
- The tutor may override the policy from the admin interface.
- Rescheduling retains the original successful payment instead of refunding and
  charging again.
