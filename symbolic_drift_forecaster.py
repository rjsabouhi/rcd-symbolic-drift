
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# ------------------------------
# Symbolic Drift Equations
# ------------------------------

def compute_coherence(theta, entropy_grad):
    return 1 / (1 + theta * entropy_grad)

def compute_drift(gamma, mu):
    return mu * (1 - gamma)

def compute_fate(drift):
    if drift < 0.2:
        return "recover"
    elif drift < 0.6:
        return "rebase"
    else:
        return "collapse"

# ------------------------------
# Simulate Drift Over Time
# ------------------------------

def simulate_drift(theta, mu, entropy_grad, steps=20):
    times = np.arange(steps)
    gammas = []
    deltas = []
    for t in times:
        # Slight increase in entropy over time
        local_entropy = entropy_grad + 0.05 * t
        gamma = compute_coherence(theta, local_entropy)
        delta = compute_drift(gamma, mu)
        gammas.append(gamma)
        deltas.append(delta)
    return times, gammas, deltas

# ------------------------------
# Streamlit App
# ------------------------------

st.set_page_config(page_title="Symbolic Drift Forecaster", layout="wide")
st.title("📉 Symbolic Drift Forecaster")
st.markdown("Simulate alignment drift in symbolic systems using clinging (Θ), memory tension (μ), and entropy gradient (∇S).")

col1, col2 = st.columns(2)
with col1:
    theta = st.slider("Θ — Clinging to initial structure", 0.0, 2.0, 1.0, 0.01)
    mu = st.slider("μ — Memory tension", 0.0, 5.0, 1.0, 0.01)
    entropy_grad = st.slider("∇S — Entropy gradient", 0.1, 10.0, 1.0, 0.1)

# Run simulation
t, gammas, deltas = simulate_drift(theta, mu, entropy_grad)
final_drift = deltas[-1]
fate = compute_fate(final_drift)

with col2:
    st.metric("Final Drift δ", f"{final_drift:.4f}")
    st.metric("System Fate ψ", fate.upper())
    if fate == "recover":
        st.success("System likely to recover original alignment.")
    elif fate == "rebase":
        st.warning("System likely to shift to a new attractor.")
    else:
        st.error("System likely to collapse from symbolic drift.")

# Plot
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(t, gammas, label="Coherence γ(t)")
ax.plot(t, deltas, label="Drift δ(t)", linestyle='--')
ax.set_xlabel("Time")
ax.set_ylabel("Value")
ax.set_title("Symbolic Drift Over Time")
ax.legend()
st.pyplot(fig)

# Footer
st.markdown("---")
st.caption("Symbolic Drift Forecaster uses Recursive Cognitive Dynamics to simulate symbolic misalignment risk. Drift is a function of memory tension and entropy acting on symbolic clinging.")
