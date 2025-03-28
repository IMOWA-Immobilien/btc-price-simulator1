import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Titel
st.title("🧮 Bitcoin-Preis-Simulator (in EUR)")
st.markdown("Passe die Marktkapitalisierung (in Billionen USD) und das BTC-Angebot an, um den theoretischen Preis pro Bitcoin in Euro zu berechnen.")

# EUR/USD-Wechselkurs
usd_to_eur = st.number_input("Aktueller USD → EUR Wechselkurs:", value=0.92, step=0.01)

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

st.markdown("---")

def plot_btc_price(market_caps, btc_supply, usd_to_eur):
    prices_usd = [(cap * 1e12) / btc_supply for cap in market_caps]
    prices_eur = [price * usd_to_eur for price in prices_usd]
    scenarios = [f"{cap} Billionen USD" for cap in market_caps]

    # Zwei Spalten: Links Textausgabe, rechts Diagramm
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("### 💶 Preisübersicht in Euro")
        for cap, eur in zip(market_caps, prices_eur):
            st.write(f"Bei {cap} Billionen USD: **{eur:,.0f} €** pro BTC".replace(",", "."))

    with col2:
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.bar(scenarios, prices_eur)
        ax.set_title("Bitcoin-Preis bei verschiedenen Marktkapitalisierungen")
        ax.set_ylabel("Preis pro Bitcoin (in EUR)")
        ax.set_yscale('log')
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        st.pyplot(fig)

if market_caps:
    plot_btc_price(market_caps, btc_supply, usd_to_eur)
else:
    st.info("Bitte wähle mindestens eine Marktkapitalisierung aus.")
