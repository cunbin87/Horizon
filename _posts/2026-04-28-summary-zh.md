---
layout: default
title: "Horizon Summary: 2026-04-28 (ZH)"
date: 2026-04-28
lang: zh
---

> From 121 items, 39 important content pieces were selected

---

1. [Linux 7.1 主线内核为 ARM 添加实时 RT 支持](#item-1) ⭐️ 9.0/10
2. [谷歌与五角大楼达成“任何合法”AI 使用协议](#item-2) ⭐️ 8.0/10
3. [谷歌安卓开放性面临威胁](#item-3) ⭐️ 8.0/10
4. [Talkie：一个基于 1930 年代文本训练的 130 亿参数语言模型](#item-4) ⭐️ 8.0/10
5. [阿联酋退出 OPEC 和 OPEC+](#item-5) ⭐️ 8.0/10
6. [pip 26.1 引入锁文件和依赖冷却期](#item-6) ⭐️ 8.0/10
7. [微软 VibeVoice：开源语音转文字与说话人分离](#item-7) ⭐️ 8.0/10
8. [OpenAI 与微软移除 AGI 条款](#item-8) ⭐️ 8.0/10
9. [杀虫剂导致美国蝴蝶数量下降 22%](#item-9) ⭐️ 8.0/10
10. [阿里平头哥发布国内首款内置 PCIe Switch 的 400G 智能网卡](#item-10) ⭐️ 8.0/10
11. [RADV Vulkan 驱动通过 AMD TMZ 获得保护内存支持](#item-11) ⭐️ 8.0/10
12. [Linux 7.1-rc1 发布，带来新 NTFS 驱动和 FRED](#item-12) ⭐️ 8.0/10
13. [LocalSend：开源跨平台 AirDrop 替代品](#item-13) ⭐️ 7.0/10
14. [Anthropic 成为 Blender 开发基金企业赞助人](#item-14) ⭐️ 7.0/10
15. [GitHub Copilot 代码审查将消耗 Actions 分钟数](#item-15) ⭐️ 7.0/10
16. [苹果 Vision Pro 首次辅助完成白内障手术，支持 3D 可视化与远程协作](#item-16) ⭐️ 7.0/10
17. [ASML 据称研发晶圆对晶圆混合键合设备](#item-17) ⭐️ 7.0/10
18. [SpaceX 为马斯克制定火星殖民薪酬方案](#item-18) ⭐️ 7.0/10
19. [《财富》：AI 成本常高于人类员工](#item-19) ⭐️ 7.0/10
20. [IBM 更新在 s390 上运行 ARM64 KVM 的补丁](#item-20) ⭐️ 7.0/10
21. [Ubuntu 26.04 LTS 在创作者工作站上超越 Windows 11](#item-21) ⭐️ 7.0/10
22. [AMD Lemonade SDK 10.3 移除 Electron，体积缩小 10 倍](#item-22) ⭐️ 7.0/10
23. [主权技术机构启动开放标准新计划](#item-23) ⭐️ 7.0/10
24. [Fedora 44 发布，搭载 GNOME 50 和 KDE Plasma 6.6](#item-24) ⭐️ 7.0/10
25. [Proton 11.0 Beta 2 更新 VKD3D-Proton](#item-25) ⭐️ 7.0/10
26. [Ubuntu 澄清 AI 功能为可选且可通过 Snap 移除](#item-26) ⭐️ 7.0/10
27. [AMDXDNA 驱动为 Ryzen AI 引入硬件调度时间量子](#item-27) ⭐️ 7.0/10
28. [Ubuntu 将在未来一年集成 AI 功能](#item-28) ⭐️ 7.0/10
29. [Google Meet 语音翻译功能扩展至移动端](#item-29) ⭐️ 6.0/10
30. [三星 Exynos 2600 推出 ENSS，移动端 AI 超分技术](#item-30) ⭐️ 6.0/10
31. [比亚迪汉 EV 闪充版：705 公里续航，9 分钟充满，起售价 17.98 万元](#item-31) ⭐️ 6.0/10
32. [比亚迪闪充站超 5500 座，覆盖 311 城](#item-32) ⭐️ 6.0/10
33. [GCC 16.1 改进错误信息，新增实验性 HTML 输出](#item-33) ⭐️ 6.0/10
34. [7-Zip 26.01 在 Linux 上支持大页面](#item-34) ⭐️ 6.0/10
35. [WayVNC 0.10 发布，支持 wlroots Wayland 合成器](#item-35) ⭐️ 6.0/10
36. [Stratis Storage 3.9 新增在线加密/解密/重新加密功能](#item-36) ⭐️ 6.0/10
37. [英特尔酷睿 Ultra 5 250K Plus 以 219 美元提供出色 Linux 性价比](#item-37) ⭐️ 6.0/10
38. [AMD VPE 2.0 支持已合并到 Mesa 26.2](#item-38) ⭐️ 6.0/10
39. [D7VK v1.8 改进 Vulkan 上的旧版 Direct3D 支持](#item-39) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Linux 7.1 主线内核为 ARM 添加实时 RT 支持](https://www.phoronix.com/news/Linux-7.1-ARM-RT) ⭐️ 9.0/10

Linux 7.1 主线内核现在允许为 ARM 架构构建实时 PREEMPT_RT 内核，无需任何外部补丁。 这一集成消除了维护单独补丁的需求，简化了在基于 ARM 的嵌入式及工业系统上部署实时 Linux 的过程，这些系统广泛应用于物联网、机器人和自动化领域。 PREEMPT_RT 功能已于 2024 年 9 月完全合并到 x86 及其他架构的主线 Linux 中，ARM 支持现在随 Linux 7.1 到来。这使得 ARM 无需外部补丁即可实现硬实时和软实时能力。

rss · Phoronix · Apr 27, 13:27

**背景**: PREEMPT_RT 是 Linux 内核的一个功能，提供实时计算能力，之前作为一组外部补丁维护。其主线集成标志着实时 Linux 的一个里程碑，而 ARM 是嵌入式系统中的主导架构，实时性能至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.phoronix.com/news/Linux-7.1-ARM-RT">With Linux 7.1 The Mainline Kernel Now Supports Real-Time "RT" On ARM - Phoronix</a></li>
<li><a href="https://en.wikipedia.org/wiki/PREEMPT_RT">PREEMPT_RT - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Linux`, `#Real-Time`, `#ARM`, `#Kernel`, `#Embedded Systems`

---

<a id="item-2"></a>
## [谷歌与五角大楼达成“任何合法”AI 使用协议](https://www.theverge.com/ai-artificial-intelligence/919494/google-pentagon-classified-ai-deal) ⭐️ 8.0/10

据报道，谷歌与五角大楼达成了一项机密协议，允许美国军方将谷歌的 AI 用于“任何合法”目的，且谷歌无权否决具体应用。 该协议标志着谷歌在 2018 年因员工抗议退出 Project Maven 后的重大逆转，重新引发了关于 AI 伦理和企业在军事应用中责任的辩论。 据报道，该机密协议不允许谷歌否决政府如何使用其 AI 模型，引发了对监督和“合法”使用定义的担忧。

hackernews · granzymes · Apr 28, 15:49

**背景**: 2018 年，谷歌在数千名员工抗议后退出了 Project Maven（五角大楼用于无人机视频分析的 AI 项目）。谷歌随后发布了 AI 原则，禁止将其 AI 用于武器或监控。这项新协议似乎通过聚焦“合法”使用绕过了这些原则。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Project_Maven">Project Maven - Wikipedia</a></li>
<li><a href="https://www.wired.com/story/3-years-maven-uproar-google-warms-pentagon/">3 Years After the Project Maven Uproar, Google Cozies to ...</a></li>
<li><a href="https://www.army.mil/article/233690/dod_adopts_5_principles_of_artificial_intelligence_ethics">DOD adopts 5 principles of artificial intelligence ethics | Article | The United States Army</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了怀疑，将“合法”漏洞比作在游戏中制定规则，并指出员工的税款已经用于他们可能不同意的军事行动。一些人认为，任何继续在谷歌工作的 AI 研究人员现在都在道德上妥协了。

**标签**: `#AI ethics`, `#military AI`, `#Google`, `#policy`, `#technology ethics`

---

<a id="item-3"></a>
## [谷歌安卓开放性面临威胁](https://keepandroidopen.org/en/) ⭐️ 8.0/10

据报道，谷歌正在加强对安卓系统的控制，限制用户运行自定义代码和侧载应用的能力，批评者认为这破坏了该平台的开源承诺。 这一转变可能消除安卓与 iOS 之间的关键区别，可能减少用户选择和创新，并可能导致类似桌面计算的供应商锁定。 这些变化影响到用户手中已有的设备，尽管谷歌仍允许一些开发者选项（如连续点击版本号七次），但总体方向是走向更封闭的生态系统。

hackernews · doener · Apr 28, 15:21

**背景**: 安卓长期以来被宣传为苹果 iOS 的开源替代品，允许用户从官方商店之外安装应用并修改设备。这种开放性一直是吸引数百万用户的核心承诺，并培育了丰富的自定义 ROM 和第三方应用生态系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vendor_lock-in">Vendor lock-in</a></li>
<li><a href="https://en.wikipedia.org/wiki/Android_(operating_system)">Android (operating system) - Wikipedia</a></li>
<li><a href="https://www.lineageos.org/">LineageOS – LineageOS Android Distribution</a></li>

</ul>
</details>

**社区讨论**: 评论表达了强烈的失望和被背叛感，一些用户因此转向 iOS。其他人则将其与桌面计算中的供应商锁定相类比，认为限制安卓的开放性是不可接受的，因为类似限制在 PC 上会遭到广泛谴责。

**标签**: `#Android`, `#open source`, `#vendor lock-in`, `#Google`, `#mobile OS`

---

<a id="item-4"></a>
## [Talkie：一个基于 1930 年代文本训练的 130 亿参数语言模型](https://talkie-lm.com/introducing-talkie) ⭐️ 8.0/10

由 Alec Radford 领导的研究人员发布了 Talkie，这是一个 130 亿参数的语言模型，仅使用 1931 年 1 月 1 日之前出版的 2600 亿个英文文本 token 进行训练，能够以 1930 年代的风格和知识生成回答。 Talkie 通过将训练数据限制在特定历史时期，展示了一种新颖的语言建模方法，实现了独特的历史推理和文化保存，并为 AI 泛化能力和训练数据影响提供了见解。 该模型是一个 130 亿参数的基础模型，规模与 Llama-13B 相当，并在精心筛选的 1931 年前英文文本语料库上训练。它能生成历史上合理的回答，但可能反映那个时代过时或有害的观点。

hackernews · jekude · Apr 27, 21:55

**背景**: 大型语言模型（如 GPT-4）通常使用覆盖近几十年的海量多样化互联网数据进行训练。而 Talkie 仅使用 1931 年前的文本，创建了一个模拟 1930 年代知识和语言的“复古”模型。该项目探索了训练数据如何塑造模型的行为和能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.roborhythms.com/pre-1931-language-model-talkie/">talkie : The Pre-1931 Language Model Alec Radford Just Released</a></li>
<li><a href="https://sesamedisk.com/talkie-1930-vintage-language-model/">Talkie 1930: A Vintage Language Model for Historical... - Sesame Disk</a></li>

</ul>
</details>

**社区讨论**: 社区评论显示，用户对该模型历史上准确但有时令人担忧的回答感到着迷，例如建议从两岁到五岁将孩子单独留在家中。用户欣赏其新颖性，但也指出了模型的局限性及其训练时代可能带来的偏见。

**标签**: `#large language models`, `#AI research`, `#historical AI`, `#natural language processing`, `#machine learning`

---

<a id="item-5"></a>
## [阿联酋退出 OPEC 和 OPEC+](https://www.reuters.com/markets/commodities/uae-says-it-quits-opec-opec-statement-2026-04-28/) ⭐️ 8.0/10

阿联酋于 2026 年 4 月 28 日宣布退出 OPEC 和 OPEC+，标志着与沙特领导的石油联盟的历史性分裂。 此举削弱了 OPEC 的定价能力，并可能重塑全球石油供应格局，尤其是在地缘政治紧张时期，一个亲美的海湾国家退出俄沙联盟。 阿联酋是 OPEC 第三大产油国，占该组织产量的 12-13%，其退出远比 2019 年卡塔尔的退出意义重大。

hackernews · TechTechTech · Apr 28, 13:13

**背景**: OPEC 和 OPEC+是协调产量以影响全球价格的产油国卡特尔。阿联酋长期不满沙特设定的产量配额，沙特经常减产而其他国家作弊。此次退出反映了内部紧张和全球能源联盟的转变。

**社区讨论**: 评论者指出 OPEC 历史上的作弊问题以及美国能源独立的趋势，一些人认为这是 OPEC 权力的重大裂痕。还有人引用迪拜前统治者的名言，关于财富与衰落的循环。

**标签**: `#geopolitics`, `#oil`, `#OPEC`, `#energy`, `#global markets`

---

<a id="item-6"></a>
## [pip 26.1 引入锁文件和依赖冷却期](https://simonwillison.net/2026/Apr/28/pip-261/#atom-everything) ⭐️ 8.0/10

pip 26.1 于 2026 年 4 月发布，通过 `pip lock` 命令增加了原生锁文件支持，并通过 `--uploaded-prior-to` 选项引入了依赖冷却期功能，允许用户指定包的最低年龄以缓解供应链攻击。 这些功能满足了社区长期以来对可重现构建和改进 Python 依赖管理安全性的需求，使 pip 更接近 npm 和 Cargo 等现代包管理器。 锁文件名为 `pylock.toml`，且特定于平台和 Python 版本。冷却期选项使用 ISO 8601 持续时间格式（例如 `P4D` 表示 4 天），仅支持天数。pip 26.1 还放弃了对 Python 3.9 的支持。

rss · Simon Willison · Apr 28, 05:23

**背景**: pip 是 Python 的默认包安装器，但此前缺乏内置的锁文件支持，迫使用户依赖 Pipenv 或 Poetry 等第三方工具来实现确定性安装。依赖冷却期通过确保只安装特定日期之前发布的包来帮助防止供应链攻击，为恶意包的检测和移除留出时间。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pip.pypa.io/en/stable/cli/pip_lock/">pip lock - pip documentation v26.0.1</a></li>
<li><a href="https://simonwillison.net/2026/Apr/28/pip-261/">What's new in pip 26.1 - lockfiles and dependency cooldowns!</a></li>
<li><a href="https://sethmlarson.dev/pip-relative-dependency-cooldowns">pip v26.1 adds support for relative dependency cooldowns</a></li>

</ul>
</details>

**标签**: `#pip`, `#Python`, `#dependency management`, `#lockfiles`, `#tooling`

---

<a id="item-7"></a>
## [微软 VibeVoice：开源语音转文字与说话人分离](https://simonwillison.net/2026/Apr/27/vibevoice/#atom-everything) ⭐️ 8.0/10

微软发布了 VibeVoice，一个采用 MIT 许可证的语音转文字模型，内置说话人分离功能；Simon Willison 演示了如何在 Mac 上通过 MLX 和 mlx-audio 本地运行该模型，在不到 9 分钟内转录了一段 99 分钟的播客。 VibeVoice 将高质量转录与说话人识别集成于一个开源模型中，使开发者能够在消费级硬件上构建保护隐私的离线语音应用。 该模型单次处理最多支持 60 分钟音频，需要约 30-60 GB 内存，并提供 4 位量化 MLX 版本（5.71 GB），可在 Apple Silicon Mac 上高效运行。

rss · Simon Willison · Apr 27, 23:46

**背景**: Whisper 风格的模型是在大规模音频数据集上训练的神经网络，用于语音识别。说话人分离传统上是独立的后期处理步骤，用于识别谁在何时说话。VibeVoice 将这两项任务集成到一个模型中，简化了流程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Apr/27/vibevoice/">microsoft/ VibeVoice | Simon Willison’s Weblog</a></li>
<li><a href="https://howaiworks.ai/blog/vibevoice-asr-microsoft-speech-recognition">VibeVoice -ASR: Long-Form Speech Breakthrough | HowAIWorks.ai</a></li>
<li><a href="https://github.com/Blaizzy/mlx-audio">GitHub - Blaizzy/mlx-audio: A text-to-speech (TTS), speech-to-text (STT) and speech-to-speech (STS) library built on Apple's MLX framework, providing efficient speech analysis on Apple Silicon. · GitHub</a></li>

</ul>
</details>

**标签**: `#speech-to-text`, `#open-source`, `#machine learning`, `#Microsoft`, `#MLX`

---

<a id="item-8"></a>
## [OpenAI 与微软移除 AGI 条款](https://simonwillison.net/2026/Apr/27/now-deceased-agi-clause/#atom-everything) ⭐️ 8.0/10

2026 年 4 月 27 日，OpenAI 与微软宣布从合作协议中移除 AGI 条款，该条款原本规定一旦实现通用人工智能，微软的知识产权将失效。 这一变化消除了将 AGI 定义与商业权利挂钩的关键治理机制，可能加速 OpenAI 技术的商业化，并重塑两家公司之间的权力平衡。 AGI 条款随时间演变：最初在 OpenAI 章程中定义为在大多数经济价值工作上超越人类的系统，后来与产生 1000 亿美元利润挂钩，最近则需独立专家小组判定。新协议完全移除此条款，而微软的知识产权保留至 2030 年。

rss · Simon Willison · Apr 27, 18:38

**背景**: AGI 条款是微软与 OpenAI 合作中的独特条款，旨在确保如果 OpenAI 实现 AGI，微软不会拥有独家商业控制权。它反映了 OpenAI 最初的非营利使命，即确保 AGI 惠及全人类。随着 OpenAI 转向营利模式并加深与微软的商业联系，该条款一直存在争议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Apr/27/now-deceased-agi-clause/">Tracking the history of the now-deceased OpenAI Microsoft AGI clause</a></li>
<li><a href="https://spyglass.org/the-openai-microsoft-agi-clause/">Microsoft Claws Away 'The Clause' as OpenAI Claws Back Some Independence</a></li>
<li><a href="https://www.unite.ai/microsoft-loses-openai-exclusivity-and-agi-clause-in-amended-deal/">Microsoft Loses OpenAI Exclusivity and AGI Clause in Amended Deal – Unite.AI</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Microsoft`, `#AGI`, `#AI governance`, `#intellectual property`

---

<a id="item-9"></a>
## [杀虫剂导致美国蝴蝶数量下降 22%](https://www.solidot.org/story?sid=84162) ⭐️ 8.0/10

2025 年 3 月发表在《科学》期刊上的研究发现，从 2000 年到 2020 年，美国蝴蝶数量下降了 22%，其中 24 种蝴蝶数量减少 90%或以上，主要原因是杀虫剂的使用。 这一显著下降凸显了杀虫剂对生物多样性和生态系统健康的严重影响，波及对植物繁殖和粮食生产至关重要的传粉昆虫及其他昆虫。 生态学家 Matt Forister 团队分析了 336 株植物，只有 22 株未检测到农药残留，其中 71 株的农药浓度对蝴蝶致命或接近致命。2022 年的一项研究发现，乳草植物平均每株含有 12.2 种杀虫剂。

rss · Solidot · Apr 27, 12:45

**背景**: 蝴蝶是重要的传粉昆虫和环境健康指示物种。杀虫剂，尤其是新烟碱类等现代杀虫剂，会杀死蝴蝶等非目标昆虫。以已灭绝蝴蝶命名的 Xerces 无脊椎动物保护协会致力于保护无脊椎动物。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Xerces_Society_for_Invertebrate_Conservation">Xerces Society for Invertebrate Conservation</a></li>
<li><a href="https://www.unr.edu/biology/people/matt-forister">Matt Forister | Faculty | Department of Biology Milkweed in Western Monarch Habitat Found to be Completely ... That Milkweed You Buy at Retail Nurseries May Contain Pesticides Store-bought milkweed plants can expose monarch caterpillars ...</a></li>
<li><a href="https://xerces.org/press/harmful-pesticides-found-in-milkweeds-critical-for-western-monarchs">Harmful Pesticides Found in Milkweeds Critical for Western ...</a></li>

</ul>
</details>

**标签**: `#ecology`, `#pesticides`, `#biodiversity`, `#environmental science`, `#insect decline`

---

<a id="item-10"></a>
## [阿里平头哥发布国内首款内置 PCIe Switch 的 400G 智能网卡](https://www.ithome.com/0/944/650.htm) ⭐️ 8.0/10

阿里平头哥发布了“磐脉 920”，这是国内首款内置 PCIe Switch 的 400G 智能网卡，目前已量产并在阿里云数据中心部署。 该智能网卡解决了大规模 AI 训练中的“通信墙”瓶颈，通过降低延迟和系统成本 30%来提升有效算力。 磐脉 920 采用 PCIe 5.0 和 112G PAM4 以太网技术，支持 400Gbps 吞吐量和 400Mpps 包处理，并支持多路径 RDMA 以缩短训练完成时间。

rss · IThome 日报 · Apr 28, 10:41

**背景**: 智能网卡将网络任务从 CPU 卸载以提高性能。网卡内部的 PCIe Switch 允许直接低延迟连接 GPU 和 SSD，降低系统复杂性和成本。多路径 RDMA 支持通过多条网络路径并行传输数据，提高效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2212.07868">Characterizing Off-path SmartNIC for Accelerating Distributed Systems</a></li>
<li><a href="https://www.microsoft.com/en-us/research/wp-content/uploads/2018/07/MP-RDMA-NSDI18.pdf">Multi-Path Transport for RDMA in Datacenters</a></li>
<li><a href="https://www.microchip.com/en-us/about/media-center/videos/6FhBb2LyN68">META-DX2L | 1.6T Ethernet PHY with 112G PAM4 SerDes</a></li>

</ul>
</details>

**标签**: `#SmartNIC`, `#AI Infrastructure`, `#Data Center`, `#Networking`, `#Alibaba`

---

<a id="item-11"></a>
## [RADV Vulkan 驱动通过 AMD TMZ 获得保护内存支持](https://www.phoronix.com/news/AMD-RADV-Protected-Memory) ⭐️ 8.0/10

AMD 工程师在开源 RADV Vulkan 驱动中，利用较新 AMD GPU 上的 Trusted Memory Zone (TMZ) 功能，增加了保护内存支持。 这一增强通过加密部分显存，显著提升了 AMD GPU 上图形和计算工作负载的安全性，对处理敏感数据的应用至关重要。 TMZ 支持使用全内存带宽 AES 密码对内存进行加密，该功能正在被上游合并到 Mesa 图形库中，以包含在未来版本中。

rss · Phoronix · Apr 27, 19:33

**背景**: RADV 是 AMD GPU 的开源 Vulkan 驱动，属于 Mesa 项目，广泛用于 Linux 发行版和 Steam Deck。Trusted Memory Zone (TMZ) 是 AMD 硬件特性，用于加密 GPU 内存以防止数据被未授权访问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.mesa3d.org/drivers/radv.html">RADV — The Mesa 3D Graphics Library latest documentation</a></li>
<li><a href="https://lpc.events/event/9/contributions/630/attachments/703/1300/xdc2020_rayhuang_secure_buffer_with_tmz.pdf">Secure Buffer Support with Trusted Memory Zone</a></li>

</ul>
</details>

**标签**: `#Vulkan`, `#RADV`, `#AMD`, `#GPU`, `#security`

---

<a id="item-12"></a>
## [Linux 7.1-rc1 发布，带来新 NTFS 驱动和 FRED](https://www.phoronix.com/news/Linux-7.1-rc1) ⭐️ 8.0/10

Linux 7.1-rc1 已发布，结束了 7.1 内核的合并窗口，其中包括一个支持完全读写的新 NTFS 驱动，并在支持的处理器上默认启用 Intel FRED（灵活返回和事件交付）。 此版本显著提升了 Linux 与 Windows NTFS 文件系统的兼容性，惠及双系统用户和企业环境；同时 FRED 增强了现代 Intel 和 AMD 处理器的性能和安全性。 新 NTFS 驱动采用现代内核基础设施（iomap、folio）设计以实现高性能，而现有的只读 NTFS 驱动和 NTFS3 驱动仍保留在内核树中。FRED 在 Intel Core Ultra Series 3 'Panther Lake' 和即将推出的 Xeon Diamond Rapids 上默认启用，AMD Zen 6 预计也将支持。

rss · Phoronix · Apr 26, 21:37

**背景**: NTFS 是 Windows 的主要文件系统，Linux 历史上依赖 NTFS-3G 等第三方驱动实现完全读写支持。FRED 是一种新的 x86 CPU 特性，可改善中断和异常处理，降低开销并实现更高效的事件交付。Linux 7.1 内核预计将于六月中旬达到稳定版本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.kernel.org/doc/html/next/filesystems/ntfs.html">The Linux NTFS filesystem driver</a></li>
<li><a href="https://linuxiac.com/linux-kernel-7-1-merges-new-ntfs-driver-with-full-write-support/">Linux Kernel 7.1 Merges New NTFS Driver With Full Write Support</a></li>
<li><a href="https://www.phoronix.com/news/Intel-FRED-By-Default-Patch">Patch Posted To Enable Intel FRED By Default On Linux</a></li>

</ul>
</details>

**标签**: `#Linux`, `#kernel`, `#NTFS`, `#FRED`, `#open-source`

---

<a id="item-13"></a>
## [LocalSend：开源跨平台 AirDrop 替代品](https://github.com/localsend/localsend) ⭐️ 7.0/10

LocalSend 是一款开源、跨平台的文件共享应用，允许用户在没有互联网连接的情况下，通过本地网络安全地共享文件。它支持 Windows、macOS、Linux、Android 和 iOS 平台。 LocalSend 满足了跨不同操作系统进行私密、离线文件共享的需求，填补了苹果 AirDrop 等平台特定工具留下的空白。其开源特性促进了社区信任和定制化。 LocalSend 使用 REST API 和 HTTPS 加密进行安全通信，并要求设备处于同一本地网络中。它不依赖外部服务器或互联网连接。

hackernews · bilsbie · Apr 28, 11:54

**背景**: 苹果的 AirDrop 利用蓝牙和 Wi-Fi 自动创建点对点本地网络，即使没有共享 Wi-Fi 网络也能进行文件共享。许多跨平台替代方案（包括 LocalSend）要求设备连接到同一本地网络，这在户外聚会等场景中可能是一个限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/localsend/localsend">localsend/localsend: An open-source cross - platform alternative to...</a></li>
<li><a href="https://localsend.org/">LocalSend: Share files to nearby devices</a></li>
<li><a href="https://alternativeto.net/software/airdrop/">12 Great AirDrop Alternatives : Top Similar Apps in 2025 | AlternativeTo</a></li>

</ul>
</details>

**社区讨论**: 社区评论指出，与能自动创建网络的 AirDrop 相比，LocalSend 要求设备处于同一本地网络是一个关键限制。用户建议使用 Sendme 和 PairDrop 等替代方案，它们通过点对点中继或基于浏览器的连接来克服这一限制。

**标签**: `#open-source`, `#file-sharing`, `#cross-platform`, `#AirDrop-alternative`, `#networking`

---

<a id="item-14"></a>
## [Anthropic 成为 Blender 开发基金企业赞助人](https://www.blender.org/press/anthropic-joins-the-blender-development-fund-as-corporate-patron/) ⭐️ 7.0/10

AI 公司 Anthropic（Claude 的开发者）以企业赞助人身份加入 Blender 开发基金，每年承诺至少 24 万欧元，重点支持 Blender Python API 的改进。 这标志着 AI 公司对开源 3D 工具的重大投资，可能加速 Blender 中的 AI 集成，惠及依赖 Python 脚本进行自动化和 AI 工作流的艺术家与开发者。 Anthropic 与 Google、Meta、Nvidia、Netflix 等企业同列最高资助级别。合作旨在增强 Blender 的基础功能，尤其是对脚本和 AI 集成至关重要的 Python API。

hackernews · Philpax · Apr 28, 16:07

**背景**: Blender 开发基金是一项允许个人和企业资助 Blender 核心开发的计划，企业赞助人每年至少贡献 24 万欧元。Blender 是一款免费开源的 3D 创作套件，广泛用于动画、视觉特效和游戏开发。其 Python API 允许用户自动化任务并扩展功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fund.blender.org/">Blender Development Fund</a></li>
<li><a href="https://gamefromscratch.com/blenders-new-corporate-patron-anthropic-ai/">Blender’s New Corporate Patron – Anthropic AI</a></li>
<li><a href="https://docs.blender.org/api/current/index.html">Blender Python API</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：有人欢迎这笔资助，认为对 Blender 有利，并指出 Google、Nvidia 等先例；也有人担心 AI 公司影响创作工具，可能削弱人类艺术。部分评论者指出，许多 AI 实验室已使用 Blender 构建 3D 管线，因此合作合乎逻辑。

**标签**: `#Blender`, `#Anthropic`, `#Open Source`, `#AI`, `#3D Graphics`

---

<a id="item-15"></a>
## [GitHub Copilot 代码审查将消耗 Actions 分钟数](https://github.blog/changelog/2026-04-27-github-copilot-code-review-will-start-consuming-github-actions-minutes-on-june-1-2026/) ⭐️ 7.0/10

自 2026 年 6 月 1 日起，GitHub Copilot 代码审查将计入 GitHub Actions 的月度分钟配额，这意味着用户需要为 AI 驱动的代码审查活动按照 Actions 计划付费。 这一变化改变了 Copilot 用户的成本结构，可能增加重度依赖自动化代码审查的团队的开支，并可能促使开发者重新考虑对 AI 审查功能的使用或寻求本地替代方案。 该政策适用于所有 Copilot 代码审查请求，包括自动或手动触发的请求；GitHub Actions 分钟数在工作流、工件和缓存之间共享，因此代码审查活动将与其它 CI/CD 任务竞争同一资源池。

hackernews · whtsky · Apr 28, 09:01

**背景**: GitHub Actions 是一个 CI/CD 平台，根据消耗的计算分钟数向用户收费。GitHub Copilot 代码审查是一项 AI 功能，可自动审查拉取请求并提供反馈。此前，该功能不消耗 Actions 分钟数，但即将到来的变更使其与其它 Actions 使用保持一致。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.github.com/en/billing/concepts/product-billing/github-actions">GitHub Actions billing - GitHub Docs</a></li>
<li><a href="https://docs.github.com/en/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review">Using GitHub Copilot code review - GitHub Docs</a></li>

</ul>
</details>

**社区讨论**: 社区成员对虚假的参与度指标表示担忧，一位用户指出 Copilot 的评论会夸大 PR 活动。其他人则讽刺地称赞 Actions 的可靠性，同时质疑对非 Actions 活动收取 Actions 分钟数的逻辑，一些人主张切换到本地模型以避免成本。

**标签**: `#GitHub`, `#Copilot`, `#pricing`, `#CI/CD`, `#developer tools`

---

<a id="item-16"></a>
## [苹果 Vision Pro 首次辅助完成白内障手术，支持 3D 可视化与远程协作](https://www.ithome.com/0/944/705.htm) ⭐️ 7.0/10

2025 年 10 月，纽约眼科医生埃里克·罗森伯格使用苹果 Vision Pro 完成了首例白内障手术，借助 ScopeXR 平台实现 3D 可视化和远程协作，此后又完成了数百例同类手术。 这一里程碑展示了 Vision Pro 在专业医疗领域的潜力，使外科医生能够获得 3D 手术视野和实时远程专家支持，有望提高手术精度并扩大专业医疗资源的可及性。 ScopeXR 将 3D 数字化手术显微镜的实时画面传输至 Vision Pro，叠加显示术前诊断数据，并支持实时远程协作，其他外科医生可看到相同画面。该头显售价 29,999 元，苹果已暂停新款 Vision 系列研发，转向轻量化智能眼镜。

rss · IThome 日报 · Apr 28, 15:18

**背景**: 像苹果 Vision Pro 这样的空间计算头显可以将数字信息叠加到现实世界，实现沉浸式 3D 交互。在手术中，它们可以用立体 3D 视图取代传统 2D 显示器，并允许远程专家虚拟参与。ScopeXR 是一个专为眼科手术设计的空间计算平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.mactech.com/2026/04/27/surgeon-performs-cataract-surgery-using-the-apple-vision-pro/">Surgeon Performs Cataract Surgery Using the Apple... - MacTech.com</a></li>
<li><a href="https://www.macrumors.com/2026/04/28/apple-vision-pro-cataract-surgery/">Apple Vision Pro Used in World-First Cataract Surgery - MacRumors</a></li>
<li><a href="https://scopexr.com/">scopexr .com</a></li>

</ul>
</details>

**标签**: `#Apple Vision Pro`, `#medical technology`, `#spatial computing`, `#surgery`, `#remote collaboration`

---

<a id="item-17"></a>
## [ASML 据称研发晶圆对晶圆混合键合设备](https://www.ithome.com/0/944/697.htm) ⭐️ 7.0/10

据报道，ASML 正基于其 Twinscan 平台研发晶圆对晶圆（W2W）混合键合设备，仁荷大学教授引用 ASML 专利指出这一点。 ASML 进入 W2W 混合键合领域可能颠覆先进封装市场，其 Twinscan 平台具有高吞吐量和对准精度，有望加速 3D 芯片集成。 Twinscan 平台于 2001 年首次出货，采用双晶圆台设计，可同时进行曝光和对准，大幅缩短工艺时间。W2W 混合键合直接键合两片半导体晶圆，缩短互连长度并提升性能。

rss · IThome 日报 · Apr 28, 14:14

**背景**: 混合键合是一种先进封装技术，可在芯片或晶圆之间形成直接的铜对铜连接，实现更高密度和更好的电气性能。与晶粒对晶圆（D2W）键合相比，W2W 键合具有更高的吞吐量和均匀性，适合大规模生产。ASML 主要以光刻系统闻名，但其 Twinscan 平台的精度可适用于键合应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.thelec.net/news/articleView.html?idxno=10055">ASML Seen Developing Wafer-to-Wafer Hybrid Bonder - The Elec Inc.</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/semiconductors/asml-launches-revolutionary-lithography-scanner-for-advanced-3d-packaging-twinscan-xt-360-machine-quadruples-throughput">ASML launches revolutionary lithography scanner for advanced ...</a></li>

</ul>
</details>

**标签**: `#ASML`, `#hybrid bonding`, `#advanced packaging`, `#semiconductor`, `#W2W`

---

<a id="item-18"></a>
## [SpaceX 为马斯克制定火星殖民薪酬方案](https://www.ithome.com/0/944/665.htm) ⭐️ 7.0/10

SpaceX 董事会批准了一项针对埃隆·马斯克的薪酬方案，若公司估值达到 7.5 万亿美元并建立拥有 100 万人的火星殖民地，或建成 100 太瓦的太空数据中心，马斯克将获得超级投票权股票。 该方案将马斯克的薪酬与前所未有的里程碑挂钩，凸显了 SpaceX 的雄心以及留住马斯克的难度。同时，这也引发了治理方面的担忧，因为 SpaceX 和特斯拉正在争夺他的精力。 该方案包括 2 亿股 B 类超级投票权股票（每股 10 票）用于火星殖民目标，以及 6040 万股用于太空数据中心目标。没有设定截止日期，若目标未达成，马斯克将无法获得任何股票。

rss · IThome 日报 · Apr 28, 11:39

**背景**: 超级投票权股票赋予持有者不成比例的投票权，常被创始人用来保持控制权。SpaceX 计划在 2026 年 6 月马斯克生日前后进行 IPO，估值约 1.75 万亿美元。100 太瓦的太空数据中心需要巨大的能源和发射能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Supervoting_shares">Supervoting shares</a></li>
<li><a href="https://www.npr.org/2026/04/03/nx-s1-5718416/ai-data-centers-in-space-spacex-elon-musk">Will data centers in space work? Elon Musk says yes : NPR</a></li>
<li><a href="https://spacexstock.com/spacex-dual-class-shares-what-it-means-for-investors/">SpaceX Dual-Class Shares: What It Means for Investors</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#Elon Musk`, `#compensation`, `#Mars colonization`, `#space data center`

---

<a id="item-19"></a>
## [《财富》：AI 成本常高于人类员工](https://www.ithome.com/0/944/658.htm) ⭐️ 7.0/10

《财富》杂志报道，当前使用 AI 往往比雇佣人类员工更昂贵，英伟达副总裁 Bryan Catanzaro 表示 AI 算力成本远高于员工薪资，麻省理工学院研究显示 AI 仅在 23%的视觉岗位中具有经济优势。 这挑战了 AI 能降低成本的普遍假设，迫使企业重新审视其 AI 投资策略，并凸显了 AI 应用中的一个重大经济悖论。 尽管没有明确证据显示生产力提升，科技公司今年已在 AI 上投入 7400 亿美元，比 2025 年增长 69%。但 Gartner 预测，到 2030 年，1 万亿参数大语言模型的推理成本将下降超过 90%。

rss · IThome 日报 · Apr 28, 11:08

**背景**: AI 应用激增，许多公司用 AI 系统替代人类员工以期节省成本。然而，硬件、能源和模型推理的高昂成本使得 AI 在许多情况下比人类劳动更昂贵。这一悖论在于，尽管 AI 能力在提升，但其经济可行性在许多任务中仍存疑问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ithome.com/0/944/658.htm">《财富》杂志提 AI 成本悖论：目前使用人工智能比雇佣人类员工更昂贵...</a></li>
<li><a href="https://finance.sina.com.cn/tech/roll/2026-04-28/doc-inhwaawa8373743.shtml">老板裁员省钱幻想破灭！NVIDIA高层揭秘：AI算力成本远超过员工薪资|AI...</a></li>
<li><a href="https://finance.technews.tw/2026/04/28/ai-can-cost-more-than-human-workers-now/">輝達高層：算力成本遠超過員工薪資！AI 省錢之說未成真先破滅 | TechN...</a></li>

</ul>
</details>

**标签**: `#AI`, `#economics`, `#cost analysis`, `#labor`, `#technology adoption`

---

<a id="item-20"></a>
## [IBM 更新在 s390 上运行 ARM64 KVM 的补丁](https://www.phoronix.com/news/ARM64-On-s390-IBM-Z-v2) ⭐️ 7.0/10

IBM 发布了第二版 Linux 内核补丁，通过 KVM 在 IBM Z（s390）服务器上实现 ARM64（AArch64）虚拟化加速。 这一进展意义重大，因为它展示了 IBM 与 Arm 合作打造双架构硬件，有望实现混合云和异构计算环境，使 ARM64 工作负载能在 IBM Z 大型机上运行。 这些补丁仍处于早期阶段，代表了一种新颖的虚拟化方法，允许 AArch64 软件通过 KVM 在 IBM s390 系统上运行。第二版根据初步反馈进行了改进。

rss · Phoronix · Apr 28, 16:54

**背景**: IBM Z 大型机使用 s390 架构，这是一种 64 位 CISC 架构。KVM（基于内核的虚拟机）是一个 Linux 内核模块，允许宿主机运行多个虚拟机。ARM64 是一种 64 位 RISC 架构，常用于移动设备和服务器。此次合作旨在利用 KVM 虚拟化技术，在 IBM Z 硬件上运行 ARM64 工作负载。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/64-bit_computing">64-bit computing - Wikipedia</a></li>
<li><a href="https://deepwiki.com/torvalds/linux/3.2-kvm-arm64-virtualization">KVM ARM64 Virtualization | torvalds/linux | DeepWiki</a></li>

</ul>
</details>

**标签**: `#Linux`, `#KVM`, `#ARM64`, `#IBM Z`, `#virtualization`

---

<a id="item-21"></a>
## [Ubuntu 26.04 LTS 在创作者工作站上超越 Windows 11](https://www.phoronix.com/review/ubuntu-2604-windows-11) ⭐️ 7.0/10

Phoronix 的基准测试预览显示，在搭载 AMD Ryzen Threadripper PRO 9975WX 和 NVIDIA RTX PRO 6000 Max-Q 的 HP Z6 G5 A 工作站上，Ubuntu 26.04 LTS 在创作者工作站任务中表现优于 Windows 11 Pro。 这一对比为在高端创作者工作负载中选择 Linux 还是 Windows 的专业人士提供了宝贵数据，可能影响内容创作和工程领域的平台决策。 测试系统配备 32 核 AMD Threadripper PRO 9975WX、八通道 DDR5-5600 内存和 NVIDIA RTX PRO 6000 Max-Q 工作站 GPU。HP Z6 G5 A 工作站的完整评测预计在一周内发布。

rss · Phoronix · Apr 28, 15:00

**背景**: Ubuntu 26.04 LTS 是流行 Linux 发行版的最新长期支持版本，而 Windows 11 Pro 是微软的专业操作系统。创作者工作负载包括视频编辑、3D 渲染和图形设计等任务，这些任务受益于高性能硬件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.amd.com/en/products/processors/workstations/ryzen-threadripper/9000-wx-series/amd-ryzen-threadripper-pro-9975wx.html">AMD Ryzen™ Threadripper™ PRO 9975WX</a></li>
<li><a href="https://www.nvidia.com/en-us/products/workstations/professional-desktop-gpus/rtx-pro-6000-max-q/">RTX PRO 6000 Blackwell Max - Q Workstation Edition | NVIDIA</a></li>

</ul>
</details>

**标签**: `#Ubuntu`, `#Windows 11`, `#performance`, `#workstation`, `#benchmark`

---

<a id="item-22"></a>
## [AMD Lemonade SDK 10.3 移除 Electron，体积缩小 10 倍](https://www.phoronix.com/news/AMD-Lemonade-10.3) ⭐️ 7.0/10

AMD 发布了 Lemonade SDK 10.3 版本，移除了 Electron 框架，使 SDK 体积缩小了 10 倍，并提升了在 AMD 硬件上运行本地 AI 服务器的性能。 这一显著的体积缩减使开发者更容易在 AMD CPU、GPU 和 NPU 上本地部署 AI 模型，可能加速 AMD AI 生态系统的采用。 移除 Electron 消除了完整的 Chromium 浏览器引擎和 Node.js 运行时的开销，从而缩短了启动时间并降低了内存使用。SDK 现在改用原生 UI 组件。

rss · Phoronix · Apr 28, 14:35

**背景**: Electron 是一个流行的跨平台桌面应用框架，使用 Web 技术构建，但会捆绑完整的 Chromium 浏览器，导致应用体积大且资源占用高。Lemonade SDK 是 AMD 支持的开源本地 AI 服务器，支持在 AMD 硬件上进行大语言模型推理。移除 Electron 符合在性能关键型应用中摒弃重型 Web 框架的趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Electron_framework">Electron framework</a></li>
<li><a href="https://github.com/lemonade-sdk/lemonade">GitHub - lemonade - sdk / lemonade : Lemonade helps users discover...</a></li>

</ul>
</details>

**标签**: `#AMD`, `#AI`, `#SDK`, `#Electron`, `#open-source`

---

<a id="item-23"></a>
## [主权技术机构启动开放标准新计划](https://www.phoronix.com/news/Sovereign-Tech-Standards) ⭐️ 7.0/10

德国主权技术机构宣布启动“主权技术标准”网络，这是一个新计划，通过将开源维护者与 IETF、W3C 和 ISO 等标准组织联系起来，支持开放标准的开发。 该计划弥合了开源实现者与标准制定者之间的鸿沟，确保关键数字基础设施保持互操作性并基于实际实践，这对数字主权至关重要。 主权技术标准网络涵盖 IETF、W3C 和 ISO 的标准，但值得注意的是，它排除了 Khronos Group 的标准，如 Vulkan、SPIR-V 和 OpenCL。

rss · Phoronix · Apr 28, 13:35

**背景**: 主权技术机构是德国公共组织，成立于 2022 年 10 月，旨在通过资助关键开源软件来维护数字主权。它受联邦经济事务和气候行动部委托，最初于 2022 年 5 月由德国联邦议院拨款。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sovereign.tech/programs/standards">Sovereign Tech Standards</a></li>
<li><a href="https://en.wikipedia.org/wiki/Sovereign_Tech_Agency">Sovereign Tech Agency</a></li>
<li><a href="https://www.phoronix.com/news/Sovereign-Tech-Standards">Sovereign Tech Agency Launches New Initiative To Help Open ...</a></li>

</ul>
</details>

**标签**: `#open-source`, `#open-standards`, `#funding`, `#Germany`, `#policy`

---

<a id="item-24"></a>
## [Fedora 44 发布，搭载 GNOME 50 和 KDE Plasma 6.6](https://www.phoronix.com/news/Fedora-44-Released) ⭐️ 7.0/10

Fedora 44 正式发布，Workstation 版本默认搭载 GNOME 50 桌面环境，并提供了更新的 KDE Plasma 6.6 桌面环境。 此次发布延续了 Fedora 提供最新开源软件的传统，使其成为希望获得最新创新的 Linux 爱好者和开发者的关键发行版。 Fedora 44 还包含了 Budgie 10.10、PHP 8.5、Ruby 4.0、Boost 1.90、Golang 1.26、CMake 4.0、GCC 16 和 LLVM 22，并改进了 Live Media 支持，增强了针对 Windows on Arm 笔记本的 AArch64 EFI 支持。

rss · Phoronix · Apr 28, 12:31

**背景**: Fedora 是由 Red Hat 赞助的免费开源 Linux 发行版，以其前沿软件和每六个月一次的发布周期而闻名。GNOME 50 是 GNOME 桌面环境的最新版本，最终移除了对 X11 的支持；KDE Plasma 6.6 是 KDE Plasma 桌面的最新迭代，提供了模块化组件架构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://release.gnome.org/50">Introducing GNOME 50 - GNOME Release Notes</a></li>
<li><a href="https://www.redhat.com/en/blog/announcing-fedora-44">Announcing Fedora 44 - redhat.com</a></li>

</ul>
</details>

**标签**: `#Linux`, `#Fedora`, `#GNOME`, `#KDE`, `#Open Source`

---

<a id="item-25"></a>
## [Proton 11.0 Beta 2 更新 VKD3D-Proton](https://www.phoronix.com/news/Proton-11.0-Beta-2) ⭐️ 7.0/10

Valve 发布了 Proton 11.0 Beta 2，更新了 VKD3D-Proton 组件，以改善通过 Steam Play 在 Linux 上运行的 Windows 游戏的 DirectX 12 兼容性。 此次更新增强了 Linux 上的游戏体验，尤其是对于现代游戏中日益常见的 DirectX 12 游戏。它通过扩展可玩游戏库，使 Linux 游戏社区和 Steam Deck 用户受益。 Proton 11.0 Beta 2 紧随 Beta 1 发布，后者基于 Wine 11.0 进行了更新。VKD3D-Proton 分支将 Direct3D 12 API 调用转换为 Vulkan，从而在 Proton 中实现 DirectX 12 支持。

rss · Phoronix · Apr 28, 11:00

**背景**: Proton 是 Valve 开发的兼容层，允许 Windows 游戏在 Linux 上运行。它集成了 Wine 和 VKD3D-Proton 等组件，将 DirectX 调用转换为 Vulkan。这使得 Linux 用户和 Steam Deck 拥有者无需原生移植即可畅玩大量 Windows 游戏。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/HansKristian-Work/vkd3d-proton">GitHub - HansKristian-Work/vkd3d-proton: Fork of VKD3D ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Proton_(compatibility_layer)">Proton (compatibility layer)</a></li>

</ul>
</details>

**标签**: `#Proton`, `#Linux Gaming`, `#VKD3D-Proton`, `#Wine`, `#Steam Play`

---

<a id="item-26"></a>
## [Ubuntu 澄清 AI 功能为可选且可通过 Snap 移除](https://www.phoronix.com/news/Ubuntu-AI-Kill-Switch-Opt-In) ⭐️ 7.0/10

Canonical 工程副总裁 Jon Seager 澄清，Ubuntu 即将推出的 AI 功能将仅通过 Snap 包提供，用户可选择安装，并通过卸载这些 Snap 来移除。 这一澄清回应了社区对隐私和控制的担忧，确保用户可以轻松禁用 AI 功能，而无需进行系统级更改。 AI 功能包括本地推理、代理系统工具和 AI 驱动的无障碍功能，所有功能初始均为可选，并可通过移除 Snap 来卸载。

rss · Phoronix · Apr 28, 10:25

**背景**: Ubuntu 是一个流行的 Linux 发行版。Snap 是 Canonical 开发的容器化软件包。此前有担忧认为 AI 集成将是强制且不可移除的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/software/operating-systems/ubuntus-ai-roadmap-revealed-universal-ai-kill-switch-and-forced-ai-integration-are-not-part-of-the-plan-cloud-tracking-local-inference-and-agentic-system-tools-take-center-stage">Ubuntu's AI roadmap revealed, universal AI 'kill switch' and ...</a></li>
<li><a href="https://www.omgubuntu.co.uk/2026/04/ubuntu-ai-features">Ubuntu is Getting AI Features in 2026 – Here's What's Planned</a></li>
<li><a href="https://www.gamingonlinux.com/2026/04/canonical-clarify-their-ai-for-plans-for-ubuntu-linux-opt-in-and-easy-to-remove/">Canonical clarify their AI for plans for Ubuntu Linux - opt ...</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：一些人赞赏可选方式，而另一些人仍对 Snap 的开销和 Canonical 的长期意图持怀疑态度。

**标签**: `#Ubuntu`, `#Linux`, `#AI`, `#Snap`, `#Canonical`

---

<a id="item-27"></a>
## [AMDXDNA 驱动为 Ryzen AI 引入硬件调度时间量子](https://www.phoronix.com/news/AMDXDNA-Hardware-Sched-Quant) ⭐️ 7.0/10

针对 Ryzen AI NPU 的 AMDXDNA 加速驱动正在准备一项硬件调度时间量子功能，以确保多用户公平访问。NPU 硬件调度器可为每个上下文强制执行固定时间片，默认量子为 30ms，可通过模块参数配置。 该功能解决了 NPU 调度中的多用户公平性问题，防止长时间运行的 AI 工作负载独占设备。这是 Ryzen AI 的一种新颖方法，可改善多租户环境中的 AI 工作负载管理。 硬件调度时间量子是 Ryzen AI NPU 的硬件能力，而非纯软件解决方案。默认时间量子为 30ms，可通过 time_quantum_ms 模块参数调整。

rss · Phoronix · Apr 28, 10:06

**背景**: NPU（神经网络处理单元）是用于加速 AI 推理任务的专用硬件。在多用户或多上下文场景中，如果没有适当的调度，单个长时间运行的工作负载可能会使其他工作负载缺乏计算资源。硬件调度时间量子在硬件层面引入时间片轮转以强制执行公平性，类似于操作系统中的 CPU 调度量子。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.phoronix.com/news/AMDXDNA-Hardware-Sched-Quant">AMDXDNA Driver Preps Hardware Scheduler Time Quantum For ...</a></li>
<li><a href="https://lkml.org/lkml/2026/4/15/1194">LKML: Lizhi Hou: [PATCH V2] accel/amdxdna: Add hardware ...</a></li>

</ul>
</details>

**标签**: `#AMD`, `#NPU`, `#scheduling`, `#AI`, `#Linux kernel`

---

<a id="item-28"></a>
## [Ubuntu 将在未来一年集成 AI 功能](https://www.phoronix.com/news/Ubuntu-AI-Features-2026) ⭐️ 7.0/10

Canonical 宣布计划在未来一年内将 AI 功能集成到 Ubuntu Linux 中，从 Ubuntu 26.04 LTS 发布后开始，重点放在本地推理和代理工作流上。 这标志着 Ubuntu 的战略转变，可能使本地 AI 在桌面和服务器上更易用，并巩固 Linux 生态系统在 AI 领域的地位。 AI 功能将包括默认的本地推理和对代理工作流的支持，Canonical 工程师将在未来一年进行集成工作。

rss · Phoronix · Apr 27, 10:30

**背景**: Ubuntu 26.04 LTS（代号 Resolute Raccoon）刚刚发布。Canonical 的 AI 推进旨在简化 GPU 计算栈的安装，这是 Linux 上本地 AI 用户的主要痛点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.phoronix.com/news/Ubuntu-AI-Features-2026">Ubuntu Linux Will Begin Landing AI Features Throughout The ...</a></li>
<li><a href="https://ubuntu.com/ai">Open source AI | Ubuntu</a></li>
<li><a href="https://www.theverge.com/tech/919411/canonical-ubuntu-linux-ai-features">Canonical lays out a plan for AI in Ubuntu Linux | The Verge</a></li>

</ul>
</details>

**标签**: `#Ubuntu`, `#AI`, `#Linux`, `#Canonical`, `#Operating Systems`

---

<a id="item-29"></a>
## [Google Meet 语音翻译功能扩展至移动端](https://simonwillison.net/2026/Apr/27/speech-translation-in-google-meet-is-now-rolling-out-to-mobile-d/#atom-everything) ⭐️ 6.0/10

Google Meet 的语音翻译功能此前仅支持桌面端，现已向 Android 和 iOS 设备推出，可在六种语言间实现近乎实时的音频翻译，并模仿原说话者的声音。 此次扩展将实时跨语言交流带到移动端，有望让多语言会议更加便捷，减少专业及个人场景中的语言障碍。 该功能目前支持英语、西班牙语、法语、德语、葡萄牙语和意大利语，仍处于 alpha 阶段，早期效果不一——在网页浏览器上运行成功，但在 iPhone 和 iPad 之间测试时未能生效。

rss · Simon Willison · Apr 27, 17:37

**背景**: Google Meet 的语音翻译利用 AI 生成覆盖原语音的音频翻译，并模仿说话者的语调和节奏。该功能最初于 2025 年在桌面端发布，2026 年 2 月正式上线。移动端扩展将其能力延伸至 Android 和 iOS 设备。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://support.google.com/meet/answer/16221730?hl=en&co=GENIE.Platform=Desktop">Learn about Speech Translation - Computer - Google Meet Help</a></li>
<li><a href="https://workspaceupdates.googleblog.com/2026/02/speech-translation-meet-ga.html">Speech translation in Google Meet now generally available for ...</a></li>
<li><a href="https://www.business-standard.com/technology/tech-news/google-meet-brings-real-time-speech-translation-to-android-ios-details-126042800295_1.html">Google Meet brings real-time speech translation to Android ...</a></li>

</ul>
</details>

**标签**: `#google meet`, `#speech translation`, `#mobile`, `#AI`

---

<a id="item-30"></a>
## [三星 Exynos 2600 推出 ENSS，移动端 AI 超分技术](https://www.ithome.com/0/944/691.htm) ⭐️ 6.0/10

三星宣布其 Exynos 2600 芯片组支持 Exynos Neural Super Sampling (ENSS)，这是一项 AI 驱动技术，结合了神经超采样和神经帧生成，可将低分辨率渲染画面进行超分并插帧，使运动画面更流畅。 ENSS 将桌面级的 AI 超分和帧生成技术引入移动设备，有望显著提升图形性能和能效。这可能为移动游戏带来公平竞争，并为设备端 AI 图形优化树立新标准。 据三星介绍，ENSS 允许 GPU 先渲染低分辨率画面，然后利用 AI 进行超分和插帧，从而降低 GPU 负载。搭载 ENSS 的 Exynos 2600 据称图形性能比竞争对手高 15%，并在 Basemark Power Board 基准测试中排名第一。

rss · IThome 日报 · Apr 28, 13:36

**背景**: AI 超分和帧插值是利用机器学习提升图像分辨率并在现有帧之间生成额外帧的技术，可改善视觉质量和流畅度。NVIDIA 的 DLSS 是 PC 端的知名例子，而三星的 ENSS 旨在为 Exynos 2600 等移动芯片带来类似优势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://semiconductor.samsung.com/technologies/processor/enss/">ENSS - Technologies | Samsung Semiconductor Global</a></li>
<li><a href="https://www.androidheadlines.com/2026/04/samsungs-exynos-2600-uses-ai-to-boost-graphics-and-its-a-lot-like-dlss-for-your-phone.html">Samsung's Exynos 2600 Uses AI to Boost Graphics, and It's a ...</a></li>
<li><a href="https://www.sammobile.com/2026/04/28/samsung-brings-ai-powered-graphics-optimization-to-the-exynos-2600/">Samsung brings AI-powered graphics optimization to the Exynos ...</a></li>

</ul>
</details>

**标签**: `#Samsung`, `#Exynos`, `#AI upscaling`, `#mobile GPU`, `#ENSS`

---

<a id="item-31"></a>
## [比亚迪汉 EV 闪充版：705 公里续航，9 分钟充满，起售价 17.98 万元](https://www.ithome.com/0/944/666.htm) ⭐️ 6.0/10

比亚迪于 2026 年 4 月 28 日发布了汉 EV 闪充版，宣称是全球最低能耗的 C 级轿车，CLTC 续航 705 公里，9 分钟充满，起售价 17.98 万元。 此次发布为中型电动轿车领域树立了快充和能效的新标杆，可能加速超快充技术的普及，并加剧电动汽车制造商之间的竞争。 该车搭载 69.07 千瓦时第二代刀片电池，百公里电耗 10.8 度，支持 5 分钟充好、9 分钟充饱，零下 30 度仅多 3 分钟。还可选装 1.2 万元的天神之眼 B 激光版辅助驾驶。

rss · IThome 日报 · Apr 28, 11:39

**背景**: C 级轿车指比亚迪汉这类中型轿车。“闪充版”采用比亚迪第二代刀片电池和闪充技术，可实现超快充电。CLTC 是中国轻型汽车测试循环，用于估算续航里程。“天神之眼”是比亚迪的先进辅助驾驶系统，分为 A、B、C 三档。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.qq.com/rain/a/20260428A082ZR00">比亚迪汉 EV 闪充版上市：17.98 万起，9 分钟充满，12 大升级香不香？</a></li>
<li><a href="https://auto.sina.com.cn/newcar/2026-04-28/detail-inhwaicx1572198.shtml">比亚迪汉EV闪充版上市 售价17.98万元起 - 新浪汽车</a></li>
<li><a href="https://chejiahao.autohome.com.cn/info/25365803">比亚迪汉EV闪充版上市，9分钟补充续航，售价17.98万元起</a></li>

</ul>
</details>

**标签**: `#EV`, `#BYD`, `#automotive`, `#fast charging`

---

<a id="item-32"></a>
## [比亚迪闪充站超 5500 座，覆盖 311 城](https://www.ithome.com/0/944/659.htm) ⭐️ 6.0/10

比亚迪在汉 EV 闪充版发布会上宣布，已在全国 311 座城市建成超过 5500 座闪充站，年底目标为 2 万座。公司还声称，第二代刀片电池可在 5 分钟内从 10%充至 70%，在零下 30°C 环境下从 20%充至 97%仅需约 12 分钟。 这一扩张显著缓解了里程焦虑，使比亚迪在超快充基础设施领域占据领先地位，可能加速电动汽车普及。低温性能的突破解决了行业关键痛点，使电动汽车在北方地区更具可行性。 比亚迪闪充站无需增容或挖地基，安装方式类似空调。公司还在加速高速公路网络覆盖，确保假期出行充电无忧。

rss · IThome 日报 · Apr 28, 11:08

**背景**: 闪充是指能在几分钟内补充大量电池容量的超快直流充电技术。比亚迪第二代刀片电池基于磷酸铁锂（LFP）化学体系，旨在支持高充电速率的同时保持安全性和长寿命。公司一直在积极建设自有充电网络以配合其电动汽车销售。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://byd.crazy-thursday.com/">比亚迪闪充站 · 全国追踪</a></li>
<li><a href="https://www.toutiao.com/article/7615994673844306438/">比亚迪闪充站分布及规划（含成都充电站点） - 今日头条</a></li>
<li><a href="https://news.qq.com/rain/a/20260316A052AZ00">比亚迪闪充站实地走访：4597座已落地，今年或远超2万座</a></li>

</ul>
</details>

**标签**: `#EV`, `#charging infrastructure`, `#BYD`, `#battery technology`

---

<a id="item-33"></a>
## [GCC 16.1 改进错误信息，新增实验性 HTML 输出](https://www.phoronix.com/news/GCC-16-Error-Messages) ⭐️ 6.0/10

GCC 16.1 作为 GCC 16 系列的第一个稳定版本，引入了增强的错误信息，默认启用层次化的 C++ 诊断，并新增了实验性的 HTML 输出选项用于编译器消息。 这些改进使 GCC 对开发者更加友好，减少了调试时间，并支持更好地集成到基于 Web 的工具和工作流中。 此前在 GCC 15 中实验性的层次化 C++ 错误信息现在默认启用，提供嵌套的要点输出，精确定位不匹配项。实验性的 HTML 输出选项允许以 HTML 格式生成诊断消息，便于在浏览器中查看。

rss · Phoronix · Apr 28, 13:13

**背景**: GCC（GNU 编译器套件）是一个广泛使用的开源编译器套件，支持 C、C++ 和 Fortran 等语言。错误信息对于开发者理解编译问题至关重要。SARIF（静态分析结果交换格式）是一种用于机器可读诊断输出的标准，GCC 从版本 13 开始支持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.redhat.com/articles/2026/04/28/gcc-16-improved-error-messages-sarif-output">New features in GCC 16: Improved error messages and SARIF output</a></li>
<li><a href="https://www.phoronix.com/news/GCC-16-Error-Messages">GCC 16's Improved Error Messages, Experimental HTML Output</a></li>

</ul>
</details>

**标签**: `#GCC`, `#compiler`, `#error messages`, `#HTML output`

---

<a id="item-34"></a>
## [7-Zip 26.01 在 Linux 上支持大页面](https://www.phoronix.com/news/7-Zip-26.01) ⭐️ 6.0/10

周一发布的 7-Zip 26.01 现在支持在 Linux 上使用 2MB 大页面，可为 7z、XZ、LZMA 和 LZMA2 格式提供约 10% 的压缩速度提升。该更新还引入了三个新的命令行选项（-spod、-spoc、-spor），用于控制解压时输出目录路径的生成。 这一性能提升对于经常压缩大文件的 Linux 用户意义重大，因为大页面减少了 TLB 未命中并提高了内存访问效率。这也表明 7-Zip 持续致力于为 Linux 平台进行优化。 大页面支持目前仅限于 2MB 页面，且仅对压缩操作有益，不解压。新的路径生成选项允许用户控制输出目录是镜像归档的内部结构还是使用扁平布局。

rss · Phoronix · Apr 28, 09:55

**背景**: 大页面是 2MB 或 1GB 的内存块，可减少转换后备缓冲区（TLB）中的条目数，从而提高内存密集型应用的性能。Linux 支持静态大页面和透明大页面（THP），后者会自动合并小页面。7-Zip 是一款流行的开源文件归档工具，以其高压缩比著称。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.phoronix.com/news/7-Zip-26.01">7-Zip 26.01 Now Allows Making Use Of Huge Pages On Linux For ...</a></li>
<li><a href="https://app.daily.dev/posts/7-zip-26-01-now-allows-making-use-of-huge-pages-on-linux-for-faster-compression-ixqzv0vvu">7-Zip 26.01 Now Allows Making Use Of Huge Pages On Linux...</a></li>
<li><a href="https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/6/html/performance_tuning_guide/s-memory-transhuge">5.2. Huge Pages and Transparent Huge Pages | Performance ...</a></li>

</ul>
</details>

**标签**: `#7-Zip`, `#Linux`, `#compression`, `#performance`

---

<a id="item-35"></a>
## [WayVNC 0.10 发布，支持 wlroots Wayland 合成器](https://www.phoronix.com/news/WayVNC-0.10-Released) ⭐️ 6.0/10

WayVNC 0.10 已发布，为使用 wlroots 库的 Wayland 合成器增加了新的 VNC 服务器功能。 此次更新改进了 Wayland 用户的远程桌面访问，随着 Wayland 的普及和 X11 协议的逐步淘汰，这一点至关重要。 WayVNC 0.10 是一个增量更新，专门为基于 wlroots 的合成器带来了 VNC 服务器的增强功能，但提供的内容中未详细说明具体新特性。

rss · Phoronix · Apr 28, 09:43

**背景**: Wayland 是一种显示服务器协议，旨在取代老旧的 X11 系统，提供更好的安全性和性能。wlroots 是一个模块化库，为构建 Wayland 合成器提供基础。WayVNC 是一个 VNC 服务器，允许通过 wlroots 远程访问 Wayland 会话。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/any1/wayvnc">GitHub - any1/ wayvnc : A VNC server for wlroots based Wayland...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Wlroots">Wlroots</a></li>

</ul>
</details>

**标签**: `#Wayland`, `#VNC`, `#wlroots`, `#Linux`, `#open-source`

---

<a id="item-36"></a>
## [Stratis Storage 3.9 新增在线加密/解密/重新加密功能](https://www.phoronix.com/news/Stratis-Storage-3.9-Released) ⭐️ 6.0/10

Red Hat 发布了 Stratis Storage 3.9，新增了存储池的在线加密、解密和重新加密功能，无需停机即可操作。 此次更新增强了 Linux 存储管理的安全灵活性，允许管理员在不中断服务的情况下更改加密密钥或对现有池启用加密，这对生产环境至关重要。 Stratis 基于 XFS、LUKS、Device Mapper 和 Clevis 构建，提供类似 ZFS/Btrfs 的功能。新的在线加密操作利用这些底层技术，可动态修改加密设置。

rss · Phoronix · Apr 28, 00:21

**背景**: Stratis 是一个 Linux 本地存储管理工具，简化了精简配置和快照等高级存储功能。它是 Red Hat 在 RHEL 中放弃 Btrfs 后创建的，采用分层方法构建在现有内核子系统之上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://stratis-storage.github.io/">Stratis Storage</a></li>
<li><a href="https://en.wikipedia.org/wiki/Device_mapper">Device mapper</a></li>

</ul>
</details>

**标签**: `#Linux`, `#storage`, `#Stratis`, `#encryption`, `#Red Hat`

---

<a id="item-37"></a>
## [英特尔酷睿 Ultra 5 250K Plus 以 219 美元提供出色 Linux 性价比](https://www.phoronix.com/review/intel-core-ultra-5-250k-plus) ⭐️ 6.0/10

Phoronix 评测了售价 219 美元的英特尔酷睿 Ultra 5 250K Plus，发现其在 Linux 上性价比出色。 这款高性价比 CPU 让高性能 Linux 计算更易获得，可能推动注重成本的用户和开发者采用。 Core Ultra 5 250K Plus 采用 Arrow Lake 架构，拥有 18 核（6 性能核+8 能效核+4 低功耗核）和 18 线程，基础频率 4.2 GHz，最高睿频 5.3 GHz。

rss · Phoronix · Apr 27, 15:06

**背景**: 英特尔 Arrow Lake 处理器于 2024 年底发布，是桌面 CPU 的新架构。Core Ultra 5 250K Plus 是一款面向预算有限但仍追求现代特性和良好性能用户的中端型号。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.intel.com/content/www/us/en/products/sku/245694/intel-core-ultra-5-processor-250k-plus-30m-cache-up-to-5-30-ghz/specifications.html">Intel® Core™ Ultra 5 processor 250K Plus</a></li>
<li><a href="https://www.techpowerup.com/cpu-specs/core-ultra-5-250k-plus.c4352">Intel Core Ultra 5 250K Plus Specs | TechPowerUp CPU Database</a></li>
<li><a href="https://www.techspot.com/specs/cpu/322328-intel-core-ultra-5-250k-plus.html">Intel Core Ultra 5 250K Plus Specs | TechSpot</a></li>

</ul>
</details>

**标签**: `#Intel`, `#CPU`, `#Linux`, `#hardware review`

---

<a id="item-38"></a>
## [AMD VPE 2.0 支持已合并到 Mesa 26.2](https://www.phoronix.com/news/AMD-VPE-2.0-Mesa) ⭐️ 6.0/10

针对未来 Radeon GPU 中的 AMD VPE 2.0 引擎的支持已合并到 Mesa 26.2 图形驱动开发代码中。 此更新为即将推出的 AMD 硬件做好了 Mesa 准备，支持 RGB 三平面格式和更多视频旋转等增强的视频处理功能。 此次合并未透露重大架构变化，但与上一版本相比，VPE 2.0 引入了 RGB 三平面支持和更多视频旋转功能。

rss · Phoronix · Apr 27, 10:10

**背景**: Mesa 是 OpenGL 和 Vulkan 等图形 API 的开源实现，将其转换为特定于供应商的硬件驱动程序。VPE（视频处理引擎）是 AMD GPU 中负责视频编解码和处理任务的硬件模块。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.phoronix.com/news/AMD-VPE-2.0-Mesa">AMD VPE 2 . 0 Support Merged For Mesa 26.2 - Phoronix</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mesa_(computer_graphics)">Mesa (computer graphics) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AMD`, `#Mesa`, `#GPU`, `#drivers`, `#open-source`

---

<a id="item-39"></a>
## [D7VK v1.8 改进 Vulkan 上的旧版 Direct3D 支持](https://www.phoronix.com/news/D7VK-1.8-Released) ⭐️ 6.0/10

D7VK v1.8 已发布，继续增强在 Vulkan API 上对旧版 Direct3D（D3D3 到 D3D7）的支持。 此更新提高了依赖早期 Direct3D API 的旧版 Windows 游戏和应用程序的兼容性，使使用 Steam Play/Proton 的 Linux 游戏玩家和软件保存工作受益。 D7VK 基于 DXVK（将 Direct3D 8/9/10/11 转换为 Vulkan），并将支持扩展到 Direct3D 3。1.8 版本为这些旧版 D3D 前端带来了增量修复和改进。

rss · Phoronix · Apr 27, 04:00

**背景**: DXVK 是一个开源转换层，将 Direct3D 8/9/10/11 调用转换为 Vulkan，使 Windows 游戏能够通过 Wine 或 Proton 在 Linux 上运行。D7VK 将此概念扩展到更旧的 Direct3D 版本（3-7），允许旧版 3D 应用程序在现代系统上使用。Valve 开发的 Proton 集成了 Wine 和 DXVK/D7VK，在 Linux 上提供无缝的 Windows 游戏兼容性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DXVK">DXVK</a></li>
<li><a href="https://en.wikipedia.org/wiki/Steam_Play_Proton">Steam Play Proton</a></li>

</ul>
</details>

**标签**: `#Vulkan`, `#Direct3D`, `#compatibility`, `#gaming`, `#open-source`

---