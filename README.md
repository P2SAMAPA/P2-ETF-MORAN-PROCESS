# Moran Process – Evolutionary Game Engine for ETFs

Applies the Moran process (population genetics) to model ETF competition. Each ETF is a type; fitness = average return. The population evolves via birth (proportional to fitness) and random death. The stationary distribution yields a survival probability – an evolutionary fitness measure used as a trend‑following signal.

## Features
- Three ETF universes (FI/Commodities, Equity Sectors, Combined)
- Seven rolling windows (63–4536 days)
- Fitness = mean return over the window (auto‑shifted to positive)
- Moran simulation: reproduce proportional to fitness, die uniformly
- Score = final population proportion (survival probability)
- Two‑tab Streamlit dashboard (auto best, manual)
- Results stored on Hugging Face: `P2SAMAPA/p2-etf-moran-process-results`

## Usage

1. Set `HF_TOKEN` environment variable.
2. Install dependencies: `pip install -r requirements.txt`
3. Run training: `python train.py` (fast, O(steps × n))
4. Launch dashboard: `streamlit run streamlit_app.py`

## Interpretation

- High survival probability indicates the ETF has a fitness advantage – expected to continue outperforming.
- Low probability suggests the ETF is being outcompeted – potential mean reversion or underperformance.
- This is a novel application of evolutionary game theory to finance.

## Requirements

See `requirements.txt`.
