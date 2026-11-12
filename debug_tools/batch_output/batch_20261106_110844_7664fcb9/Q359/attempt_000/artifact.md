```cardspec
{
  "title": "轮休表格",
  "description": "1号到31号轮休安排",
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
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Column","children":["__layout__root__static_header","__layout__root__static_body"],"itemMargin":6.0,"styles":{"width":"matchParent","height":"matchParent","padding":{"top":12.0,"bottom":12.0,"left":0,"right":0},"borderRadius":20.0,"clip":true,"alignItems":"start","justifyContent":"start","linearGradient":{"direction":"RightBottom","colors":[["#FFCBDDFE",0],["#FFF1F6FE",1]]}}},{"id":"__layout__root__static_header","component":"Column","children":["header"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","padding":{"left":12.0,"right":12.0},"height":16.0},"itemMargin":0},{"id":"header","component":"Column","children":["header__static_title"],"itemMargin":0.0,"styles":{"width":"matchParent","height":16.0,"alignItems":"start","justifyContent":"start","flexShrink":0}},{"id":"header__static_title","component":"Text","content":"轮休表格","styles":{"fontSize":12.0,"fontWeight":400,"lineHeight":1.3333333333333333,"maxLines":1,"height":16.0,"width":"matchParent","flexShrink":0,"fontColor":"#FF1F4799","textOverflow":"clip","wordBreak":"normal"}},{"id":"__layout__root__static_body","component":"Column","children":["body"],"itemMargin":6.0,"styles":{"width":"matchParent","layoutWeight":1,"alignItems":"start","justifyContent":"start","padding":{"left":12.0,"right":12.0}}},{"id":"body","component":"Column","children":["body__static_top"],"itemMargin":0.0,"styles":{"width":"matchParent","height":"matchParent","alignItems":"start","justifyContent":"start","flexShrink":0,"layoutWeight":1,"constraintSize":{"minHeight":18.0}}},{"id":"body__static_mainText","component":"Text","content":"1号至31号轮休安排","styles":{"fontSize":18.0,"fontWeight":700,"lineHeight":1.0,"maxLines":1,"height":18.0,"width":"matchParent","flexShrink":0,"fontColor":"#FF1F4799","textOverflow":"clip","wordBreak":"normal"}},{"id":"body__static_top","component":"Column","children":["body__static_mainText"],"itemMargin":2.0,"styles":{"width":"matchParent","height":18.0,"alignItems":"start","justifyContent":"start","flexShrink":0}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"state":{"ready":true}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "制作一个轮休表格卡片，从1号到31号，展示轮休安排。本轮卡片静态内容（用作展示的外部事实）：轮休表格，从1号到31号",
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
  "artifactId": "46c8dcbe-b706-4e72-991b-d5762ef8377a",
  "createdAt": 1793934596766
}
```
```designcompactdsl
["root","Layout",{"layout":"W-static-content"},["header","body"]]
["header","SingleLineTitle",{"title":"轮休表格"}]
["body","EmphasisText",{"mainText":"1号至31号轮休安排"}]
["/state/ready",true]
```
```request
{
  "content": {
    "bundleName": "com.huawei.genui",
    "userQuery": "制作一个轮休表格卡片，从1号到31号，展示轮休安排。本轮卡片静态内容（用作展示的外部事实）：轮休表格，从1号到31号",
    "candidateDataBindings": [],
    "title": "轮休表格",
    "size": "2x4",
    "candidateEventCandidates": [],
    "description": "1号到31号轮休安排",
    "candidateAssetIds": []
  },
  "deviceInfo": {
    "countryCode": "CN",
    "deviceFormation": "HDSpeaker",
    "deviceType": 0,
    "locale": "zh-CN",
    "phoneType": "HLS-AL00",
    "prdVer": "11.7.8.342",
    "sysVer": "EmotionUI_9.0.0",
    "time": "20261030133825998"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q359-000",
    "isNew": true,
    "sessionId": "batch-7664fcb9"
  },
  "userAuth": {
    "user": {}
  },
  "utterance": {
    "original": "制作一个轮休表格卡片，从1号到31号，展示轮休安排。本轮卡片静态内容（用作展示的外部事实）：轮休表格，从1号到31号",
    "type": "text"
  },
  "version": "1.0",
  "functionName": "generateWidgetCardCompactDsl",
  "romVersion": "HLS-AL00 7.0.0.111",
  "bundleName": "com.huawei.genui",
  "userQuery": "制作一个轮休表格卡片，从1号到31号，展示轮休安排。本轮卡片静态内容（用作展示的外部事实）：轮休表格，从1号到31号",
  "candidateDataBindings": [],
  "title": "轮休表格",
  "size": "2x4",
  "candidateEventCandidates": [],
  "description": "1号到31号轮休安排",
  "candidateAssetIds": []
}
```
