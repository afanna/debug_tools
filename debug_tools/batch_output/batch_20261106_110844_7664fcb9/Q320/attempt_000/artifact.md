```cardspec
{
  "title": "生日快乐",
  "description": "生日贺卡",
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
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Column","children":["__layout__root__static_header","__layout__root__static_body"],"itemMargin":6.0,"styles":{"width":"matchParent","height":"matchParent","padding":{"top":12.0,"bottom":12.0,"left":0,"right":0},"borderRadius":20.0,"clip":true,"alignItems":"start","justifyContent":"start","linearGradient":{"direction":"RightBottom","colors":[["#FFFFE0CC",0],["#FFFFF7F2",1]]}}},{"id":"__layout__root__static_header","component":"Column","children":["header"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","padding":{"left":12.0,"right":12.0},"height":16.0},"itemMargin":0},{"id":"header","component":"Column","children":["header__static_title"],"itemMargin":0.0,"styles":{"width":"matchParent","height":16.0,"alignItems":"start","justifyContent":"start","flexShrink":0}},{"id":"header__static_title","component":"Text","content":"生日贺卡","styles":{"fontSize":12.0,"fontWeight":400,"lineHeight":1.3333333333333333,"maxLines":1,"height":16.0,"width":"matchParent","flexShrink":0,"fontColor":"#FF8C4B1C","textOverflow":"clip","wordBreak":"normal"}},{"id":"__layout__root__static_body","component":"Column","children":["body"],"itemMargin":6.0,"styles":{"width":"matchParent","layoutWeight":1,"alignItems":"start","justifyContent":"start","padding":{"left":12.0,"right":12.0}}},{"id":"body","component":"Column","children":["body__static_top"],"itemMargin":0.0,"styles":{"width":"matchParent","height":"matchParent","alignItems":"start","justifyContent":"start","flexShrink":0,"layoutWeight":1,"constraintSize":{"minHeight":36.0}}},{"id":"body__static_mainText_line0","component":"Text","content":"祝沈大哥生日","styles":{"fontSize":18.0,"fontWeight":700,"lineHeight":1.0,"maxLines":1,"height":18.0,"width":"matchParent","flexShrink":0,"fontColor":"#FF8C4B1C","textOverflow":"clip","wordBreak":"normal"}},{"id":"body__static_mainText_line1","component":"Text","content":"快乐","styles":{"fontSize":18.0,"fontWeight":700,"lineHeight":1.0,"maxLines":1,"height":18.0,"width":"matchParent","flexShrink":0,"fontColor":"#FF8C4B1C","textOverflow":"clip","wordBreak":"normal"}},{"id":"body__static_mainText","component":"Column","children":["body__static_mainText_line0","body__static_mainText_line1"],"itemMargin":0.0,"styles":{"width":"matchParent","height":36.0,"alignItems":"start","justifyContent":"start","flexShrink":0}},{"id":"body__static_top","component":"Column","children":["body__static_mainText"],"itemMargin":2.0,"styles":{"width":"matchParent","height":36.0,"alignItems":"start","justifyContent":"start","flexShrink":0}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"state":{"ready":true}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "制作一张生日贺卡，上面写明祝沈大哥生日快乐。本轮卡片静态内容（用作展示的外部事实）：祝沈大哥生日快乐",
  "size": "2x2",
  "appVersion": "11.7.8.342",
  "eventCandidates": [],
  "dataModelSchema": {
    "data": {}
  },
  "assetCandidates": [
    {
      "id": "asset.cake_fill",
      "src": "resources/base/media/cake_fill.svg",
      "description": "样式：默认黑色的单色实心生日蛋糕图标，顶部带蜡烛，原始尺寸为 24×24；适用：生日、纪念日、节日、庆祝事件与运动目标达成。"
    }
  ]
}
```
```effectivecapabilities
{
  "data": [],
  "event": [],
  "asset": [
    "asset.cake_fill"
  ]
}
```
```removedcapabilities
[]
```
```generationplan
{
  "candidateDataBindings": [],
  "candidateEventCandidates": [],
  "candidateAssetIds": [
    "asset.cake_fill"
  ]
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
  "artifactId": "c629904a-0b42-4a73-9842-c437aa60d45e",
  "createdAt": 1793934559470
}
```
```designcompactdsl
["root","Layout",{"layout":"S-static-content"},["header","body"]]
["header","SingleLineTitle",{"title":"生日贺卡"}]
["body","EmphasisText",{"mainText":"祝沈大哥生日快乐"}]
["/state/ready",true]
```
```request
{
  "content": {
    "bundleName": "com.huawei.genui",
    "userQuery": "制作一张生日贺卡，上面写明祝沈大哥生日快乐。本轮卡片静态内容（用作展示的外部事实）：祝沈大哥生日快乐",
    "candidateDataBindings": [],
    "title": "生日快乐",
    "size": "2x2",
    "candidateEventCandidates": [],
    "description": "生日贺卡",
    "candidateAssetIds": [
      "asset.cake_fill"
    ]
  },
  "deviceInfo": {
    "countryCode": "CN",
    "deviceFormation": "HDSpeaker",
    "deviceType": 0,
    "locale": "zh-CN",
    "phoneType": "CMS-AL20",
    "prdVer": "11.7.8.342",
    "sysVer": "EmotionUI_9.0.0",
    "time": "20261029132737963"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q320-000",
    "isNew": true,
    "sessionId": "batch-7664fcb9"
  },
  "userAuth": {
    "user": {}
  },
  "utterance": {
    "original": "制作一张生日贺卡，上面写明祝沈大哥生日快乐。本轮卡片静态内容（用作展示的外部事实）：祝沈大哥生日快乐",
    "type": "text"
  },
  "version": "1.0",
  "functionName": "generateWidgetCardCompactDsl",
  "romVersion": "CMS-AL20 7.0.0.111",
  "bundleName": "com.huawei.genui",
  "userQuery": "制作一张生日贺卡，上面写明祝沈大哥生日快乐。本轮卡片静态内容（用作展示的外部事实）：祝沈大哥生日快乐",
  "candidateDataBindings": [],
  "title": "生日快乐",
  "size": "2x2",
  "candidateEventCandidates": [],
  "description": "生日贺卡",
  "candidateAssetIds": [
    "asset.cake_fill"
  ]
}
```
