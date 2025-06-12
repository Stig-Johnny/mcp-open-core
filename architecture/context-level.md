# MCP Open Core Architecture — C4 Level 1

```mermaid
C4Context
title MCP Open Core Architecture

Person(Operator, "Stig-Johnny", "Sovereign Quant System Operator")

System(MCP, "MCP Sovereign Open Core", "Open-Source AI Quant Trading Intelligence")

System_Ext(Exchanges, "Crypto Exchanges", "Binance, Kraken, Coinbase")
System_Ext(NewsFeeds, "News Sources", "CryptoNews, Cointelegraph, Bloomberg, X")
System_Ext(OnChainData, "On-Chain Providers", "Glassnode, Whale Alert, Santiment")
System_Ext(Macros, "Macro Data", "CPI, FED, Dollar Index")

Rel(Operator, MCP, "Oversight & Tactical Execution")
Rel(MCP, Exchanges, "Market Data")
Rel(MCP, NewsFeeds, "Narrative Parsing")
Rel(MCP, OnChainData, "Whale Flow, Liquidity")
Rel(MCP, Macros, "Liquidity Macro Signals")
