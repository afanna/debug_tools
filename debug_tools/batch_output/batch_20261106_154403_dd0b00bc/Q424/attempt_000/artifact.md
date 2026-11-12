```cardspec
{
  "title": "算题面板",
  "description": "空白算题面板",
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
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Column","children":["__layout__root__static_header","__layout__root__static_body"],"itemMargin":6.0,"styles":{"width":"matchParent","height":"matchParent","padding":{"top":12.0,"bottom":12.0,"left":0,"right":0},"borderRadius":20.0,"clip":true,"alignItems":"start","justifyContent":"start","linearGradient":{"direction":"RightBottom","colors":[["#FFFFE0CC",0],["#FFFFF7F2",1]]}}},{"id":"__layout__root__static_header","component":"Column","children":["header"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","padding":{"left":12.0,"right":12.0},"height":16.0},"itemMargin":0},{"id":"header","component":"Column","children":["header__static_title"],"itemMargin":0.0,"styles":{"width":"matchParent","height":16.0,"alignItems":"start","justifyContent":"start","flexShrink":0}},{"id":"header__static_title","component":"Text","content":"算题面板","styles":{"fontSize":12.0,"fontWeight":400,"lineHeight":1.3333333333333333,"maxLines":1,"height":16.0,"width":"matchParent","flexShrink":0,"fontColor":"#FF8C4B1C","textOverflow":"clip","wordBreak":"normal"}},{"id":"__layout__root__static_body","component":"Column","children":["body"],"itemMargin":6.0,"styles":{"width":"matchParent","layoutWeight":1,"alignItems":"start","justifyContent":"start","padding":{"left":12.0,"right":12.0}}},{"id":"body","component":"Column","children":["body__static_top"],"itemMargin":0.0,"styles":{"width":"matchParent","height":"matchParent","alignItems":"start","justifyContent":"start","flexShrink":0,"layoutWeight":1,"constraintSize":{"minHeight":18.0}}},{"id":"body__static_mainText","component":"Text","content":"空白面板，用于书写算题","styles":{"fontSize":18.0,"fontWeight":700,"lineHeight":1.0,"maxLines":1,"height":18.0,"width":"matchParent","flexShrink":0,"fontColor":"#FF8C4B1C","textOverflow":"clip","wordBreak":"normal"}},{"id":"body__static_top","component":"Column","children":["body__static_mainText"],"itemMargin":2.0,"styles":{"width":"matchParent","height":18.0,"alignItems":"start","justifyContent":"start","flexShrink":0}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"state":{"ready":true}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "做一个空白面板卡片，用于写算题。本轮卡片静态内容（用作展示的外部事实）：空白面板，用于书写算题。",
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
  "artifactId": "7b33acf0-2bfd-4696-94f6-8c9f210641e6",
  "createdAt": 1793951069182
}
```
```designcompactdsl
["root","Layout",{"layout":"W-static-content"},["header","body"]]
["header","SingleLineTitle",{"title":"算题面板"}]
["body","EmphasisText",{"mainText":"空白面板，用于书写算题"}]
["/state/ready",true]
```
```request
{
  "content": {
    "size": "2x4",
    "functionName": "generateWidgetCardCompactDsl",
    "romVersion": "HLS-AL00 7.0.0.111",
    "candidateAssetIds": [],
    "candidateEventCandidates": [],
    "bundleName": "com.huawei.genui",
    "description": "空白算题面板",
    "userQuery": "做一个空白面板卡片，用于写算题。本轮卡片静态内容（用作展示的外部事实）：空白面板，用于书写算题。",
    "title": "算题面板",
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
    "time": "20261101132344888"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q424-000",
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
  "romVersion": "HLS-AL00 7.0.0.111",
  "candidateAssetIds": [],
  "candidateEventCandidates": [],
  "bundleName": "com.huawei.genui",
  "description": "空白算题面板",
  "userQuery": "做一个空白面板卡片，用于写算题。本轮卡片静态内容（用作展示的外部事实）：空白面板，用于书写算题。",
  "title": "算题面板",
  "candidateDataBindings": []
}
```
