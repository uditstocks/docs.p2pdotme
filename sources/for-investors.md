# For Token Holders

## Start Here

This page covers the token thesis, economics, governance model, and token-holder FAQs in one place.

**Quick links to key sections.**

- [Token thesis](/for-token-holders/token-thesis)
- [Why the token exists](/for-token-holders/why-the-token-exists)
- [Token details and allocation](/for-token-holders/token-details)
- [MetaDAO sale](/for-token-holders/metadao-sale)
- [Vesting schedules](/for-token-holders/vesting-schedules)
- [Buy-and-burn](/for-token-holders/treasury-and-buy-and-burn)
- [Staking mechanics](/for-token-holders/staking-mechanics)
- [Token-holder governance](/for-token-holders/token-holder-governance)
- [Progressive decentralization](/for-token-holders/progressive-decentralization)
- [Insurance](/for-token-holders/insurance)
- [FAQ](/for-token-holders/faq)

Also see [`/whitepaper`](/whitepaper/abstract) for protocol context and [`/for-builders`](/for-builders/start-here) for contract-level governance detail.

---

## Token Thesis

The core rails exist today. Onramp and offramp, matching, disputes, and on-chain parameter controls are live and processing volume. The expansion path builds on what already runs: remittance and multi-currency tracks add corridors and users while reusing the existing trust model, and a B2B SDK for third-party developers to integrate P2P Protocol rails is targeted for June 2026.

The launch structure is early-stage by design. Supply is compact with no insider tokens at TGE, and governance is admin-operated today with a documented multi-phase migration to token-governed control. Value capture is structural rather than promotional. Staking, delegation, and treasury contributions route protocol revenue to network participants.

