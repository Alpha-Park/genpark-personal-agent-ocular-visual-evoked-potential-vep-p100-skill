"""
Example usage for Ocular Pattern-Reversal Visual Evoked Potential (PR-VEP) & P100 Latency Skill.
"""

from client import VisualEvokedPotentialClient


def main():
    client = VisualEvokedPotentialClient()

    print("--- Case 1: Normal Bilateral Visual Evoked Potential ---")
    normal_case = client.evaluate_vep(
        od_p100_latency_ms=101.5,
        od_amplitude_uv=12.4,
        os_p100_latency_ms=103.0,
        os_amplitude_uv=11.8,
        check_size_arcmin=60.0,
        patient_age_years=32
    )
    print("OD Latency:", normal_case["vep_metrics"]["od_right_eye"]["p100_latency_ms"], "ms")
    print("OS Latency:", normal_case["vep_metrics"]["os_left_eye"]["p100_latency_ms"], "ms")
    print("Interocular Latency Delta:", normal_case["vep_metrics"]["interocular_comparisons"]["interocular_latency_delta_ms"], "ms")
    print("Neuro Status:", normal_case["clinical_assessment"]["neuro_ophthalmological_status"])
    print("Pathophysiology:", normal_case["clinical_assessment"]["pathophysiology_summary"])
    print()

    print("--- Case 2: Unilateral Optic Neuritis (Demyelinating Conduction Delay) ---")
    neuritis_case = client.evaluate_vep(
        od_p100_latency_ms=138.5,
        od_amplitude_uv=8.5,
        os_p100_latency_ms=102.0,
        os_amplitude_uv=11.2,
        patient_age_years=29
    )
    print("OD Latency:", neuritis_case["vep_metrics"]["od_right_eye"]["p100_latency_ms"], "ms")
    print("OS Latency:", neuritis_case["vep_metrics"]["os_left_eye"]["p100_latency_ms"], "ms")
    print("Interocular Latency Delta:", neuritis_case["vep_metrics"]["interocular_comparisons"]["interocular_latency_delta_ms"], "ms")
    print("Neuro Status:", neuritis_case["clinical_assessment"]["neuro_ophthalmological_status"])
    print("Pathophysiology:", neuritis_case["clinical_assessment"]["pathophysiology_summary"])
    print()

    print("--- Case 3: Ischemic Optic Neuropathy (Axonal Loss) ---")
    axonopathy_case = client.evaluate_vep(
        od_p100_latency_ms=106.0,
        od_amplitude_uv=2.8,
        os_p100_latency_ms=104.0,
        os_amplitude_uv=10.5,
        patient_age_years=68
    )
    print("OD Amplitude:", axonopathy_case["vep_metrics"]["od_right_eye"]["amplitude_uv"], "uV")
    print("OS Amplitude:", axonopathy_case["vep_metrics"]["os_left_eye"]["amplitude_uv"], "uV")
    print("Neuro Status:", axonopathy_case["clinical_assessment"]["neuro_ophthalmological_status"])
    print("Pathophysiology:", axonopathy_case["clinical_assessment"]["pathophysiology_summary"])


if __name__ == "__main__":
    main()
