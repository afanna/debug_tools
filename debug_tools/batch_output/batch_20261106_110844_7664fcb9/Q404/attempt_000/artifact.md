```cardspec
{
  "title": "密码卡片",
  "description": "密码卡片",
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
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Column","children":["__layout__root__static_header","__layout__root__static_body"],"itemMargin":6.0,"styles":{"width":"matchParent","height":"matchParent","padding":{"top":12.0,"bottom":12.0,"left":0,"right":0},"borderRadius":20.0,"clip":true,"alignItems":"start","justifyContent":"start","linearGradient":{"direction":"RightBottom","colors":[["#FFDBCCFF",0],["#FFF6F2FF",1]]}}},{"id":"__layout__root__static_header","component":"Column","children":["header"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","padding":{"left":12.0,"right":12.0},"height":16.0},"itemMargin":0},{"id":"header","component":"Column","children":["header__static_title"],"itemMargin":0.0,"styles":{"width":"matchParent","height":16.0,"alignItems":"start","justifyContent":"start","flexShrink":0}},{"id":"header__static_title","component":"Text","content":"密码信息","styles":{"fontSize":12.0,"fontWeight":400,"lineHeight":1.3333333333333333,"maxLines":1,"height":16.0,"width":"matchParent","flexShrink":0,"fontColor":"#FF563D99","textOverflow":"clip","wordBreak":"normal"}},{"id":"__layout__root__static_body","component":"Column","children":["body"],"itemMargin":6.0,"styles":{"width":"matchParent","layoutWeight":1,"alignItems":"start","justifyContent":"end","padding":{"left":12.0,"right":12.0}}},{"id":"body","component":"Column","children":["body__static_item0","body__static_item1"],"itemMargin":4.0,"styles":{"width":"matchParent","height":68.0,"alignItems":"start","justifyContent":"start","flexShrink":0}},{"id":"body__static_item0_text","component":"Text","content":"密码","styles":{"fontSize":12.0,"fontWeight":400,"lineHeight":1.3333333333333333,"maxLines":1,"height":16.0,"width":25.200000000000003,"flexShrink":0,"fontColor":"#99563D99","textOverflow":"clip","wordBreak":"normal"}},{"id":"body__static_item0_assist","component":"Text","content":"88122092","styles":{"fontSize":12.0,"fontWeight":700,"lineHeight":1.3333333333333333,"maxLines":1,"height":16.0,"flexShrink":0,"fontColor":"#FF563D99","layoutWeight":1,"textAlign":"end","textOverflow":"clip","wordBreak":"normal"}},{"id":"body__static_item0","component":"Row","children":["body__static_item0_text","body__static_item0_assist"],"itemMargin":8.0,"styles":{"width":"matchParent","height":32.0,"alignItems":"center","flexShrink":0,"padding":{"left":12.0,"right":12.0},"borderRadius":8.0,"backgroundColor":"#CCFFFFFF"}},{"id":"body__static_item1_text","component":"Text","content":"类型","styles":{"fontSize":12.0,"fontWeight":400,"lineHeight":1.3333333333333333,"maxLines":1,"height":16.0,"width":25.200000000000003,"flexShrink":0,"fontColor":"#99563D99","textOverflow":"clip","wordBreak":"normal"}},{"id":"body__static_item1_assist","component":"Text","content":"永久","styles":{"fontSize":12.0,"fontWeight":700,"lineHeight":1.3333333333333333,"maxLines":1,"height":16.0,"flexShrink":0,"fontColor":"#FF563D99","layoutWeight":1,"textAlign":"end","textOverflow":"clip","wordBreak":"normal"}},{"id":"body__static_item1","component":"Row","children":["body__static_item1_text","body__static_item1_assist"],"itemMargin":8.0,"styles":{"width":"matchParent","height":32.0,"alignItems":"center","flexShrink":0,"padding":{"left":12.0,"right":12.0},"borderRadius":8.0,"backgroundColor":"#CCFFFFFF"}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"state":{"ready":true}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "创建一张桌面卡片，展示图片中的密码信息。本轮卡片静态内容（用作展示的外部事实）：图片显示操作成功，密码为 88122092，类型为永久。",
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
  "artifactId": "5da2dcd4-6835-41e3-b999-9df178a585f5",
  "createdAt": 1793934650716
}
```
```designcompactdsl
["root","Layout",{"layout":"S-static-content"},["header","body"]]
["header","SingleLineTitle",{"title":"密码信息"}]
["body","SingleLineList",{"items":[{"text":"密码","assist":"88122092"},{"text":"类型","assist":"永久"}]}]
["/state/ready",true]
```
```request
{
  "content": {
    "bundleName": "com.huawei.genui",
    "userQuery": "创建一张桌面卡片，展示图片中的密码信息。本轮卡片静态内容（用作展示的外部事实）：图片显示操作成功，密码为 88122092，类型为永久。",
    "candidateDataBindings": [],
    "title": "密码卡片",
    "size": "2x2",
    "candidateEventCandidates": [],
    "description": "密码卡片",
    "candidateAssetIds": []
  },
  "deviceInfo": {
    "countryCode": "CN",
    "deviceFormation": "HDSpeaker",
    "deviceType": 0,
    "locale": "zh-CN",
    "phoneType": "CMS-AL20",
    "prdVer": "11.7.8.342",
    "sysVer": "EmotionUI_9.0.0",
    "time": "20261031135327827"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q404-000",
    "isNew": true,
    "sessionId": "batch-7664fcb9"
  },
  "userAuth": {
    "user": {}
  },
  "utterance": {
    "original": "创建一张桌面卡片，展示图片中的密码信息。本轮卡片静态内容（用作展示的外部事实）：图片显示操作成功，密码为 88122092，类型为永久。",
    "type": "text"
  },
  "version": "1.0",
  "functionName": "generateWidgetCardCompactDsl",
  "romVersion": "CMS-AL20 7.0.0.111",
  "bundleName": "com.huawei.genui",
  "userQuery": "创建一张桌面卡片，展示图片中的密码信息。本轮卡片静态内容（用作展示的外部事实）：图片显示操作成功，密码为 88122092，类型为永久。",
  "candidateDataBindings": [],
  "title": "密码卡片",
  "size": "2x2",
  "candidateEventCandidates": [],
  "description": "密码卡片",
  "candidateAssetIds": []
}
```
