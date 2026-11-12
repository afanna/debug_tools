```cardspec
{
  "title": "渡人先渡己",
  "description": "自爱圆满，天地同尘",
  "suggestSize": "2x2",
  "imageDomainWhitelist": [
    "hag-ability-test.obs.cn-north-1.myhuaweicloud.com",
    "lfcontentcenterdev.hwcloudtest.cn",
    "hagres-drcn.dbankcdn.com"
  ]
}
```
```genui
{"version":"v0.9","createSurface":{"surfaceId":"surface_card","catalogId":"ohos.a2ui.extended.catalog.form"}}
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Column","children":["__layout__root__static_header","__layout__root__static_body"],"itemMargin":6.0,"styles":{"width":"matchParent","height":"matchParent","padding":{"top":12.0,"bottom":12.0,"left":0,"right":0},"borderRadius":20.0,"clip":true,"alignItems":"start","justifyContent":"start","linearGradient":{"direction":"RightBottom","colors":[["#FFDBCCFF",0],["#FFF6F2FF",1]]}}},{"id":"__layout__root__static_header","component":"Column","children":["header"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","padding":{"left":12.0,"right":12.0},"height":16.0},"itemMargin":0},{"id":"header","component":"Column","children":["header__static_title"],"itemMargin":0.0,"styles":{"width":"matchParent","height":16.0,"alignItems":"start","justifyContent":"start","flexShrink":0}},{"id":"header__static_title","component":"Text","content":"向内修爱","styles":{"fontSize":12.0,"fontWeight":400,"lineHeight":1.3333333333333333,"maxLines":1,"height":16.0,"width":"matchParent","flexShrink":0,"fontColor":"#FF563D99","textOverflow":"clip","wordBreak":"normal"}},{"id":"__layout__root__static_body","component":"Column","children":["body"],"itemMargin":6.0,"styles":{"width":"matchParent","layoutWeight":1,"alignItems":"start","justifyContent":"end","padding":{"left":12.0,"right":12.0}}},{"id":"body","component":"Column","children":["body__static_item0","body__static_divider0","body__static_item1"],"itemMargin":12.0,"styles":{"width":"matchParent","height":91.0,"alignItems":"start","justifyContent":"start","flexShrink":0}},{"id":"body__static_item0_primaryText","component":"Text","content":"渡人先渡己","styles":{"fontSize":12.0,"fontWeight":500,"lineHeight":1.3333333333333333,"maxLines":1,"height":16.0,"width":"matchParent","flexShrink":1,"fontColor":"#FF563D99","textOverflow":"ellipsis","constraintSize":{"minWidth":0},"wordBreak":"normal"}},{"id":"body__static_item0_secondaryText","component":"Text","content":"先把自己活成一道光，黑暗自会循光而来","styles":{"fontSize":10.0,"fontWeight":400,"lineHeight":1.3,"maxLines":1,"height":13.0,"width":"matchParent","flexShrink":1,"fontColor":"#99563D99","textOverflow":"ellipsis","constraintSize":{"minWidth":0},"wordBreak":"normal"}},{"id":"body__static_item0_main","component":"Column","children":["body__static_item0_primaryText","body__static_item0_secondaryText"],"itemMargin":4.0,"styles":{"height":33.0,"alignItems":"start","justifyContent":"start","flexShrink":1,"layoutWeight":1,"constraintSize":{"minWidth":0}}},{"id":"body__static_item0_badge","component":"Text","content":"1","styles":{"fontSize":10.0,"fontWeight":500,"lineHeight":1.6,"maxLines":1,"height":16.0,"width":16.0,"flexShrink":0,"fontColor":"#FF563D99","textAlign":"center","backgroundColor":"#33563D99","borderRadius":8.0,"textOverflow":"clip","wordBreak":"normal"}},{"id":"body__static_item0_text","component":"Row","children":["body__static_item0_main"],"itemMargin":0.0,"styles":{"height":33.0,"layoutWeight":1,"alignItems":"center","flexShrink":0,"constraintSize":{"minWidth":0}}},{"id":"body__static_item0","component":"Row","children":["body__static_item0_badge","body__static_item0_text"],"itemMargin":8.0,"styles":{"width":"matchParent","height":33.0,"alignItems":"center","flexShrink":0}},{"id":"body__static_divider0","component":"Divider","styles":{"width":"matchParent","height":1.0,"strokeWidth":1.0,"flexShrink":0,"color":"#1F563D99"}},{"id":"body__static_item1_primaryText","component":"Text","content":"爱是向内修出的内丹","styles":{"fontSize":12.0,"fontWeight":500,"lineHeight":1.3333333333333333,"maxLines":1,"height":16.0,"width":"matchParent","flexShrink":1,"fontColor":"#FF563D99","textOverflow":"ellipsis","constraintSize":{"minWidth":0},"wordBreak":"normal"}},{"id":"body__static_item1_secondaryText","component":"Text","content":"自己未曾炼成，给出的只是半剂药","styles":{"fontSize":10.0,"fontWeight":400,"lineHeight":1.3,"maxLines":1,"height":13.0,"width":"matchParent","flexShrink":1,"fontColor":"#99563D99","textOverflow":"ellipsis","constraintSize":{"minWidth":0},"wordBreak":"normal"}},{"id":"body__static_item1_main","component":"Column","children":["body__static_item1_primaryText","body__static_item1_secondaryText"],"itemMargin":4.0,"styles":{"height":33.0,"alignItems":"start","justifyContent":"start","flexShrink":1,"layoutWeight":1,"constraintSize":{"minWidth":0}}},{"id":"body__static_item1_badge","component":"Text","content":"2","styles":{"fontSize":10.0,"fontWeight":500,"lineHeight":1.6,"maxLines":1,"height":16.0,"width":16.0,"flexShrink":0,"fontColor":"#FF563D99","textAlign":"center","backgroundColor":"#33563D99","borderRadius":8.0,"textOverflow":"clip","wordBreak":"normal"}},{"id":"body__static_item1_text","component":"Row","children":["body__static_item1_main"],"itemMargin":0.0,"styles":{"height":33.0,"layoutWeight":1,"alignItems":"center","flexShrink":0,"constraintSize":{"minWidth":0}}},{"id":"body__static_item1","component":"Row","children":["body__static_item1_badge","body__static_item1_text"],"itemMargin":8.0,"styles":{"width":"matchParent","height":33.0,"alignItems":"center","flexShrink":0}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"state":{"ready":true}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "制作一张静态文字卡片，展示以下内容：世人皆向外求爱，不知爱是向内修出的内丹。自己未曾炼成，给出的也只是半剂药。先把自己活成一道光，黑暗自会循光而来——那才是真正的慈悲。渡人先渡己，自爱圆满，天地同尘。\n本轮卡片静态内容（用作展示的外部事实）：世人皆向外求爱，不知爱是向内修出的内丹。自己未曾炼成，给出的也只是半剂药。先把自己活成一道光，黑暗自会循光而来——那才是真正的慈悲。渡人先渡己，自爱圆满，天地同尘。",
  "size": "2x2",
  "appVersion": "11.7.8.342",
  "eventCandidates": [],
  "dataModelSchema": {
    "data": {}
  },
  "assetCandidates": []
}
```
```effectivecapabilities
{
  "data": [],
  "event": [],
  "asset": []
}
```
```removedcapabilities
[]
```
```generationplan
{
  "candidateDataBindings": [],
  "candidateEventCandidates": [],
  "candidateAssetIds": []
}
```
```meta
{
  "apiVersion": "v1",
  "taskSpecVersion": "task-spec-v1",
  "cardSpecVersion": "card-spec-v1",
  "dslProtocolVersion": "v0.9",
  "skillVersion": "skill-widget-v1",
  "protocolProfileId": "a2ui-form-rom6.0-v1",
  "capabilityRegistryVersion": "app-11.7.7.300_rom-7.0",
  "artifactSchemaVersion": "widget-artifact-v2",
  "generationMode": "create",
  "artifactId": "4673e57c-df93-4948-b748-f61b34c288c0",
  "createdAt": 1793951103209
}
```
```designcompactdsl
["root","Layout",{"layout":"S-static-content"},["header","body"]]
["header","SingleLineTitle",{"title":"向内修爱"}]
["body","TextList",{"items":[{"primaryText":"渡人先渡己","secondaryText":"先把自己活成一道光，黑暗自会循光而来"},{"primaryText":"爱是向内修出的内丹","secondaryText":"自己未曾炼成，给出的只是半剂药"}]}]
["/state/ready",true]
```
```request
{
  "content": {
    "size": "2x2",
    "functionName": "generateWidgetCardCompactDsl",
    "romVersion": "HLS-AL00 7.0.0.111",
    "candidateAssetIds": [],
    "candidateEventCandidates": [],
    "bundleName": "com.huawei.genui",
    "description": "自爱圆满，天地同尘",
    "userQuery": "制作一张静态文字卡片，展示以下内容：世人皆向外求爱，不知爱是向内修出的内丹。自己未曾炼成，给出的也只是半剂药。先把自己活成一道光，黑暗自会循光而来——那才是真正的慈悲。渡人先渡己，自爱圆满，天地同尘。\n本轮卡片静态内容（用作展示的外部事实）：世人皆向外求爱，不知爱是向内修出的内丹。自己未曾炼成，给出的也只是半剂药。先把自己活成一道光，黑暗自会循光而来——那才是真正的慈悲。渡人先渡己，自爱圆满，天地同尘。",
    "title": "渡人先渡己",
    "candidateDataBindings": []
  },
  "deviceInfo": {
    "countryCode": "CN",
    "deviceFormation": "HDSpeaker",
    "deviceType": 0,
    "locale": "zh-CN",
    "phoneType": "HLS-AL00",
    "prdVer": "11.7.8.342",
    "sysVer": "EmotionUI_9.0.0",
    "time": "20261102012654770"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q441-000",
    "isNew": true,
    "sessionId": "batch-dd0b00bc"
  },
  "userAuth": {
    "user": {}
  },
  "utterance": {
    "original": "",
    "type": "text"
  },
  "version": "1.0",
  "size": "2x2",
  "functionName": "generateWidgetCardCompactDsl",
  "romVersion": "HLS-AL00 7.0.0.111",
  "candidateAssetIds": [],
  "candidateEventCandidates": [],
  "bundleName": "com.huawei.genui",
  "description": "自爱圆满，天地同尘",
  "userQuery": "制作一张静态文字卡片，展示以下内容：世人皆向外求爱，不知爱是向内修出的内丹。自己未曾炼成，给出的也只是半剂药。先把自己活成一道光，黑暗自会循光而来——那才是真正的慈悲。渡人先渡己，自爱圆满，天地同尘。\n本轮卡片静态内容（用作展示的外部事实）：世人皆向外求爱，不知爱是向内修出的内丹。自己未曾炼成，给出的也只是半剂药。先把自己活成一道光，黑暗自会循光而来——那才是真正的慈悲。渡人先渡己，自爱圆满，天地同尘。",
  "title": "渡人先渡己",
  "candidateDataBindings": []
}
```
```repair-1
{
  "modelGeneratedCompactDsl": "[\"root\",\"Layout\",{\"layout\":\"S-static-content\"},[\"header\",\"body\"]]\n[\"header\",\"SingleLineTitle\",{\"title\":\"向内修爱\"}]\n[\"body\",\"EmphasisText\",{\"mainText\":\"爱是向内修出的内丹；自己未曾炼成，给出的只是半剂药\",\"secondaryText\":\"先把自己活成一道光，黑暗自会循光而来\"}]\n[\"/state/ready\",true]",
  "generatedDsl": "",
  "validationErrors": [
    {
      "stage": "validation",
      "code": "COMPACT_DSL_VALIDATION_FAILED",
      "message": "COMPACT_STATIC_TEXT_CAPACITY: body: body.mainText 完整文字需要 5 行，126vp 区域仅允许 2 行；请保持已接受文字与字号，换用更合适的组件；Plan阶段才能忠实精简。",
      "compactDiagnostics": [
        {
          "code": "COMPACT_STATIC_TEXT_CAPACITY",
          "validationClass": "semantic",
          "category": "layout",
          "severity": "error",
          "message": "COMPACT_STATIC_TEXT_CAPACITY: body: body.mainText 完整文字需要 5 行，126vp 区域仅允许 2 行；请保持已接受文字与字号，换用更合适的组件；Plan阶段才能忠实精简。",
          "legacyMessage": "COMPACT_STATIC_TEXT_CAPACITY: body: body.mainText 完整文字需要 5 行，126vp 区域仅允许 2 行；请保持已接受文字与字号，换用更合适的组件；Plan阶段才能忠实精简。",
          "expected": {
            "completeTextFits": true,
            "fontSizeUnchanged": true
          },
          "fixHint": "按组件固定文字规格及实际可用宽度修复被指出的字段；保持已接受文字与对象归属，必要时更换静态语义组件或重新分配主副字段；不修改字体、行高或固定间距，不用maxLines隐藏内容。"
        }
      ]
    }
  ]
}
```
```repair-2
{
  "modelGeneratedCompactDsl": "[\"root\",\"Layout\",{\"layout\":\"S-static-content\"},[\"header\",\"body\"]]\n[\"header\",\"SingleLineTitle\",{\"title\":\"向内修爱\"}]\n[\"body\",\"TextList\",{\"items\":[{\"primaryText\":\"渡人先渡己\",\"secondaryText\":\"先把自己活成一道光，黑暗自会循光而来\"},{\"primaryText\":\"爱是向内修出的内丹\",\"secondaryText\":\"自己未曾炼成，给出的只是半剂药\"}]}]\n[\"/state/ready\",true]",
  "generatedDsl": "{\"version\":\"v0.9\",\"createSurface\":{\"surfaceId\":\"surface_card\",\"catalogId\":\"ohos.a2ui.extended.catalog.form\"}}\n{\"version\":\"v0.9\",\"updateComponents\":{\"surfaceId\":\"surface_card\",\"root\":\"root\",\"components\":[{\"id\":\"root\",\"component\":\"Column\",\"children\":[\"__layout__root__static_header\",\"__layout__root__static_body\"],\"itemMargin\":6.0,\"styles\":{\"width\":\"matchParent\",\"height\":\"matchParent\",\"padding\":{\"top\":12.0,\"bottom\":12.0,\"left\":0,\"right\":0},\"borderRadius\":20.0,\"clip\":true,\"alignItems\":\"start\",\"justifyContent\":\"start\"}},{\"id\":\"__layout__root__static_header\",\"component\":\"Column\",\"children\":[\"header\"],\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"padding\":{\"left\":12.0,\"right\":12.0},\"height\":16.0},\"itemMargin\":0},{\"id\":\"header\",\"component\":\"Column\",\"children\":[\"header__static_title\"],\"itemMargin\":0.0,\"styles\":{\"width\":\"matchParent\",\"height\":16.0,\"alignItems\":\"start\",\"justifyContent\":\"start\",\"flexShrink\":0}},{\"id\":\"header__static_title\",\"component\":\"Text\",\"content\":\"向内修爱\",\"styles\":{\"fontSize\":12.0,\"fontWeight\":400,\"lineHeight\":1.3333333333333333,\"maxLines\":1,\"height\":16.0,\"width\":\"matchParent\",\"flexShrink\":0,\"fontColor\":\"@theme:primary/1\",\"textOverflow\":\"clip\",\"wordBreak\":\"normal\"}},{\"id\":\"__layout__root__static_body\",\"component\":\"Column\",\"children\":[\"body\"],\"itemMargin\":6.0,\"styles\":{\"width\":\"matchParent\",\"layoutWeight\":1,\"alignItems\":\"start\",\"justifyContent\":\"end\",\"padding\":{\"left\":12.0,\"right\":12.0}}},{\"id\":\"body\",\"component\":\"Column\",\"children\":[\"body__static_item0\",\"body__static_divider0\",\"body__static_item1\"],\"itemMargin\":12.0,\"styles\":{\"width\":\"matchParent\",\"height\":91.0,\"alignItems\":\"start\",\"justifyContent\":\"start\",\"flexShrink\":0}},{\"id\":\"body__static_item0_primaryText\",\"component\":\"Text\",\"content\":\"渡人先渡己\",\"styles\":{\"fontSize\":12.0,\"fontWeight\":500,\"lineHeight\":1.3333333333333333,\"maxLines\":1,\"height\":16.0,\"width\":\"matchParent\",\"flexShrink\":1,\"fontColor\":\"@theme:primary/1\",\"textOverflow\":\"ellipsis\",\"constraintSize\":{\"minWidth\":0},\"wordBreak\":\"normal\"}},{\"id\":\"body__static_item0_secondaryText\",\"component\":\"Text\",\"content\":\"先把自己活成一道光，黑暗自会循光而来\",\"styles\":{\"fontSize\":10.0,\"fontWeight\":400,\"lineHeight\":1.3,\"maxLines\":1,\"height\":13.0,\"width\":\"matchParent\",\"flexShrink\":1,\"fontColor\":\"@theme:primary/0.6\",\"textOverflow\":\"ellipsis\",\"constraintSize\":{\"minWidth\":0},\"wordBreak\":\"normal\"}},{\"id\":\"body__static_item0_main\",\"component\":\"Column\",\"children\":[\"body__static_item0_primaryText\",\"body__static_item0_secondaryText\"],\"itemMargin\":4.0,\"styles\":{\"height\":33.0,\"alignItems\":\"start\",\"justifyContent\":\"start\",\"flexShrink\":1,\"layoutWeight\":1,\"constraintSize\":{\"minWidth\":0}}},{\"id\":\"body__static_item0_badge\",\"component\":\"Text\",\"content\":\"1\",\"styles\":{\"fontSize\":10.0,\"fontWeight\":500,\"lineHeight\":1.6,\"maxLines\":1,\"height\":16.0,\"width\":16.0,\"flexShrink\":0,\"fontColor\":\"@theme:primary/1\",\"textAlign\":\"center\",\"backgroundColor\":\"@theme:primary/0.2\",\"borderRadius\":8.0,\"textOverflow\":\"clip\",\"wordBreak\":\"normal\"}},{\"id\":\"body__static_item0_text\",\"component\":\"Row\",\"children\":[\"body__static_item0_main\"],\"itemMargin\":0.0,\"styles\":{\"height\":33.0,\"layoutWeight\":1,\"alignItems\":\"center\",\"flexShrink\":0,\"constraintSize\":{\"minWidth\":0}}},{\"id\":\"body__static_item0\",\"component\":\"Row\",\"children\":[\"body__static_item0_badge\",\"body__static_item0_text\"],\"itemMargin\":8.0,\"styles\":{\"width\":\"matchParent\",\"height\":33.0,\"alignItems\":\"center\",\"flexShrink\":0}},{\"id\":\"body__static_divider0\",\"component\":\"Divider\",\"styles\":{\"width\":\"matchParent\",\"height\":1.0,\"strokeWidth\":1.0,\"flexShrink\":0,\"color\":\"@theme:primary/0.12\"}},{\"id\":\"body__static_item1_primaryText\",\"component\":\"Text\",\"content\":\"爱是向内修出的内丹\",\"styles\":{\"fontSize\":12.0,\"fontWeight\":500,\"lineHeight\":1.3333333333333333,\"maxLines\":1,\"height\":16.0,\"width\":\"matchParent\",\"flexShrink\":1,\"fontColor\":\"@theme:primary/1\",\"textOverflow\":\"ellipsis\",\"constraintSize\":{\"minWidth\":0},\"wordBreak\":\"normal\"}},{\"id\":\"body__static_item1_secondaryText\",\"component\":\"Text\",\"content\":\"自己未曾炼成，给出的只是半剂药\",\"styles\":{\"fontSize\":10.0,\"fontWeight\":400,\"lineHeight\":1.3,\"maxLines\":1,\"height\":13.0,\"width\":\"matchParent\",\"flexShrink\":1,\"fontColor\":\"@theme:primary/0.6\",\"textOverflow\":\"ellipsis\",\"constraintSize\":{\"minWidth\":0},\"wordBreak\":\"normal\"}},{\"id\":\"body__static_item1_main\",\"component\":\"Column\",\"children\":[\"body__static_item1_primaryText\",\"body__static_item1_secondaryText\"],\"itemMargin\":4.0,\"styles\":{\"height\":33.0,\"alignItems\":\"start\",\"justifyContent\":\"start\",\"flexShrink\":1,\"layoutWeight\":1,\"constraintSize\":{\"minWidth\":0}}},{\"id\":\"body__static_item1_badge\",\"component\":\"Text\",\"content\":\"2\",\"styles\":{\"fontSize\":10.0,\"fontWeight\":500,\"lineHeight\":1.6,\"maxLines\":1,\"height\":16.0,\"width\":16.0,\"flexShrink\":0,\"fontColor\":\"@theme:primary/1\",\"textAlign\":\"center\",\"backgroundColor\":\"@theme:primary/0.2\",\"borderRadius\":8.0,\"textOverflow\":\"clip\",\"wordBreak\":\"normal\"}},{\"id\":\"body__static_item1_text\",\"component\":\"Row\",\"children\":[\"body__static_item1_main\"],\"itemMargin\":0.0,\"styles\":{\"height\":33.0,\"layoutWeight\":1,\"alignItems\":\"center\",\"flexShrink\":0,\"constraintSize\":{\"minWidth\":0}}},{\"id\":\"body__static_item1\",\"component\":\"Row\",\"children\":[\"body__static_item1_badge\",\"body__static_item1_text\"],\"itemMargin\":8.0,\"styles\":{\"width\":\"matchParent\",\"height\":33.0,\"alignItems\":\"center\",\"flexShrink\":0}}]}}\n{\"version\":\"v0.9\",\"updateDataModel\":{\"surfaceId\":\"surface_card\",\"path\":\"/\",\"value\":{\"state\":{\"ready\":true}}}}",
  "validationErrors": []
}
```
