---
name: genpark-personal-agent-ocular-visual-evoked-potential-vep-p100-skill
description: Evaluates anterior visual pathway functional integrity using pattern-reversal visual evoked potential (PR-VEP) P100 peak latency, N75-P100 amplitude, and interocular asymmetry.
---

# Ocular Pattern-Reversal Visual Evoked Potential (PR-VEP) & P100 Latency Skill

This skill computes neuro-ophthalmological electrophysiological metrics from pattern-reversal visual evoked potentials to quantify visual pathway conduction delay, demyelination, and optic axonopathy according to ISCEV standards.

## Core Capabilities
- Evaluates P100 peak latency (normal: 95 - 115 ms; prolongation > 118 ms).
- Evaluates N75-P100 peak-to-peak amplitude (normal: >= 5.0 uV; attenuation < 4.5 uV).
- Calculates interocular latency delta ($\Delta L \le 6.0\text{ ms}$) and interocular amplitude ratio.
- Distinguishes saltatory conduction slowing (demyelinating optic neuritis) from primary axonal dropout (ischemic or compressive optic neuropathy).

## Zero-Mock Architecture
Standard Python standard library only with zero external dependencies.
