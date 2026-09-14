# 图像生成与交付

本文件是输入顺序、输出目录、母版思考、排版与装饰设计和一体生成的执行真源。

## 运行目录

```text
output/tactile/<run-id>/
  inputs/                 # 来源副本，不修改用户原图
  analysis/
    creative-brief.md
    source-manifest.json
    generation-prompt.txt
    readback.md
  master/                 # 可选的无字预览或母版方案
  final/                  # 图像与排版一体化的完成海报
```

不得把任务产物、缓存或下载图片写入技能包。

## 图像角色与调用

照片转化默认使用 edit：

```text
Image 1 — SOURCE / EDIT TARGET：材质、对象身份和摄影可信度的来源
Image 2 — STYLE BOARD：整体迁移材质叙事、编辑克制、比例、留白与精调程度
Image 3+ — SUPPORT：只使用简报逐张点名的事实
```

必须把所有角色对应的文件实际传给图像工具。不得在提示词中声称“参考 Image 2”却没有传入，或把九张风格板误当成九宫格输出模板。

概念生图没有来源照片时，可以只使用风格板；提示词必须声明风格板不提供品牌、商品、地点和文案事实。

## 第一阶段：视觉母版方案

先把母版作为独立的视觉设计段写清，不让文字或装饰承担构图修补。构图风险高时，可以用此段先生成无字预览；正常情况下不必输出中间图，直接在第二阶段与排版设计段组合生成。

```text
Create one portrait editorial visual master about [主题/概念].
Use [主材质] and its physical property [属性] as the visual metaphor for [语义].
Image roles: Image 1 supplies only [2–3 material facts / identity anchors]; Image 2 is a style board and supplies only material-led abstraction, editorial restraint, proportion, and negative-space discipline.
Primary transformation: [裁切、尺度、面积重分配或重组] makes [唯一接触关系] the single focal event.
Remove or crop away [场景信息], roughly 50–70% of recognizable context unless recognition is required.
Show believable scale, directional side light, surface depth, irregular edges, local sharpness, and restrained grain.
Use [3–5 色] with one dominant light-dark relation and purposeful negative space.
Use invisible alignment logic and information zones; do not render grid lines, guides, registration marks, coordinate lines, bounding boxes, or layout scaffolding.
The background must actively form a color field, negative shape, tonal cut, or continuous rebuilt space.
Create one finished poster background, not a 3x3 grid, mood board, contact sheet, product packshot, or collage.
Do not copy content, brands, symbols, or layouts from the style board. Avoid generic marble luxury, neon cyberpunk, uniform grunge, repeating texture, plastic CGI gloss, and decorative clutter.
```

若需要实际生成无字预览，再追加 `Render no typography, letters, numbers, logos, watermarks, signatures, labels, or pseudo-text.`。只写当前方案真正使用的内容，不要把评分表、失败案例、几十个禁词或内部步骤全部回灌给模型。

## 第二阶段：排版与装饰设计、一体生成

母版逻辑通过硬门后，再完成包含文字和必要装饰元素的排版方案并生成最终海报：

1. 根据母版的材质、色域、光线与气质，选择环境中真实存在的字体、字重、宽窄和颜色；字体可与母版融合或形成克制反差，但不得成为无依据的默认样式。
2. 根据视觉重心、唯一焦点、负空间和动线确定文字区域、字号、行长、断行与对齐；文字应形成平衡、延伸或边界关系，不是简单贴在剩余空白。
3. 以内部网格建立共同轴、边距和层级；成品不显示网格。
4. 选择真正承担结构功能的装饰元素，例如分隔线、色块、括号、编号、圆点或抽象标记；明确其对齐、分区、节奏、指向或身份作用，不做填空式点缀。
5. 把准确文案、字体方案和装饰系统加入最终图像生成/编辑提示，使图像和排版默认在同一成图阶段一并生成。
6. 导出后打开最终文件，检查中文断行、字形、字体真实性、颜色对比、装饰必要性、边缘距离和手机缩略图。

字体设计段至少写清：

```text
Typography: render the exact copy [标题 / 副标题 / 元信息] using [真实字体或明确字体系统], with [字重、宽窄、字距和行距].
Choose text colors that respond to [母版色域 / 高光 / 材质] with deliberate, readable contrast.
Place and size the type according to [视觉重心、焦点、负空间和动线], using [共同轴 / 对齐关系] so typography and image feel composed as one system.
Use only [必要装饰元素], each serving [对齐 / 分区 / 节奏 / 指向 / 身份识别]; match their color, weight, scale, and placement to the visual master.
Keep small text clean and fully legible. Render no extra letters, pseudo-text, invented logos, or labels.
```

一体生成是默认路径，不等于降低准确性。若工具无法可靠呈现指定真实字体或逐字文案，保持既定的字体风格、颜色、位置和大小，用真实字体局部替换错误字区；不要重新退化成与母版无关的通用叠字。

## 读回与迭代

成图后只检查：

1. 材质是否发生抽象和尺度重构，而非统一滤镜；
2. 背景是否主动参与构图；
3. 真实表面是否有方向、光线和深度；
4. 字体选择与颜色是否匹配母版，文字位置与大小是否回应视觉重心；
5. 装饰元素是否具有结构功能，图形、摄影与整套排版是否共同服务同一概念，文案、身份锚点和来源边界是否准确。

把最明显的 0–3 个问题写入 `analysis/readback.md`。局部字形或边缘问题可以编辑当前成图；概念、材质、主体尺度或主构图失败时回到来源图重做，不在失败结构上叠补丁。
