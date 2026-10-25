# China's olive-extract skincare market (油橄榄 / 橄榄苦苷 / 羟基酪醇), 2023–2026: products, claims, independent tests, suppliers, patents and regulation

**Method and limits (read first).** Research date: 2026-10-25.

What these notes build on, and what they leave out:
- They build on the earlier folder `research_notes/欧玛 橄榄叶 橄榄苦苷 全链条尽调/`, mainly `china_market_regulatory.md` and `china_filings_round2.md`.
- They do not repeat facts already established there: the CSS penalty, the CSS non-detects and the company's 0.2–0.8 mg/kg hydroxytyrosol result; 欧玛's "10%" claim; and IECIC No. 08138 / 32%. Where the product table needs one of these, it is marked "(established)".

Access limits:
- **Searches:** 16 WebSearch queries ran before the shared per-turn search budget (200 calls across all agents) ran out. Three more were refused: a CN102451235B text search, a query on 欧玛's patent and ingredient-list position, and a query for brands' CMA test reports.
- **Fetches:** every WebFetch to a Chinese host failed with `getaddrinfo ENOTFOUND`. Hosts tried: sohu.com, mztoutiao.com, plamed-extract.com, zmuni.com, patents.google.com, sina.cn, finance.sina.cn, 36kr.com, bk.cnpharm.com, tmtpost.com, cnr.cn, cirs-group.com, yesstyle.com and news.qq.com. None was retried.
- **The one full primary document:** the CN107217076B patent PDF, retrieved from patentimages.storage.googleapis.com and text-extracted locally.
- **Everything else** comes from search-result summaries. Text in 「」 is what the search tool returned. It may be the tool's own condensation rather than verified page text; I mark it "(as summarized)" where the wording is clearly the tool's. When the tool did not say which result a quote came from, I list the result set and mark it "(not disambiguated)".

Evidence tiers:
- **[OFFICIAL]** regulator or patent record
- **[3P-DB]** third-party regulatory or ingredient database, or compliance consultancy
- **[BRAND]** brand, operator, PR newswire or store copy
- **[SUPPLIER]** raw-material vendor
- **[MEDIA]** news, industry or self-media
- **[KOL]** influencer statements
- **[CONSUMER]** consumer posts

---

## 1. Which domestic and imported products sold in China lead with olive actives, and what do they claim? (product table)

### Takeaway
Sixteen brands with olive-led products surfaced: two imported (欧玛/Phyto-C and CSS 希妍萃) and fourteen domestic. Claim details could be retrieved for only four of them: CSS, 欧玛, John Jeff and 安修泽 (ONCUR).

The usual market claim is a percentage of "油橄榄叶提取物", a trade material that is often a liquid extract, rather than a marker-compound content. John Jeff's own reply shows how far apart these can be: its "7.7%" solution equals 0.5775% dry extract.

No NMPA-filed ingredient list or 功效宣称依据摘要 was retrieved for any product. The one exception is CSS, whose filed list media reported as having 油橄榄叶提取物 second, after water.

### Cited Findings

**Table A. Products with retrievable claim details.** "NF" means not found with the queries listed in Gaps.

| Brand (origin) | Product | Olive active's position in CN ingredient list | Claimed content | Claimed technology | Named raw-material supplier | Efficacy claims / 功效宣称依据摘要 | Independent tests | Price (CNY) | Controversies |
|---|---|---|---|---|---|---|---|---|---|
| **CSS 希妍萃** (US-branded; operator 上海景跃贸易有限公司) | Filed name 「希妍萃橄榄积雪草舒颜精华液」 | **2nd, after 水** (NMPA-filed list as reported by media) | 「含有较高的橄榄苦苷」 (established; found false) | NF | Brand said it bought the extract from a US company (earlier notes) | NF | Neither marker detected (大虎; 中检科 retest; another blogger's two labs; 骆王宇 team's batch tests); company's own test found HT 0.2–0.8 mg/kg (established) | NF | ¥500,000 fine (established); ¥1.5亿 KOL refund; 2025 headline 「退出中国？」 |
| **欧玛 Phyto-C** (US; operator 上海梵朵斯) | 欧玛橄榄修护精华 / O-Live Gel | No filed list found. Unofficial lists put it right after 水 (earlier notes, 可爱网) | 「10%高纯度的油橄榄叶提取物」 (established; no spec) | 「专利萃取」, pointing to US 6,743,449, which is assigned to SkinCeuticals (earlier notes) | None named (own "patent" extract) | 「敏弱肤质,修红镇定」 (brand); no 依据摘要 found | No marker test found. 「欧*油橄榄精华」 appears in 大虎's masked list; its identity and result are unconfirmed | Tmall 868–1,398 / 30 ml; JD self-operated about 920 (earlier notes) | Counterfeits; patent not brand-owned (earlier notes) |
| **John Jeff** (domestic) | 油橄榄精华液, several versions (5%, 7.7%, 10% "清爽版", "3rd gen"); English titles "For Sensitive Skin" / "For Acne-Prone Skin" | NF | Solution %: 5% → 7.7%, and 10%. Dry extract: **0.5775%** (5% and 7.7% versions), **0.75%** (10%), **1.325%** (3rd gen) | Co-developed with Hallstar | **Hallstar, Eurol®BT Gly** | Store title 「舒缓淡痘印改善泛红维稳肌肤」; no 依据摘要 found | NF | NF | 「"反向升级"误导消费者？」: a "5%→7.7%" upgrade with unchanged dry matter |
| **安修泽 ONCUR** (domestic; 缙嘉集团 院线皮肤学品牌) | 油橄榄精华 3.0 (launched April 2026); 油橄榄水乳 2.0 | NF | 「152%的橄榄苦苷浓度提升」; inhibition 「至高为单一橄榄苦苷的220%」; "40%" in a 2026 self-media title (meaning not visible) | 「L70油橄榄因子」 (橄榄苦苷 + 毛蕊花糖苷 + 羟基酪醇), 「全球首发」; PDRN复配 | Not named | 28-day human efficacy test, data presented by 叶理 (南方医科大学皮肤病医院化妆品检测中心); no report number seen | NF. 「安**」 in 大虎's list might be this brand (inference only) | NF | None found; the 2026 numbers are unverifiable |
| **Unnamed brand** (smzdm review) | Oil-skin product | NF | 「5%的Oleaxcel™（水解油橄榄叶提取）」 | Hydrolysis, which the copy says releases 橄榄苦苷 and 羟基酪醇 | Oleaxcel™ (vendor not visible) | NF | NF | NF | NF |

**Table B. Domestic brands named in a self-media 「14款热门国货油橄榄精华」 roundup.** None had claim details retrievable beyond this list.

