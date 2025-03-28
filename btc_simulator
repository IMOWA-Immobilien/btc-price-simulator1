import streamlit as st
import matplotlib.pyplot as plt

# Titel
st.title("🧮 Bitcoin-Preis-Simulator")
st.markdown("Passe die Marktkapitalisierung und das BTC-Angebot an, um den theoretischen BTC-Preis zu sehen.")

# Eingabefelder
market_caps = st.multiselect(
    label="Wähle die Marktkapitalisierung aus (in Billionen US-Dollar):",
    options=[1, 5, 10, 21, 50, 100, 200],
    default=[1, 10, 21, 100]
)

btc_supply = st.slider(
    label="Bitcoin im Umlauf (Anzahl):",
    min_value=15_000_000,
    max_value=21_000_000,
    value=21_000_000,
    step=100_000
)

# Berechnung & Anzeige
def plot_btc_price(market_caps, btc_supply):
    prices = [(cap * 1e12) / btc_supply for cap in market_caps]
    scenarios = [f"{cap} Billionen $" for cap in market_caps]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(scenarios, prices)
    ax.set_title("Bitcoin-Preis bei verschiedenen Marktkapitalisierungen")
    ax.set_ylabel("Preis pro Bitcoin (in USD)")
    ax.set_yscale('log')
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(fig)

if market_caps:
    plot_btc_price(market_caps, btc_supply)
else:
    st.info("Bitte wähle mindestens eine Marktkapitalisierung aus.")