The growth record supports the thesis. The protocol has sustained an average month-on-month growth of approximately 27% over the past 16 months, and its stated target is $500M in monthly volume over the next 18 months. Targets are goals, not guarantees. Protocol metrics can be tracked on-chain [here](https://dune.com/p2pme/latest).

---

## Why the Token Exists

P2P on/off ramping is critical infrastructure for emerging markets. Millions of people depend on it to move between fiat and stablecoins every day. Infrastructure this important cannot remain under the control of a single operator. The token exists to decentralize ownership of this utility so that no single team, company, or jurisdiction can shut it down, censor it, or extract from it unfairly.

`$P2P` is an **ownership token**. Under the target governance model, protocol intellectual property, treasury funds, and the ability to mint new tokens are controlled by token-holder governance through an on-chain Governor rather than by any single team. Holders are designed to control protocol financials, govern operational parameters, direct treasury spending, and hold enforceable claim over protocol IP. If protocol resources or IP were ever misappropriated, token governance gives holders the mechanism to redirect control, making control over the protocol and its resources enforceable and distributed.

The token enables four things. The first is decentralized governance: holders vote on fees, limits, merchant rules, and treasury allocation, so no single operator controls these decisions. The second is trust staking through Circles of Trust, where token holders stake $P2P on merchant liquidity pools to attest to their trustworthiness, earning stablecoin yield from the Circle's transaction revenue.

The third is revenue-linked ownership. 20% of protocol revenue flows to the DAO-governed treasury, and the treasury can fund buy-and-burn or other value-accruing actions only through a passed governance proposal. The fourth is censorship resistance: decentralized ownership means no single point of failure, so the protocol can survive regulatory pressure in any one jurisdiction because control is distributed globally among token holders.

---

## Token Details

<div className="stats-grid">
  <div className="stat-card">
    <div className="stat-label">Name</div>
    <div className="stat-value">P2P Governance Token</div>
  </div>
  <div className="stat-card">
    <div className="stat-label">Ticker</div>
    <div className="stat-value stat-highlight">$P2P</div>
  </div>
  <div className="stat-card">
    <div className="stat-label">Chain</div>
    <div className="stat-value">
      <span style={{display:'inline-flex', alignItems:'center', gap:'6px', marginRight:'12px'}}>
        <span style={{width:'8px', height:'8px', borderRadius:'50%', background:'#4ade80', display:'inline-block'}}></span>
        Solana
      </span>
      <span style={{display:'inline-flex', alignItems:'center', gap:'6px', opacity:'0.5'}}>
        <span style={{width:'8px', height:'8px', borderRadius:'50%', background:'#a78bfa', display:'inline-block'}}></span>
        Base
      </span>
    </div>
    <span className="stat-subtext">Solana live · Base coming soon</span>
  </div>
  <div className="stat-card" style={{gridColumn: '1 / -1'}}>
    <div className="stat-label">Total Supply</div>
    <div className="stat-value">25,800,000 <span className="stat-subtext">(25.8M at launch)</span></div>
  </div>
  <div className="stat-card" style={{gridColumn: '1 / -1'}}>
    <div className="stat-label">Initial Float</div>
    <div className="stat-value">12.9M at TGE <span className="stat-subtext">(10M sale + 2.9M liquidity = 50%)</span></div>
  </div>
  <div className="stat-card" style={{gridColumn: '1 / -1'}}>
    <div className="stat-label">Future Issuance</div>
    <div className="stat-value">Only via governance-approved proposals</div>
  </div>
</div>

---

## Token Utility

**Ownership.** $P2P is an ownership token. Protocol IP, treasury funds, and mint authority are controlled by token holders through the on-chain Governor, not by any single team, foundation, or entity. This means the token carries enforceable governance rights, including the mechanism to redirect control described in "Why the Token Exists." Decisions that affect token supply (minting) must pass an on-chain vote, where one staked $P2P equals one vote and a proposal passes only with majority support and quorum.

**Governance.** Token holders vote on protocol parameters such as fees, limits, merchant rules, oracle configs, and treasury allocation. One staked $P2P = one vote, with delegation.

**Staking.** Circle Admins stake $P2P to operate merchant networks. Community members delegate $P2P to Circles to participate in revenue sharing. Merchants stake USDC as working capital. The staking design aligns incentives by requiring economic commitment at every layer.

**Fee distribution.** Protocol revenue is routed across participants.

| Recipient              | Share of Revenue                                             |
| ---------------------- | ------------------------------------------------------------ |
| Merchants + Delegators | 53.33%                                                       |
| Treasury               | 20%, roadmap toward 33% buy-and-burn share (governed via the on-chain Governor) |
| Insurance Pools        | 17.78%                                                       |
| Circle Admins          | 8.89%                                                        |

No single party captures a majority of protocol revenue. Merchants earn the most because they provide working capital and operational labor. Treasury contributions tie protocol usage to the network treasury. Governance can direct these funds toward buy-and-burn or other uses through a passed on-chain proposal. Insurance pools exist so disputes don't become externalised costs.

---

## Token Allocation

| Category         | Tokens         | % of Supply | Vesting                                    |
| ---------------- | -------------- | ----------- | ------------------------------------------ |
| **MetaDAO Sale** | **10,000,000** | **38.8%**   | Unlocked at launch                         |
| **Liquidity**    | **2,900,000**  | **11.2%**   | Treasury-provided to DEX pools at launch   |
| **Team**         | **7,740,000**  | **30%**     | Performance-based (see vesting)            |
| **Early Backers** | **5,160,000**  | **20%**     | 12-month cliff, then five equal tranches at months 12, 15, 18, 21, 24 |
| **Total**        | **25,800,000** | **100%**    |                                            |

No backer or team tokens unlock at TGE. At launch, 12.9M tokens circulate (10M sale + 2.9M liquidity). Future issuance is governance-gated.

---

## MetaDAO Sale

The $P2P token launches through a MetaDAO-style sale mechanism designed for fair, community-first distribution.

1. Users commit USDC during a 4-day commitment window
2. Founders set a discretionary cap on total raise accepted
3. If oversubscribed, allocations and refunds are distributed pro-rata
4. 10M tokens are distributed proportionally among all participants at launch
5. Post-sale, the treasury provides 20% of raised USDC and 2.9M tokens to liquidity pools
6. Mint authority transfers to the market-governed treasury

Existing protocol users receive a preferential allocation at the same valuation as other sale participants, based on their on-chain XP.

---

## Vesting Schedules

### Team Tokens (30% / 7.74M)

Team tokens follow the MetaDAO performance package model. Rather than time-based vesting, tokens unlock based on protocol performance milestones.

- 5 equal tranches of 1,548,000 tokens each
- Tranches unlock at 2x, 4x, 8x, 16x, 32x ICO price
- 12-month cliff from launch. No tranche unlocks before month 12.
- After the cliff, tranches unlock only when the price threshold is met. There is no fixed calendar unlock beyond the cliff.
- Price measured via 3-month TWAP after the cliff

Because every tranche is gated by a sustained price threshold, team unlocks track protocol performance rather than elapsed time.

### Early Backer Tokens (20% / 5.16M)

- Months 0 through 12 are fully locked (cliff)
- At month 12, 1,032,000 tokens unlock (20%)
- At months 15, 18, 21, and 24, 1,032,000 tokens unlock each quarter
- Fully vested at month 24

Vesting is enforced via on-chain vesting contracts. Locked tokens cannot be staked.

---

## Treasury and Buy-and-Burn

20% of protocol revenue is routed to the DAO-governed treasury, with a stated roadmap toward a 33% buy-and-burn share by 2027 via governance. Through the on-chain Governor, token holders decide how those funds are deployed, including buy-and-burn, ecosystem grants, liquidity incentives, or other uses.

There is no automatic buyback schedule. Every buy-and-burn requires a passed governance proposal, and the mechanism itself is one governance-approved option: tokens purchased on the open market via DEX and sent to the zero address. The first treasury contribution is expected from June 2026.

The mechanism gives token holders direct control over treasury deployment. Revenue comes in, governance decides deployment, and the treasury scales with volume.

---

## Staking Mechanics

- **Circle Admins** stake $P2P to operate merchant networks. Their stake is slashable, and a portion of their rewards is locked as an insurance buffer.
- **Merchants** stake USDC as working capital for order fulfillment. Their capacity is bounded by their stake.
- **Delegators** stake $P2P to Circles to earn a share of revenue. Governance voting power derives from staked $P2P (one staked $P2P equals one vote), with standard on-chain delegation.

---

## Token-Holder Governance

The target model gives token holders direct control over protocol parameters, treasury, and upgrades.

| Parameter          | Value. Target or typical, with on-chain bounds in parentheses |
| ------------------ | ------------------------------------ |
| Voting Power       | 1 staked $P2P = 1 vote (delegatable) |
| Voting Delay       | 1 day (configurable, 1s to 30d)      |
| Voting Period      | 7 days (configurable, 1h to 30d)     |
| Quorum             | Snapshot quorum, set by governance   |
| Passing condition  | For-votes exceed against-votes and meet quorum |
| Proposal threshold | Capped at 10% of supply              |
| Timelock           | 7 days typical (configurable, 1h to 30d) |

Governable parameters include fee percentages, spread configuration, staking and slashing rules, transaction volume limits, treasury allocation, smart contract upgrades, and token whitelisting.

For contract-level governance detail (roles, permissions, dispute mechanics), see [`/for-builders`](/for-builders/start-here).

---

## Progressive Decentralization

Decentralization is phased because governance quality matters more than governance speed.

**Phase 1 (months 0-6 post-TGE).** Foundation multisig controls upgrades. Emergency pause capability exists.

**Phase 2 (months 6-18 post-TGE).** Token-holder voting activates for non-critical parameters. Community can submit governance proposals.

**Phase 3 (month 18+ post-TGE).** DAO-primary control of all protocol parameters. Foundation veto sunsets, with a narrow admin emergency capability retained for safety.

---

## Insurance

The protocol design includes a three-tier insurance stack.

**CAIP (Circle Admin Insurance Pool).** First-line coverage funded by a percentage of Circle volume plus slashed stakes.

**CALR (Circle Admin Locked Rewards).** A portion of admin earnings locked in a rolling buffer.

**PIP (Protocol Insurance Pool).** Backstop for systemic failures or depleted lower-tier pools.

_The full insurance-pool stack with programmable slash/reward logic and dispute-linked payouts is planned for a future release._

---

## Protocol Metrics

All protocol metrics are verifiable on-chain. See the live [Dune dashboard](https://dune.com/p2pme/latest) for current volume, revenue, and user activity.

The protocol earns revenue entirely from transaction fees on a working product, with no reliance on token emissions or inflationary incentives.

---

## FAQ

### Why does P2P need a token?

P2P on/off ramping is essential financial infrastructure in emerging markets. Without a token, control over this infrastructure stays with a single operator who can change fees, censor users, or shut it down. The token transfers that control to the community.

### Is this an ownership token?

Yes. This is protocol ownership, distinct from equity in a traditional company. The "Why the Token Exists" section above covers the full ownership thesis.

### How does the MetaDAO-style sale work?

Users commit USDC during a 4-day window. If oversubscribed, allocations are pro-rata. Existing protocol users with XP get priority. No new private round happens at TGE. The sale is the primary distribution event.

### What unlocks at TGE?

10M sale tokens + 2.9M liquidity tokens (12.9M total, 50% of supply). Zero backer or team tokens unlock at launch.

### How does the treasury work?

The treasury is funded entirely by transaction revenue from a working product, and token holders decide how to deploy those funds through the on-chain Governor. There is no automatic buyback schedule. The [Treasury and Buy-and-Burn](/for-token-holders/treasury-and-buy-and-burn) section covers the full mechanics, including the revenue share and the buy-and-burn roadmap.

### Is supply fixed?

Yes, fixed at launch (25.8M $P2P). Future issuance requires governance approval through the on-chain Governor. The protocol runs on transaction revenue, not token emissions.

### Why Base for the protocol, and where does the token live?

The protocol contracts run on Base for its low fees, fast finality, and Ethereum tooling, which make frequent small transactions practical. The $P2P token is an SPL token already live on Solana. Broader protocol deployment to Solana is on the roadmap. Chain choice does not lock the token design.

### How do I separate what's live from what's planned?

Inline notes throughout the docs mark features planned for future releases. For contract-level detail on what is deployed, see [`/for-builders`](/for-builders/start-here).

---

## Get $P2P

import { LivePrice, CopyAddress } from '../../src/components/TokenBuyWidgets';

<div className="htb-hero">
  <h2>$P2P Token</h2>
  <p>The governance and utility token of the p2p.me protocol. Used for staking and on-chain governance. Available on Solana via Jupiter.</p>
  <div style={{display: 'flex', justifyContent: 'center', width: '100%', margin: '0'}}>
    <a className="htb-buy-btn" href="https://jup.ag/tokens/P2PXup1ZvMpCDkJn3PQxtBYgxeCSfH39SFeurGSmeta" target="_blank" rel="noopener noreferrer">
      View on Jupiter ↗
    </a>
  </div>
</div>

### Live Price

<LivePrice />

### Contract Address

<CopyAddress />

:::warning Avoid scams
Always verify the contract address above before buying. Never click $P2P buy links shared in Telegram, Discord, or Twitter DMs.
:::

### Steps to Buy

<ol className="htb-steps">
  <li>Set up a Solana wallet. <a href="https://phantom.app" target="_blank">Phantom</a> or <a href="https://www.solflare.com/" target="_blank">Solflare</a> are recommended.</li>
  <li>Fund your wallet with SOL to cover the token purchase and transaction fees.</li>
  <li>Open <a href="https://jup.ag/tokens/P2PXup1ZvMpCDkJn3PQxtBYgxeCSfH39SFeurGSmeta" target="_blank">Jupiter</a> and connect your wallet.</li>
  <li>Swap SOL (or any supported token) for <strong>$P2P</strong>.</li>
  <li>Confirm the transaction - your $P2P will appear in your wallet shortly.</li>
</ol>

### After You Buy

<div className="htb-next-grid">
  <a className="htb-next-card" href="/for-token-holders/staking-mechanics">
    <div className="htb-next-icon">
      <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
        <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
        <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
      </svg>
    </div>
    <p className="htb-next-title">Stake $P2P</p>
    <p className="htb-next-desc">Earn protocol fees by staking your tokens.</p>
  </a>
  <a className="htb-next-card" href="/for-token-holders/token-holder-governance">
    <div className="htb-next-icon">
      <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
        <path d="M9 11l3 3L22 4"></path>
        <path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"></path>
      </svg>
    </div>
    <p className="htb-next-title">Governance</p>
    <p className="htb-next-desc">Vote on proposals and shape the protocol.</p>
  </a>
  <a className="htb-next-card" href="/for-community/start-here">
    <div className="htb-next-icon">
      <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
        <circle cx="12" cy="12" r="10"></circle>
        <line x1="2" y1="12" x2="22" y2="12"></line>
        <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
      </svg>
    </div>
    <p className="htb-next-title">Join Community</p>
    <p className="htb-next-desc">Connect with other holders and contributors.</p>
  </a>
</div>

### Track $P2P

<div className="htb-track-row">
  <a className="htb-track-link" href="https://dexscreener.com/solana/P2PXup1ZvMpCDkJn3PQxtBYgxeCSfH39SFeurGSmeta" target="_blank">DexScreener ↗</a>
  <a className="htb-track-link" href="https://jup.ag/tokens/P2PXup1ZvMpCDkJn3PQxtBYgxeCSfH39SFeurGSmeta" target="_blank">Jupiter ↗</a>
  <a className="htb-track-link" href="https://www.geckoterminal.com/solana/pools/EPynJir3BRBZGvb9ZqoJJuxFopf83RXPYkrWeh24srVA" target="_blank">GeckoTerminal ↗</a>
  <a className="htb-track-link" href="https://dex.coinmarketcap.com/token/solana/P2PXup1ZvMpCDkJn3PQxtBYgxeCSfH39SFeurGSmeta/" target="_blank">CoinMarketCap ↗</a>
</div>

---

## Disclosures

The $P2P token is a utility and governance token. It is not an asset-referenced token or an e-money token, and it is not equity, debt, or a security. It carries governance rights and protocol utility, with no redemption rights and no claim on the issuer's or foundation's assets, revenue, or profit. Value, if any, derives from protocol usage and network participation, not from any promise of returns. US persons were excluded from the primary sale.
