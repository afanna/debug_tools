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
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Column","children":["__layout__root__static_header","__layout__root__static_body"],"itemMargin":6.0,"styles":{"width":"matchParent","height":"matchParent","padding":{"top":12.0,"bottom":12.0,"left":0,"right":0},"borderRadius":20.0,"clip":true,"alignItems":"start","justifyContent":"start","linearGradient":{"direction":"RightBottom","colors":[["#FFDBCCFF",0],["#FFF6F2FF",1]]}}},{"id":"__layout__root__static_header","component":"Column","children":["header"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","padding":{"left":12.0,"right":12.0},"height":16.0},"itemMargin":0},{"id":"header","component":"Column","children":["header__static_title"],"itemMargin":0.0,"styles":{"width":"matchParent","height":16.0,"alignItems":"start","justifyContent":"start","flexShrink":0}},{"id":"header__static_title","component":"Text","content":"向内修爱","styles":{"fontSize":12.0,"fontWeight":400,"lineHeight":1.3333333333333333,"maxLines":1,"height":16.0,"width":"matchParent","flexShrink":0,"fontColor":"#FF563D99","textOverflow":"clip","wordBreak":"normal"}},{"id":"__layout__root__static_body","component":"Column","children":["body"],"itemMargin":6.0,"styles":{"width":"matchParent","layoutWeight":1,"alignItems":"start","justifyContent":"start","padding":{"left":12.0,"right":12.0}}},{"id":"body","component":"Column","children":["body__static_top","body__static_secondaryText"],"itemMargin":0.0,"styles":{"width":"matchParent","height":"matchParent","alignItems":"start","justifyContent":"start","flexShrink":0,"layoutWeight":1,"constraintSize":{"minHeight":90.0}}},{"id":"body__static_mainText_line0","component":"Text","content":"爱是向内修出","styles":{"fontSize":18.0,"fontWeight":700,"lineHeight":1.0,"maxLines":1,"height":18.0,"width":"matchParent","flexShrink":0,"fontColor":"#FF563D99","textOverflow":"clip","wordBreak":"normal"}},{"id":"body__static_mainText_line1","component":"Text","content":"的内丹","styles":{"fontSize":18.0,"fontWeight":700,"lineHeight":1.0,"maxLines":1,"height":18.0,"width":"matchParent","flexShrink":0,"fontColor":"#FF563D99","textOverflow":"clip","wordBreak":"normal"}},{"id":"body__static_mainText","component":"Column","children":["body__static_mainText_line0","body__static_mainText_line1"],"itemMargin":0.0,"styles":{"width":"matchParent","height":36.0,"alignItems":"start","justifyContent":"start","flexShrink":0}},{"id":"body__static_top","component":"Column","children":["body__static_mainText"],"itemMargin":2.0,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","flexShrink":0,"layoutWeight":1,"constraintSize":{"minHeight":42.0},"padding":{"bottom":6.0}}},{"id":"body__static_secondaryText","component":"Text","content":"自己未曾炼成，给出的也只是半剂药；先把自己活成一道光，渡人先渡己","styles":{"fontSize":12.0,"fontWeight":400,"lineHeight":1.3333333333333333,"maxLines":3,"height":48.0,"width":"matchParent","flexShrink":1,"fontColor":"#99563D99","textOverflow":"ellipsis","constraintSize":{"minWidth":0},"wordBreak":"normal"}}]}}
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
  "artifactId": "939dc210-a039-4ec7-83f1-7aa995dc2e8a",
  "createdAt": 1793952171822
}
```
```designcompactdsl
["root","Layout",{"layout":"S-static-content"},["header","body"]]
["header","SingleLineTitle",{"title":"向内修爱"}]
["body","EmphasisText",{"mainText":"爱是向内修出的内丹","secondaryText":"自己未曾炼成，给出的也只是半剂药；先把自己活成一道光，渡人先渡己"}]
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
    "sessionId": "batch-13ea8cbd"
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
