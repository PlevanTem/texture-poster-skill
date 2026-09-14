# 图源、证据与权利边界

联网找图不是“找到能下载的图”，而是建立可追溯、适合转译且权利状态明确的输入。

## 来源优先级

1. 用户自有或明确授权的摄影、品牌资产、press kit。
2. 品牌官网的产品页、媒体中心或官方社交账号。
3. 政府、博物馆、机构和可靠媒体页面。
4. 有清晰许可的图库或公共版权资源。
5. 聚合站、转载页和搜索缩略图只作线索；不能冒充官方来源。

涉及当前品牌文案、参数、材料、产地或可持续声明时，必须查品牌官网或一手资料。无法确认的内容不进入海报。

## 图像适配门槛

每张候选图先判断角色：

- `texture-evidence`：分辨率与细节足以承担材质采样。
- `structure-evidence`：只能证明轮廓、包装结构或接触关系，不能放大成高分辨率纹理。
- `reject`：来源不明、压缩严重、关键主体被遮挡，或无任何不可替代事实。

低清素材可以作为结构证据，但生成的微观纹理必须标记为模型补充，不能声称来自原图。不要通过锐化或放大伪造来源精度。

## 来源清单

每个任务保存 `analysis/source-manifest.json`：

```json
{
  "accessed_at": "YYYY-MM-DD",
  "sources": [
    {
      "id": "SRC-01",
      "page_url": "https://...",
      "asset_url": "https://...",
      "local_file": "inputs/SRC-01.ext",
      "role": "texture-evidence",
      "observed_facts": ["..."],
      "retained_facts": ["..."],
      "removed_context": ["..."],
      "generated_additions": [],
      "rights_status": "authorized | open-license | public-web-experiment-only | unknown",
      "sha256": "..."
    }
  ]
}
```

`generated_additions` 必须与照片事实分开记录。SHA-256 用于证明本地输入是哪一个文件，不代表拥有版权。

## 商用判断

- `authorized`：有权利方明确授权，可按授权范围使用。
- `open-license`：保存具体许可、作者和署名要求；仍需检查商标、人物肖像与衍生使用限制。
- `public-web-experiment-only`：公开可访问，但未发现允许独立商业再利用的许可。只能作为内部、非官方、转化性实验输入。
- `unknown`：不得作为正式投放依据，先替换或确认授权。

“来自官网”不等于“可以商用”。README 案例均为实验作品；正式品牌投放必须换成授权资产或获得权利方确认。
