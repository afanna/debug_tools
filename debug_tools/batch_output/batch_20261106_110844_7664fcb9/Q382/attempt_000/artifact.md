```cardspec
{
  "title": "日期时间",
  "description": "当前日期时间",
  "suggestSize": "2x2",
  "imageDomainWhitelist": [
    "hag-ability-test.obs.cn-north-1.myhuaweicloud.com",
    "lfcontentcenterdev.hwcloudtest.cn",
    "hagres-drcn.dbankcdn.com"
  ],
  "dataBindings": [
    {
      "capabilityId": "GetCurrentTime",
      "arguments": {},
      "writeResultTo": "/data/time"
    }
  ]
}
```
```genui
{"version":"v0.9","createSurface":{"surfaceId":"surface_card","catalogId":"ohos.a2ui.extended.catalog.form"}}
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Column","children":["first","second"],"itemMargin":8,"styles":{"width":"matchParent","height":"matchParent","borderRadius":20,"clip":true,"alignItems":"start","justifyContent":"start","padding":8,"linearGradient":{"direction":"RightBottom","colors":[["#FFCBDDFE",0],["#FFF1F6FE",1]]}}},{"id":"first","component":"Column","children":["first_text"],"itemMargin":0,"styles":{"padding":{"left":8,"right":8},"borderRadius":16,"alignItems":"start","justifyContent":"center","clip":true,"flexShrink":0,"width":"matchParent","height":63,"backgroundColor":"#CCFFFFFF","layoutWeight":1}},{"id":"first_text","component":"Column","children":["first_primary","first_secondary"],"itemMargin":0,"styles":{"alignItems":"start","justifyContent":"center","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent"}},{"id":"first_primary","component":"Text","content":"{{ ${/data/time/currentDate} }}","styles":{"height":22,"fontSize":16,"fontWeight":700,"maxLines":1,"flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent","fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"first_secondary","component":"Text","content":"日期","styles":{"height":16,"fontSize":12,"fontWeight":500,"maxLines":1,"textOverflow":"ellipsis","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent","fontColor":"#991F4799"}},{"id":"second","component":"Column","children":["second_text"],"itemMargin":0,"styles":{"padding":{"left":8,"right":8},"borderRadius":16,"alignItems":"start","justifyContent":"center","clip":true,"flexShrink":0,"width":"matchParent","height":63,"backgroundColor":"#CCFFFFFF","layoutWeight":1}},{"id":"second_text","component":"Column","children":["second_primary","second_secondary"],"itemMargin":0,"styles":{"alignItems":"start","justifyContent":"center","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent"}},{"id":"second_primary","component":"Text","content":"{{ ${/data/time/dayOfWeek} }}","styles":{"height":22,"fontSize":16,"fontWeight":700,"maxLines":1,"flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent","fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"second_secondary","component":"Text","content":"星期","styles":{"height":16,"fontSize":12,"fontWeight":500,"maxLines":1,"textOverflow":"ellipsis","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent","fontColor":"#991F4799"}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"time":{"currentDate":"示例","dayOfWeek":"示例"}}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "在当前屏幕上方添加一个显示日期和时间的卡片，显示当前日期、星期和时间。本轮卡片静态内容（用作展示的外部事实）：",
  "size": "2x2",
  "appVersion": "11.7.8.342",
  "eventCandidates": [],
  "dataModelSchema": {
    "data": {
      "time": {
        "currentDate": {
          "type": "string",
          "description": "格式化的当前公历日期（年-月-日），例如 '2026-07-09'。",
          "sampleValue": "示例"
        },
        "dayOfWeek": {
          "type": "string",
          "description": "中文的星期描述，例如 '星期四'。",
          "sampleValue": "示例"
        },
        "updatedAt": {
          "type": "string",
          "description": "端侧完成该时间数据组装的时间戳字符串，格式如 '2026-07-09 15:30:00'。",
          "sampleValue": "示例"
        }
      }
    }
  },
  "assetCandidates": []
}
```
```effectivecapabilities
{
  "data": [
    "GetCurrentTime"
  ],
  "event": [],
  "asset": []
}
```
```removedcapabilities
[]
```
```generationplan
{
  "candidateDataBindings": [
    {
      "capabilityId": "GetCurrentTime",
      "arguments": {},
      "writeResultTo": "/data/time",
      "candidateOutputFields": [
        "/currentDate",
        "/dayOfWeek",
        "/updatedAt"
      ]
    }
  ],
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
  "artifactId": "de949f83-dee5-45a2-8237-ff796b14bbbc",
  "createdAt": 1793934620163
}
```
```designcompactdsl
["root","Layout",{"layout":"S-dual-info"},["first","second"]]
["first","InfoBlock",{"surfaceRole":"panel","primaryText":{"path":"/data/time/currentDate"},"secondaryText":"日期"}]
["second","InfoBlock",{"surfaceRole":"panel","primaryText":{"path":"/data/time/dayOfWeek"},"secondaryText":"星期"}]
["/data/time/currentDate","示例"]
["/data/time/dayOfWeek","示例"]
```
```request
{
  "content": {
    "bundleName": "com.huawei.genui",
    "userQuery": "在当前屏幕上方添加一个显示日期和时间的卡片，显示当前日期、星期和时间。本轮卡片静态内容（用作展示的外部事实）：",
    "candidateDataBindings": [
      {
        "capabilityId": "GetCurrentTime",
        "arguments": {},
        "writeResultTo": "/data/time",
        "candidateOutputFields": [
          "/currentDate",
          "/dayOfWeek",
          "/updatedAt"
        ]
      }
    ],
    "title": "日期时间",
    "size": "2x2",
    "candidateEventCandidates": [],
    "description": "当前日期时间",
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
    "time": "20261031022008375"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q382-000",
    "isNew": true,
    "sessionId": "batch-7664fcb9"
  },
  "userAuth": {
    "user": {}
  },
  "utterance": {
    "original": "在当前屏幕上方添加一个显示日期和时间的卡片，显示当前日期、星期和时间。本轮卡片静态内容（用作展示的外部事实）：",
    "type": "text"
  },
  "version": "1.0",
  "functionName": "generateWidgetCardCompactDsl",
  "romVersion": "CMS-AL20 7.0.0.111",
  "bundleName": "com.huawei.genui",
  "userQuery": "在当前屏幕上方添加一个显示日期和时间的卡片，显示当前日期、星期和时间。本轮卡片静态内容（用作展示的外部事实）：",
  "candidateDataBindings": [
    {
      "capabilityId": "GetCurrentTime",
      "arguments": {},
      "writeResultTo": "/data/time",
      "candidateOutputFields": [
        "/currentDate",
        "/dayOfWeek",
        "/updatedAt"
      ]
    }
  ],
  "title": "日期时间",
  "size": "2x2",
  "candidateEventCandidates": [],
  "description": "当前日期时间",
  "candidateAssetIds": []
}
```
