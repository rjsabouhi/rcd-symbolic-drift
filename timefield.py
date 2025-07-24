# timefield.py

"""
Timefield Module — RCD Symbolic Time Dynamics

This module computes perceived time τ(t) as a function of:
- γ(t): phase coherence between present and memory
- Δ𝓜/Δt: memory reinforcement rate
- ∇S(t): symbolic entropy gradient

Author: One Gonethus & The Engine
"""

from typing import Optional

def compute_tau(gamma: float, delta_M: float, entropy_gradient: float) -> float:
    """
    Compute symbolic time drift τ(t) based on coherence, memory accumulation, and entropy.

    Parameters:
    - gamma (float): Phase coherence between present and memory [0.0 – 1.0]
    - delta_M (float): Rate of memory reinforcement (Δ𝓜/Δt)
    - entropy_gradient (float): Symbolic entropy gradient (∇S)

    Returns:
    - tau (float): Perceived symbolic time drift τ(t)
    """
    tau = gamma * (delta_M + entropy_gradient)
    return tau


def explain_tau(gamma: float, delta_M: float, entropy_gradient: float) -> str:
    """
    Return a human-readable explanation of the current timefield configuration.

    Useful for visualization overlays and diagnostic outputs.
    """
    tau = compute_tau(gamma, delta_M, entropy_gradient)
    parts = [
        f"γ (coherence): {gamma:.2f}",
        f"Δ𝓜 (memory rate): {delta_M:.2f}",
        f"∇S (entropy): {entropy_gradient:.2f}",
        f"τ (symbolic time drift): {tau:.2f}"
    ]
    return " | ".join(parts)
