# Focused Schema Migration Check

After loading `coaching_state.md`, compare it with `references/coaching-state-schema.md` and migrate silently.

- Add missing Storybank `Secondary Skill`, `Earned Secret`, `Strength`, `Use Count`, and `Last Used` columns. Initialize unknown values conservatively.
- Add missing full Story Details; never infer unsupported metrics or outcomes from an index row.
- Add missing Interview Intelligence, Active Coaching Strategy, Calibration State, Lead/Staff Upleveling Readiness, Meta-Check Log, Session Log, and Coaching Notes sections.
- Initialize Calibration Status to `uncalibrated`, Last calibration check to `never`, and Data points available from known real outcomes.
- Add missing Profile fields with conservative defaults. Set unknown anxiety to `unknown`; populate target context from `data/candidate_profile.json` and `data/target_anduril_air_defense.json` only when the state does not contain a newer user correction.
- Rename legacy Score History `Signal` to `Hire Signal` without changing row values.
- Add missing Interview Loop fields: Status, Round formats, Fit verdict, Fit confidence, Fit signals, Structural gaps, and Date researched.
- Preserve legacy sections from old states as archived data, but do not recreate LinkedIn Analysis, Resume Optimization, Positioning Statement, or Outreach Strategy sections in new focused states.
- Never overwrite a candidate correction or convert a hypothesis into a verified fact during migration.

Do not announce migration unless it changes the immediate recommendation or reveals missing evidence that affects an interview claim.
