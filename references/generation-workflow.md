# 图像生成与交付

本文件是输入顺序、输出目录、提示词和两阶段交付的执行真源。

## 运行目录

```text
output/tactile/<run-id>/
  inputs/                 # 来源副本，不修改用户原图
  analysis/
    creative-brief.md
    source-manifest.json
    generation-prompt.txt
    readback.md
  master/                 # 无字视觉母版
  final/                  # 完成海报
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

## 第一阶段：无字母版

提示词保持为一个统一艺术方向：

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
Render no typography, letters, numbers, logos, watermarks, signatures, labels, or pseudo-text.
Do not copy content, brands, symbols, or layouts from the style board. Avoid generic marble luxury, neon cyberpunk, uniform grunge, repeating texture, plastic CGI gloss, and decorative clutter.
```

只写当前方案真正使用的内容。不要把评分表、失败案例、几十个禁词或内部步骤全部回灌给模型。

## 第二阶段：排版

母版通过硬门后再排版：

1. 复制母版到 `final/`，保留原始无字文件。
2. 使用可控排版工具与真实字体写入准确文案。
3. 以内部网格建立共同轴、边距和层级；成品不显示网格。
4. 检查中文断行、字形、字体回退、边缘距离和手机缩略图。
5. 导出后打开最终文件读回。

若用户明确接受快速探索，可让图像模型直接生成极少文字，但必须把文字错误风险写入交付说明。品牌投放、活动信息、产品参数和中文长文默认走精确排版。

## 读回与迭代

成图后只检查：

1. 材质是否发生抽象和尺度重构，而非统一滤镜；
2. 背景是否主动参与构图；
3. 真实表面是否有方向、光线和深度；
4. 图形、摄影与排版是否共同服务同一概念；
5. 文案、身份锚点和来源边界是否准确。

把最明显的 0–3 个问题写入 `analysis/readback.md`。局部字形或边缘问题可以编辑当前成图；概念、材质、主体尺度或主构图失败时回到来源图重做，不在失败结构上叠补丁。
