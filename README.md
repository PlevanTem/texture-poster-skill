<div align="center">

# Texture Poster

**材质肌理海报 Skill**

把普通照片、产品图或品牌主题转译成以真实材质肌理承担概念的编辑海报。

[简体中文](README.md) · [English](README.en.md) · [Gallery](https://plevantem.github.io/texture-poster-skill/)

[![GitHub Stars](https://img.shields.io/github/stars/PlevanTem/texture-poster-skill?style=social)](https://github.com/PlevanTem/texture-poster-skill/stargazers)
![微信 lelouchdbf](https://img.shields.io/badge/WeChat-lelouchdbf-07C160?style=flat-square&logo=wechat&logoColor=white)

</div>

它解决的不是“给照片加一层纹理”，而是先删掉无关场景，再让材质肌理、尺度、光线、负空间和准确排版共同传达一个隐性联想。

![五个品牌原图转材质肌理海报对照](examples/brand-source-studies/source-to-poster-contact-sheet.png)

## 如何安装

### 方法 1：使用 [`npx skills`](https://github.com/vercel-labs/skills)（推荐）

一次安装到 Codex 和 Claude Code 的用户级 Skill 目录：

```bash
npx skills add PlevanTem/texture-poster-skill --global --agent codex --agent claude-code --copy --yes
```

只使用其中一个 Agent 时，删除另一项 `--agent` 即可。安装后新开一个会话，让 Agent 重新发现 Skill。

### 方法 2：手动安装

1. 下载本仓库 ZIP 并解压，确认目录内直接包含 `SKILL.md`。
2. 将完整的 `texture-poster-skill` 文件夹复制到对应目录：

| Agent | Windows | macOS / Linux |
| --- | --- | --- |
| Codex | `C:\Users\<用户名>\.codex\skills\texture-poster-skill` | `~/.codex/skills/texture-poster-skill` |
| Claude Code | `C:\Users\<用户名>\.claude\skills\texture-poster-skill` | `~/.claude/skills/texture-poster-skill` |

3. 新开会话并用 `$texture-poster-skill` 调用。

## 快速开始

安装后，附上原图，并像提出真实设计委托一样说明业务目标、受众、投放场景、传播主题、准确文案和品牌限制。材质选择、画面取舍与视觉转译由 Skill 自行完成。

### 1. 户外服饰：旧衣修补计划

```text
附件是品牌的一款旧款羊羔绒夹克商品图。请用 $texture-poster-skill 为秋季“旧衣修补计划”制作一张 4:5 社交媒体预热海报。
受众是购买过品牌外套、关注耐用性与环保的 25–40 岁用户。核心信息不是省钱，而是让一件衣服继续陪伴使用者。标题“留下”，副标题“温暖不必从崭新开始”；语气克制，不要环保说教感。
```

### 2. 茶饮：区域风味新品预热

```text
附件是奶盖红茶新品图。请用 $texture-poster-skill 为区域限定新品制作一张开售前预热海报，用于门店公众号和小红书。
希望城市消费者感知到原料与山地风物的联系，但不要直白画茶山或罗列配料。标题“风物入水”，副标题“山里的风物，换一种方式抵达杯中”，竖版 4:5；整体要有食欲，但不能像促销菜单。
```

### 3. 身体护理：会员月刊专题封面

```text
附件是品牌的琥珀玻璃身体护理产品图。请用 $texture-poster-skill 为会员月刊“每日护理”专题制作一张 4:5 编辑封面。
读者已经熟悉产品，本次不承担电商卖点说明。希望表达“每天重复的动作，也能让时间发生”，主标题“复苏”；整体安静、克制，保持品牌的理性气质。
```

### 4. 消费电子：新品发布会主视觉

```text
附件是即将发布的铝制家用音箱产品图。请用 $texture-poster-skill 制作一张用于发布会预告和社交传播的 4:5 主视觉。
受众是设计从业者与高端音响用户。核心表达是“声音没有形状，但会在空间留下方向”。主标题“定形”，副标题“给听不见的形状”；画面需要高级、精确，不要做参数说明页。
```

### 5. 运动营养：长距离训练专题

```text
附件是品牌能量胶的包装图。请用 $texture-poster-skill 为马拉松训练营的“补给时机”专题制作一张 4:5 内容封面。
受众是目标完赛时间 3–5 小时的跑者，本次不强调折扣或口味。核心信息是“能量被稳定携带，并在身体需要时释放”。标题“穿过”，副标题“为下一段路留下能量”；视觉要有运动感，但不要使用常见速度线。
```

## 它会做什么

- 把输入拆成材质事实、身份锚点和可删除场景，而不是默认保留整张照片。
- 用一个“物理属性 → 概念感知”的命题选择材质，避免把肌理当装饰。
- 通过微距、尺度跃迁、面积重分配、接触线或相变建立唯一焦点。
- 先按无字标准完成视觉母版判断，再让匹配母版的真实字体和必要装饰元素与图像在最终成图中一体生成。
- 用不可见网格组织对齐、留白和阅读顺序，但不把辅助线画进成品。
- 为网页素材记录来源、访问日期、用途、模型补充内容和权利状态。
- 用五项硬门与 100 分量表区分完成稿、方向稿和失败稿。

## 工作方式

```text
输入：图片或文字
      ↓
识神：分析概念动词 + 材质物理属性
      ↓
减法：保留 2–3 个事实 / 删除 50%–70% 场景
      ↓
聚焦：一个焦点 + 一个实验动作 + 不可见网格
      ↓
设计：视觉母版方案 → 五项硬门
      ↓
排版：字体/颜色/位置/大小 + 必要装饰 → 匹配母版重心
      ↓
成图：图像与整套排版一体生成 → 逐字与缩略图检查
      ↓
校验：80 分以上且无硬失败 → 交付
```

完整执行入口见 [SKILL.md](SKILL.md)。

## 五个品牌实验

以下均为非官方实验作品，用于检验同一机制在五个赛道能否成立；不是品牌委托，也不代表已取得商业发布授权。

| 户外服饰 | 茶饮 | 身体护理 |
| --- | --- | --- |
| ![Patagonia 材质海报](examples/brand-source-studies/patagonia.png) | ![去茶山材质海报](examples/brand-source-studies/quchashan.png) | ![Aesop 材质海报](examples/brand-source-studies/aesop.png) |
| 羊羔绒成为“留下”的时间地貌 | 奶盖与茶液成为“风物入水”的边界 | 琥珀玻璃与气泡成为日常的时间容器 |

| 消费电子 | 运动营养 |
| --- | --- |
| ![Bang & Olufsen 材质海报](examples/brand-source-studies/bang-olufsen.png) | ![Maurten 材质海报](examples/brand-source-studies/maurten.png) |
| 拉丝铝的曲率替无形声音“定形” | 热封膜与水凝胶形成“包裹—穿过” |

每个案例的原图页面、直链、保留事实、删除内容、模型补充和 SHA-256 见 [案例索引](examples/brand-source-studies/case-index.json)；转译判断见 [案例复盘](references/case-studies.md)。

## 适用场景

| 场景 | 适合解决的问题 |
| --- | --- |
| 品牌概念海报 | 不直接陈列产品，用材质物理属性表达品牌命题 |
| 新品发布与活动主视觉 | 从产品原图提炼一个有辨识度的视觉母题 |
| 产品材质肌理叙事 | 放大面料、玻璃、金属、液体、膜材等真实表面证据 |
| 编辑封面与社交内容 | 在手机缩略图中建立单一焦点和清晰明暗关系 |
| 文化与自然主题 | 将地貌、建筑、植物或手工材料转成隐性的概念联想 |

它不是电商白底主图、常规磨皮调色或信息密集长图工具，也不用于复制某张标杆的具体构图。

## 输入建议

最有效的输入通常包含：

- 一张有真实表面细节的高分辨率照片；
- 一句传播目标，而不是一串风格词；
- 必须准确出现的标题、副标题和品牌限制；
- 对“还要不要认出原对象”的明确要求。

低清图只能证明包装或轮廓时，技能会把它标为 `structure-evidence`，不会假装其中存在可采样的微观纹理。

## 质量标准

| 硬门槛 | 通过标准 | 失败信号 |
| --- | --- | --- |
| 视觉传达效果 | 图像本身已通过裁切、尺度、明暗、色域、层次与动线形成主动后期美学 | 仍是普通照片、统一滤镜或等待文字补救的背景图 |
| 缩略图 | 缩到手机预览仍只有一个焦点，且大面积明暗关系清楚 | 多个焦点争抢，第一眼不知道看哪里 |
| 材质不可替换 | 所选材质的物理属性直接表达主题，换成其他材质会破坏概念 | 纸、石、金属或水互换后仍不影响表达 |
| 减法 | 无需识别原对象时，约 50%–70% 的环境信息已被删除或重组 | 产品和场景几乎原样保留，只叠加文字与噪点 |
| 真实性 | 尺度、方向、光线、粗糙度和空间深度可信 | 平铺贴图、重复噪点或塑料 CGI 感 |

五项必须全部通过。完整海报还需达到 80/100，才作为完成稿交付。

详见 [质量门控](references/quality-gates.md)。

## 目录

```text
texture-poster-skill/
├── SKILL.md                       # Agent 的主执行入口与核心合同
├── README.md                      # 中文使用说明
├── README.en.md                   # English documentation
├── artifact-template.json         # 图像模板类型、标杆图与预览图声明
├── agents/
│   └── openai.yaml                # 展示名称、图标、默认提示词与调用策略
├── assets/
│   ├── reference.png              # 九张标杆组成的风格板，不是构图模板
│   └── preview.png                # Skill 列表与画廊预览图
├── references/
│   ├── creative-brief.md           # 生成前的概念与材质简报
│   ├── art-direction.md            # 材质、光线、色彩与不可见网格方法
│   ├── generation-workflow.md      # 母版思考、排版与装饰设计、一体生成与读回
│   ├── source-and-rights.md        # 图源记录与商用权利边界
│   ├── quality-gates.md            # 五项硬门、评分表与失败修正
│   └── case-studies.md             # 五个品牌实验的转译复盘
├── examples/
│   └── brand-source-studies/
│       ├── source-to-poster-contact-sheet.png  # 五组原图—成图对照
│       ├── case-index.json                    # 来源、取舍、补充与文件校验信息
│       └── *.png                              # 五张完成海报
└── scripts/
    └── validate_package.py          # Agent 内部运行的包结构与案例校验
```

## 使用边界

技能包中的五个品牌案例使用公开网页图片做内部、非官方、转化性测试。公开可访问不等于拥有商用权。正式投放前，使用品牌授权的 press kit、用户自有摄影或具有明确许可的图片，并核对商标、人物肖像与衍生使用范围。
