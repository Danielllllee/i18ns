# 中国外部环境与全球"大周期"定位（截至 2026-10-08）— External order & external demand

> **方法与可靠性说明（给报告撰写人）**：本轮对目标站点（safe.gov.cn、stats.gov.cn、federalreserve.gov、imf.org、cnbc.com、axios.com、congress.gov、china-briefing.com、globaltradealert.org 等）的直接抓取（WebFetch 与经代理的 curl）全部失败（DNS/CONNECT 被出口策略拒绝），因此下文事实**全部来自 WebSearch 对所列链接页面的检索综述**，未能逐页核对原文。之后本会话共享的 WebSearch 配额耗尽，下列子问题**未能检索**：EV/电池/光伏全球份额、中国占全球制造业增加值份额、R&D/专利/GII、IMF 等潜在增速估计、新兴市场（墨西哥/巴西/印度等）对华贸易救济、9 月末外储精确值与 CFETS 指数、外汇局结售汇数据、外资持债、10 月 WEO。凡来源冲突均已标注；"推算"均为笔者基于已引数据的算术，非来源原文。

> **总览（解读，非事实）**：
> 1. **周期（外需）维度**：2026 年外需是中国经济最强的顺风——美元口径出口 1–8 月同比约 +19%，6 月 +27% 为 2021-10 以来最快，全年顺差大概率再创纪录（2025 年为 1.189 万亿美元）。但顺风的"质量"在下降：增长高度依赖全球 AI/存储芯片**价格**周期（芯片出口量跌、价翻倍），进口增速更快使顺差扩张有限；欧盟钢铁新规、EV 价格承诺、反倾销增多与美国"产能过剩"301 预示保护主义上升；9 月以来全球金融条件收紧（美联储加息至 3.75–4.00%、美元指数约 102、布伦特 >100 美元）。判断：**顺风，但处于高位/边际见顶，方向由"改善"转向"持平偏弱"**。
> 2. **Dalio 大周期（外部秩序）维度**：中国在制造与技术上呈"上升国"特征（2025 年工业机器人装机占全球 59%；中国开源大模型在部分路由平台 token 份额过半；国产 AI 芯片替代加速），债权国地位强化（顺差、经常账户高位），储备多元化持续（黄金连续 23 个月增持）；但人口逆风加剧、人民币国际化仍小（SWIFT 支付份额约 3%），中美冲突处于"短期展期的管理型休战"（到期日 2027-01-10），未进入解决阶段，且伊朗战争/霍尔木兹、台海与中日摩擦构成地缘尾部风险。

---

## 1. 中美关系时间线（2025-10 → 2026-10）：釜山框架及执行、两次国事访问、美国对华关税的法律基础、中方反制、芯片管制、台海与日程

### Takeaway
中美处于"交易型、可逆的管理休战"：釜山（2025-10-30）框架靠短期展期维持（9 月白宫峰会后展期至 **2027-01-10**）。最高法院 **2026-02-20** 裁定 IEEPA 不授权关税后，美对华"第二任期附加税"由 IEEPA 20% → 第 122 条 10%（2/24–7/24）→ 301"强迫劳动"12.5%（7/24 起），叠加 2018/2024 年 301 税；CRS 估 7 月美对华平均税率约 36.5%、中对美约 31%。下一批关键节点：USTR"产能过剩"301 结果（传对华 7.5%，"数周内"）、APEC 深圳（**11/18–19**，特朗普表示将出席）、休战到期（2027-01-10）。

### Cited Findings

