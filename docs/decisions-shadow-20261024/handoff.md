# SkillOpt Decisions companion — DL-20261024

Base main1a44050fc53aa4938a7a3927b6cca550491bfe51; isolated branchfeature/decisions-shadow-companion-20261024. Code: skillopt_sleep/decision_shadow.py. Two local companion tests pass; ACC's cross-repository contract test exercises this module with its actual shared DecisionsAdapter. No existing backend, judge, optimizer, state, collector, intake, learning or adoption code changed.

This is an explicit optional consumer, not an activated optimizer integration. Caller passes a scoped typed Context(category='skillopt'), minimized facts, existing outcome and the shared ACC adapter. Existing outcome always wins. The shared implementation and full map/tests/security/rollback are in The-ACC-AgentCommandCenter branchfeature/decisions-live-shadow-20261024, docs/DECISIONS-LIVE-INTEGRATION.md. No SDK dependency or second implementation is added here.

Run `env -u TYPESAFE_API_KEY -u OPENAI_API_KEY python -m unittest discover -s tests -p 'test_decision_shadow.py'` from this repository. The ACC contract additionally sets SKILLOPT_CHECKOUT to this absolute checkout. These are mocked/offline tests; no API model quality/cost or device claim.

Open: DL-01 confirmed API account/secure credential; DL-02 explicit test-spending limit and actual measurements; DL-03 supported owning-runtime Chase invocation; DL-04 native Sentry voice/source mapping; DL-05 existing summary-write denials. All pre-existing IDs/gates/history remain in their original records. No merge/deploy/schedule activation authorized.

Next agent: read live sources, use shared adapter through explicit injection only after the relevant authorization; do not wire this into intake/optimizer/adoption under the current prompt. Optional reviewer: test existing-outcome preservation and cross-repo adapter reuse. Rollback: remove these added files/abandon feature branch; no state migration/restoration required.
