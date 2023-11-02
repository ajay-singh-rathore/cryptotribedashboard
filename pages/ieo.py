import streamlit as st
import plotly.express as px
import requests
import pandas as pd
import base64 
from dotenv import load_dotenv
import os

load_dotenv()

base_url = 'https://api.cryptorank.io/v1'
api_key = os.getenv("CRYPTORANK_API_KEY")


def fetch_current_prices():
    endpoint = '/currencies'
    params = {'api_key': api_key, 'limit': 6000}
    response = requests.get(base_url + endpoint, params=params)
    data = response.json()
    currencies = []
    for currency in data.get('data', []):
        name = currency.get('name', '')
        symbol = currency.get('symbol', '')
        price_usd = currency.get('values', {}).get('USD', {}).get('price', 0)
        currencies.append({"name": name, "Symbol": symbol, "Price (USD)": price_usd})
    return currencies

exchange_data = {
    "Okx": [
        {"name": "SUI", "listing_price": "$0.100", "current_price": None},
        {"name": "TAKI", "listing_price": "$0.04", "current_price": None},
        {"name": "ELT", "listing_price": "$0.009", "current_price": None},
        {"name": "ORB", "listing_price": "$0.035", "current_price": None},
        {"name": "GARI", "listing_price": "$0.200", "current_price": None},
        {"name": "WGRT", "listing_price": "$0.003", "current_price": None},
        {"name": "NDN", "listing_price": "$0.006", "current_price": None},
        {"name": "DEP", "listing_price": "$0.0025", "current_price": None},
        {"name": "IMVU", "listing_price": "$0.00286", "current_price": None}
    ],

    "KuCoin": [
        {"name": "IMVU", "listing_price": "$0.00286", "current_price": None},
        {"name": "Sui", "listing_price": "$0.394", "current_price": None},
        {"name": "Mechaverse", "listing_price": "$0.00342", "current_price": None},
        {"name": "Fracton Protocol", "listing_price": "$1.77", "current_price": None},
        {"name": "Pikaster", "listing_price": "$0.028", "current_price": None},
        {"name": "Aurigami", "listing_price": "$0.0000851", "current_price": None},
         {"name": "Melos Studio", "listing_price": "$0.00207", "current_price": None},
        {"name": "Gari Network", "listing_price": "$0.0216", "current_price": None},
        {"name": "ClearDAO", "listing_price": "$0.00187", "current_price": None},
        {"name": "Chumbi Valley", "listing_price": "$0.000134", "current_price": None},
        {"name": "Victoria VR", "listing_price": "$0.006", "current_price": None},
        {"name": "Cryowar", "listing_price": "$0.0067", "current_price": None},
        {"name": "IX Swap", "listing_price": "$0.0111", "current_price": None},
        {"name": "Lithium Finance", "listing_price": "$0.000247", "current_price": None},
         {"name": "Burp", "listing_price": "$0.00034", "current_price": None}
    ],
    "HTX Primelist": [
    {"name": "HistoryDAO / HAO", "listing_price": "$0.01", "current_price": None},
    {"name": "Metababy / BABY", "listing_price": "$0.03", "current_price": None},
    {"name": "Hero Blaze: Three Kingdoms / MUDOL2", "listing_price": "$0.120", "current_price": None},
    {"name": "StonkLeague / AEGIS", "listing_price": "$0.03", "current_price": None},
    {"name": "Koi Network / KOI", "listing_price": "$0.025", "current_price": None},
    {"name": "Fellaz / FLZ", "listing_price": "$0.100", "current_price": None},
    {"name": "Walken / WLKN", "listing_price": "$0.0165", "current_price": None},
    {"name": "SIGNIN / SIGN", "listing_price": "$0.02", "current_price": None},
    {"name": "Cube Network / CUBE", "listing_price": "$0.300", "current_price": None},
    {"name": "WeBuy / WE", "listing_price": "$0.500", "current_price": None},
    {"name": "Konnect / KCT", "listing_price": "$0.01", "current_price": None},
    {"name": "Plato Farm / PLATO", "listing_price": "$0.01", "current_price": None},
    {"name": "EdgeSwap / EGS", "listing_price": "$0.02", "current_price": None},
    {"name": "H2O DAO / H2O", "listing_price": "$0.01", "current_price": None},
    {"name": "Launchblock / LBP", "listing_price": "$0.02", "current_price": None},
    {"name": "Ark Rivals / ARKN", "listing_price": "$0.05", "current_price": None},
    {"name": "PhotoChromic / PHCR", "listing_price": "$0.00", "current_price": None},
    {"name": "KingdomX / KKT", "listing_price": "$0.01", "current_price": None},
    {"name": "Synesis One / SNS", "listing_price": "$0.05", "current_price": None},
    {"name": "Spellfire / SPELLFIRE", "listing_price": "$0.03", "current_price": None},
    {"name": "Atlas DEX / ATS", "listing_price": "$0.14", "current_price": None},
    {"name": "Lootex / LOOT", "listing_price": "$0.80", "current_price": None},
    {"name": "Gari Network / GARI", "listing_price": "$0.20", "current_price": None},
    {"name": "Deesse / LOVE", "listing_price": "$0.00", "current_price": None},
    {"name": "Ertha / ERTHA", "listing_price": "$0.02", "current_price": None},
    {"name": "Decimated / DIO", "listing_price": "$0.05", "current_price": None},
    {"name": "GamesPad / GMPD", "listing_price": "$0.06", "current_price": None},
    {"name": "Unbound Finance / UNB", "listing_price": "$0.01", "current_price": None},
    {"name": "Biconomy / BICO", "listing_price": "$0.30", "current_price": None},
    {"name": "MonoX Protocol / MONO", "listing_price": "$0.40", "current_price": None},
    {"name": "Gold Fever / NGL", "listing_price": "$0.15", "current_price": None},
    {"name": "ImmutableX / IMX", "listing_price": "$0.16", "current_price": None},
    {"name": "EPIK Prime / EPIK", "listing_price": "$0.01", "current_price": None},
    {"name": "Whole Network / NODE", "listing_price": "$0.00", "current_price": None}
],

   "Coinstore": [
    {"name": "Innovator Metaverse (INVT)", "listing_price": "$0.01", "current_price": None},
    {"name": "KISSAN (KSN)", "listing_price": "$0.08", "current_price": None},
    {"name": "Sportzchain (SPN)", "listing_price": "$0.0024", "current_price": None},
    {"name": "Cointrading (CNT)", "listing_price": "$0.015", "current_price": None},
    {"name": "KeeDX (KDX)", "listing_price": "$0.25", "current_price": None},
    {"name": "Meta Warriors (MWS)", "listing_price": "$0.095", "current_price": None},
    {"name": "Social Innovation (SOIT)", "listing_price": "$0.008", "current_price": None},
    {"name": "PomeBox ($POMB)", "listing_price": "$0.016", "current_price": None},
    {"name": "NIKEL ($NIKL)", "listing_price": "$0.0801", "current_price": None},
    {"name": "Hippo Wallet Token (HPO)", "listing_price": "$0.003", "current_price": None},
    {"name": "NORDEK ($NRK)", "listing_price": "$0.025", "current_price": None},
    {"name": "Damex.io (DAMEX)", "listing_price": "$0.15", "current_price": None},
    {"name": "Magic Shiba Starter ($MSHIB)", "listing_price": "$0.00001881", "current_price": None},
    {"name": "Royal Society NFT ($ROYSY)", "listing_price": "$0.0001", "current_price": None},
    {"name": "Bearium", "listing_price": "$0.0067", "current_price": None},
    {"name": "BAJ Token", "listing_price": "$0.0010", "current_price": None},
    {"name": "ixo", "listing_price": "$0.02", "current_price": None}
],
  "Bitmart": [
    {"name": "Crypto Tex", "listing_price": "$0.212", "current_price": None},
    {"name": "O-MEE", "listing_price": "$0.000084", "current_price": None},
    {"name": "Hibiki Run", "listing_price": "$0.0038", "current_price": None},
    {"name": "Evadore", "listing_price": "$0.0988", "current_price": None},
    {"name": "RADA", "listing_price": "$0.00269", "current_price": None},
    {"name": "Family Over Everything", "listing_price": "$0.0107", "current_price": None},
    {"name": "CyberConnect", "listing_price": "$4.23", "current_price": "$4.23"},
    {"name": "Damex", "listing_price": "$0.0114", "current_price": "$0.0114"},
    {"name": "Quantum Hunter", "listing_price": "$0.0000102", "current_price": "$0.0000102"},
    {"name": "Crypto Tex", "listing_price": "$0.800", "current_price": None},
    {"name": "O-MEE", "listing_price": "$0.007", "current_price": None},
    {"name": "Hibiki Run", "listing_price": "$0.04", "current_price": None},
    {"name": "Evadore", "listing_price": "$0.00225", "current_price": None},
    {"name": "RADA", "listing_price": "$1.80", "current_price": None},
    {"name": "Family Over Everything", "listing_price": "$0.0075", "current_price": None}
],
    "Probit" :[
  
    {"name": "Obortech", "listing_price": "$0.038", "current_price": None},
    {"name": "Bitcoin BAM", "listing_price": "$3.00", "current_price": None},
    {"name": "Olyseum", "listing_price": "$0.600", "current_price": None},
    {"name": "MMAON", "listing_price": "$0.110", "current_price": None},
    {"name": "NagaSwap Token", "listing_price": "$0.06", "current_price": None},
    {"name": "Carnomaly", "listing_price": "$0.650", "current_price": None},
    {"name": "Skey Network", "listing_price": "$0.035", "current_price": None},
    {"name": "Dymmax", "listing_price": "$1.25", "current_price": None},
    {"name": "Berry", "listing_price": "$0.0042", "current_price": None},
    {"name": "idap.io", "listing_price": "$0.031", "current_price": None},
    {"name": "Sportx", "listing_price": "$0.01", "current_price": None},
    {"name": "Smathium", "listing_price": "$0.006", "current_price": None},
    {"name": "Nuvo Cash", "listing_price": "$0.0025", "current_price": None},
    {"name": "ProBit Token", "listing_price": "$0.200", "current_price": None},
    {"name": "TealToken", "listing_price": "$1.25", "current_price": None},

 ],

 "Bitget":[
     {"name": "1", "listing_price": "$0.05", "current_price": None},
    {"name": "2", "listing_price": "$0.083", "current_price": None},
    {"name": "3", "listing_price": "$0.100", "current_price": None},
    {"name": "Typelt", "listing_price": "$0.017", "current_price": None},
    {"name": "Bitcoin Improvement Proposals", "listing_price": "$0.100", "current_price": None},
    {"name": "Gosleep", "listing_price": "$0.083", "current_price": None},
    {"name": "HALO", "listing_price": "$0.017", "current_price": None},
    {"name": "PandaFarm", "listing_price": "$0.05", "current_price": None},
    {"name": "Revoland", "listing_price": "$0.600", "current_price": None},
    {"name": "Kyoko", "listing_price": "$0.100", "current_price": None},
    {"name": "Karmaverse", "listing_price": "$0.05", "current_price": None},
    {"name": "Bot Planet", "listing_price": "$0.500", "current_price": None},
    {"name": "Zebec Protocol", "listing_price": "$0.021", "current_price": None}

],

"Latoken": [
    {"name": "GVR", "listing_price": "$0.00125", "current_price": None},
    {"name": "SBET", "listing_price": "$0.0085", "current_price": None},
    {"name": "WT", "listing_price": "$0.2", "current_price": None},
    {"name": "CKU", "listing_price": "$0.05", "current_price": None},
    {"name": "TURN", "listing_price": "$0.1", "current_price": None},
    {"name": "EEAT", "listing_price": "$0.023", "current_price": None},
    {"name": "G", "listing_price": "$0.16", "current_price": None},
    {"name": "MANC", "listing_price": "$1", "current_price": None},
    {"name": "CTEX", "listing_price": "$0.8", "current_price": None},
    {"name": "EMG SUPERAPP", "listing_price": "$0.1", "current_price": None},
    {"name": "TARALITY", "listing_price": "$0.00135", "current_price": None},
    {"name": "NINJA WARRIORS META", "listing_price": "$0.015", "current_price": None},
    {"name": "INTELLIGENT SIGNALS", "listing_price": "$0.18", "current_price": None},
    {"name": "EMG SUPERAPP (EMG)", "listing_price": "$0.1", "current_price": None},
    {"name": "SAFETY BANK CUSTODY FUND (SB.", "listing_price": "$7", "current_price": None},
    {"name": "NFT SPACE", "listing_price": "$07", "current_price": None}
],

"Coinbit":[
    
     {"name": "Zororium", "listing_price": "0.00", "current_price": None},
    {"name": "MetaViral", "listing_price": "436.50", "current_price": None},
    {"name": "Intelligent Signals", "listing_price": "174.60", "current_price": None},
    {"name": "IUSTITIA Coin", "listing_price": "0.00", "current_price": None},
    {"name": "Tycoon Fintech", "listing_price": "24.00", "current_price": None},
    {"name": "BOR COIN", "listing_price": "29.10", "current_price": None},
    {"name": "RICHMINT WORLD", "listing_price": "96.90", "current_price": None},
    {"name": "PUPILS TOKEN", "listing_price": "0.00", "current_price": None},
    {"name": "PrivaCoin", "listing_price": "0.30", "current_price": None},
    {"name": "Funex Coin", "listing_price": "679.20", "current_price": None},
    {"name": "Digital Landlord", "listing_price": "0.00", "current_price": None},
    {"name": "Tidal 2 Round", "listing_price": "3.60", "current_price": None},
    {"name": "Yoda_coin_swap", "listing_price": "145.50", "current_price": None},
    {"name": "Xcavator", "listing_price": "203.70", "current_price": None},
    {"name": "ArtRino 2 Round", "listing_price": "96.90", "current_price": None}
],

"MEXC":[
  
    {"name": "Shattered LegionsLG", "listing_price": "$0.03", "current_price": None},
    {"name": "ColonycLY", "listing_price": "$0.400", "current_price": None},
    {"name": "SubDAOGOV", "listing_price": "$0.150", "current_price": None},
    {"name": "Heroes TDHTD", "listing_price": "$0.06", "current_price": None},
    {"name": "TRVLTRVL", "listing_price": "$0.09", "current_price": None},
    {"name": "GenopetsGENE", "listing_price": "$0.800", "current_price": None},
    {"name": "CropBytesCBX", "listing_price": "$0.100", "current_price": None},
    {"name": "StartFISTFI", "listing_price": "$ 0.200", "current_price": None},
    {"name": "103 Swap", "listing_price": "$1.00", "current_price": None},
    {"name": "BlackHole ProtocolBLACK", "listing_price": "$0.05", "current_price": None},
    {"name": "BusyBUSY", "listing_price": "$0.06", "current_price": None},
    {"name": "FranklinFLY", "listing_price": "$0.024", "current_price": None},
    {"name": "ETHA Lend", "listing_price": "$1.00", "current_price": None},
    {"name": "15 WOO Network", "listing_price": "$0.03", "current_price": None}

],

"Bybit": [
    {"name": "Virtual Versions", "listing_price": "$0.007", "current_price": None},
    {"name": "Cashtree Token", "listing_price": "$0.0033", "current_price": None},
    {"name": "GameSwift", "listing_price": "$0.0144", "current_price": None},
    {"name": "Sui", "listing_price": "$0.100", "current_price": None},
    {"name": "XCAD Network", "listing_price": "$0.01", "current_price": None},
    {"name": "Medieval Empires", "listing_price": "$0.01", "current_price": None},
    {"name": "PUML Better Health", "listing_price": "$0.07", "current_price": None},
    {"name": "MIBR", "listing_price": "$1.00", "current_price": None},
    {"name": "Diamond Launch", "listing_price": "$0.02", "current_price": None},
    {"name": "OKSE / OKSE", "listing_price": "$0.06", "current_price": None},
    {"name": "DEFY", "listing_price": "$0.02", "current_price": None},
    {"name": "Shattered LegionSLG", "listing_price": "$0.03", "current_price": None},
    {"name": "OpenBloxOBX", "listing_price": "$0.00", "current_price": None},
    {"name": "WalkenWLKN", "listing_price": "$0.02", "current_price": None},
    {"name": "AurigamiPLY", "listing_price": "$0.01", "current_price": None},
    {"name": "ApeX ProtocolAPEX", "listing_price": "$0.05", "current_price": None},
    {"name": "Tap FantasyTAP", "listing_price": "$0.04", "current_price": None},
    {"name": "Monster GalaxyGGM", "listing_price": "$0.03", "current_price": None},
    {"name": "Kasta", "listing_price": "$0.04", "current_price": None},
    {"name": "iZUMi FinanceIZI", "listing_price": "$0.04", "current_price": None},
    {"name": "RealyREAL", "listing_price": "$1.00", "current_price": None},
    {"name": "Symbiosis FinanceSIS", "listing_price": "$0.80", "current_price": None},
    {"name": "Pintu TokenPTU", "listing_price": "$0.67", "current_price": None},
    {"name": "GenopetsGENE", "listing_price": "$0.80", "current_price": None},
    {"name": "CropBytesCBX", "listing_price": "$0.10", "current_price": None},
    {"name": "BitDAOBIT", "listing_price": "$2.80", "current_price": None}
],

"Gate.io": [
    {"name": "ZTX", "listing_price": "$0.025", "current_price": None},
    {"name": "VinuChain", "listing_price": "$0.02", "current_price": None},
    {"name": "Raft", "listing_price": "$0.015", "current_price": None},
    {"name": "Phantom of the Kill", "listing_price": "$0.04", "current_price": None},
    {"name": "Tezos Domains", "listing_price": "$0.180", "current_price": None},
    {"name": "Soil", "listing_price": "$0.00138", "current_price": None},
    {"name": "Cyber Arena", "listing_price": "$0.180", "current_price": None},
    {"name": "Archway", "listing_price": "$0.500", "current_price": None},
    {"name": "Kunji Finance", "listing_price": "$0.05", "current_price": None},
    {"name": "O-MEE", "listing_price": "$0.015", "current_price": None},
    {"name": "Connext", "listing_price": "$0.025", "current_price": None},
    {"name": "PymeDAO", "listing_price": "$0.02", "current_price": None},
    {"name": "SolidusAITECH", "listing_price": "$0.01", "current_price": None},
    {"name": "MetaElfLandMELD", "listing_price": "$0.00", "current_price": None},
    {"name": "KaratKAT", "listing_price": "$0.03", "current_price": None},
    {"name": "ClipperSAIL", "listing_price": "$0.08", "current_price": None},
    {"name": "BG TradeBGT", "listing_price": "$0.33", "current_price": None},
    {"name": "Antmons EntertainmentAMs", "listing_price": "$0.45", "current_price": None},
    {"name": "TrossardTROSS", "listing_price": "$0.01", "current_price": None},
    {"name": "Lucky BirdWBIRD", "listing_price": "$5.00", "current_price": None},
    {"name": "SophiaVerseSOPH", "listing_price": "$0.03", "current_price": None},
    {"name": "HatomHTM", "listing_price": "$0.40", "current_price": None},
    {"name": "Neon Link", "listing_price": "$0.06", "current_price": None},
    {"name": "Unity TokenUNT", "listing_price": "$0.06", "current_price": None},
    {"name": "GetaverseGETA", "listing_price": "$0.02", "current_price": None},
    {"name": "EthlasELS", "listing_price": "$0.30", "current_price": None},
    {"name": "AradenaAG", "listing_price": "$0.04", "current_price": None},
    {"name": "OmegaNetworkOMN", "listing_price": "$0.04", "current_price": None},
    {"name": "OtterHomeHOME", "listing_price": "$0.001", "current_price": None},
    {"name": "BiopBIOP", "listing_price": "$0.28", "current_price": None}
],

 "AscendEX": [
    {"name": "Waterfall DeFi", "listing_price": "$0.350", "current_price": None},
    {"name": "Jet Protocol", "listing_price": "$0.040", "current_price": None},
    {"name": "Oxygen", "listing_price": "$0.100", "current_price": None},
    {"name": "Showcase", "listing_price": "$0.075", "current_price": None},
    {"name": "Persistence", "listing_price": "$0.400", "current_price": None},
    {"name": "Maps.me", "listing_price": "$0.150", "current_price": None},
    {"name": "Bonfida", "listing_price": "$0.100", "current_price": None},
    {"name": "The Virtua Kolect", "listing_price": "$0.012", "current_price": None},
    {"name": "Akash Network", "listing_price": "$0.767", "current_price": None},
    {"name": "StaFi", "listing_price": "$0.130", "current_price": None},
    {"name": "Serum", "listing_price": "$0.170", "current_price": None},
    {"name": "SwingbySWINGBY", "listing_price": "$0.07", "current_price": None},
    {"name": "Stake", "listing_price": "$0.55", "current_price": None},
    {"name": "UltrAlphaUAT", "listing_price": "$0.08", "current_price": None},
    {"name": "DeepCloud AIDEEP", "listing_price": "$0.10", "current_price": None},
    {"name": "DUO NetworkDUO", "listing_price": "$0.15", "current_price": None}
],

}

