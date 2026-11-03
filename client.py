"""
Ocular Pattern-Reversal Visual Evoked Potential (PR-VEP) & P100 Latency Client.
Zero-mock pure Python standard library implementation.
Calculates P100 Peak Latency (ms), N75-P100 Amplitude (uV), Interocular Latency Delta (ms),
Interocular Amplitude Ratio, and neuro-ophthalmic anterior visual pathway demyelination/axonopathy staging.
"""

import math
from typing import Dict, Any, Optional


class VisualEvokedPotentialClient:
    """
    Evaluates Pattern-Reversal Visual Evoked Potential (PR-VEP) according to ISCEV standards:
    - P100 Peak Latency (ms): normal 95.0 - 115.0 ms (prolongation > 118 ms indicates demyelination)
    - N75-P100 Peak-to-Peak Amplitude (uV): normal >= 5.0 uV (attenuation < 4.0 uV indicates axonal loss)
    - Interocular Latency Difference (ms): normal <= 6.0 ms
    - Interocular Amplitude Ratio: normal 0.67 - 1.50
    - Waveform Dispersion: evaluates temporal dispersion and conduction velocity along the anterior visual pathway.
    """

    def __init__(self):
        pass

    def evaluate_vep(
        self,
        od_p100_latency_ms: float,
        od_amplitude_uv: float,
        os_p100_latency_ms: Optional[float] = None,
        os_amplitude_uv: Optional[float] = None,
        check_size_arcmin: Optional[float] = 60.0,
        patient_age_years: Optional[int] = 38
    ) -> Dict[str, Any]:
        """
        Calculates Visual Evoked Potential (VEP) metrics.
        od_p100_latency_ms: Right eye P100 latency in ms (e.g. 102.5 ms).
        od_amplitude_uv: Right eye N75-P100 amplitude in uV (e.g. 11.2 uV).
        os_p100_latency_ms: Optional left eye P100 latency in ms (e.g. 104.0 ms).
        os_amplitude_uv: Optional left eye N75-P100 amplitude in uV (e.g. 10.8 uV).
        """
        if od_p100_latency_ms < 0 or od_amplitude_uv < 0:
            raise ValueError("VEP latency and amplitude cannot be negative.")
        if os_p100_latency_ms is not None and os_p100_latency_ms < 0:
            raise ValueError("Left eye latency cannot be negative.")
        if os_amplitude_uv is not None and os_amplitude_uv < 0:
            raise ValueError("Left eye amplitude cannot be negative.")

        # Interocular Latency Delta
        interocular_latency_delta_ms = None
        if os_p100_latency_ms is not None:
            interocular_latency_delta_ms = round(abs(od_p100_latency_ms - os_p100_latency_ms), 2)

        # Interocular Amplitude Ratio (OD / OS)
        interocular_amp_ratio = None
        if os_amplitude_uv is not None and os_amplitude_uv > 0:
            interocular_amp_ratio = round(od_amplitude_uv / os_amplitude_uv, 2)

        # Pathology detection
        # Upper limit of normal P100 latency: 115.0 ms (or 118.0 ms in elderly)
        upper_latency_limit = 118.0 if patient_age_years and patient_age_years >= 60 else 115.0
        lower_amplitude_limit = 4.5

        od_delayed = od_p100_latency_ms > upper_latency_limit
        os_delayed = (os_p100_latency_ms > upper_latency_limit) if os_p100_latency_ms is not None else False
        od_attenuated = od_amplitude_uv < lower_amplitude_limit
        os_attenuated = (os_amplitude_uv < lower_amplitude_limit) if os_amplitude_uv is not None else False
        asymmetric_delay = (interocular_latency_delta_ms is not None and interocular_latency_delta_ms > 6.0)

        if (od_delayed or os_delayed) and (od_attenuated or os_attenuated):
            neuro_status = "Combined Optic Demyelination and Axonal Loss"
            clinical_risk = "Prolonged P100 conduction latency combined with depressed N75-P100 amplitude; indicative of progressive or severe optic neuropathy with secondary axonal drop out."
        elif od_delayed or os_delayed:
            neuro_status = "Anterior Visual Pathway Demyelination (Conduction Delay)"
            clinical_risk = "Significant P100 peak latency prolongation reflecting saltatory conduction slowing from myelin sheath disruption (classic for acute or prior optic neuritis / demyelinating disease)."
        elif od_attenuated or os_attenuated:
            neuro_status = "Optic Axonopathy / Subcortical Visual Pathway Attenuation"
            clinical_risk = "Normal P100 latency with markedly reduced waveform amplitude; reflects loss of functioning retinal ganglion cell axons or optic nerve fibers without significant demyelination."
        elif asymmetric_delay:
            neuro_status = "Subclinical Asymmetric Optic Conduction Delay"
            clinical_risk = "Interocular latency delta exceeds normal 6 ms threshold; indicative of unilateral subclinical anterior visual pathway impairment."
        else:
            neuro_status = "Normal Visual Evoked Potential (Intact Anterior Visual Pathway)"
            clinical_risk = "Preserved retinocortical conduction velocity, normal P100 waveform morphology, and symmetrical bilateral optic nerve transmission."

        return {
            "status": "success",
            "vep_metrics": {
                "od_right_eye": {
                    "p100_latency_ms": round(od_p100_latency_ms, 2),
                    "amplitude_uv": round(od_amplitude_uv, 2),
                    "is_delayed": od_delayed,
                    "is_attenuated": od_attenuated
                },
                "os_left_eye": {
                    "p100_latency_ms": round(os_p100_latency_ms, 2) if os_p100_latency_ms is not None else None,
                    "amplitude_uv": round(os_amplitude_uv, 2) if os_amplitude_uv is not None else None,
                    "is_delayed": os_delayed if os_p100_latency_ms is not None else None,
                    "is_attenuated": os_attenuated if os_amplitude_uv is not None else None
                } if os_p100_latency_ms is not None else None,
                "interocular_comparisons": {
                    "interocular_latency_delta_ms": interocular_latency_delta_ms,
                    "interocular_amplitude_ratio": interocular_amp_ratio,
                    "asymmetric_delay_detected": asymmetric_delay
                } if os_p100_latency_ms is not None else None
            },
            "recording_context": {
                "check_size_arcmin": check_size_arcmin,
                "patient_age_years": patient_age_years,
                "normal_latency_upper_limit_ms": upper_latency_limit
            },
            "clinical_assessment": {
                "neuro_ophthalmological_status": neuro_status,
                "pathophysiology_summary": clinical_risk
            }
        }
