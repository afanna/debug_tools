```cardspec
{
  "title": "值班表",
  "description": "本周值班安排",
  "suggestSize": "2x4",
  "imageDomainWhitelist": [
    "hag-ability-test.obs.cn-north-1.myhuaweicloud.com",
    "lfcontentcenterdev.hwcloudtest.cn",
    "hagres-drcn.dbankcdn.com"
  ]
}
```
```genui
{"version":"v0.9","createSurface":{"surfaceId":"surface_card","catalogId":"ohos.a2ui.extended.catalog.form"}}
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Column","children":["__layout__root__static_header","__layout__root__static_body"],"itemMargin":6.0,"styles":{"width":"matchParent","height":"matchParent","padding":{"top":12.0,"bottom":12.0,"left":0,"right":0},"borderRadius":20.0,"clip":true,"alignItems":"start","justifyContent":"start","linearGradient":{"direction":"RightBottom","colors":[["#FFCBDDFE",0],["#FFF1F6FE",1]]}}},{"id":"__layout__root__static_header","component":"Column","children":["header"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","padding":{"left":12.0,"right":12.0},"height":16.0},"itemMargin":0},{"id":"header","component":"Column","children":["header__static_title"],"itemMargin":0.0,"styles":{"width":"matchParent","height":16.0,"alignItems":"start","justifyContent":"start","flexShrink":0}},{"id":"header__static_title","component":"Text","content":"一周值班安排","styles":{"fontSize":12.0,"fontWeight":400,"lineHeight":1.3333333333333333,"maxLines":1,"height":16.0,"width":"matchParent","flexShrink":0,"fontColor":"#FF1F4799","textOverflow":"clip","wordBreak":"normal"}},{"id":"__layout__root__static_body","component":"Column","children":["body"],"itemMargin":6.0,"styles":{"width":"matchParent","layoutWeight":1,"alignItems":"start","justifyContent":"end","padding":{"left":12.0,"right":12.0}}},{"id":"body","component":"Column","children":["body__static_item0","body__static_divider0","body__static_item1"],"itemMargin":12.0,"styles":{"width":"matchParent","height":91.0,"alignItems":"start","justifyContent":"start","flexShrink":0}},{"id":"body__static_item0_primaryText","component":"Text","content":"周三、周五","styles":{"fontSize":12.0,"fontWeight":500,"lineHeight":1.3333333333333333,"maxLines":1,"height":16.0,"width":"matchParent","flexShrink":1,"fontColor":"#FF1F4799","textOverflow":"ellipsis","constraintSize":{"minWidth":0},"wordBreak":"normal"}},{"id":"body__static_item0_secondaryText","component":"Text","content":"全天上班","styles":{"fontSize":10.0,"fontWeight":400,"lineHeight":1.3,"maxLines":1,"height":13.0,"width":"matchParent","flexShrink":1,"fontColor":"#991F4799","textOverflow":"ellipsis","constraintSize":{"minWidth":0},"wordBreak":"normal"}},{"id":"body__static_item0_main","component":"Column","children":["body__static_item0_primaryText","body__static_item0_secondaryText"],"itemMargin":4.0,"styles":{"height":33.0,"alignItems":"start","justifyContent":"start","flexShrink":1,"layoutWeight":1,"constraintSize":{"minWidth":0}}},{"id":"body__static_item0_badge","component":"Text","content":"1","styles":{"fontSize":10.0,"fontWeight":500,"lineHeight":1.6,"maxLines":1,"height":16.0,"width":16.0,"flexShrink":0,"fontColor":"#FF1F4799","textAlign":"center","backgroundColor":"#331F4799","borderRadius":8.0,"textOverflow":"clip","wordBreak":"normal"}},{"id":"body__static_item0_text","component":"Row","children":["body__static_item0_main"],"itemMargin":0.0,"styles":{"height":33.0,"layoutWeight":1,"alignItems":"center","flexShrink":0,"constraintSize":{"minWidth":0}}},{"id":"body__static_item0","component":"Row","children":["body__static_item0_badge","body__static_item0_text"],"itemMargin":8.0,"styles":{"width":"matchParent","height":33.0,"alignItems":"center","flexShrink":0}},{"id":"body__static_divider0","component":"Divider","styles":{"width":"matchParent","height":1.0,"strokeWidth":1.0,"flexShrink":0,"color":"#1F1F4799"}},{"id":"body__static_item1_primaryText","component":"Text","content":"周六、周日","styles":{"fontSize":12.0,"fontWeight":500,"lineHeight":1.3333333333333333,"maxLines":1,"height":16.0,"width":"matchParent","flexShrink":1,"fontColor":"#FF1F4799","textOverflow":"ellipsis","constraintSize":{"minWidth":0},"wordBreak":"normal"}},{"id":"body__static_item1_secondaryText","component":"Text","content":"上午上班，下午休息","styles":{"fontSize":10.0,"fontWeight":400,"lineHeight":1.3,"maxLines":1,"height":13.0,"width":"matchParent","flexShrink":1,"fontColor":"#991F4799","textOverflow":"ellipsis","constraintSize":{"minWidth":0},"wordBreak":"normal"}},{"id":"body__static_item1_main","component":"Column","children":["body__static_item1_primaryText","body__static_item1_secondaryText"],"itemMargin":4.0,"styles":{"height":33.0,"alignItems":"start","justifyContent":"start","flexShrink":1,"layoutWeight":1,"constraintSize":{"minWidth":0}}},{"id":"body__static_item1_badge","component":"Text","content":"2","styles":{"fontSize":10.0,"fontWeight":500,"lineHeight":1.6,"maxLines":1,"height":16.0,"width":16.0,"flexShrink":0,"fontColor":"#FF1F4799","textAlign":"center","backgroundColor":"#331F4799","borderRadius":8.0,"textOverflow":"clip","wordBreak":"normal"}},{"id":"body__static_item1_text","component":"Row","children":["body__static_item1_main"],"itemMargin":0.0,"styles":{"height":33.0,"layoutWeight":1,"alignItems":"center","flexShrink":0,"constraintSize":{"minWidth":0}}},{"id":"body__static_item1","component":"Row","children":["body__static_item1_badge","body__static_item1_text"],"itemMargin":8.0,"styles":{"width":"matchParent","height":33.0,"alignItems":"center","flexShrink":0}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"state":{"ready":true}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "做一张值班表卡片，显示一周的值班安排：星期二上午上班、下午休息；星期四上午休息、下午上班；星期三、星期五全天上班；星期六、星期天上午上班、下午休息。本轮卡片静态内容（用作展示的外部事实）：值班安排：周二上午上班下午休息，周四上午休息下午上班，周三周五全天上班，周六周日上午上班下午休息。",
  "size": "2x4",
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
  "artifactId": "53054d95-9d3d-4cbc-ab3b-5dd58e713eb2",
  "createdAt": 1793951196081
}
```
```designcompactdsl
["root","Layout",{"layout":"W-static-content"},["header","body"]]
["header","SingleLineTitle",{"title":"一周值班安排"}]
["body","TextList",{"items":[{"primaryText":"周三、周五","secondaryText":"全天上班"},{"primaryText":"周六、周日","secondaryText":"上午上班，下午休息"}]}]
["/state/ready",true]
```
```request
{
  "content": {
    "size": "2x4",
    "functionName": "generateWidgetCardCompactDsl",
    "romVersion": "CMM-AL10 7.0.0.111",
    "candidateAssetIds": [],
    "candidateEventCandidates": [],
    "bundleName": "com.huawei.genui",
    "description": "本周值班安排",
    "userQuery": "做一张值班表卡片，显示一周的值班安排：星期二上午上班、下午休息；星期四上午休息、下午上班；星期三、星期五全天上班；星期六、星期天上午上班、下午休息。本轮卡片静态内容（用作展示的外部事实）：值班安排：周二上午上班下午休息，周四上午休息下午上班，周三周五全天上班，周六周日上午上班下午休息。",
    "title": "值班表",
    "candidateDataBindings": []
  },
  "deviceInfo": {
    "countryCode": "CN",
    "deviceFormation": "HDSpeaker",
    "deviceType": 0,
    "locale": "zh-CN",
    "phoneType": "CMM-AL10",
    "prdVer": "11.7.8.342",
    "sysVer": "EmotionUI_9.0.0",
    "time": "20261103023632529"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q480-000",
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
  "size": "2x4",
  "functionName": "generateWidgetCardCompactDsl",
  "romVersion": "CMM-AL10 7.0.0.111",
  "candidateAssetIds": [],
  "candidateEventCandidates": [],
  "bundleName": "com.huawei.genui",
  "description": "本周值班安排",
  "userQuery": "做一张值班表卡片，显示一周的值班安排：星期二上午上班、下午休息；星期四上午休息、下午上班；星期三、星期五全天上班；星期六、星期天上午上班、下午休息。本轮卡片静态内容（用作展示的外部事实）：值班安排：周二上午上班下午休息，周四上午休息下午上班，周三周五全天上班，周六周日上午上班下午休息。",
  "title": "值班表",
  "candidateDataBindings": []
}
```
