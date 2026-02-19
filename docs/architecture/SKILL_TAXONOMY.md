# MW-Omega Skill Taxonomy

Document Control: MW-DOC-ARCH-002-v1.0

## Skill Categories

Every MW-Omega skill belongs to exactly one category. Skills within a category share dependencies and integration patterns.

### Core (skills/core/)

Skills that govern all other skills. Always active.

| Skill | Version | Status |
|-------|---------|--------|
| decision-compressor | v1.0 | ACTIVE |
| execution-cadence-controller | v1.0 | ACTIVE |
| content-humanizer | v1.0 | ACTIVE |

### Creative (skills/creative/)

Skills that produce shippable creative artifacts.

| Skill | Version | Status |
|-------|---------|--------|
| flame-spiral-executor | v1.0 | ACTIVE |
| kdp-shipping-engine | v1.0 | ACTIVE |
| kdp-cover-engine | v1.0 | ACTIVE |
| music-production-engine | v1.0 | ACTIVE |
| audiobook-production-engine | v1.0 | ACTIVE |
| film-video-production-engine | v1.0 | DEFERRED (Phase 3-4) |

### Institutional (skills/institutional/)

Skills that upgrade artifacts into institutional-grade infrastructure.

| Skill | Version | Status |
|-------|---------|--------|
| institutional-perfection-engine | v2.1 | ACTIVE |
| stack-deployment-engine | v1.1 | ACTIVE |
| institutional-translator | v1.0 | ACTIVE |
| facilitator-training-system | v1.0 | ACTIVE |

### Financial (skills/financial/)

Skills that model and manage revenue architecture.

| Skill | Version | Status |
|-------|---------|--------|
| capital-architecture-modeler | v1.0 | ACTIVE |
| private-equity-engine | v1.0 | DEFERRED (Phase 3-4) |

### Operational (skills/operational/)

Skills that manage execution capacity and team building.

| Skill | Version | Status |
|-------|---------|--------|
| skill-acquisition-accelerator | v1.0 | ACTIVE |
| delegation-team-builder | v1.0 | ACTIVE |
| entity-legal-operations | v1.0 | ACTIVE |

### Language (skills/language/)

The Language OS subsystem -- a standalone operating system within MW-Omega.

| Skill | Version | Status |
|-------|---------|--------|
| language-os-controller | v4.2 | ACTIVE |
| language-os-session-engine | v4.2 | ACTIVE |
| language-os-gate-assessor | v4.2 | ACTIVE |

### Growth (skills/growth/)

Skills that build audience, distribution, and market presence.

| Skill | Version | Status |
|-------|---------|--------|
| substack-content-architect | v1.0 | ACTIVE |
| audience-growth-engine | v1.0 | ACTIVE |
| consulting-speaking-engine | v1.0 | ACTIVE |
| ip-asset-tracker | v1.0 | ACTIVE |
| visual-art-merchandise-engine | v1.0 | DEFERRED (Phase 2-3) |
| course-production-system | v1.0 | DEFERRED (Phase 2-3) |
| counterfactual-simulator | v1.0 | ACTIVE |

## Integration Map

```
decision-compressor
  --> execution-cadence-controller (what to ship today)
  --> flame-spiral-executor (how to structure creative output)
      --> kdp-shipping-engine (publish books)
      --> music-production-engine (release music)
      --> substack-content-architect (publish essays)
          --> audience-growth-engine (grow distribution)
      --> ip-asset-tracker (register all outputs)
          --> capital-architecture-modeler (model revenue)
          --> entity-legal-operations (protect legally)
              --> stack-deployment-engine (deploy institutionally)
                  --> facilitator-training-system (scale beyond founder)
```
