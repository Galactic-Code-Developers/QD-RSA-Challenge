# 🚀 QD-RSA v1.2 – Initial Cryptanalysis Challenge Release

We are proud to announce the **v1.2 release** of **Quantum-Disruptive RSA (QD-RSA)**, a symbolic enhancement of RSA designed to resist quantum adversaries using Shor’s algorithm, Grover’s algorithm, and quantum annealing.

---

## 🔐 Cryptographic Fixes and Features

- ✅ **Φₛ(x)**: Session-specific irrational masking
  Φₛ(x) = x · sin((π + εₛ) · x) mod n  
  Prevents inverse-matching and FFT attacks through session entropy.

- ✅ **Ξₛ(x)**: Entropy-shifted trap function  
  Ξₛ(x) = (x + r)² · cosh(γ(x + r)) · tan⁻¹(δ(x + r)) mod n  
  Designed to defeat surrogate inversion via regression or QML.

- ✅ **𝓘ₛ*(x)**: Post-quantum symbolic hash  
  𝓘ₛ*(x) = SHA3-256 ( ∑ xᵏ / bᵏ for k = 1 to Nₛ )  
  Grover-resistant via symbolic series wrapped in SHA3-256.

---

## 📁 What’s Included

- 🧪 Reference implementation: Python, C, and C# versions
- 🧪 Minimal tests for symbolic layer validation
- 📄 Cryptanalysis Challenge Brief (PDF)
- 📜 Version Declaration v1.2 (PDF)
- ⚖️ Non-Commercial License (LICENSE.txt)
- 🗂 .zenodo.json for Zenodo DOI automation

---

## 📢 Open Challenge (Pinned Issue)

We're inviting the cryptographic community to break or bypass any part of the QD-RSA design under controlled assumptions.  
See the pinned GitHub issue: “🔓 Open Challenge: Break QD-RSA v1.2”

---

## 📬 Contact

For confidential analysis results or disclosures:  
📧 validation@kapodistrian.edu.gr