| Group label in the post | Brands |
|---|---|
| 蹭流量党 ("riding the hype") | 百植萃, 诠润 |
| 浓度党 ("concentration") | John Jeff, 安修泽, 瑞沛, 森芝玑, 艾酸氏 |
| 复配党 ("combination formulas") | purid, 春日来信, 成分星球, 言之有物 |
| 创新党 ("innovation") | 至本, 米蓓尔, 毕生之研 |

Sources and quotes behind the tables:

- **[MEDIA/self-media] The 14-brand roundup.** The post title reads verbatim: 「14款热门国货油橄榄精华怎么选❓一次性告诉你❗️第 组：蹭流量党👉🏻百植萃&诠润第 组：浓度党👉🏻John Jeff&安修泽&瑞沛&森芝玑&艾酸氏第 组：复配党👉🏻purid&春日来信&成分星球&言之有物第 组：创新党👉🏻至本&米蓓尔&毕生之研」 (date not retrieved). — [新浪 4808949637319838](https://www.sina.cn/news/detail/4808949637319838.html)

**CSS 希妍萃**
- **[MEDIA, citing the NMPA site] Filed ingredient position:** 「国家药监局网站公开信息显示，备案名为"希妍萃橄榄积雪草舒颜精华液"的产品成分列表中，第一位为水，第二位就是"油橄榄叶提取物"」 — [速豹新闻网 2024-03-05](http://news.subaoxw.com/guonei/2024/0305/154192.html); [中国医药报 2024-08-03](https://bk.cnpharm.com/zgyyb/2024/08/03/app_317921.html) (not disambiguated)
- **[MEDIA] Public argument from the filed position:** commentators argued that, with the extract filed second, 「可以排除含量低于检出限值的情况」 (as summarized). — [网易](https://m.163.com/dy/article/ISDR3AH905118GNL.html); [36氪](https://36kr.com/p/2666173787498240); [腾讯新闻 2024-07-15](https://news.qq.com/rain/a/20240715A00OXF00) (not disambiguated)
- **[MEDIA] Filed ingredient name:** the penalty context records 「该产品备案成分为油橄榄(OLEAEUROPAEA)叶提取物」 (as summarized). — same result set, including [澎湃 实锤了！"骆王宇油橄榄事件"官方已定性](https://m.thepaper.cn/baijiahao_29559360) and [东方财富 2024-12-03](https://caifuhao.eastmoney.com/news/20241203201138929120810) (not disambiguated)
- **[BRAND] Responses:**
  - Initial response: 「品牌方回应称产品符合中国大陆法规要求，并给出售后方案」 (as summarized).
  - Later, 「CSS希妍萃分别于3月、4月在抖音和小红书等官方账号发布了两则声明,称该事件是由于资料整理和撰写的不严谨所致」.
  - Sources: [搜狐 a/760581059](https://www.sohu.com/a/760581059_121338856); [腾讯新闻 2024-07-15](https://news.qq.com/rain/a/20240715A00OXF00) (not disambiguated)
- **[MEDIA] Headlines (content not retrieved):**
  - 「博主赔偿1.5亿，品牌希妍萃却隐身了？涉事产品仍正常销售」 — [奥一网 2024-07-16](https://m.mp.oeeee.com/a/BAAFRD000020240716975589.html)
  - 「油橄榄事件"主角"退出中国？」, page tags 品牌 / 骆王宇 / 景跃, date not retrieved — [搜狐 a/915150904](https://m.sohu.com/a/915150904_329832)

**欧玛 (established in earlier notes; restated for the table only)**
- **[BRAND] Price and claims:** Tmall prices and the 「添加了10%高纯度的油橄榄叶提取物」 copy — [smzdm p/107779377](https://www.smzdm.com/p/107779377/); [smzdm p/98574502](https://www.smzdm.com/p/98574502/); [京东搜索](https://list.jd.com/Search?enc=utf-8&keyword=%E6%AC%A7%E7%8E%9B%E6%A9%84%E6%A6%84%E7%B2%BE%E5%8D%8E&spm=2.1.5)
- **[MEDIA] A reviewer's opinion, not brand data:** 「它们家是有自己专利的，主要是针对咱们上面说的橄榄苦苷这一活性物质进行一系列优化」 — [澎湃号 "油橄榄"爆火…应该怎么选？](https://www.thepaper.cn/newsDetail_forward_15620543); [知乎 p/439569623](https://zhuanlan.zhihu.com/p/439569623) (not disambiguated)

**John Jeff**
- **[BRAND, English retailer copy] Supplier:** 「Cooperated with U.S. HALLSTAR Beauty to develop a natural olive leaf extract active ingredient - Eurol®BT Gly.」 Two variant titles: "Olive Oil Serum (For Sensitive Skin)" and "(For Acne-Prone Skin)". — [YesStyle acne-prone](https://www.yesstyle.com/en/john-jeff-olive-oil-serum-for-acne-prone-skin-15ml/info.html/pid.1133599739); [YesStyle sensitive](https://www.yesstyle.com/en/john-jeff-olive-oil-serum-for-sensitive-skin-15ml/info.html/pid.1133599736)
- **[MEDIA] The 10% version and the crowded market:**
  - 「John Jeff与美国Hallstar合作开发10%浓度的清爽版原料」, which reportedly 「上市几个月卖出数万支」 (as summarized).
  - 「油橄榄精华当时竞争很多，不少产品原料相近，肤感也常被诟病」 (as summarized).
  - Source: [澎湃号 这9个技术流的"国货之光"](https://m.thepaper.cn/baijiahao_16597930) (probable)
- **[MEDIA + BRAND reply] The "upgrade" controversy:**
  - 「油橄榄精华液（原5%浓度版本）近期升级，油橄榄叶提取物溶液的浓度宣称由5%提升至7.7%」.
  - 「品牌回应称，原5%版本和现7.7%版本的油橄榄叶提取物干料浓度均为0.5775%，10%版本干料浓度为0.75%」 (as summarized).
  - Headline: 「"原料桶"难做，John Jeff"反向升级"误导消费者？」
  - Sources: [风闻](https://user.guancha.cn/main/content?id=752096&s=fwzwyzzwzbt); [知乎 p/507109152](https://zhuanlan.zhihu.com/p/507109152)
- **[MEDIA] Third generation:** launched in May, according to an article the tool dated about four years old (so roughly 2022). It raised dry extract 「从0.75%提高到1.325%」 (as summarized), and an English page states "1.325% olive leaf extract". — [知乎 爆品扒皮 p/533107542](https://zhuanlan.zhihu.com/p/533107542); [YesStyle](https://www.yesstyle.com/en/john-jeff-olive-oil-serum-for-acne-prone-skin-15ml/info.html/pid.1133599739) (probable)
- **[BRAND, store title]** 「John Jeff 油橄榄精华液 舒缓淡痘印改善泛红维稳肌肤」 — [识货](https://m.shihuo.cn/page/goodsDetail/1471459?goodsId=1471459&skuId=3345387510&styleId=46265452&fromSource=renrenapp.com)
- **[SUPPLIER] Hallstar's Eurol BT (from earlier notes, `skin_delivery_stability.md`):**
  - INCI: Olea Europaea (Olive) Leaf Extract, Water.
  - Recommended use: 0.5–1% as an anti-irritant, 0.1–0.5% as an antioxidant.
  - Oleuropein content: not found.
  - Sources: [Hallstar Beauty page](https://dev.hallstarbeauty.com/?p=490); [CosDNA](https://www.cosdna.com/chs/supplier/product_7b7a9218.html)

**安修泽 (ONCUR)**
- **[BRAND/PR] April 2026 launch:** 「缙嘉集团旗下院线皮肤学品牌ONCUR安修泽在上海研发中心举办」 the launch of 油橄榄精华3.0 and 「L70油橄榄因子」. — [央广网 2026-04-15](https://www.cnr.cn/mspd/jrhm/20260415/t20260415_527585997.shtml); [钛媒体](https://www.tmtpost.com/7953941.html); [中国商业品牌网 2026-04-20](https://m.chinapp.net.cn/pinpairenwu/2026/0420/16396.html)
- **[BRAND/PR] Numeric claims:**
  - The three actives (橄榄苦苷、毛蕊花糖苷、羟基酪醇) together inhibit inflammatory factors 「至高为单一橄榄苦苷的220%」.
  - One article claims 「152%的橄榄苦苷浓度提升」; another gives no figure.
  - 「高浓度橄榄苦苷与自修型PDRN复配」 (as summarized).
  - Sources: [新浪 安修泽油橄榄精华升级](https://www.sina.cn/news/detail/5287321756500677.html); [新浪 安修泽油橄榄精华3.0升级](https://www.sina.cn/news/detail/5287365753179005.html); [央广网](https://www.cnr.cn/mspd/jrhm/20260415/t20260415_527585997.shtml) (not disambiguated)
- **[BRAND/PR] Human test:** 「南方医科大学皮肤病医院化妆品检测中心常务副主任叶理教授现场公布了人体功效测试数据」, and the product 「通过专业检测机构28天人体功效测试」 (as summarized). No report number, method or full data was visible. — same result set
- **[MEDIA/self-media, 2026] Unverifiable figures:**
  - Title: 「2026油橄榄祛痘精华对比测评：安修泽40% vs 理肤泉/修丽可/露得清/雅漾」.
  - It cites 「IRB批准，双盲随机对照，n=150」 and 「油脂下降34%、毛孔面积缩小7.14%」, with no verifiable source.
  - Source: [搜狐 a/1092163011](https://www.sohu.com/a/1092163011_121081803)
- **[MEDIA] 水乳2.0:** promoted with 「L70油橄榄因子包含橄榄苦苷、毛蕊花糖苷、羟基酪醇三大成分」 (as summarized). — [今日头条 油敏肌本命水乳红榜](https://www.toutiao.com/w/7631562739474907698)

**Other products and market framing**
- **[MEDIA] Oleaxcel product (brand not visible in the snippet):** 「整个配方最大的亮点在于5%的Oleaxcel™（水解油橄榄叶提取），将油橄榄叶中功效性较强的诸如橄榄苦苷、羟基酪醇等多个活性成分分解出来」 — [什么值得买 夏日油皮护理与产品选择VOL.07](https://post.smzdm.com/p/axz5nxod/)
- **[CONSUMER]** 「空瓶言之有物油橄榄VC精华，有效肤感好～」 — [55海淘 336924](https://m.55haitao.com/show/336924/)
- **[MEDIA] An unnamed 2026 product** claimed its 「核心成分浓度是上一代的10倍」 (as summarized). — result set for "油橄榄精华检测发布 橄榄苦苷 含量 2026" (not disambiguated)
- **[MEDIA] Industry-media framing (titles only, dates not retrieved):**
  - 「油橄榄，需要一把火」 — [界面新闻 8424857](https://www.jiemian.com/article/8424857.html)
  - 「青刺果VS油橄榄，谁是下一个爆款？」 — [界面新闻 8838393](https://www.jiemian.com/article/8838393.html)
- **[MEDIA, citing supplier data]** 「1%的油橄榄提取物，7天对油痘肌的泛红、油脂分泌有改善」 (as summarized). — [澎湃号](https://www.thepaper.cn/newsDetail_forward_15620543)

### Inferences
- **The headline numbers cannot be compared.** 欧玛's "10%", John Jeff's "5%/7.7%/10%" and "5% Oleaxcel" are percentages of a trade material. John Jeff's own reply shows a 7.7% "solution" is 0.5775% dry extract, about 13× less.
- **John Jeff's labels are probably solution percentages.** Hallstar's Eurol BT is a water-carrier extract recommended at 0.1–1%, so John Jeff's 5–10% labels are 5–100× above Hallstar's recommended range. That fits a solution-percentage reading. Whether "Eurol BT Gly" is a glycerin variant of Eurol BT is not confirmed.
- **安修泽's claims cannot be checked.** The 152% and 220% figures are relative and come with no absolute baseline. The test presenter is named, but no report or data was published that could be verified.
- **The two kinds of brand tell their story differently.** Both imported leaders (欧玛, CSS) lean on a US-origin or "patent" story. Domestic leaders lean on named imported suppliers (Hallstar), proprietary "因子" complexes and percentage escalation (5% → 7.7% → 10%; "10倍"; "152%").

### Gaps
- **Prices:** none found except 欧玛'. CSS, John Jeff, 安修泽 and the 14-list brands were not priced.
- **Filings:** no NMPA filing number, filed ingredient order, efficacy category or 功效宣称依据摘要 was found for any product except CSS's position. The NMPA platform and 美丽修行 are not reachable or indexed (see the earlier notes).
- **12 of the 14 domestic brands:** no claim details found (百植萃, 诠润, 瑞沛, 森芝玑, 艾酸氏, purid, 春日来信, 成分星球, 言之有物, 至本, 米蓓尔, 毕生之研). The search budget ran out before brand-specific queries.
- **Imported products:** no olive-led import beyond 欧玛 and CSS was identified. The 2026 Sohu piece names 理肤泉, 修丽可, 露得清 and 雅漾 only as comparators; whether those products contain olive actives was not determined.
- **No market-size or sales data** was found for the category.
- **Queries run:**
  - 「油橄榄 精华 新品 品牌 2023 羟基酪醇 青眼」
  - 「"油橄榄" 赛道 国货 品牌 精华 橄榄苦苷 聚美丽」
  - 「羟基酪醇 精华液 品牌 化妆品 宣称 浓度」
  - 「安修泽 油橄榄精华 L70 橄榄苦苷 检测报告」
  - 「John Jeff 油橄榄精华 Hallstar 橄榄苦苷 含量」
  - 「欧玛 油橄榄精华 10%油橄榄叶提取物 橄榄苦苷」
- **Refused (budget):** a 欧玛 patent and ingredient-position query.

---

## 2. The February 2024 「大虎课代表」 test of six 油橄榄精华 (product list, measured values, 中检科 retest) and later tests

### Takeaway
The six products are reported only in masked form: 「A***、希**、欧*、安**、朴*、神***」 油橄榄精华. Only 希** (CSS 希妍萃) is named in coverage.

No snippet gave any per-product number for oleuropein or hydroxytyrosol. Coverage says only that four products were 「含量都不高」 and that CSS showed neither marker.

Retest and follow-ups:
- 大虎 sent all products to **中检科（北京）化妆品技术有限公司** (under the Chinese Academy of Inspection and Quarantine) for a retest, with 「结果相同」.
- An unnamed blogger had CSS tested at two labs, in Shanghai and Guangzhou (March 2024): neither marker detected.
- 骆王宇's team had all CSS batches made between 2022 and early 2024 tested: no oleuropein.

No numeric test by 美丽修行, Xiaohongshu testers or a media lab was found.

### Cited Findings
- **[MEDIA] Date anchor:** 「抖音美妆一哥又"翻车"了」, 2024-02-27. — [手机新浪网 2024-02-27](https://finance.sina.cn/2024-02-27/detail-inaknhxm3442100.d.html)
- **[MEDIA] Masked list and results:**
  - The tool summarized the list as 「A***油橄榄精华、希**油橄榄精华、欧*油橄榄精华、安**油橄榄精华、朴*油橄榄精华、神***油橄榄精华」, noting that names in the sources are mostly masked.
  - 「其中美国护肤品牌希妍萃未检出羟基酪醇和橄榄苦苷」, and 「其中4款橄榄苦苷、羟基醇的含量都不高」 (snippet text; 「羟基醇」 is as written).
  - Sources (not disambiguated): [搜狐 a/760581059 这个化妆品被测评博主"锤"了！](https://www.sohu.com/a/760581059_121338856); [手机新浪网 2024-02-27](https://finance.sina.cn/2024-02-27/detail-inaknhxm3442100.d.html); [速豹新闻网 2024-03-05](http://news.subaoxw.com/guonei/2024/0305/154192.html); [美妆头条 美业开年第一大瓜！油橄榄里"没橄榄"](https://www.mztoutiao.com/index/index/wenzhang.html?id=3041)
- **[MEDIA] Source conflicts:**
  - Outlets differ on the count: 「有的写为6款，也有写为7款，名单亦略有差异」 (as summarized). — same result set
  - Two tool summaries dated the test 「2023年初」 and 「2026年初」. Both conflict with the dated 2024-02-27 report and the 2024 coverage, so they are treated here as tool errors.
- **[MEDIA] The 中检科 retest:** 「他又将上述所有产品送至隶属于中国检验检疫科学研究院的中检科（北京）化妆品技术有限公司进行了复检，而结果相同。」 — result set including [搜狐 a/760581059](https://www.sohu.com/a/760581059_121338856) and [新京报 2024-12-08](https://m.bjnews.com.cn/detail/1733647882168430.html) (not disambiguated)
- **[MEDIA] Second blogger, two labs:**
  - 「另有护肤博主在今年3月购买了CSS油橄榄精华，并分别送去了上海和广州的两家实验室检测，结果同样未检出这两种成分」.
  - 「两个实验室的检测结果都是未在样品中检测到羟基酪醇和橄榄苦苷」.
  - Sources: [知乎 646339571](https://www.zhihu.com/question/646339571); [奥一网 2024-07-15](https://m.mp.oeeee.com/a/BAAFRD000020240715975097.html) (not disambiguated)
- **[KOL] 骆王宇's position:**
  - 「油橄榄叶提取物是一个成分组，其中并非只含有橄榄苦苷和羟基酪醇」.
  - 「中国化妆品已备案的原料是油橄榄叶提取物,而不是橄榄苦苷和羟基酪醇」.
  - He 「于25日发布澄清视频(现已删除)」.
  - He also argued that 油橄榄提取物 has 「十几种活性成分」 (as summarized).
  - Sources: [腾讯新闻 2024-07-15](https://news.qq.com/rain/a/20240715A00OXF00); [36氪](https://36kr.com/p/2666173787498240); [网易](https://m.163.com/dy/article/ISDR3AH905118GNL.html) (not disambiguated)
- **[KOL] 骆王宇's batch testing:** 「其团队委托同一家检测机构,对2022年至2024年初生产的CSS油橄榄精华所有批次产品进行检验」. The result reported was no oleuropein in any batch (as summarized). — same result set
- **[KOL] 大虎's counter:** 「该品牌在官方平台明确宣传含有较高橄榄苦苷，未检出就存在虚假宣传的嫌疑」 (as summarized). The opposing argument was that 「以橄榄苦苷、羟基酪醇两种成分以及浓度来判断是否是油橄榄提取物是个人标准」. — [知乎 646339571](https://www.zhihu.com/question/646339571) and result set (not disambiguated)
- **[MEDIA] Industry views:**
  - One industry source: 「可以认定产品中没有添加油橄榄叶提取物或者添加量很小，小到检测不到。」
  - Others cited 「量不足…检测方法不统一、质量不达标，或者失活了」 (as summarized).
  - Sources: [速豹新闻网](http://news.subaoxw.com/guonei/2024/0305/154192.html); [中国医药报 2024-08-03](https://bk.cnpharm.com/zgyyb/2024/08/03/app_317921.html) (not disambiguated)
- **[KOL/MEDIA] Refund and exit:** 「其个人将和合作机构共同为在其账号购买了"CSS油橄榄精华"的用户退款,涉及金额达1.5亿元」 (July 2024), followed by his announced 退网. — [腾讯新闻 2024-07-15](https://news.qq.com/rain/a/20240715A00OXF00); [奥一网 2024-07-15](https://m.mp.oeeee.com/a/BAAFRD000020240715975097.html)
- **[MEDIA] Possible 2026 test (title only):** a 新浪 item titled 「油橄榄精华检测发布」 surfaced among 2026 安修泽 results. Its content, products, lab and values were not retrievable. — [新浪 5290598879465045](https://www.sina.cn/news/detail/5290598879465045.html)

### Inferences
- **One product is unaccounted for.** Six products minus CSS (none detected) and four "not high" leaves one product described neither way. It was presumably the highest-content one, but its identity and values were not found.
- **Possible identities for the masked names (unconfirmed):**
  - 希** = 希妍萃 is confirmed by coverage.
  - By character count, 欧* fits 欧玛 and 安** fits 安修泽; both appear in this research as 油橄榄精华 brands.
  - A***, 朴* and 神*** are unidentified.
- **What the retest result means.** 「结果相同」 for the 中检科 retest most likely means the same qualitative pattern (CSS none, others low). It does not show that the numbers matched.
- **The repeated non-detects are consistent.** They span 大虎's lab, 中检科, two labs in Shanghai and Guangzhou, and 骆王宇's own batch tests of 2022 to early 2024. Combined with the company's own 0.2–0.8 mg/kg hydroxytyrosol result (established), the evidence points to marker levels at or near detection limits, not to a lab artifact.

### Gaps
- **Missing details of the test itself:** per-product oleuropein and hydroxytyrosol values and units for all six; the first lab's name; method and LOD; the 中检科 report number and whether it carries CMA/CNAS marks; the identities of A***, 朴*, 神*** (and confirmation of 欧*, 安**); and the seventh product, if there was one.
- **No later tests found:** no 美丽修行, 小红书, 青眼 or media-lab tests with numbers. The 2026 「油橄榄精华检测发布」 page was not retrievable.
- **Queries run:**
  - 「大虎课代表 油橄榄精华 检测 橄榄苦苷 羟基酪醇」
  - 「油橄榄精华 检测 中检科 橄榄苦苷 未检出」
  - 「大虎课代表 送检 6款 油橄榄精华 名单 结果」
  - 「骆王宇 希妍萃 检测报告 回应 油橄榄 成分组」
  - 「油橄榄精华 测评 橄榄苦苷 含量 mg/kg 送检 博主」
  - 「油橄榄精华检测发布 橄榄苦苷 含量 2026」
- **Fetches that failed (DNS):** sohu.com, mztoutiao.com, 36kr.com, finance.sina.cn, sina.cn, news.qq.com.

---

## 3. Which brands publish finished-product active content or third-party test reports (e.g., CMA/CNAS HPLC)?

### Takeaway
None was found. No brand in China was seen publishing finished-product oleuropein or hydroxytyrosol content from a CMA/CNAS laboratory. The nearest cases:
- **John Jeff** disclosed dry-extract percentages for the ingredient, not marker content, and only after it was challenged.
- **安修泽** names a human-efficacy test presenter and institution, but publishes only relative content claims and no report.
- **CSS** produced a test only in the enforcement context (established). The penalty decision recorded that the company could not provide an oleuropein test report.

### Cited Findings
- **[BRAND reply via MEDIA] John Jeff:** dry extract 「均为0.5775%」 for the 5% and 7.7% versions and 0.75% for the 10% version; later 1.325% for the 3rd generation (as summarized). — [风闻](https://user.guancha.cn/main/content?id=752096&s=fwzwyzzwzbt); [知乎 p/507109152](https://zhuanlan.zhihu.com/p/507109152); [知乎 p/533107542](https://zhuanlan.zhihu.com/p/533107542)
- **[BRAND/PR] 安修泽:**
  - Claims: 「152%的橄榄苦苷浓度提升」 and 「220%」.
  - Test: 「叶理教授现场公布了人体功效测试数据」 and 「28天人体功效测试」.
  - No report number, method or data was visible in any snippet.
  - Sources: [央广网 2026-04-15](https://www.cnr.cn/mspd/jrhm/20260415/t20260415_527585997.shtml); [钛媒体](https://www.tmtpost.com/7953941.html)
- **[OFFICIAL-reported] CSS:** 「处罚决定书显示其未能提供橄榄苦苷的检测报告」. — [新京报 2024-12-08](https://m.bjnews.com.cn/detail/1733647882168430.html)
- **[OFFICIAL – patent record, as a reference method] Simultaneous HPLC for both markers.** CN107217076B (§4) publishes a method that measures oleuropein and hydroxytyrosol together:
  - 「色谱仪：安捷伦高效液相色谱仪1260；色谱柱：ZORBAX Eclipse，XDB-C18 (250×4.6mm, 5μm)；检测器：紫外检测，波长230nm；流动相：100％甲醇和0.2％磷酸水溶液」.
  - Calibration used Sigma standards, with R² of 0.9999 and 0.9998.
  - Source: [CN107217076B PDF](https://patentimages.storage.googleapis.com/9a/d8/2b/bec891cb369b58/CN107217076B.pdf)

### Inferences
- **The market discloses at the wrong level.** Disclosure stops at the ingredient level (percentage of a trade material), which says nothing about how much marker compound a product contains. The CSS case shows regulators act on unsubstantiated marker claims (「含有较高的橄榄苦苷」). That gives brands a reason either to publish HPLC data or to avoid marker claims. The pattern found here is mostly avoidance plus relative claims.
- **A published method already exists.** A simultaneous oleuropein and hydroxytyrosol HPLC-UV method is in the public patent record, so "there is no standard method" (a point both sides of the CSS dispute made) does not stop a brand from commissioning and publishing a validated test. The absence of a 国家标准 does not mean testing is impossible.

### Gaps
- **Unknown:** whether 欧玛, 安修泽, John Jeff or any 14-list brand has ever posted a CMA/CNAS finished-product report on WeChat, Xiaohongshu or Tmall detail pages. These platforms are not indexed by the search tool, and the query 「油橄榄精华 公布 第三方检测报告 CMA 橄榄苦苷 含量 品牌 回应 大虎」 was refused (budget).
- **No 功效宣称依据摘要** (the NMPA-published efficacy summary) was retrieved for any product.

---

## 4. Chinese ingredient suppliers and their olive leaf / hydroxytyrosol materials, and the Chinese patents brands cite

### Takeaway
**Supplier with a published spec:** **PCR® 油橄榄叶提取物** (plamed-extract.com):
- 40% 橄榄苦甙, product code PMQH02
- leaf from 陇南, combined with 羟丙基环糊精
- water-soluble, positioned for 抗炎祛红

**Suppliers with listing pages only:**
- Olive leaf extract / oleuropein / hydroxytyrosol: 西安尚诚, 彬州森荣, 湖北常奥 and hm-herb.com.
- Hydroxytyrosol: 云南西力, 中山迪欣 and 上海吉至, plus 南京腾象 under a 「生物合成系列」 category.
- New-ingredient filers for hydroxytyrosol (filed as 二羟基苯乙醇): 杭州唯铂莱 and 浙江熙正霖 (§5).
- Imported materials named by brands: Hallstar's Eurol®BT Gly (John Jeff) and Oleaxcel™.

**Patents:**
- **CN107217076B** belongs to **南京林业大学** and covers *converting* oleuropein into hydroxytyrosol (enzyme + heat). Its "81.04%" figure is a **prior-art citation** of another group's oleuropein substrate (原姣姣等), not the patent's own material.
- **CN102451235B** (from earlier notes) is a macroporous-resin oleuropein process: more than 55%, and about 90% or more with an added column. Its assignee was not retrieved.
- No source showed which brands cite either patent.

### Cited Findings

**Suppliers**
- **[SUPPLIER] PCR® 油橄榄叶提取物:**
  - Specification: 活性含量为40%橄榄苦甙, 产品编号PMQH02 (as summarized).
  - 「PCR®油橄榄叶提取物主要成分组成为油橄榄叶提取物（产自陇南地区）和羟丙基环糊精」.
  - Positioned as 「具有抗炎祛红功效的水溶性化妆品原料」 (as summarized).
  - The search tool could not tie the name 「绿天」 to this page, so the brief's 绿天 attribution was not independently confirmed here.
  - Source: [plamed-extract.com PCR®油橄榄叶提取物](http://www.plamed-extract.com/product/pcr-olea-europaea-leaf-extract/)
- **[SUPPLIER] Other olive leaf / oleuropein listings (titles or claims only):**
  - 「橄榄叶提取物|橄榄苦甙|羟基酪醇|植物提取物化妆品原料|西安尚诚生物科技有限公司」 — [尚诚](https://www.shangchengbio.com/oleuropein)
  - 「橄榄叶提取物 - 彬州森荣生物科技有限公司」 — [森荣](https://www.bingzhoushengwu.com/product/details/9/11/77.html)
  - 「橄榄苦苷 32619-42-4 量大优惠 厂家直销-湖北常奥药业有限公司」 — [常奥](http://www.hbchangao.com/products/show25291515.html)
  - hm-herb.com's 橄榄苦甙 page claims 「高含量的橄榄苦甙主要用于护肤品，可以保护皮肤细胞不受紫外线的伤害」 — [hm-herb](http://www.hm-herb.com/product_detail/id/1.html)
- **[3P-DB] Commercial grades:** 「橄榄提取物，橄榄苦甙，规格有10%、20%、40%等」 (as summarized). — [ChemicalBook](https://m.chemicalbook.com/ProductChemicalPropertiesCB4950923.htm)
- **[SUPPLIER/3P-DB] Hydroxytyrosol listings:**
  - 云南西力生物技术股份有限公司 — [化源网 7480348](https://www.chemsrc.com/Product/7480348.html)
  - 中山市迪欣化工有限公司 — [化源网 5371735](https://www.chemsrc.com/Product/5371735.html)
  - 上海吉至生化科技有限公司 — [化源网 4035607](https://www.chemsrc.com/Product/4035607.html)
  - 「羟基酪醇_生物合成系列_产品展示_南京腾象进出口贸易有限公司」 — [腾象](https://www.jinxiangchem.com/biological/108.html)
- **[SUPPLIER/3P] Caution on vendor content:** the search tool flagged a Baidu B2B wiki article (「羟基酪醇解密」) as vendor content with exaggerated efficacy claims. — [b2bwiki.baidu.com](https://b2bwiki.baidu.com/article/d1hsuc9ftjstcns13gh0)

**Patent CN107217076B** (primary document, text extracted)
- **[OFFICIAL – patent] Bibliographic data:**
  - 「(10)授权公告号 CN 107217076 B」; 「(45)授权公告日 2020.03.24」; 「(21)申请号 201710358546.8」; 「(22)申请日 2017.05.19」; 「申请公布号 CN 107217076 A」 / 「(43)申请公布日 2017.09.29」.
  - 「(73)专利权人 南京林业大学」; 「(72)发明人 余世袁 刘敏 勇强 连之娜 朱均均」.
  - 「(54)发明名称 一种酶催化与高温水解相结合的制备羟基酪醇的方法」.
  - Source: [CN107217076B PDF](https://patentimages.storage.googleapis.com/9a/d8/2b/bec891cb369b58/CN107217076B.pdf)
- **[OFFICIAL – patent] Claim 1:** 「先以富含β-葡萄糖苷酶的纤维素酶对橄榄苦苷进行酶解反应，然后不经处理直接控温80-100℃继续水解24h以上，获得橄榄苦苷的降解率95%以上，羟基酪醇的得率80%以上的羟基酪醇溶液」. The enzyme is 「Novozyme」, used at 「10-60FPU/g橄榄苦苷」 at 50 °C and pH 4.8 for 1–12 h. — same PDF
- **[OFFICIAL – patent] Where the "81.04%" comes from (background section, [0004]):** 「原姣姣等研究了橄榄苦苷(含量81.04％)半纤维素酶解制备羟基酪醇，得到橄榄苦苷的降解率为98.54％，羟基酪醇含量为11.31％(羟基酪醇的得率相当于40.31％)」.
  - The same paragraph cites CN104926615A: 「橄榄苦苷(含量38.6％)的降解率为85.28％，羟基酪醇的含量为6.07％」.
  - Source: same PDF
- **[OFFICIAL – patent] The patent's own examples:** HPLC on oleuropein solutions of 5.0–12.5 g/L gives 「橄榄苦苷的降解率为100％」, with hydroxytyrosol yields of 88.90% (2.53 g/L), 83.89% (2.99 g/L), 82.38% (2.35 g/L), 83.32% (2.37 g/L) and 84.54% (1.20 g/L). Yield is defined against the theoretical factor 「154/540＝0.285g」. — same PDF
- **[OFFICIAL – patent] An internal inconsistency:** paragraph [0008] states 「橄榄苦苷的浓度28-50g/L」, while claim 2 states 「橄榄苦苷的含量7.0-12.5g/L」. — same PDF
- **[OFFICIAL – patent] Background on raw material:**
  - 「油橄榄叶中橄榄苦苷的含量可以达到10-17％」.
  - 「我国每年因对油橄榄树进行维护剪枝产生的叶子多达60万吨」.
  - Source: same PDF

**Patent CN102451235B and others**
- **[OFFICIAL – patent, via earlier notes] CN102451235B:** a macroporous-resin process giving more than 55% oleuropein, and about 90% or more with an added column step. — [CN102451235B (Google Patents)](https://patents.google.com/patent/CN102451235B/en), as recorded in `raw_material_chemistry.md`. This session's query 「CN102451235B 橄榄 专利」 returned no record of it.
- **[OFFICIAL – patent titles only] Other Chinese olive patents that surfaced:**
  - CN111303236B 「从油橄榄叶中同时提取分离山楂酸、橄榄苦苷、齐墩果酸的方法」 — [Google Patents](https://patents.google.com/patent/CN111303236B/zh)
  - CN109021042B "Method for extracting high-purity oleuropein from olive leaves" — [Google Patents](https://patents.google.com/patent/CN109021042B/en)
  - CN105997703B 「橄榄叶提取物以及包含该提取物的化妆品」 — [Google Patents](https://patents.google.com/patent/CN105997703B/zh)
  - CN107530388A 「橄榄叶萃取物及其制造方法」 — [Google Patents](https://patents.google.com/patent/CN107530388A/zh)

### Inferences
- **A brand citing CN107217076B to back "81.04% oleuropein" would be misreading or misrepresenting it**, for three reasons:
  1. 81.04% describes another research group's starting material, cited as prior art.
  2. The patent's purpose is to *destroy* oleuropein (95–100% degradation) to make hydroxytyrosol.
  3. The patentee is a university, so a brand would need a licence to call it "its" patent.
- **The patent's likely term.** It was filed 2017-05-19, so it would run to 2037-05-19 if maintained. Its legal status was not checked.
- **The 40% PCR® figure has an open question.** A 40% oleuropein material co-formulated with hydroxypropyl-β-cyclodextrin raises the question of whether 40% is measured on the whole complex or on the extract fraction; the snippet did not say. The cyclodextrin is presumably there for water solubility and stability, but the page's rationale was not retrieved.
- **"羟基酪醇" in a product does not prove olive origin.** Hydroxytyrosol is sold under a "biosynthesis" category (南京腾象) and by fine-chemical suppliers. This is an inference from a category label, not a confirmed manufacturing route.

### Gaps
- **The 「绿天」 company name** behind plamed-extract.com is not confirmed. Prices, minimum orders and customers of PCR® are not known.
- **Brand citations:** no brand was found citing CN107217076B or CN102451235B. The query that would have tested this was refused (budget).
- **CN102451235B:** title, assignee, dates and legal status were not retrieved. Google Patents is DNS-blocked.
- **Product use of these materials:** no evidence was found tying any finished product to 尚诚, 森荣, 常奥, 西力, 迪欣, 吉至, 腾象 or 唯铂莱 material.
- **Oleaxcel™'s vendor** was not identified.

---

## 5. Regulatory status: 橄榄苦苷 and IECIC, 羟基酪醇's status, NMPA notices on olive claims

### Takeaway
- **橄榄苦苷:** not in the IECIC as a single ingredient, so labels use 油橄榄叶提取物 (established as IECIC No. 08138). China sets no quality-specification indicators for that extract beyond a safety assessment.
- **羟基酪醇:** entered China as a **filed new cosmetic ingredient** under the standard Chinese name **二羟基苯乙醇**:
  - first filing 国妆原备字20240003, by 杭州唯铂莱生物科技有限公司, 2024-01-12, listed in 「安全监测期」;
  - **6 cumulative filings** by May 2026, the latest 20260085 by 浙江熙正霖, 2026-05-15.
- **NMPA notices:** none specific to olive claims was found. The CSS action came from a district market regulator, under advertising law (established).

### Cited Findings
- **[3P/consultancy]** 「橄榄苦苷并未收录在《原料目录》中」 (as summarized), and 「根据我国目前化妆品法规要求，对油橄榄（OLEA EUROPAEA）叶提取物的使用，除要求对其在产品中的应用进行安全评估外，并无对其质量规格中具体指标的要求」. — [中贸合规中心 油橄榄叶提取物未检出橄榄苦苷、羟基酪醇，一定是虚假宣传吗？](https://www.zmuni.com/zh-hans/news/you-gan-lan-ye-ti-qu-wu-wei-jian-chu-gan-lan-ku-gan-qiang/)
- **[MEDIA]** 「橄苦苷这一成分并未在国家药监局备案，其检测方法也没有明确统一的规定或者国家标准」 (「橄苦苷」 is as written), and 「由于油橄榄提取物并没有一个标准的检测方法，未检出是否等于未添加，仍有待进一步调查」 (as summarized). — [速豹新闻网 2024-03-05](http://news.subaoxw.com/guonei/2024/0305/154192.html); [中国医药报 2024-08-03](https://bk.cnpharm.com/zgyyb/2024/08/03/app_317921.html) (not disambiguated)
- **[3P/consultancy] Non-detect is not automatically false advertising.** 「该产品的检测结果显示未检出橄榄苦苷及羟基酪醇，并不能直接判断其虚假宣传」. Content depends on 提取工艺、树龄、产地、采摘时期, and oleuropein can degrade over time (as summarized). — [中贸合规中心](https://www.zmuni.com/zh-hans/news/you-gan-lan-ye-ti-qu-wu-wei-jian-chu-gan-lan-ku-gan-qiang/)
- **[3P/consultancy] Hydroxytyrosol filing:** 「羟基酪醇在我国已有企业申请化妆品新原料备案（标准中文名称：二羟基苯乙醇；备案号：国妆原备字20240003；备案人：杭州唯铂莱生物科技有限公司），技术要求文件暂未公示」. Also: 「羟基酪醇（Hydroxytyrosol，CAS号10597-60-1）目前已收录于欧盟CosIng数据库，使用目的为皮肤漂白剂、皮肤调理剂」 (probable attribution). — [中贸合规中心 油橄榄-羟基酪醇化妆品新原料备案快速攻略](https://www.zmuni.com/zh-hans/news/you-gan-lan-qiang-ji-lao-chun-hua-zhuang-pin-xin-yuan-liao/)
- **[3P/consultancy] Filing date and status:** 20240003 was filed 2024-01-12, and a 2024 analysis lists it as 「安全监测期」. — [瑞旭科新 2024年中国化妆品新原料备案最新情况分析](https://www.cirs-bio.com/2024-nian-zhong-guo-hua-zhuang-pin-xin-yuan-liao-bei-an-zui-xin-qing-kuang-fen-xi); [中贸合规中心 月度汇总 2024年1月](https://www.zmuni.com/zh-hans/news/yue-du-hui-zong-2024-nian-1-yue-zhong-guo-ji-guo-ji-hua/) (not disambiguated)
- **[3P/consultancy] Repeat filings:**
  - 「二羟基苯乙醇累计备案6次」, including 国妆原备字20250014, 20250078, 20250149, 20260065 and 20260085. 20260085 was filed 2026-05-15 by 浙江熙正霖生物科技有限公司. — [瑞旭 2026年5月新原料备案分析](https://www.cirs-group.com/cn/cosmetics/2026-nian-5-yue-hua-zhuang-pin-xin-yuan-liao-bei-an-zui-xin-qing-kuang-fen-xi-bao-gao)
  - The June 2025 report counted 4 filings. — [瑞旭 2025年6月](https://www.cirs-group.com/cn/cosmetics/2025-nian-6-yue-hua-zhuang-pin-xin-yuan-liao-bei-an-zui-xin-qing-kuang-fen-xi-bao-gao)
  - Sources conflict on the date of 20250149: 2025-11-26 vs. 2023-11-26 (the latter is implausible for a 2025 number). — [瑞旭 2025年11月](https://www.cirs-group.com/cn/cosmetics/2025-nian-11-yue-hua-zhuang-pin-xin-yuan-liao-bei-an-zui-xin-qing-kuang-fen-xi-bao-gao)
- **[OFFICIAL-reported] What the penalty turned on:** the decision noted the company 「未能提供橄榄苦苷的检测报告」. — [新京报 2024-12-08](https://m.bjnews.com.cn/detail/1733647882168430.html)

### Inferences
- **Hydroxytyrosol was evidently not in IECIC 2021.** It needed new-ingredient filing in 2024, and a 新原料 is by definition one not previously used in Chinese cosmetics (that definition was not re-verified this session). So before 2024-01-12, hydroxytyrosol could reach Chinese products only as a constituent of listed extracts such as 油橄榄叶提取物. On such products, "羟基酪醇" marketing describes a constituent, not a labelled ingredient. A product that labels it separately should show 「二羟基苯乙醇」.
- **Monitoring periods are still running.** With six filings, at least one company's three-year monitoring period runs into 2027 or later (2024-01-12 + 3 years). The usage restrictions during monitoring were not verified this session.
- **The enforcement hook is claim substantiation.** The CSS case was decided on the inability to substantiate a marker claim (「含有较高的橄榄苦苷」), not on whether the extract was present. So brands that claim only "油橄榄叶提取物 X%" carry less legal exposure than brands that claim marker content, even though the former tells consumers less.

### Gaps
- **The official IECIC 2021 file** was not checked directly for 羟基酪醇 or 二羟基苯乙醇, or for 橄榄苦苷. The non-listing rests on consultancy statements plus the new-ingredient filing.
- **The technical requirements (技术要求)** for 20240003 and the later filings were not retrieved, nor were the filers of 20250014, 20250078, 20250149 and 20260065.
- **No query was run for NMPA notices, 抽检 results or 化妆品监管 app items on olive claims** (budget), so their absence is unconfirmed.
- **Not found:** any NMPA statement on testing 橄榄苦苷 in cosmetics, and whether any finished product in China labels 「二羟基苯乙醇」.

---

## 6. Ranking of products by transparency and evidence

### Takeaway
On what could be retrieved, no product meets a high bar: marker content in the finished product, measured by a named accredited lab, for a named batch. The provisional order is below. The supplier spec for PCR® (40% oleuropein, origin and carrier stated) is more transparent than any finished product found. Twelve domestic brands could not be ranked because no data was retrieved.
1. **John Jeff:** names its supplier and trade material, and disclosed dry-extract percentages.
2. **安修泽:** names its marker trio and a human-test presenter, but gives only relative numbers.
3. **欧玛:** a "10%" claim with no spec, and a "patent" it does not own.
4. **CSS 希妍萃:** a claim that tests and the regulator both contradicted.

### Cited Findings
The rubric is my own. Each criterion is scored 0, 1 or 2:
- **A.** Finished-product marker content disclosed, with method and lab.
- **B.** Raw-material identity disclosed (supplier or trade name, and whether the % is dry or solution).
- **C.** A brand-published third-party test (content or efficacy).
- **D.** Independent tests consistent with the claims.
- **E.** Regulatory record (no adverse action; filing or 依据摘要 visible).

| Rank | Product | A | B | C | D | E | Basis |
|---|---|---|---|---|---|---|---|
| 1 | John Jeff 油橄榄精华液 | 0 | 2 | 0 | n/a (none found) | 1 | Names Hallstar Eurol®BT Gly; dry matter 0.5775% / 0.75% / 1.325% disclosed; "反向升级" criticism — [YesStyle](https://www.yesstyle.com/en/john-jeff-olive-oil-serum-for-acne-prone-skin-15ml/info.html/pid.1133599739); [风闻](https://user.guancha.cn/main/content?id=752096&s=fwzwyzzwzbt); [知乎 p/533107542](https://zhuanlan.zhihu.com/p/533107542) |
| 2 | 安修泽 油橄榄精华 3.0 | 0 | 1 | 1 | n/a (the masked 「安**」 may be it; unconfirmed) | 1 | Names L70 composition and 叶理 / 南方医科大学皮肤病医院化妆品检测中心; claims only relative (152%, 220%) with no report — [央广网 2026-04-15](https://www.cnr.cn/mspd/jrhm/20260415/t20260415_527585997.shtml); [钛媒体](https://www.tmtpost.com/7953941.html) |
| 3 | 欧玛 橄榄修护精华 (O-Live Gel) | 0 | 1 | 0 | n/a (the masked 「欧*」 may be it; result not public) | 1 | 10% with no spec; cited patent assigned to SkinCeuticals; no filing found — earlier notes: [smzdm p/107779377](https://www.smzdm.com/p/107779377/); `china_market_regulatory.md` |
| 4 | CSS 希妍萃橄榄积雪草舒颜精华液 | 0 | 0 | 0 | 0 | 0 | Multiple non-detects; ¥500,000 false-advertising fine; no oleuropein report — [新京报 2024-12-08](https://m.bjnews.com.cn/detail/1733647882168430.html) |
| — | Supplier reference: PCR® 油橄榄叶提取物 | n/a | 2 | n/a | n/a | n/a | 40% 橄榄苦甙, PMQH02, 陇南 + 羟丙基环糊精 published — [plamed-extract.com](http://www.plamed-extract.com/product/pcr-olea-europaea-leaf-extract/) |
| unrated | 百植萃, 诠润, 瑞沛, 森芝玑, 艾酸氏, purid, 春日来信, 成分星球, 言之有物, 至本, 米蓓尔, 毕生之研 | — | — | — | — | — | Named only in the 14-brand roundup — [新浪 4808949637319838](https://www.sina.cn/news/detail/4808949637319838.html) |

### Inferences
- **The top two are close.** John Jeff and 安修泽 differ mainly in kind: John Jeff's disclosures are absolute and checkable in principle (dry-extract %), while 安修泽's are relative PR figures. I rank John Jeff first on that basis. Neither has an independent marker test on record.
- **What would move any product to the top:** a published HPLC result for both markers in the finished product (mg/kg or % w/w), from a CMA/CNAS lab, with batch number and date. A validated simultaneous method already exists (see §3).
- **The ranking is sensitive to the six-product test.** If 大虎's masked 「欧*」 and 「安**」 really are 欧玛 and 安修泽, both were probably among the low-content group or were the one unaccounted-for product. Identifying them and their numbers could change ranks 2 and 3.

### Gaps
- **Coverage:** no retrievable data to score the 12 other domestic brands, any 羟基酪醇-labelled product, or imported olive-led products beyond 欧玛 and CSS.
- **Weighting:** the rubric's weights are unvalidated judgment calls. With more data (prices, 依据摘要, independent tests) the order could change.
- **Search budget:** further work needs a follow-up session with a fresh WebSearch budget. Priority queries:
  - each 14-list brand plus 「油橄榄 成分表 备案」;
  - 「大虎课代表 油橄榄 检测 数据 mg/kg」 on video-transcript mirrors;
  - 「二羟基苯乙醇 精华」;
  - 「CN107217076B 精华」 and 「81.04% 橄榄苦苷 精华」, to find the brand that cites the patent.