st.title("Crypto ROI Dashboard")

currencies = fetch_current_prices()
df2 = pd.DataFrame(currencies)

selected_exchange = st.selectbox("Select an Exchange", list(exchange_data.keys()))
df = pd.DataFrame(exchange_data[selected_exchange])

# Cleaning the 'listing_price' column
df["listing_price"] = df["listing_price"].str.replace('$', '').astype(float)

# Fill the 'current_price' column with fetched data from the API
for i, row in df.iterrows():
    coin_name = row['name']
    matching_row = df2[(df2['name'].str.contains(coin_name)) | (df2['Symbol'].str.contains(coin_name))]
    if not matching_row.empty:
        price = matching_row.iloc[0]['Price (USD)']
        df.at[i, 'current_price'] = price

# Calculate ROI
df["current_price"] = pd.to_numeric(df["current_price"], errors='coerce')
df["ROI"] = ((df["current_price"] - df["listing_price"]) / df["listing_price"]) * 100

st.write("Price Data for Selected Exchange:")
st.write(df)

st.write("Bar Chart:")
fig_bar = px.bar(
    df, x="name", y="ROI", title=f"ROI for Crypto Coins on {selected_exchange} Exchange", text="ROI",
    labels={"name": "Crypto Coin", "ROI": "ROI %"}
)
fig_bar.update_traces(marker_line_width=3, opacity=0.8)
fig_bar.update_layout(yaxis_tickformat="%")
st.plotly_chart(fig_bar)

st.write("Line Chart:")
fig_line = px.line(
    df, x="name", y=["listing_price", "current_price"],
    title=f"Price Comparison for Crypto Coins on {selected_exchange} Exchange",
    labels={"name": "Crypto Coin", "value": "Price (USDT)"}
)
fig_line.update_traces(line=dict(width=2))
st.plotly_chart(fig_line)