#### 1a. 釜山（2025-10-30）框架条款
- 白宫事实清单：中国在 2025 年最后两个月购买≥1,200 万吨美国大豆，2026、2027、2028 年每年≥2,500 万吨（发布于 2025-11）— [White House fact sheet, Nov 2025](https://www.whitehouse.gov/fact-sheets/2025/11/fact-sheet-president-donald-j-trump-strikes-deal-on-economic-and-trade-relations-with-china/)
- 中国暂停 2025-10-09 公布的稀土相关出口管制新措施一年（至 2026-11-10），换取美方暂停 BIS"关联方（50%）规则"一年 — [Mining Technology](https://www.mining-technology.com/news/china-rare-earth-export-pause-nears-expiry-amid-persistent-supply-concentration/); [Global Trade Alert state act](https://globaltradealert.org/state-act/95168-china-temporary-suspension-of-additional-export-controls-for-rare-earth-related-technologies/)
- 釜山后中国商品承受的 IEEPA 附加税合计 20%（10%"对等"+10%"芬太尼"）— [Global Trade Alert, "From IEEPA to Section 122"](https://globaltradealert.org/blog/from-ieepa-to-section-122)
- 中国对全部美国商品的反制关税为 10%（自 125% 降下，依 2025-11 协议维持）— [Zonos US tariff tracker](https://zonos.com/docs/guides/us-tariff-changes)
- 不可靠实体清单：北京同意撤销 2025 年 3 月所列 15 家企业的相关措施、对 4 月所列一批暂停一年；中方 2025-11-05 公告措辞比白宫表述更窄 — [MoFo, 2025-11-13](https://www.mofo.com/resources/insights/251113-united-states-and-china-reach-trade-agreement); [China Trade Monitor](https://www.chinatrademonitor.com/tag/unreliable-entity-list/)
- 美方于 2025-11-13 在联邦公报修改"中国海事/物流/造船"301 行动（港口费相关）；CRS（2026-05-21 更新）称 USTR 已认定海事与半导体做法"可诉"但推迟实施救济 — [Federal Register, 2025-11-13](https://www.federalregister.gov/documents/2025/11/13/2025-19873/notice-of-modification-of-section-301-action-chinas-targeting-of-the-maritime-logistics-and); [CRS IF12125 (updated 2026-05-21)](https://www.congress.gov/crs_external_products/IF/PDF/IF12125/IF12125.10.pdf)

#### 1b. 釜山框架执行情况
- 2025 年大豆承诺是否完成存在争议：Bessent 1 月称已完成；USDA 数据显示截至 2026-01-08 仅 >800 万吨，销售累计到 2026 年 6 月中旬才达 1,196 万吨 — [Fortune, 2026-01-21](https://fortune.com/2026/01/21/china-buys-all-12-million-tons-of-soybeans-it-promised-just-in-time-for-trump-to-announce-new-tariffs/); [Dim Sums blog, 2026-06](http://dimsums.blogspot.com/2026/06/tracking-chinas-2025-soybean-purchase.html)
- 截至 2026 年 9 月下旬，中国已完成 2026 年 2,500 万吨大豆承诺的一半以上，但另一项数十亿美元其他农产品采购承诺"基本停滞" — [Bloomberg, 2026-09-21](https://www.bloomberg.com/news/articles/2026-09-21/china-s-selective-crop-buying-tests-us-trade-truce-before-summit)
- 9 月展期未新增大豆采购承诺，美豆仍适用现行 10% 关税（商业买家转向南美）— [DTN, 2026-09-28](https://www.dtnpf.com/agriculture/web/ag/columns/washington-insider/article/2026/09/28/us-china-extends-trade-truce-new)
- 稀土：2025 年 4 月起的许可制度仍在；钇、镝、铽出口仍较限制前低约 50%（5 月下旬分析）；中国 2026 年持续对特定企业实施较窄限制；白宫"事实上取消管制"的说法未获中方确认 — [TechTimes, 2026-05-26](https://www.techtimes.com/articles/317208/20260526/china-rare-earth-export-controls-april-curbs-still-bite-after-beijing-summit.htm)
- 2026 年 7 月稀土出口量同比降近 30% — [China-Global South Project, 2026-08-07](https://chinaglobalsouth.com/2026/08/07/china-exports-july-2026-ai-high-tech-demand/)
- 关键矿产方面没有双方共同书面确认的解决方案，展期被视为未完成的谈判 — [BISI](https://bisi.org.uk/reports/chinas-rare-earth-processing-dominance-and-what-the-trump-xi-summit-didnt-change)
- Bessent 公开指出中方釜山承诺仍有未完成项 — [CNBC, 2026-09-24](https://www.cnbc.com/2026/09/24/us-china-trade-truce-bessent-trump-xi.html)

#### 1c. 2026 年 5 月特朗普国事访华（北京）
- 访问日期各源不一（5/13–15、5/14–15 或至 5/16）— [Wikipedia: 2026 state visit by Donald Trump to China](https://en.wikipedia.org/wiki/2026_state_visit_by_Donald_Trump_to_China)
- 白宫 2026-05-17 事实清单：中方采购 200 架波音；2028 年前每年≥170 亿美元美国农产品（在大豆承诺之外）；恢复无禽流感州禽肉准入、承诺重开牛肉市场；处理美方对稀土/关键矿产（钇、钪、钕、铟）短缺的关切；设立"Board of Trade"（贸易委员会）与"Board of Investment"（投资委员会）；伊朗：不得拥核、霍尔木兹应重开、不得收"过路费"；文件**未提台湾** — [White House fact sheet, 2026-05](https://www.whitehouse.gov/fact-sheets/2026/05/fact-sheet-president-donald-j-trump-secures-historic-deals-with-china-delivering-for-american-workers-farmers-and-industry/); [UPI, 2026-05-18](https://www.upi.com/Top_News/US/2026/05/18/China-Trump-deals/5841779079659/); [Business Standard](https://www.business-standard.com/amp/world-news/white-house-fact-sheet-on-trump-s-china-visit-cites-iran-deal-omits-taiwan-126051800020_1.html)
- 商务部确认波音订单，并将其与美方发动机/零部件供应承诺及"关税削减"磋商挂钩；中方将成果定性为初步、相互的，读稿提"贸易理事会"做产品级对等降税 — [CNN, 2026-05-20](https://www.cnn.com/2026/05/20/china/china-confirms-boeing-purchases-deals-intl-hnk); [The Asia Group](https://theasiagroup.com/washington-and-beijing-produce-divergent-readouts-on-trump-xi-summit/)
- 波音称为"初步承诺"，型号/交付不明，消息后股价跌约 4% — [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/boeing-gets-china-deal-trump-124040564.html)
- 5 月峰会**未延长**2025-10 休战，具体关税成果有限（CNBC 称以排场为主）— [China Briefing](https://www.china-briefing.com/news/xi-trump-beijing-summit-what-was-agreed/); [CNBC, 2026-09-28](https://www.cnbc.com/2026/09/28/cnbcs-the-china-connection-trump-xi-summit-about-domestic-messaging.html)
- USTR 2026-06-05 就"与中国促进对等管理贸易机制"征求公众意见（7/10 截止，7/27 回复）— [Federal Register, 2026-06-05](https://www.federalregister.gov/documents/2026/06/05/2026-11291/request-for-comments-on-the-scope-and-operation-of-a-mechanism-to-promote-reciprocal-managed-trade)
- 两党议员对"投资委员会"持怀疑；Greer 称对华投资政策基本不变 — [Semafor, 2026-05-14](https://www.semafor.com/article/05/14/2026/lawmakers-skeptical-of-trump-plans-for-us-china-investment-board)

#### 1d. 2026 年 9 月习近平国事访问华盛顿（9/23–25）
- 9/23 抵达，9/24 白宫会谈；为 2015 年后首次国事访美 — [Wikipedia: 2026 state visit by Xi Jinping to the US](https://en.wikipedia.org/wiki/2026_state_visit_by_Xi_Jinping_to_the_United_States); [Al Jazeera, 2026-09-23](https://www.aljazeera.com/news/2026/9/23/trump-meets-chinas-xi-jinping-at-us-airport-on-arrival-for-three-day-trip)
- Bessent 9/23 宣布休战由 2026-11-10 展期至 **2027-01-10**；商务部表述为将"吉隆坡联合安排"延至 2027-01-10，文本**未点名稀土** — [CNBC, 2026-09-24](https://www.cnbc.com/2026/09/24/us-china-trade-truce-bessent-trump-xi.html); [Rinnovabili](https://www.rinnovabili.net/policy-and-affairs/environmental-policies/chinese-rare-earth-exports-trump-xi-truce/)；冲突：部分 10 月初报道仍称稀土暂停 11-10 到期 — [Rare Earth Exchanges](https://rareearthexchanges.com/news/china-rare-earth-controls-trump-xi-deadline/)
- "30-for-30"：双方各约 300 亿美元"非敏感商品"降税推荐清单（合计约 600 亿美元），9/27 公布；按出口额约覆盖美对华出口近 30%、中对美出口约 10%；中方清单含部分农产品、海产品、木制品、化妆品、医疗器械，美方含小家电、玩具、节日装饰、儿童安全座椅；需完成各自国内法律程序，**未定降幅与生效日**；白宫称"协议"，商务部称"仍在寻求共识的框架" — [Axios, 2026-09-26](https://www.axios.com/2026/09/26/us-china-tariffs-trade-30-billion); [Al Jazeera, 2026-09-28](https://www.aljazeera.com/economy/2026/9/28/us-china-list-goods-recommended-for-tariff-cuts-following-trump-xi-summit); [Covington, 2026-10](https://www.cov.com/en/news-and-insights/insights/2026/10/white-house-announces-product-lists-for-potential-tariff-cuts-under-us-china-board-of-trade-mechanism)
- Sinolytics 标题称清单为"77 vs. 1,619"（推测为两侧税目数，未核实）— [Sinolytics](https://sinolytics.de/global-business-news/blog/geopolitics/u-s-china-tariff-deal-30-bn-usd)
- 中国 2027、2028 年每年采购 1,000 万吨美国煤炭；另设贸易与 AI 对话机制；农业工作组年内首会 — [Breakwave Advisors, 2026-10-06](https://www.breakwaveadvisors.com/insights/2026/10/6/us-china-trade-deal-reshaping-grain-and-coal-trade-flows); [Asia Society](https://asiasociety.org/policy-institute/what-actually-happened-xi-trump-summit)
- 白宫 2026-09-25 事实清单：贸易委员会与投资委员会已运作；中方 8 月依美方线索拘捕 21 名涉芬太尼前体人员；**未提台湾**（新华社读稿提及反对"台独"）— [White House fact sheet, 2026-09-25](https://www.whitehouse.gov/fact-sheets/2026/09/fact-sheet-president-donald-j-trump-advances-a-fair-and-reciprocal-relationship-with-china-while-hosting-historic-state-visit/); [Focus Taiwan, 2026-09-26](https://focustaiwan.tw/politics/202609260010)
- 观点：Brookings（O'Hanlon）认为无意重塑关系核心；Fortune 称"有管理的衰退"；CNN 称"重排场轻实质"；一中国经济简报认为清单有意义，部分中国商品税率可能优于美国盟友 — [Brookings](https://www.brookings.edu/articles/what-did-the-trump-xi-summit-actually-accomplish/); [Fortune, 2026-09-28](https://fortune.com/2026/09/28/xi-trump-summit-us-china-relations-managed-decline/); [CNN, 2026-09-25](https://www.cnn.com/2026/09/25/world/xi-dc-trump-analysis-intl-hnk); [China Econ Notes](https://chinaeconnotes.substack.com/p/october-5-2026-trump-xi-summit-outcomes)

#### 1e. 美国对华关税：按法律基础（截至 2026-10-08）

| 层级 / 法律基础 | 对华税率 | 状态 | 来源 |
|---|---|---|---|
| IEEPA"芬太尼"+"对等" | 合计 20%（各 10%） | 最高法院 2026-02-20 裁定无效；CBP 自 2026-02-24 停征 | [GTA](https://globaltradealert.org/blog/from-ieepa-to-section-122); [BDO](https://www.bdo.com/insights/tax/supreme-court-invalidates-ieepa-tariffs-administration-replaces-with-new-surcharge-what-importers) |
| 第 122 条（Proclamation 11012） | 10%（全球；15% 仅宣布未实施） | 2026-02-24 至 07-24 到期；CIT 2026-05-07 以 2–1 判越权（救济限原告，上诉中） | [Wiley](https://www.wiley.law/alert-Trump-Imposes-Section-122-Tariffs-After-Halting-IEEPA-Tariffs-Previews-New-Section-301-Investigations); [Skadden](https://www.skadden.com/insights/publications/2026/05/us-trade-court-strikes-down-section-122-tariffs) |
| 301"强迫劳动"（2026） | 12.5%（约 60 个经济体 10–12.5%） | 2026-07-24 起生效 | [Covington, 2026-06](https://www.cov.com/en/news-and-insights/insights/2026/06/ustr-announces-findings-and-calls-for-comments-in-section-301-forced-labor-investigation); [TariffsTool](https://www.tariffstool.com/guides/section-122-tariff-rates-2026) |
| 301（2018 清单 1–3 / 4A） | 25% / 7.5% | 有效；USTR 2026-10-06 决定延续（联邦公报 10-07）；约 178 项排除延至 11/9 或 11/10 | [KPMG, 2026-10](https://kpmg.com/us/en/taxnewsflash/news/2026/10/ustr-china-section-301-actions-product-exclusion.html); [FR 2026-10-07](https://www.govinfo.gov/content/pkg/FR-2026-10-07/pdf/2026-20510.pdf); [The Tariff Desk China tracker](https://www.thetariffdesk.com/tools/china-tariff-tracker) |
| 301（2024 四年审查加征） | 部分产品 25%–100% | 有效（据 9 月关税追踪器） | [The Tariff Desk China tracker](https://www.thetariffdesk.com/tools/china-tariff-tracker); [Airlift USA](https://airliftusa.com/tariff-updates/section-301) |
| 301"结构性产能过剩"（2026-03 启动，16 经济体） | 传对华有效 7.5% | 未落地；Greer 10 月初称"数周内" | [FR 2026-03-17](https://www.federalregister.gov/documents/2026/03/17/2026-05214/initiation-of-section-301-investigations-acts-policies-and-practices-of-certain-economies-relating); [Yahoo/Bloomberg](https://finance.yahoo.com/economy/policy/articles/us-plans-7-5-china-161734641.html); [Seoul Economic Daily, 2026-10-02](https://en.sedaily.com/international/2026/10/02/us-vows-action-on-overcapacity-within-weeks) |
| 301"第一阶段协议执行"（2025-10-24 启动） | — | 仍开放，未见裁定 | [USTR, 2025-10](https://ustr.gov/about/policy-offices/press-office/press-releases/2025/october/ustr-initiates-section-301-investigation-chinas-implementation-phase-one-agreement) |
| 301 半导体（成熟制程） | — | 2026-01 肯定性裁定；救济推迟 | [Thompson Hine, 2026-01](https://www.thompsonhinesmartrade.com/2026/01/ustr-issues-affirmative-determination-in-china-semiconductor-section-301-investigation/); [CRS IF12125](https://www.congress.gov/crs_external_products/IF/PDF/IF12125/IF12125.10.pdf) |
| 第 232 条（钢铝/汽车/铜等） | **本轮未核实** | — | — |

- 平均税率：CRS 估第 122 条期间对华总体约 34%；7 月数据美对华平均约 36.5%、中对美约 31% — [CRS IF12990 (updated 2026-08-14)](https://www.congress.gov/crs_external_products/IF/PDF/IF12990/IF12990.13.pdf)；与之有差异：某商业工具称对华"有效"37.5% — [TariffsTool](https://www.tariffstool.com/guides/china-tariff-rate)
- 12.5%+7.5%=20% 被视为釜山时美方承诺的新增税上限；CSIS 称北京预期以 20% 为上限 — [CSIS](https://www.csis.org/analysis/section-301-tariffs-and-china-risky-gambit)
- IEEPA 退税：CIT 2026-03-04 令 CBP 启动退税，4/20 开放第一阶段申报；BDO 估 IEEPA 关税征收额截至春季超 1,660 亿美元 — [Offit Kurman](https://www.offitkurman.com/offit-kurman-blogs/tariff-litigation-ieepa-refunds-section-122); [BDO](https://www.bdo.com/insights/tax/supreme-court-invalidates-ieepa-tariffs-administration-replaces-with-new-surcharge-what-importers)
- G20 贸易部长会（密尔沃基）在产能过剩问题上无共识；10/7 Greer 宣布 14–15 个经济体签署产能过剩联合声明，中国不在其列 — [France 24, 2026-10-02](https://www.france24.com/en/economy/20261002-g20-trade-ministers-overcapacity-impasse-greer); [MLex](https://mlex.com/mlex/trade/articles/2535402)
- 特朗普 10 月初威胁对"不在美投资"的国家征 300% 关税（仅见标题，未核实细节）— [Motley Fool, 2026-10-07](https://www.fool.com/investing/2026/10/07/donald-trump-threaten-tariffs-countries-xi-china/)

#### 1f. 中方反制（2026）
- 中国对 7/24 起的 12.5% 301 关税截至 7 月底未报复 — [China Briefing tariff tracker](https://www.china-briefing.com/news/us-china-tariff-rates-2025/)
- 2026-01：收紧对日本两用物项出口（与涉台言论挂钩）— [Global Times, 2026-01](https://www.globaltimes.cn/page/202601/1352441.shtml)
- 2026-05-02：首次援引《阻断外国法律与措施不当域外适用办法》，禁止执行 OFAC 对 5 家"茶壶"炼厂的制裁 — [Jones Day, 2026-05](https://www.jonesday.com/en/insights/2026/05/caught-in-the-crossfire-two-new-china-decrees-raise-the-stakes-on-sanctions-compliance)
- 2026-06-22：商务部与财政部对 56 家美国实体采取措施（10 家列入出口管制管控名单，46 家禁止政府采购）— [Arnold & Porter, 2026-07](https://www.arnoldporter.com/en/perspectives/advisories/2026/07/china-imposes-export-control-and-government-procurement-restrictions-on-designated-us-companies)
- 2026-08-05：7 家美国实体列入反制清单（含 Responsible Business Alliance、Compliance Testing LLC）；对美无人机相关两用物项改为逐案审查；首次对进口打印机/复印机开展"对外贸易国家安全调查"；暂停美方机构 CCC 跟踪检查；新华社称系回应 FCC 与 DHS 限制 — [Xinhua, 2026-08-06](https://english.news.cn/20260806/70bb6afe4f49496b8a3b9f94bd30485c/c.html); [MoFo, 2026-08-21](https://www.mofo.com/resources/insights/260821-mofcom-places-the-responsible-business-alliance)
- 未发现 2026 年新增美国企业进入"不可靠实体清单"；最近一批为 2025-10-09（14 家）— [China Law Vision, 2026-08](https://www.chinalawvision.com/2026/08/compliance/chinas-counter-sanctions-measures-an-up-to-date-overview/); [Bloomberg Law](https://news.bloomberglaw.com/bankruptcy-law/china-adds-more-foreign-entities-to-unreliable-entity-list-1)

#### 1g. 芯片出口管制与中国对英伟达采购的限制
- 美方：2025-12 允许 H200 对华出口，美国政府取 25% 收益；2026 年 1 月中旬规则改为逐案审批；总量上限为美国国内出货量的 50%；单一买家上限 75,000（路透系）与 100,000（FT）两说冲突；Blackwell 仍禁 — [IAPS](https://www.iaps.ai/research/bis-licensing-policy-for-h200s); [Tech-Insider](https://tech-insider.org/nvidia-h200-chip-sales-china-2026/)
- 2026-05-14：美方批准对 10 家中国企业销售 H200 — [CNBC, 2026-05-14](https://www.cnbc.com/2026/05/14/us-clears-h200-chip-sales-to-10-china-firms-as-nvidia-ceo-looks-for-breakthrough.html)
- 中方：2026 年 1 月起仅"特殊情况"允许购买（如高校实验室），海关被要求拦截；NDRC 逐单审批，大部分配额导向香港（境外关区）；目的在保护华为等国产芯片需求 — [The Information](https://www.theinformation.com/articles/china-restricts-nvidia-chip-purchases-special-circumstances); [Tom's Hardware](https://www.tomshardware.com/pc-components/gpus/first-nvidia-h200-shipments-reach-bytedance-and-tencent-as-beijing-loosens-its-import-block)
- 2026-07-14 美贸易官员称"极少" H200 已运往中国 — [CNBC, 2026-07-14](https://www.cnbc.com/2026/07/14/nvidia-h200-ai-chips-china.html)
- 2026-08：字节、腾讯各收到约 1 万片 H200（FT 单一来源，约占 75,000 上限的 13%）— [Digitimes, 2026-08-19](https://www.digitimes.com/news/a20260819VL212/nvidia-bytedance-chips-tencent-beijing.html); [TechTimes, 2026-08-20](https://www.techtimes.com/articles/325078/20260820/nvidia-h200-chips-enter-china-13-quota-beijing-not-washington-controls-rest.htm)
- 英伟达：截至 2026-07-26 的季度对华 H200 销售不足数据中心收入 1%；为过剩 H200 库存计提约 4 亿美元 — [Bloomberg, 2026-08-26](https://www.bloomberg.com/news/articles/2026-08-26/nvidia-steps-back-into-china-market-with-first-h200-chip-sales); [SCMP](https://www.scmp.com/tech/big-tech/article/3365383/nvidia-ships-first-h200s-china-forecasts-no-data-centre-computing-revenue)

#### 1h. 台海与地区安全
- 2025-12：美国宣布约 110 亿美元对台军售（82 套 HIMARS、420 枚 ATACMS）— [NPR, 2025-12-18](https://www.npr.org/2025/12/18/nx-s1-5648080/us-arms-sales-taiwan-10-billion)
- 2025-12-29/30 "正义使命-2025"演习（2022 年以来第 6 次大规模环台演习），首日 130 架次、90 架次越过中线，演练封锁港口 — [Global Taiwan Institute, 2026-01](https://globaltaiwan.org/2026/01/pla-justice-mission-2025/)
- 约 140 亿美元对台军售包（2026-01 获国会通过）至 9 月下旬仍被搁置；代理海军部长称因伊朗战争需保留弹药（路透引述消息源否认关联）；5 月峰会后特朗普称将"作出决定" — [Al Jazeera, 2026-05-22](https://www.aljazeera.com/news/2026/5/22/us-pausing-14bn-arms-sale-to-taiwan-due-to-iran-war-navy-chief-says); [Business Standard, 2026-09-29](https://www.business-standard.com/amp/world-news/us-arms-sales-unchanged-but-14-billion-package-remains-on-hold-taiwan-126092900525_1.html); [PBS](https://www.pbs.org/newshour/world/trump-weighs-taiwan-arms-package-after-summit-aimed-at-steadying-us-china-ties)
- 2026 年 7 月下旬：赖清德讲话后，解放军在福建东山岛外进行两天实弹演习 — [SCMP](https://www.scmp.com/news/china/military/article/3361554/pla-conducts-2-days-live-fire-drills-taiwan-strait-fujian-island)
- 2026-10：台湾海巡与大陆渔船冲突引发大陆舆论愤怒，北京暂未出动海上力量 — [The Diplomat, 2026-10](https://thediplomat.com/2026/10/taiwans-maritime-law-enforcement-operation-has-sparked-anger-in-chinese-society)
- 美日"Keen Sword 27"（10/19–29）：美方拟首次在与那国岛部署先进反舰导弹系统 — [Bloomberg, 2026-10-02](https://bloomberg.com/news/articles/2026-10-02/us-may-put-missile-system-on-japan-island-near-taiwan-in-drills)
- 中日危机自 2025-11 高市早苗涉台言论起持续；2026-08 下旬日本议员访华寻求缓和，言论未撤回 — [Al Jazeera, 2026-08-24](https://www.aljazeera.com/news/2026/8/24/japanese-delegation-seeks-to-soothe-strained-ties-with-china); [Wikipedia: 2025–2026 China–Japan diplomatic crisis](https://en.wikipedia.org/wiki/2025%E2%80%932026_China%E2%80%93Japan_diplomatic_crisis)

#### 1i. 日程（已排定）
- APEC 第 33 次领导人非正式会议：2026-11-18/19 深圳（CEO 峰会 11/17–18），日期于 2025-12 公布；特朗普表示将出席（尚无白宫正式行程）；习近平预计出席 12 月迈阿密 G20 — [Shenzhen Government](https://www.sz.gov.cn/en_szgov/news/latest/content/post_12548726.html); [CGTN, 2025-12-13](https://news.cgtn.com/news/2025-12-13/2026-APEC-meeting-to-be-held-Nov-18-19-in-Shenzhen-China-1J43L2Fb2w0/index.html); [CSIS](https://www.csis.org/analysis/takeaways-trump-xi-white-house-summit)
- 美国中期选举在 11 月初（市场关注其前后中东升级风险）— [Oilprice.com](https://oilprice.com/Latest-Energy-News/World-News/Oil-Jumps-2-as-Iran-Steps-Up-Attacks-on-Hormuz-Tankers.html)

### Inferences
- 关税"水平"在 2026 年实际是**下降**的：IEEPA 20% 被 12.5% 取代；即便产能过剩 301 的 7.5% 落地，新增税也回到约 20%（≈釜山后的水平），因此关税本身不是 2026 年的新增冲击，冲击来自**不确定性**（法律基础反复切换、两个月短展期）。
- 两次国事访问的产出以"采购承诺 + 清单式管理贸易（Board of Trade）"为主，结构性议题（技术管制、稀土、补贴/产能）均未解决——符合 Dalio 框架中大国冲突的"谈判/对峙并存"阶段，而非缓和拐点。
- 技术脱钩方向正在反转主体：美方放松 H200，而中方自我限制采购以保护国产，说明中国在 AI 芯片上选择"以替代换安全"，短期牺牲算力效率。
- 中方杠杆运用更精细：避免关税报复（对 12.5% 未报复），转向实体清单、出口管制、阻断办法、国家安全调查等"非关税、可逆"工具；稀土许可制保持事实上的杠杆。
- 台海：华盛顿冻结 140 亿美元军售、两份白宫清单均不提台湾，显示美方当前优先稳定对华关系；但中日对立与美日在与那国部署导弹抬高了地区军事风险的"第二条线"。

### Gaps
- 第 232 条（钢铝、汽车/零部件、铜、木材、卡车、半导体等）对中国商品的现行税率未在本轮核实（检索配额耗尽）。
- 釜山时港口费互相暂停的具体条款、BIS 关联方规则暂停与中方 10% 反制关税是否随 9 月展期一并延至 2027-01-10，均未确认。
- 未取得 USTR/商务部原始文本（包括 9 月 30-for-30 清单税号明细）；"300% 关税威胁"细节未核实。
- PIIE/Rhodium 等对美对华平均关税的独立估算未检索。

### Cycle signal（解读，非事实）
- **中性偏顺风，短期趋稳**：关税较 2025 年低、APEC/G20 日程与贸易委员会提供"护栏"。但事件风险密集：产能过剩 301（+7.5%）、休战 2027-01-10 到期、稀土与芯片互相牵制、伊朗与台海。方向：**持平**（不是改善的拐点）。

---

## 2. 贸易：2026 年月度数据、2025 年顺差、目的地结构、出口价格（"输出通缩"）、贸易救济、经常账户

### Takeaway
2026 年美元口径出口强劲（1–7 月 +18.5%，按已引数据推算 1–8 月约 +19%；6 月 +27% 为 2021-10 以来最快；8 月 +25%），主因全球 AI 相关电子/芯片**价格**上涨与对东盟、拉美等转移；进口增速更快（1–7 月 +26.8%），故 1–8 月顺差约 8,060 亿美元，仅略高于 2025 年同期。2025 年全年顺差创纪录 1.189 万亿美元。欧盟钢铁新规（7/1 起配额削减约 47%、超配额税 50%）、EV 价格承诺、反倾销增多与美国产能过剩 301 显示贸易救济压力上升。上半年经常账户顺差 3,780 亿美元。

### Cited Findings

#### 2a. 2025 年全年（海关总署 2026-01-14 发布）
- 2025 年货物贸易顺差 1.189 万亿美元（约 +20%，2024 年为 9,920 亿美元），11 月首次累计破万亿；12 月顺差 1,141.4 亿美元、12 月出口 +6.6%（预期 +3.0%）；全年有 7 个月顺差超 1,000 亿美元 — [Yahoo/Reuters](https://finance.yahoo.com/news/chinas-trade-ends-2025-record-031557801.html); [SCMP](https://www.scmp.com/economy/economic-indicators/article/3339811/china-records-us119-trillion-trade-surplus-2025-exports-jump-55)
- 美元口径：出口 3.77 万亿美元（+5.5%），进口 2.58 万亿美元（约持平）；人民币口径：出口 26.99 万亿元（+6.1%）、进口 18.48 万亿元（+0.5%）、进出口 45.47 万亿元（+3.8%）— [SCMP](https://www.scmp.com/economy/economic-indicators/article/3339811/china-records-us119-trillion-trade-surplus-2025-exports-jump-55); [Macao News](https://macaonews.org/news/greater-china/china-2025-record-trade-surplus/)
- 2025 年对美出口下降约 30%（Macao News 归因于关税；未与海关原表核对）— [Macao News](https://macaonews.org/news/greater-china/china-2025-record-trade-surplus/)
- 数据冲突：Registration China 引 1.076 万亿美元，按笔者核算应为 1–11 月数 — [Registration China](https://www.registrationchina.com/articles/chinas-trade-surplus-hits-1-trillion-by-2025-drivers-impact-outlook/)

#### 2b. 2026 年月度（美元口径，同比；海关总署）

| 期间 | 出口 (USD bn) | 出口同比 | 进口 (USD bn) | 进口同比 | 顺差 (USD bn) | 发布日 | 来源 |
|---|---|---|---|---|---|---|---|
| 1–2 月 | 未获 | +21.8%（预期 +7.1%；人民币口径 +19.2%） | 未获 | 未获 | 未获 | 2026-03-10 | [ING](https://think.ing.com/snaps/chinas-trade-growth-starts-2026-strong-with-biggest-gain-in-four-years-a/); [gov.cn](https://english.www.gov.cn/archive/statistics/202603/10/content_WS69afb2c2c6d00ca5f9a09c60.html) |
| 3 月 | 未获 | +2.5%（低于预期） | 未获 | "四年多最大增幅"（数值未获） | 未获 | 2026-04-14 | [CNBC](https://www.cnbc.com/2026/04/14/china-trade-data-march-exports-imports-march.html); [Fortune](https://fortune.com/2026/04/14/china-march-exports-iran-war-oil-crisis/) |
| 4 月 | ≈359 | +14.1%（**冲突**：chinadata.live 称 +9.8%） | 未获 | 未获 | 未获 | 2026-05-09 | [CNBC](https://www.cnbc.com/2026/05/09/china-april-exports-rebound-strongly-after-sluggish-march.html); [chinadata.live](https://chinadata.live/insights/china-trade-april-2026-analysis/) |
| 5 月 | ≈376.8（环比 +4.9%） | +19.4% | 未获 | 未获 | 105.43 | 2026-06-09 | [GACC table](http://english.customs.gov.cn/Statics/d7718500-aa23-4590-9996-a31a8827798c.html); [CNBC](https://www.cnbc.com/2026/06/09/china-trade-exports-imports-iran-war.html) |
| 6 月 | 412.39（纪录） | +27.0%（2021-10 以来最快） | 286.76（纪录） | +36.0% | 125.62（史上第二高） | 2026-07-14 | [CNBC](https://www.cnbc.com/2026/07/14/china-june-trade-data-exports-imports.html); [Trading Economics](https://tradingeconomics.com/china/balance-of-trade/news/566591) |
| 7 月 | 397.85 | +23.9% | ≈285.35 | +27.5% | 112.5（2025-07：97.4） | 2026-08-07 | [China-Global South](https://chinaglobalsouth.com/2026/08/07/china-exports-july-2026-ai-high-tech-demand/); [SCMP](https://www.scmp.com/economy/economic-indicators/article/3363236/chinas-exports-hold-firm-july-despite-trade-and-geopolitical-headwinds) |
| 8 月 | 401.44 | +25.0%（人民币口径 +18.6%） | 282.36 | +28.2%（预期 30%） | 119.09（2025-08：101.01） | 2026-09-08 | [BNN Bloomberg/AP](https://www.bnnbloomberg.ca/business/international/2026/09/08/chinas-exports-pick-up-in-august-jumping-25-as-its-trade-surplus-widens/); [CNBC](https://www.cnbc.com/2026/09/08/china-exports-imports-august-trade-rebalance-demand-surplus-.html) |
| 1–6 月 | ≈2,120 | +17.6% | 未获 | +26.6% | 575.98（2025 同期 ≈586） | 2026-07-14 | [SCMP](https://www.scmp.com/economy/economic-indicators/article/3360451/chinas-trade-surges-june-maintaining-growth-streak-despite-global-tensions) |
| 1–7 月 | ≈2,520 | +18.5% | ≈1,840 | +26.8% | 686.4（+0.8%） | 2026-08-07 | [China-Global South](https://chinaglobalsouth.com/2026/08/07/china-exports-july-2026-ai-high-tech-demand/) |
| 1–8 月 | ≈2,921（推算） | ≈+19%（推算） | 未获 | 未获 | ≈806 | 2026-09-08 | [BNN Bloomberg/AP](https://www.bnnbloomberg.ca/business/international/2026/09/08/chinas-exports-pick-up-in-august-jumping-25-as-its-trade-surplus-widens/) |
| 9 月 | 待发布 | | | | | 2026-10-14 | — |

- 人民币口径上半年：进出口 25.47 万亿元（+16.9%，首次上半年破 25 万亿），出口 14.73 万亿元（+13.4%），进口 10.74 万亿元（+22.1%）；1–7 月进出口 30.13 万亿元（+17.3%），7 月 4.66 万亿元（+19.2%）— [Global Times, 2026-07](https://www.globaltimes.cn/page/202607/1365880.shtml); [CGTN, 2026-08-07](https://news.cgtn.com/news/2026-08-07/news-1Ppo6uZen6g/p.html)
- 上半年电子与电脑零部件合计贡献出口增长 6.9 个百分点；半导体、稀土、汽车、船舶领涨，玩具、鞋、钢材、家具拖累；比较基数低（2025 年上半年出口 +5.9%、进口 −3.9%）— [SCMP](https://www.scmp.com/economy/economic-indicators/article/3360451/chinas-trade-surges-june-maintaining-growth-streak-despite-global-tensions)
- 1–2 月：芯片 +72.6%、汽车 +67.1%、船舶 +52.8% — [ING](https://think.ing.com/snaps/chinas-trade-growth-starts-2026-strong-with-biggest-gain-in-four-years-a/)
- 3 月放缓归因于伊朗战争/霍尔木兹封锁冲击能源价格与全球需求 — [Fortune, 2026-04-14](https://fortune.com/2026/04/14/china-march-exports-iran-war-oil-crisis/); [SCMP](https://www.scmp.com/economy/china-economy/article/3349849/chinas-imports-surge-march-exports-soften-amid-hormuz-blockade)
- 7 月：集成电路出口金额 +约 117%、数量仅 +约 1.8%；集成电路进口金额 +约 71%、数量 +约 8.5%；原油进口 227.8 亿美元（−4.6%）— [China-Global South, 2026-08-07](https://chinaglobalsouth.com/2026/08/07/china-exports-july-2026-ai-high-tech-demand/)
- 8 月：半导体出口 +129.8%、汽车 +43%；Caixin 称 AI 相关涨价掩盖了实物量下降，芯片出口量约 −8% — [BNN Bloomberg/AP](https://www.bnnbloomberg.ca/business/international/2026/09/08/chinas-exports-pick-up-in-august-jumping-25-as-its-trade-surplus-widens/); [Caixin, 2026-09-08](https://www.caixinglobal.com/2026-09-08/chinas-august-exports-jump-25-on-ai-price-surge-102482780.html)
- 中国称 2026 年上半年芯片出口近翻倍至 1,770 亿美元（+96%），主要受存储涨价推动 — [Tom's Hardware](https://www.tomshardware.com/tech-industry/china-claims-chip-exports-nearly-doubled-to-177-billion-in-the-first-half-of-2026)
- 外汇局国际收支口径货物和服务贸易：8 月顺差 944 亿美元（货物 1,163 亿美元、服务逆差 218 亿美元，2026-09-29 发布）；7 月 912 亿美元（2026-08-28 发布）— [SAFE, 2026-09-29](https://www.safe.gov.cn/en/2026/0929/2456.html); [SAFE, 2026-08-28](https://www.safe.gov.cn/en/2026/0828/2448.html)
- ING（宋林）预计出口将继续快于进口、全年顺差再创纪录；Trading Economics 模型预计季末单月顺差约 910 亿美元（与 ING 观点分歧）— [BNN Bloomberg/AP](https://www.bnnbloomberg.ca/business/international/2026/09/08/chinas-exports-pick-up-in-august-jumping-25-as-its-trade-surplus-widens/); [Trading Economics](https://tradingeconomics.com/china/balance-of-trade)
- 背景：2026 年二季度 GDP 同比 4.3%，低于"4.5–5%"全年目标，为 2022 年以来最慢季度增速（国内部分由其他研究员覆盖）— [BNN Bloomberg/AP](https://www.bnnbloomberg.ca/business/international/2026/09/08/chinas-exports-pick-up-in-august-jumping-25-as-its-trade-surplus-widens/); [CNBC, 2026-07-15](https://www.cnbc.com/2026/07/15/china-gdp-retail-sales-investment-june-.html)

#### 2c. 目的地结构（"美国份额下降、东盟/拉美/非洲上升"）
- 对美出口：1–2 月 −11%；3 月 −26.5%；5 月 +35%（五年最高增速）；6 月约 +14%；8 月 425 亿美元（+34.4%，低基数），8 月对美顺差 292 亿美元 — [ING](https://think.ing.com/snaps/chinas-trade-growth-starts-2026-strong-with-biggest-gain-in-four-years-a/); [CNBC, 2026-04-14](https://www.cnbc.com/2026/04/14/china-trade-data-march-exports-imports-march.html); [CNBC, 2026-06-09](https://www.cnbc.com/2026/06/09/china-trade-exports-imports-iran-war.html); [CNBC, 2026-07-14](https://www.cnbc.com/2026/07/14/china-june-trade-data-exports-imports.html); [BNN Bloomberg/AP](https://www.bnnbloomberg.ca/business/international/2026/09/08/chinas-exports-pick-up-in-august-jumping-25-as-its-trade-surplus-widens/)
- 8 月：对东南亚 +30.2%、拉美 +17.5%、欧盟 +6.6%；3 月：欧盟 +8.6%、东盟 +6.9% — [BNN Bloomberg/AP](https://www.bnnbloomberg.ca/business/international/2026/09/08/chinas-exports-pick-up-in-august-jumping-25-as-its-trade-surplus-widens/); [CNBC, 2026-04-14](https://www.cnbc.com/2026/04/14/china-trade-data-march-exports-imports-march.html)
- 6 月对欧盟顺差创纪录 329 亿美元（+27%），对美顺差 289 亿美元（5 月 260.2 亿美元）— [CNBC, 2026-07-14](https://www.cnbc.com/2026/07/14/china-june-trade-data-exports-imports.html); [SCMP](https://www.scmp.com/economy/economic-indicators/article/3360451/chinas-trade-surges-june-maintaining-growth-streak-despite-global-tensions)
- 海关官员称 2026 年外贸"困难"，但贸易伙伴更多元、基本面稳 — [Yahoo/Reuters](https://finance.yahoo.com/news/chinas-trade-ends-2025-record-031557801.html)

#### 2d. 出口价格："输出通缩"是否仍在
- 海关出口价格指数（上年同期=100）：2026-01 为 100、2026-02 为 94.9（约 −5%）；4 月同比 +5%，为 2023 年以来最大涨幅（油价与 AI 电子带动；石油相关 +22%、化肥 +17%）；5–8 月指数未获 — [IndexBox](https://www.indexbox.io/blog/chinas-export-prices-see-steepest-rise-in-three-years-driven-by-oil-and-ai-demand/); [Trading Economics](https://tradingeconomics.com/china/export-prices)
- 出口单位价值（CEIC 贸易指数）：2026-03 为 98.8（同比约 −1.2%）— [CEIC](https://www.ceicdata.com/en/china/trade-index-yoy/trade-index-export-value)
- PricePedia（美元 FOB 价格）：7 月总商品环比 −5.5%（能源回落）；8 月总商品 −0.4%、工业品 −1.5% — [PricePedia, 2026-09-24](https://www.pricepedia.it/en/magazine/article/2026/09/24/china-economic-update-august-2026/)
- 美国 BLS：自中国进口价格 2026 年 8 月环比 +1.0%（2004 年有序列以来最大单月涨幅，电脑与电子领涨），同比 +3.0% — [BLS, Import/Export Price Indexes Aug 2026](https://www.bls.gov/news.release/ximpim.nr0.htm)
- MRB Partners（2026-05-13）：中国出口通缩今年已大幅缓解 — [MRB Partners](https://www.mrbpartners.com/build-mrbp/wp-content/public-reports/May/MRB_EM-China%E2%80%99s-Export-Prices-Losing-A-Key-Anchor-On-Global-Inflation_May-13_2026.pdf)
- Rhodium：2022–2025 年许多产品章节的单位价值大幅下跌，且这种下跌已接近极限 — [Rhodium Group](https://rhg.com/research/who-loses-from-chinas-export-gains/)
- 9 月 3 日国家发改委与市场监管总局发布认定"过低价格"的成本基准（"反内卷"）— [PricePedia, 2026-09-24](https://www.pricepedia.it/en/magazine/article/2026/09/24/china-economic-update-august-2026/)
- 数据冲突（国内价格，供国内组核对）：国家统计局 7 月 PPI 同比 +3.5%、环比 −0.7%；某博客称 −4.1% — [NBS, 2026-08-10](https://www.stats.gov.cn/english/PressRelease/202608/t20260810_1965017.html); [PrimeStrider](https://blog.primestrider.com/article/china-july-2026-ppi-slowdown-macro-analysis)

#### 2e. 贸易救济（欧盟与多边）
- 欧盟钢铁新规 2026-07-01 起取代原保障措施：免税配额削减约 47%、超配额税率由 25% 升至 50%、配额池 1,830 万吨、30 个产品类别（实施条例 2026/1457）— [CMS](https://cms.law/en/deu/legal-updates/unprecedented-eu-steel-regulation-targets-global-overcapacity); [European Commission](https://policy.trade.ec.europa.eu/enforcement-and-protection/protecting-eu-steelmaking_en); [IndexBox](https://www.indexbox.io/blog/eu-steel-market-regulation-adopted-new-quotas-and-tariffs-set-for-july-2026/)
- 欧盟 2026-02-04 对中国高压无缝钢瓶征反倾销税 — [European Commission, 2026-02-04](https://policy.trade.ec.europa.eu/news/commission-acts-against-dumped-imports-high-pressure-seamless-steel-cylinders-2026-02-04_en)
- 欧盟对华 EV 反补贴税 7.8%–35.3%（另加 10% 普通关税，2024-10-29 起）；2026-01-12 发布价格承诺指南；2026-02-10 首个价格承诺获批（大众安徽/SEAT CUPRA Tavascan，否则税负 30.7%）— [electrive, 2026-01-12](https://www.electrive.com/2026/01/12/good-bye-tariffs-eu-publishes-guidance-on-minimum-price-mechanism-with-china/); [European Commission, 2026-02-10](https://policy.trade.ec.europa.eu/news/commission-accepts-price-undertaking-chinese-electric-car-producer-2026-02-10_en)
- Bruegel 估若出口商转向价格承诺，欧盟年损关税收入约 20 亿欧元 — [Bruegel](https://www.bruegel.org/first-glance/scant-benefits-significant-risks-price-undertakings-chinese-electric-vehicles-entering)
- 商业追踪器称欧盟对华在审反倾销案件数为 2019 年以来最高（可靠性较低）— [GetSinoSource tracker](https://www.getsinosource.com/tariff-tracker)
- 中方对欧反制：欧盟白兰地自 2025-07 起最高 34.9% 反倾销税（5 年）— [GetSinoSource tracker](https://www.getsinosource.com/tariff-tracker)
- 美国主导的产能过剩联合声明（10/7，14–15 个经济体，中国未签）与 G20 贸易部长会无共识 — [MLex](https://mlex.com/mlex/trade/articles/2535402); [France 24](https://www.france24.com/en/economy/20261002-g20-trade-ministers-overcapacity-impasse-greer)

#### 2f. 经常账户
- IMF 估 2025 年中国经常账户顺差占 GDP 3.3%，为 2010 年以来最高（经 2026-01 贸易数据报道转述，原始 IMF 页面未取得）— [Yahoo/Reuters](https://finance.yahoo.com/news/chinas-trade-ends-2025-record-031557801.html)
- 2026 年二季度经常账户顺差 1,937 亿美元（2026-09-29 正式数，较 8/14 初值 1,951 亿美元下修）：货物 2,788 亿、服务 −554 亿、初次收入 −359 亿、二次收入 +63 亿；一季度 1,843 亿美元；上半年 3,780 亿美元 — [SAFE, 2026-09-29](https://www.safe.gov.cn/en/2026/0929/2458.html); [SAFE, 2026-08-14](https://www.safe.gov.cn/en/2026/0814/2442.html); [IndexBox](https://www.indexbox.io/blog/china-q2-2026-current-account-surplus-revised-down-to-1937-billion/)
- 存疑表述：检索综述称外汇局解读提到二季度"能源进口基本停止、动用库存"，与海关 7 月原油进口 227.8 亿美元（−4.6%）不一致，慎用 — [SAFE, 2026-09-29](https://www.safe.gov.cn/en/2026/0929/2458.html); [China-Global South](https://chinaglobalsouth.com/2026/08/07/china-exports-july-2026-ai-high-tech-demand/)

### Inferences
- **量价分化**：芯片出口"价翻倍、量下降"，说明 2026 年出口强劲很大部分是全球 AI/存储价格周期的价格红利，而非全面的外需扩张；若 AI 资本开支或存储价格回落，出口增速可能快速回落。
- **顺差扩张温和**：进口金额增速（价格驱动：芯片单价、油价）高于出口，1–7 月顺差仅 +0.8%；按笔者推算 1–8 月顺差约 8,060 亿美元，较 2025 年同期（约 7,820 亿美元）多约 3%。若 9–12 月与 2025 年同期（推算约 4,070 亿美元）持平，2026 全年约 1.21 万亿美元，仍为纪录。
- **对美份额**：8 月对美出口 425 亿美元 / 总出口 4,014 亿美元 ≈ 10.6%（推算，单月）；对美出口 2026 年的高增速主要是低基数与抢运（7/24 关税切换前），不改变"对美份额长期下降"的格局。
- **"输出通缩"阶段性缓解**：2026 年出口价格同比转正（4 月 +5%）、美国自华进口价格同比 +3%，主要来自油价与 AI 电子；但工业品美元价格 7–8 月重新环比下跌，"反内卷"新规显示国内低价竞争仍在——Dalio 意义上的"过剩产能外溢"并未消失，只是被价格周期遮盖。
- **保护主义扩散**：欧盟从临时保障走向长期化（50% 超配额税）、美国产能过剩 301、14–15 国联合声明，预示 2027 年中国对非美市场出口的摩擦成本上升。

### Gaps
- 1–2 月、3 月、4 月的进口与顺差数值，以及 1–8 月进口累计未获取。
- 2026 年 1–8 月对美、东盟、欧盟、非洲、拉美的**份额**未获取（仅有增速）；2025 年对美份额未获取。
- 墨西哥（2026 年对华加征）、巴西、印度、土耳其、印尼等新兴市场对华贸易救济未能检索（配额耗尽）。
- 5–8 月海关出口价格指数官方值未获取；2026 年上半年经常账户占 GDP 比重未获取。

### Cycle signal（解读，非事实）
- 外需是 2026 年中国周期的**主要顺风**（内需偏弱、二季度 GDP 4.3%），水平处于高位；但驱动高度集中于 AI/存储价格周期与转口转移，且贸易救济在扩散。方向：**高位、边际见顶**；若 9 月数据（10/14 发布）增速明显回落，将确认拐点。

---

## 3. 汇率与资本流动：USD/CNY、CFETS、中间价行为、外储与黄金、国际收支（FDI、证券投资）、出口商结汇、人民币国际化

### Takeaway
人民币 2026 年明显升值：USD/CNY 9/30 为 6.7045（美联储 H.10），10/8 约 6.7044；至 9 月中年内 +4.3%，正迈向连续第 7 个季度升值；CFETS 指数 8 月末 101.87（2025 年末 97.99），9 月下旬创 2022 年 7 月以来新高。PBOC 中间价持续明显弱于市场模型预估（数百点）——"控速不控向"。出口商结汇连续 16 个月净卖出美元，监管推动提高套保比率。9 月末外储约 3.4 万亿美元（月减 381 亿美元，估值因素）；黄金连续 23 个月增持至 7,747 万盎司。二季度直接投资净流出 70 亿美元、证券投资净流出 55 亿美元。SWIFT 人民币支付份额约 3.1%（第 5）。

### Cited Findings

#### 3a. 汇率水平与趋势
- USD/CNY：2026-09-30 为 6.7045（美联储 H.10）；2026-10-08 约 6.7044（Trading Economics，未注明在岸/离岸，过去 12 个月人民币约升值 6%）— [FRED DEXCHUS](https://fred.stlouisfed.org/series/DEXCHUS); [Trading Economics](https://tradingeconomics.com/china/currency)
- 路透：至 9 月中旬人民币年内升值 4.3%，接近四年高位 — [Investing.com/Reuters, 2026-09-14](https://www.investing.com/news/economy-news/china-urges-more-fx-hedging-as-strong-yuan-hits-exporters-sources-say-4899029)
- 9/30：人民币正迈向连续第 7 个季度升值；节前出口商结汇 — [Business Recorder/Reuters, 2026-09-30](https://www.brecorder.com/news/40441962)
- 20 个月累计升值近 9% — [IDN Financials](https://www.idnfinancials.com/news/68151/is-china-curbing-the-yuans-appreciation)
- 12 家国际投行中位预测约 6.68（发布时间不明）— [SCMP](https://www.scmp.com/economy/china-economy/article/3354323/chinas-yuan-hits-3-year-high-as-global-banks-issue-bullish-forecasts)

#### 3b. PBOC 中间价行为（中间价持续弱于模型预估 = 控速迹象；是否动用"逆周期因子"未见来源确认）
- 2026-07-10 中间价 6.7989，2023 年以来首次强于 6.80 — [Bloomberg, 2026-07-10](https://www.bloomberg.com/news/articles/2026-07-10/pboc-sets-fixing-below-6-8-per-dollar-for-first-time-since-2023-mre95kva)
- 2026-07-31 中间价 6.7894，远弱于预期，意在放缓升值（人民币当时触及三年高位）— [Bloomberg, 2026-07-31](https://www.bloomberg.com/news/articles/2026-07-31/pboc-s-weaker-daily-fixing-to-temper-yuan-gains-analysts-say)
- 8/17 中间价 6.7873（路透预估 6.7382）；9/3 为 6.7807（预估 6.7167）（Tradingpedia 页面质量较差，需核对）— [Tradingpedia, 2026-08-17](https://www.tradingpedia.com/2026/08/17/pboc-marginally-lowers-daily-yuan-fix-against-the-dollar/); [Tradingpedia, 2026-09-03](https://www.tradingpedia.com/2026/09/03/pboc-nudges-yuan-fix-stronger-against-dollar/)
- 9/30 中间价 6.7351，为 2023-02 以来最强，但比路透预估弱 326 点 — [Business Recorder/Reuters, 2026-09-30](https://www.brecorder.com/news/40441962)
- 10 月 1–8 日（国庆）期间中间价未找到。

#### 3c. CFETS 人民币汇率指数（月末，chinamoney 发布）

| 月末 | 指数 | 环比 | 发布 | 来源 |
|---|---|---|---|---|
| 2025-12 | 97.99 | — | 2026-01-05 | [CFETS](https://www.chinamoney.com.cn/english/bmkidxrud/20260105/3260816.html) |
| 2026-03 | 100.87 | +2.32% | — | [CFETS index page](https://www.chinamoney.com.cn/english/bmkidxrud/) |
| 2026-04 | 100.17 | −0.69% | 2026-05-06 | [CFETS](https://www.chinamoney.com.cn/english/bmkidxrud/20260506/3333002.html) |
| 2026-06 | 102.59 | +1.92% | 2026-07-01 | [CFETS](https://www.chinamoney.org.cn/english/bmkidxrud/20260701/3368234.html) |
| 2026-07 | 102.19 | −0.39% | 2026-08-03 | [CFETS](https://www.chinamoney.com.cn/english/bmkidxrud/20260803/3388354.html) |
| 2026-08 | 101.87 | −0.31% | 2026-09-01 | [CFETS](https://www.chinamoney.com.cn/english/bmkidxrud/20260901/3410905.html) |
| 2026-09 | **未获**（DBS 9/24 称处于 2022-07 以来最高） | — | — | [DBS, 2026-09-24](https://www.dbs.com.hk/treasures-private-client/aics/archive/templatedata/article/generic/data/en/GR/macro_strategy/092026/260924_fx.xml) |

- 2026-01-01 年度调整：美元在 CFETS 篮子中权重下调 0.6 个百分点至 18.3% — [Caixin, 2026-01-01](https://www.caixinglobal.com/2026-01-01/china-cuts-dollar-weighting-in-yuan-index-in-annual-reset-102399380.html)

#### 3d. 出口商结汇与套保
- 企业外汇净卖出连续第 16 个月（2026-08）；8 月远期锁汇降至 6 个月低点 — [Finimize](https://finimize.com/content/chinese-exporters-kept-selling-dollars-but-hedging-slipped)
- 路透 9/14：外汇局非正式要求银行推动企业提高套保，沿海出口大省目标约 40% 以上；上半年企业外汇衍生品交易约 1.4 万亿美元（+约 40%），全国套保比率 35.3% — [Investing.com/Reuters, 2026-09-14](https://www.investing.com/news/economy-news/china-urges-more-fx-hedging-as-strong-yuan-hits-exporters-sources-say-4899029)
- UBS：2026 年上半年 A 股非金融企业汇兑损失 1,070 亿元，约占净利润 5.5%（2015–2025 年均值 0.4%）— [Investing.com (UBS)](https://ng.investing.com/news/stock-market-news/chinas-ashare-exporters-face-rising-currency-losses-in-h1-2026-says-ubs-93CH-2715767)
- 4 月人民币急升令出口商出现亏损，倾向于逢美元反弹卖出 — [Bloomberg, 2026-04-22](https://www.bloomberg.com/news/articles/2026-04-22/china-exporters-beset-by-yuan-surge-look-to-sell-dollar-rallies)
- ING 将 2026 年人民币强势主要归因于出口商结汇 — [ING](https://think.ing.com/articles/cny-at-a-glance-tightening-our-forecast-band-for-2h26/)

#### 3e. 外汇储备与黄金（2026-10-07 发布）
- 9 月末外储约 3.4 万亿美元，较 8 月减少 381 亿美元（−1.11%），外汇局归因于美元指数走强与全球资产价格下跌的估值效应（精确值未获；按笔者推算 8 月末约 3.432 万亿、9 月末约 3.394 万亿美元；数字来自多篇二手报道的检索综述，未取得外汇局原文）— [BigGo Finance](https://finance.biggo.com/news/de5361b8-8fbf-4d32-947a-9df28ce9f375); [BigGo Finance](https://finance.biggo.com/news/304bf858-9886-4e9d-a807-275ee78a0680); [Kitco, 2026-10-07](https://www.kitco.com/news/article/2026-10-07/chinas-central-bank-buys-21-tonnes-gold-september-largest-monthly-purchase)
- 黄金：9 月末 7,747 万盎司（约 2,410 吨），9 月增持 74 万盎司（约 23 吨），**连续第 23 个月**增持（自 2024-11 恢复）；8 月末 7,673 万盎司；黄金储备价值由 3,501 亿美元降至 3,235 亿美元 — [BigGo Finance](https://finance.biggo.com/news/7ec1bcf4-a98b-41f3-9e92-6b875057f0db); [BigGo Finance](https://finance.biggo.com/news/304bf858-9886-4e9d-a807-275ee78a0680)
- 冲突：Kitco 称 9 月增持 21 吨、总量 2,196 吨，与盎司数不一致；对"9 月增量是否为三年最大/恢复以来最大/3 月以来最大"各源说法不一 — [Kitco, 2026-10-07](https://www.kitco.com/news/article/2026-10-07/chinas-central-bank-buys-21-tonnes-gold-september-largest-monthly-purchase)
- 内部不一致（笔者核算）：按价值/盎司推算，金价 9 月约由 4,563 降至 4,176 美元/盎司（约 −8.5%），与报道的"−6.52%"不符。

#### 3f. 国际收支：直接投资与证券投资（外汇局 2026-09-29 正式数）
- 2026 年二季度：资本和金融账户净流出 1,571 亿美元；对外直接投资 336 亿美元、来华直接投资 266 亿美元、直接投资净流出 70 亿美元；外国直接投资者新增股本投资（不含再投资收益）二季度 224 亿美元、上半年 431 亿美元；证券投资净流出 55 亿美元（对外证券投资 488 亿美元，笔者推算来华证券投资约 430 亿美元）— [SAFE, 2026-09-29](https://www.safe.gov.cn/en/2026/0929/2458.html); [SAFE, 2026-08-14](https://www.safe.gov.cn/en/2026/0814/2442.html)
- CEIC 第三方数据与外汇局表格不完全一致（如直接投资净额 −117 亿美元）— [CEIC](https://www.ceicdata.com/en/china/balance-of-payments-bpm6-quarterly/bop-fa-nonreserve-direct-investment-liability)
- 口径差异：外汇局国际收支口径 2025 年"净 FDI"765 亿美元 vs 商务部口径 1,047 亿美元；商务部 2026 年上半年实际使用外资 4,021.4 亿元（约 592 亿美元，−约 5%）— [China Briefing](https://www.china-briefing.com/news/china-fdi-h1-2026/)
- 上半年近 4,800 家外资企业增资 — [SCIO, 2026-07-23](http://english.scio.gov.cn/m/pressroom/2026-07/23/content_118614682.html)
- 2025 年末国际投资头寸：对外直接投资资产 3.58 万亿、证券投资资产 1.99 万亿；来华直接投资负债 3.98 万亿、证券投资负债 2.35 万亿美元 — [SAFE, 2026-03-27](https://www.safe.gov.cn/en/2026/0327/2405.html)
- 二手综述称上半年各类来华投资净流入 1,920 亿美元（上年同期 682 亿美元）（口径不明，慎用）— [BigGo Finance](https://finance.biggo.com/news/b98ab344-a72e-48ca-b4d5-4e01bf3f9a03)

#### 3g. 人民币国际化
- SWIFT（2026-02 起更名 Global Currency Tracker）：人民币占全球支付 3.10%，第 5 位（月份归属 6 月或 7 月各源不一）；剔除欧元区内部为 2.34%；贸易融资份额 8.43%，第 2 位（美元 79.86%）— [Trade Treasury Payments](https://tradetreasurypayments.com/articles/usd-leads-global-payments-swifts-global-currency-tracker-july-2026); [Axis Intelligence](https://axis-intelligence.com/swift-payment-statistics/)
- 序列：2025-01 为 3.79%（第 4）；2025 年中 2.88%（第 6）；2025-12 为 2.73%（第 6）；2026-01 为 3.13%（第 5）— [SWIFT RMB Tracker Jan 2026](https://www.swift.com/sites/default/files/files/rmb-tracker_january-2026.pdf); [Trade Treasury Payments](https://tradetreasurypayments.com/articles/rmb-maintains-6th-place-with-2-88-of-global-payment-share-swift-data)
- CIPS：2026-03 日均约 9,205 亿元（同比 +20%），单日纪录约 1.22 万亿元（3 月末/4 月初，日期各源不一）；5 月日均 6,740 亿元（+约 5%）— [FXC Intelligence](https://www.fxcintel.com/research/analysis/cips-volumes-may-2026)
- 2025 年 CIPS 约 844 万笔、25.55 万亿美元（加密媒体引 PBOC，可靠性一般）；大西洋理事会称过去一年日均 850–1,050 亿美元 — [CryptoRank](https://cryptorank.io/news/feed/4321e-cips-hits-7-trillion-monthly-as-china-expands-yuan-payments-beyond-swift); [Atlantic Council](https://www.atlanticcouncil.org/dispatches/inside-tehrans-toll-booth/)
- 错误数据警示：某博客称 2025 年 CIPS 2,450 亿亿（$245 万亿），约为 PBOC 口径的 10 倍，不可用 — [chinainvestors.xyz](https://chinainvestors.xyz/blog/2026-05-12-cips-vs-swift-de-dollarization/)
- 印尼允许出口商以人民币持有大宗商品出口收入（日期未核实）— [ANTARA](https://en.antaranews.com/news/416592/indonesia-allows-exporters-to-hold-yuan-for-commodity-earnings)

### Inferences
- 人民币升值的主驱动是**经常账户顺差 + 出口商结汇**（而非资本流入），且发生在美元指数 9 月反弹之时，说明人民币的强势具有内生性；PBOC 中间价持续弱于模型数百点，政策意图是"放缓而非逆转"升值。
- 升值对周期是"被动收紧"：上半年企业汇兑损失骤增，削弱出口企业利润，与国内通缩/弱需求叠加；但也降低输入性油价冲击。
- 资本账户：直接投资由净流入转为小幅净流出（二季度 −70 亿美元），FDI 新增股本仍为正但规模小；顺差主要以私人部门对外资产（及外储估值外）形式回流海外——典型"债权国"结构（Dalio）。
- 储备多元化：外储规模基本稳定而黄金持续增持（23 个月），叠加 CIPS 使用上升，与 Dalio 所描述的"新兴大国积累硬资产、减少对主导储备货币依赖"一致；但 SWIFT 支付份额约 3% 仍远低于美元/欧元，人民币距"储备货币挑战者"尚远。

### Gaps
- 9 月末外储精确值、9 月末 CFETS 指数、10 月中间价未获取。
- 外汇局银行结售汇（含企业结汇率/售汇率）8–9 月官方数据、外资持有中国债券/股票（北向、托管数据）未检索。
- 人民币在中国货物贸易结算中的占比、PBOC/CIPS 官方 2026 年上半年数据未获取。

### Cycle signal（解读，非事实）
- 外部收支维度**强且改善**（顺差、汇率、储备）；但对企业盈利与出口竞争力是**温和逆风**（升值 + 全球美元走强期间仍升值）。Dalio 储备货币维度：**缓慢改善**（黄金、CIPS），但仍处早期。

---

## 4. 科技/创新竞争力（Dalio 决定因素：创新与技术、产出竞争力）

### Takeaway
领先指标集中在"规模化部署与应用"：2025 年中国工业机器人装机约 35.4 万台，占全球 59%；中国开源大模型（DeepSeek V4 系列、Qwen、Kimi 等）在 OpenRouter 等平台的 token 份额于 2026 年 9 月中旬达 57–67%；华为昇腾据称已占中国 AI 加速器市场约一半。短板在先进制程：SMIC 5nm 良率约 20%、缺 EUV。EV/电池/光伏份额、制造业增加值份额、R&D 与专利数据本轮未能检索。

### Cited Findings
- 机器人（IFR《World Robotics 2026》，2026-09-24 发布）：2025 年中国安装约 35.4 万台（+20%），占全球 60.3 万台（+11%）的 59%（2016 年 32%、2022 年 52%、2024 年 54%）；本土品牌约 19.5 万台，占中国市场 55%（上年 57%）；美国约 3.84 万台（+12%）；全球存量约 500 万台；预计 2026 年全球约 65.5 万台 — [IFR press release (China), 2026-09-24](https://ifr.org/downloads/press_docs/EN-2026-SEP-24-IFR_Press_Release_WR-CHINA.pdf); [The Next Web](https://thenextweb.com/news/industrial-robots-world-robotics-2026-china-59-eu-falls)
- DeepSeek V4：2026-04-24 预览（V4-Pro 1.6T 总参数/49B 激活；V4-Flash 284B/13B；默认 1M 上下文；MIT 许可）— [DeepSeek API docs, 2026-04-24](https://api-docs.deepseek.com/news/news260424/)
- V4-Flash 于 2026-07-31 正式发布（晚于 7 月中旬目标），API 降价最多一半；Caixin 认为其落后于月之暗面 Kimi K3 — [Caixin, 2026-08-01](https://www.caixinglobal.com/2026-08-01/deepseek-releases-official-v4-flash-model-as-chinas-ai-race-intensifies-102470292.html)
- V4-Pro 于 2026-08-13 GA；V4.1-Flash 于 2026-09-10 发布 — [Yotta Labs](https://www.yottalabs.ai/post/deepseek-v4-release-date-specs-how-to-access-2026)
- 中国模型使用份额：2026-09-14 当周 OpenRouter token 份额 57–67%（2 月为 6–13%）；Vercel 8 月 55%（1 月 11%）— [CNBC, 2026-09-26](https://www.cnbc.com/2026/09/26/china-ai-global-adoption.html)
- Nikkei 估 2025-11 中国生成式 AI 全球份额约 15%（一年前约 1%）— [TrendForce, 2026-01-26](https://www.trendforce.com/news/2026/01/26/news-chinese-ai-models-reportedly-hit-15-global-share-in-nov-2025-fueled-by-deepseek-open-source-push/)
- 截至 2025-08 的一年中国开源模型下载量份额 17.1%，首超美国（15.86%）；Qwen 在 Hugging Face 累计下载超 7 亿、超过 Llama — [MIT Technology Review, 2026-02-12](https://www.technologyreview.com/2026/02/12/1132811/whats-next-for-chinese-open-source-ai/)
- 能力差距：Epoch AI 估中国模型落后约 7 个月（2026-01 引述）— [IEEE ComSoc tech blog, 2026-01-27](https://techblog.comsoc.org/2026/01/27/chinas-open-source-ai-models-to-capture-a-larger-share-of-2026-global-ai-market/)
- SMIC 2026 年二季度收入约 30.1 亿美元（+约 36%），首破 30 亿美元；产能利用率 93.7%；毛利率 25.3%；三季度指引收入环比 +2–4%、毛利率 26–28%；约 90% 收入来自中国 — [AnySilicon](https://anysilicon.com/news/smic-q2-2026-revenue-surpasses-3-billion-as-ai-demand-tightens-foundry-capacity/); [Investing.com transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-smic-beats-q2-2026-forecasts-on-aidriven-demand-93CH-4859626)
- 先进制程瓶颈：AEI（2026-04）估 SMIC 5nm 良率约 20%；高盛模型假设良率从 23% 升至 75%，并估到 2035 年先进逻辑自给仍有约 34% 缺口/停在约 34%（报道表述不一）— [TechTimes, 2026-08-24](https://www.techtimes.com/articles/325392/20260824/goldman-sees-china-34-short-chip-self-sufficiency-2035-smic-yield-fragile-key.htm)
- 自给率目标与基线：13 位业界高管起草的计划目标 2030 年芯片自给 80%；Nikkei 称 2024 年自给率约 33% — [TrendForce, 2026-03-31](https://www.trendforce.com/news/2026/03/31/news-china-reportedly-targets-80-chip-self-sufficiency-by-2030-eyes-domestic-7nm-line-and-14nm-production-stability/); [Techwire Asia, 2026-05](https://techwireasia.com/2026/05/china-semiconductor-self-sufficiency-wafer-target-2026/)
- AI 芯片自给：摩根士丹利称从 2023 年约 20% 升至 2026 年 41% 以上 — [Seoul Economic Daily, 2026-04-17](https://en.sedaily.com/finance/2026/04/17/chinas-ai-chip-self-sufficiency-hits-41-percent-korea-slips)
- 华为昇腾约占中国 AI 加速器市场一半、英伟达约 8%（华为内部监测/Bernstein，非独立核实）；摩根士丹利 5 月预测华为 2026 年 62%；IDC 称 2025 年约 400 万张加速卡中中国厂商约 41%（英伟达约 55%，Bernstein 称约 40%）— [Tom's Hardware](https://www.tomshardware.com/tech-industry/huawei-expects-12-billion-in-ai-chip-revenue-this-year-as-nvidias-china-market-share-hits-zero); [Huawei Central](https://www.huaweicentral.com/huawei-ascend-chips-market-share/); [CnBizInsight](https://cnbizinsight.com/inside-chinas-ai-chip-race/)
- 出口端科技含量：8 月汽车出口 +43%、半导体 +129.8%；上半年芯片出口 1,770 亿美元（+96%）— [BNN Bloomberg/AP](https://www.bnnbloomberg.ca/business/international/2026/09/08/chinas-exports-pick-up-in-august-jumping-25-as-its-trade-surplus-widens/); [Tom's Hardware](https://www.tomshardware.com/tech-industry/china-claims-chip-exports-nearly-doubled-to-177-billion-in-the-first-half-of-2026)
- 政策方向："十五五"（2026–2030）以科技自立自强与传统产业升级为核心（IFR 中国新闻稿提及）— [IFR press release (China)](https://ifr.org/downloads/press_docs/EN-2026-SEP-24-IFR_Press_Release_WR-CHINA.pdf)

### Inferences
- 中国在"把技术变成产能与应用"的环节（机器人、开源模型扩散、电子制造）优势在扩大，这正是 Dalio 框架中"创新与技术 + 产出竞争力"的上升国特征；美国仍在前沿模型能力、先进制程与 EUV/HBM 生态上领先。
- 芯片自给呈"分层"：成熟制程与 AI 卡数量上快速替代，先进逻辑（7nm 以下）在 2030 年代前仍是瓶颈；北京限制 H200 采购说明其愿以短期算力效率换取长期替代。
- 出口结构升级（芯片、汽车、船舶）同时意味着与发达经济体正面竞争加剧——将推高贸易摩擦（见第 2 节）。

### Gaps
- EV（全球销量/出口份额）、动力电池（宁德时代等，SNE Research）、光伏组件全球份额未能检索。
- 中国占全球制造业增加值（UNIDO/世界银行）份额、2025 年 R&D 经费与强度（统计公报）、WIPO PCT 2025 申请量、2026 年全球创新指数排名均未检索（配额耗尽）。

### Cycle signal（解读，非事实）
- **结构性顺风，持续改善**（机器人、AI 应用与国产替代）；对短周期的作用是通过高技术出口与设备投资支撑增长，但先进制程瓶颈与美国管制仍限制上限。

---

## 5. 人口与长期潜在增长

### Takeaway
2025 年出生 792 万（出生率 5.63‰）、死亡 1,131 万（8.04‰），自然增长率 −2.41‰，年末总人口 14.0489 亿，减少 339 万，为连续第 4 年下降；出生较 2024 年（954 万）减少 162 万；60 岁以上 3.23 亿（+1,307 万）。潜在增长率的 IMF 等权威估计本轮未能检索；IMF/世界银行对 2027 年的增长预测（4.1%/4.3%）可作中期参照。

### Cited Findings
- 国家统计局（2026-01-19 首发，2026-02-28 统计公报）：2025 年末全国人口 140,489 万人，比上年末减少 339 万；全年出生 792 万、出生率 5.63‰；死亡 1,131 万、死亡率 8.04‰；自然增长率 −2.41‰ — [国家统计局 王萍萍解读, 2026-01-19](https://www.stats.gov.cn/sj/sjjd/202601/t20260119_1962338.html); [中国教育在线, 2026-01-19](https://www.eol.cn/news/yaowen/202601/t20260119_2716530.shtml); [中国教育在线, 2026-02-28](https://news.eol.cn/yaowen/202602/t20260228_2719994.shtml)
- 出生较 2024 年 954 万减少 162 万（约 −17%），为建国以来新低；2022 年起人口连续 4 年下降 — [搜狐](https://www.sohu.com/a/1008108698_122541855); [知乎](https://zhuanlan.zhihu.com/p/1997027287506391837)
- 年龄结构：60 岁及以上 3.23 亿（+1,307 万），65 岁及以上约 2.24 亿（+342 万）；16–59 岁 8.51 亿；城镇化率 67.89%（+0.89 个百分点）— [国家统计局解读](https://www.stats.gov.cn/sj/sjjd/202601/t20260119_1962338.html); [新浪](https://news.sina.cn/gn/2026-01-19/detail-inhhuziz1397767.d.html?vt=4)
- 劳动年龄人口（16–59 岁）2025 年减少 662 万（媒体据统计局数据整理）— [网易](https://www.163.com/dy/article/KJKP28UB05210099.html)
- IMF 2026-07 WEO 更新：中国 2026 年 4.6%、2027 年 4.1%；世界银行：2026 年 4.4%、2027 年 4.3% — [IMF WEO Update July 2026](https://www.imf.org/en/publications/weo/issues/2026/07/08/world-economic-outlook-update-july-2026); [Global Times, 2026-07](https://www.globaltimes.cn/page/202607/1365486.shtml)
- IFR 指出人口结构导致的劳动力紧张推动中国工厂自动化 — [IFR press release (China)](https://ifr.org/downloads/press_docs/EN-2026-SEP-24-IFR_Press_Release_WR-CHINA.pdf)

### Inferences
- 出生断崖（792 万）+ 60 岁以上一年增加 1,300 万 → 劳动投入的拖累在 2026–2035 年加速；这会压低潜在增速并削弱国内消费吸收能力，使经济更依赖外需与投资，进而放大第 2 节的贸易摩擦——Dalio 框架中的"内部周期"与"外部秩序"在此相互强化。
- 机器人密度提升（第 4 节）是对劳动力下降的部分对冲，但只能部分抵消。

### Gaps
- IMF（Article IV 2026）、世界银行、OECD、学界对中国潜在增长率的最新估计未能检索；联合国 WPP 劳动年龄人口预测未检索。
- 劳动年龄人口的官方口径（15–64 岁）2025 年数值未获取。

### Cycle signal（解读，非事实）
- **结构性逆风，持续恶化**；对外部维度的含义是：国内吸收能力下降 → 顺差与"输出产能"倾向上升 → 外部摩擦上升。

---

## 6. 全球背景：美国经济与美联储、AI 资本开支、美元、油价与大宗、地缘（中东、俄乌）、IMF 预测

### Takeaway
2026 年全球背景由"伊朗战争油价冲击 + 美国 AI 资本开支热潮 + 美联储重新加息"主导：美联储在沃什（2026-05-22 就任主席）领导下于 **2026-09-16 加息 25bp 至 3.75–4.00%**（2023 年 7 月以来首次加息），点阵图中位数指向年内再加一次；8 月 CPI 3.4%；二季度 GDP 年化 2.2%；美元指数约 102（年内约 +4%）；布伦特约 100–105 美元/桶；伊朗战争（2/28 起）仍无停火，10 月霍尔木兹仍有袭船；俄乌无停火。IMF 7 月：全球 2026 年 3.0%（下调）、通胀 4.7%，中国 4.6%（上调）、美国 2.3%。美国四大云厂商 2026 年资本开支约 7,200–7,450 亿美元。

### Cited Findings

#### 6a. 美联储与美国经济
- 2026-09-16 FOMC：联邦基金目标区间上调 25bp 至 3.75%–4.00%，12 票全票赞成，为 2023 年 7 月以来首次加息；2026 年各月核心 PCE 均高于 3% — [CNBC, 2026-09-16](https://www.cnbc.com/2026/09/16/fed-rate-decision-september-2026.html); [Fed statement, 2026-09-16](https://www.federalreserve.gov/monetarypolicy/files/monetary20260916a1.pdf)
- 点阵图：2026 年末中位数 4.00–4.25%（再加一次），2027 年持平；18 份预测中 16 份预计年内至少再加一次；PCE 通胀回到 2% 推迟至 2029 年；沃什不提交点位 — [PNC, 2026-09-16](https://www.pnc.com/content/dam/pnc-com/pdf/aboutpnc/EconomicReports/EconomicUpdates/2026/PNC_Economics_Research_FOMC_Statement_16_September_2026.pdf); [Raisin](https://www.raisin.com/en-us/news/fed-decision-dot-plot-breakdown-september-2026/)
- 会议纪要（2026-10-07 发布）显示多数官员预期年内再加息；剩余会议 10/28、12/9；10 月加息概率一周内由 51% 降至约 19%，12 月约 70% — [Fed minutes](https://www.federalreserve.gov/monetarypolicy/fomcminutes20260916.htm); [24/7 Wall St, 2026-10-07](https://247wallst.com/investing/2026/10/07/october-rate-hike-odds-just-fell-from-51-to-19-in-one-week/)
- 沃什 2026-05-13 获参议院 54–45 确认，5-22 就任；鲍威尔留任理事；特朗普批评加息、要求利率 ≤1% — [CNBC, 2026-05-13](https://www.cnbc.com/2026/05/13/kevin-warsh-wins-senate-confirmation-as-the-next-federal-reserve-chair.html); [Bloomberg, 2026-10-01](https://www.bloomberg.com/news/articles/2026-10-01/trump-says-warsh-should-have-voted-against-fed-s-rate-hike)
- 未发现 2026 年降息的证据（加息前区间推定为 3.50–3.75%）；JPMorgan 预测 2026 年不降息 — [Yahoo Finance (JPM)](https://finance.yahoo.com/news/j-p-morgan-predicts-fed-035700750.html)
- 美国 CPI：2026 年 8 月同比 3.4%（与 7 月持平），环比 +0.4%；汽油同比 +27.4%（BLS 2026-09-11 发布）；年内峰值 4 月 4.2%（二手来源）— [USInflationCalculator](https://www.usinflationcalculator.com/inflation/us-cpi-august-2026/100073342/); [Trading Economics](https://tradingeconomics.com/united-states/inflation-cpi)
- **冲突**：同一二手来源称 8 月核心 CPI 2.4%（2021-03 以来最低），与美联储"核心 PCE 每月 >3%"的表述明显不一致，需以 BLS 原表核对 — [USInflationCalculator](https://www.usinflationcalculator.com/inflation/us-cpi-august-2026/100073342/)
- 就业：8 月失业率 4.1%、非农 +16.2 万；9 月失业率 4.2% — [BLS](https://www.bls.gov/news.Release/pdf/empsit.Pdf); [USAFacts](https://usafacts.org/answers/what-is-the-unemployment-rate/country/united-states/)
- GDP：2026 年二季度年化 2.2%（2026-09-30 第三次估计，前两次 1.5%），一季度 2.5%；消费 +3.8%；非住宅投资 +9%（AI 相关）；三季度初值 10/29 发布 — [Yahoo Finance](https://finance.yahoo.com/economy/articles/u-q2-2026-gdp-revised-123130729.html); [BEA](https://www.bea.gov/news/2026/gdp-second-estimate-and-corporate-profits-2nd-quarter-2026)

#### 6b. 美国 AI 资本开支
- 2026 年四大云厂商资本开支合计约 7,200–7,450 亿美元：亚马逊约 2,200 亿（7 月由 2,000 亿上调，主因存储涨价）、Alphabet 1,950–2,050 亿、Meta 1,300–1,450 亿、微软约 1,750 亿（日历年，因会计调整较 4 月约 1,900 亿下调）；2025 年约 4,100 亿（笔者推算增速 +76–82%）；部分卖方预计 2027 年超 1 万亿 — [Tom's Hardware](https://www.tomshardware.com/tech-industry/big-tech/big-techs-ai-spending-plans-reach-725-billion); [CNBC, 2026-07-30](https://www.cnbc.com/2026/07/30/amazon-amzn-q2-earnings-report-2026.html); [MLQ.ai](https://mlq.ai/news/big-techs-2026-capex-range-reaches-720-billion-to-745-billion/)
- IMF：科技供应链相关经济体受 AI 需求提振 — [IMF WEO Update July 2026](https://www.imf.org/en/publications/weo/issues/2026/07/08/world-economic-outlook-update-july-2026)

#### 6c. 美元
- 美元指数 2026-10-05 为 102.12；9/25 收于 100.97（年内 +2.74%）；2025 年末约 97.96（另一来源 1/2 为 98.46）→ 年内约 +3.7%–4.2%（推算）；9 月约 +2%（美联储加息后）— [usmacro](https://usmacro.com/indicator/dxy); [Portfolio Terminal](https://portfolio-terminal.com/markets/us-dollar-index); [Cambridge Currencies](https://cambridgecurrencies.com/us-dollar-index-dxy-forecast/)

#### 6d. 油价、中东与其他大宗
- 布伦特：10/8 约 102.9 美元（前收 100.2）至 105 美元以上（单日 +约 4.8%）；52 周区间约 59–126 美元；9 月初以来多在 100 美元以上，比战前高约 30 美元（主要为运费与战争风险溢价，库存偏低）— [Oilprice.com](https://oilprice.com/Latest-Energy-News/World-News/Oil-Jumps-2-as-Iran-Steps-Up-Attacks-on-Hormuz-Tankers.html); [Yahoo Finance](https://finance.yahoo.com/markets/article/oil-prices-climb-above-100-on-strait-of-hormuz-attacks-gulf-storm-threat-122612488.html); [Trading Economics](https://tradingeconomics.com/commodity/brent-crude-oil)
- 伊朗战争时间线：2/28 美以空袭开始、伊朗封锁霍尔木兹；3/19 美军打击以重开海峡；4/7–8 巴基斯坦斡旋停火；4 月中美国对伊朗港口实施海上封锁；6/17 签署结束战争协议；7/8 伊朗袭击商船、冲突恢复；9 月下旬各自与调停方接触，美方拒绝伊方条件；10/3–4 三艘油轮遇袭，10 月已有至少 9 起袭击 — [Wikipedia: 2026 Iran war](https://en.wikipedia.org/wiki/2026_Iran_war); [Wikipedia: 2026 Iran war ceasefire](https://en.wikipedia.org/wiki/2026_Iran_war_ceasefire); [CNBC, 2026-09-29](https://www.cnbc.com/2026/09/29/us-iran-war-trump-hormuz-.html); [CNBC, 2026-10-07](https://www.cnbc.com/2026/10/07/us-iran-war-trump-hormuz.html)
- 10/6 联合国秘书长在伊斯兰堡呼吁停火 — [UN News, 2026-10](https://news.un.org/en/story/2026/10/1168532)
- 胡塞武装袭击沙特拉比格炼厂，沙特首次海上炮击胡塞港口（第二个海峡风险）（据 Oilprice.com 10 月报道的检索综述，具体文章归属未能逐一核对）— [Oilprice.com](https://oilprice.com/Energy/Oil-Prices/Why-100-Oil-Is-Hard-to-Kill.html)
- 对中国的直接影响：3 月出口增速降至 +2.5%（霍尔木兹封锁）；7 月原油进口金额 −4.6% — [Fortune, 2026-04-14](https://fortune.com/2026/04/14/china-march-exports-iran-war-oil-crisis/); [China-Global South](https://chinaglobalsouth.com/2026/08/07/china-exports-july-2026-ai-high-tech-demand/)
- 黄金 9 月下跌（由 PBOC 黄金储备估值推算约 −7% 至 −8.5%，见第 3 节）；铜、铁矿石价格本轮未获取。

#### 6e. 俄乌
- 截至 10/4–5 无停火；俄方加强对基辅等城市打击，乌方称将继续打击俄炼厂；美方提议月底前举行美俄乌三方会谈（阿联酋或其他地点），乌方表示愿意 — [CNBC, 2026-10-05](https://www.cnbc.com/2026/10/05/ukraine-war-russia-kyiv-putin-zelenskyy-trump.html); [Kyiv Independent](https://kyivindependent.com/us-proposes-trilateral-talks-with-russia-ukraine-by-end-of-october-zelensky-says/); [Al Jazeera, 2026-10-04](https://www.aljazeera.com/news/2026/10/4/ukraine-ready-for-us-backed-talks-with-russia-zelenskyy)
- 2026 年仅有短暂停火（4/11 东正教复活节 32 小时；5/9–11 胜利日）；俄方要求乌军完全撤出顿巴斯 — [Wikipedia: April 2026 truce](https://en.wikipedia.org/wiki/April_2026_Russo-Ukrainian_truce); [Wikipedia: May 2026 truce](https://en.wikipedia.org/wiki/May_2026_Russo-Ukrainian_truce); [House of Commons Library](https://commonslibrary.parliament.uk/research-briefings/cbp-12198/)
- 普京计划出席 APEC 深圳，可能讨论美俄中会面（社交媒体来源，未核实）— [Visegrád 24 (X)](https://x.com/visegrad24/status/2103505895002902778)

#### 6f. IMF 预测
- IMF WEO 更新（2026-07-08）：全球 2026 年 3.0%（较 4 月 3.1% 下调 0.1）、2027 年 3.4%；全球通胀 2026 年 4.7%（2025 年 4.1%）；中国 2026 年 4.6%（4 月 4.4%）、2027 年 4.1%；美国 2026 年 2.3%、2027 年 2.2%；发达经济体 1.7%；中东局势再升级为首要下行风险 — [IMF WEO Update July 2026](https://www.imf.org/en/publications/weo/issues/2026/07/08/world-economic-outlook-update-july-2026); [IMF press briefing transcript, 2026-07-08](https://www.imf.org/en/news/articles/2026/07/08/tr070826-weo-press-briefing-transcript-july-8-2026); [Global Times, 2026-07](https://www.globaltimes.cn/page/202607/1365486.shtml)

### Inferences
- 全球处于"滞胀型后周期"：油价冲击推高通胀（IMF 2026 年全球通胀 4.7%），美联储被迫加息而非降息——与 2025 年市场预期的"宽松周期"相反；美元走强与美债利率上行收紧全球金融条件，对中国是"外部货币条件收紧 + 输入性成本上升"。
- 对中国外需的最大支撑来自美国 AI 资本开支（2026 年约 7,200–7,450 亿美元，2027 年预期更高）：它通过芯片/存储/服务器零部件价格与数量直接传导至中国出口（第 2 节）。这一支撑在 2027 年仍可能持续，但集中度高、受存储价格周期与美国企业现金流（部分已为负）约束。
- 地缘：伊朗战争使中国面临能源安全与制裁（茶壶炼厂）双重压力，但也提升中国作为调停/对话方的分量（5 月峰会共同表态）；俄乌未停火延续中俄能源绑定与西方二级制裁风险。

### Gaps
- IMF 2026 年 10 月 WEO（预计年会期间发布）的日期与数字未检索。
- 铜、铁矿石、天然气（LNG）价格与中国贸易条件（ToT）数据未获取。
- 美国核心 CPI 与核心 PCE 的口径冲突未能用 BLS/BEA 原表核实。

### Cycle signal（解读，非事实）
- **混合，边际恶化**：AI 资本开支是强顺风；但美联储加息、强美元、油价 >100 美元与霍尔木兹持续袭船构成金融与成本逆风，且 9 月以来同时加剧。对中国周期：外需"量"仍有支撑，"价/金融条件"转紧；若 10/28 或 12/9 再加息、油价继续上行，2027 年上半年外部环境将由顺风转为中性偏逆风。
