"""
MCP Server implementation for Ocular Pattern-Reversal Visual Evoked Potential (PR-VEP) & P100 Latency Skill.
Exposes standard FastMCP-compatible tools for neuro-ophthalmological anterior visual pathway electrophysiology.
"""

import sys
import json
from typing import Dict, Any, Optional
from client import VisualEvokedPotentialClient


def evaluate_visual_evoked_potential(
    od_p100_latency_ms: float,
    od_amplitude_uv: float,
    os_p100_latency_ms: Optional[float] = None,
    os_amplitude_uv: Optional[float] = None,
    check_size_arcmin: Optional[float] = 60.0,
    patient_age_years: Optional[int] = 38
) -> str:
    """
    Evaluates Pattern-Reversal Visual Evoked Potential (PR-VEP) metrics.
    Returns structured analysis of optic nerve conduction delay, demyelination, and axonal loss.
    """
    client = VisualEvokedPotentialClient()
    result = client.evaluate_vep(
        od_p100_latency_ms=od_p100_latency_ms,
        od_amplitude_uv=od_amplitude_uv,
        os_p100_latency_ms=os_p100_latency_ms,
        os_amplitude_uv=os_amplitude_uv,
        check_size_arcmin=check_size_arcmin,
        patient_age_years=patient_age_years
    )
    return json.dumps(result, indent=2)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--tools":
        tools = [
            {
                "name": "evaluate_visual_evoked_potential",
                "description": "Quantifies ocular pattern-reversal visual evoked potential (PR-VEP) P100 latency, N75-P100 amplitude, and interocular asymmetry to detect optic demyelination and axonopathy.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "od_p100_latency_ms": {"type": "number", "description": "Right eye (OD) P100 peak latency in ms (normal: 95 - 115 ms)"},
                        "od_amplitude_uv": {"type": "number", "description": "Right eye (OD) N75-P100 peak-to-peak amplitude in uV (normal >= 5.0 uV)"},
                        "os_p100_latency_ms": {"type": "number", "description": "Optional left eye (OS) P100 peak latency in ms"},
                        "os_amplitude_uv": {"type": "number", "description": "Optional left eye (OS) N75-P100 amplitude in uV"},
                        "check_size_arcmin": {"type": "number", "description": "Stimulus check size in arcminutes (default: 60.0 arcmin)"},
                        "patient_age_years": {"type": "integer", "description": "Patient age in years (default: 38)"}
                    },
                    "required": ["od_p100_latency_ms", "od_amplitude_uv"]
                }
            }
        ]
        print(json.dumps(tools, indent=2))
    else:
        # Simple self-test
        client = VisualEvokedPotentialClient()
        test_res = client.evaluate_vep(
            od_p100_latency_ms=101.5,
            od_amplitude_uv=12.4,
            os_p100_latency_ms=103.0,
            os_amplitude_uv=11.8
        )
        print("Self-test passed:")
        print(json.dumps(test_res, indent=2))
