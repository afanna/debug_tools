```cardspec
{
  "title": "时钟",
  "description": "实时时钟卡片",
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
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Column","children":["title","__layout__root__body"],"itemMargin":6,"styles":{"width":"matchParent","height":"matchParent","borderRadius":20,"clip":true,"alignItems":"start","justifyContent":"start","padding":12,"linearGradient":{"direction":"RightBottom","colors":[["#FFCBDDFE",0],["#FFF1F6FE",1]]}}},{"id":"title","component":"Row","children":["title_title"],"styles":{"width":"matchParent","height":12,"flexShrink":0,"justifyContent":"start","alignItems":"center"},"itemMargin":0},{"id":"title_title","component":"Text","content":"时钟","styles":{"fontSize":12,"fontWeight":400,"lineHeight":1,"textAlign":"start","maxLines":1,"flexShrink":0,"width":"matchParent","fontColor":"#991F4799"}},{"id":"__layout__root__body","component":"Column","children":["__layout__root__content","__layout__root__action"],"itemMargin":8,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1}},{"id":"__layout__root__content","component":"Column","children":["content"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1},"itemMargin":0},{"id":"content","component":"Column","children":["content_primary","content_support"],"itemMargin":2,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start"}},{"id":"content_primary","component":"Column","children":["content_primary_main"],"itemMargin":2,"styles":{"alignItems":"start","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent"}},{"id":"content_primary_main","component":"Text","content":"当前时间","styles":{"height":18,"fontSize":18,"fontWeight":700,"lineHeight":1,"maxLines":1,"flexShrink":1,"width":"matchParent","fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"content_support","component":"Column","children":["content_support_row0","content_support_row1","content_support_row2"],"itemMargin":2,"styles":{"width":"matchParent","alignItems":"start","flexShrink":1}},{"id":"content_support_item0_label","component":"Text","content":"日期","styles":{"height":12,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":0,"lineHeight":1,"fontColor":"#991F4799","textOverflow":"clip"}},{"id":"content_support_item0_value","component":"Text","content":"{{ ${/data/time/currentDate} }}","styles":{"height":12.0,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":1,"lineHeight":1,"fontColor":"#FF1F4799","layoutWeight":1,"textOverflow":"clip"}},{"id":"content_support_item0","component":"Row","children":["content_support_item0_label","content_support_item0_value"],"itemMargin":4,"styles":{"height":12.0,"alignItems":"top","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"content_support_row0","component":"Row","children":["content_support_item0"],"itemMargin":0,"styles":{"width":"matchParent","height":12.0,"alignItems":"top","flexShrink":0}},{"id":"content_support_item1_label","component":"Text","content":"星期","styles":{"height":12,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":0,"lineHeight":1,"fontColor":"#991F4799","textOverflow":"clip"}},{"id":"content_support_item1_value","component":"Text","content":"{{ ${/data/time/dayOfWeek} }}","styles":{"height":12.0,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":1,"lineHeight":1,"fontColor":"#FF1F4799","layoutWeight":1,"textOverflow":"clip"}},{"id":"content_support_item1","component":"Row","children":["content_support_item1_label","content_support_item1_value"],"itemMargin":4,"styles":{"height":12.0,"alignItems":"top","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"content_support_row1","component":"Row","children":["content_support_item1"],"itemMargin":0,"styles":{"width":"matchParent","height":12.0,"alignItems":"top","flexShrink":0}},{"id":"content_support_item2_label","component":"Text","content":"农历","styles":{"height":12,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":0,"lineHeight":1,"fontColor":"#991F4799","textOverflow":"clip"}},{"id":"content_support_item2_value","component":"Text","content":"{{ ${/data/time/lunarDate} }}","styles":{"height":12.0,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":1,"lineHeight":1,"fontColor":"#FF1F4799","layoutWeight":1,"textOverflow":"clip"}},{"id":"content_support_item2","component":"Row","children":["content_support_item2_label","content_support_item2_value"],"itemMargin":4,"styles":{"height":12.0,"alignItems":"top","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"content_support_row2","component":"Row","children":["content_support_item2"],"itemMargin":0,"styles":{"width":"matchParent","height":12.0,"alignItems":"top","flexShrink":0}},{"id":"__layout__root__action","component":"Column","children":["action"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","height":36,"flexShrink":0},"itemMargin":0},{"id":"action","component":"Row","children":["action_icon","action_text"],"onClick":[{"call":"clickToDeeplink","args":{"abilityName":"com.huawei.hmos.clock.phone","bundleName":"com.huawei.hmos.clock","intentName":"Clock","uri":""}}],"itemMargin":8,"styles":{"height":36,"borderRadius":30,"padding":0,"flexShrink":0,"width":"matchParent","backgroundColor":"#331F4799","justifyContent":"center","alignItems":"center"}},{"id":"action_icon","component":"Image","src":"resources/base/media/emoji_time.png","styles":{"width":20,"height":20,"objectFit":"contain","flexShrink":0}},{"id":"action_text","component":"Text","content":"打开时钟","styles":{"maxWidth":96,"height":17,"fontSize":14,"fontWeight":500,"textAlign":"center","maxLines":1,"flexShrink":0,"fontColor":"#FF1F4799","textOverflow":"clip"}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"time":{"currentDate":"示例","dayOfWeek":"示例","lunarDate":"示例"}},"state":{"ready":true}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "创建一张桌面时钟卡片，显示当前时间、日期、星期和农历信息。",
  "size": "2x2",
  "appVersion": "11.7.8.342",
  "eventCandidates": [
    {
      "id": "event.open.clock.alarm",
      "description": "打开华为时钟应用首页。",
      "call": "clickToDeeplink",
      "args": {
        "abilityName": "com.huawei.hmos.clock.phone",
        "bundleName": "com.huawei.hmos.clock",
        "intentName": "Clock",
        "uri": ""
      }
    }
  ],
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
        "lunarDate": {
          "type": "string",
          "description": "格式化的中国传统农历日期，例如 '五月廿六'。若系统获取失败则可能为空字符串。",
          "sampleValue": "示例"
        }
      }
    }
  },
  "assetCandidates": [
    {
      "id": "asset.emoji_time",
      "src": "resources/base/media/emoji_time.png",
      "description": "样式：蓝色圆形外框与浅蓝表盘组成的写实 3D 时钟，白色指针和刻度清晰，透明背景，原始尺寸为 512×512，PNG 位图需保留原色；适用：当前时间、计时或时长统计相关卡片。不适用：只含时间字段的日程或会议卡片。"
    }
  ]
}
```
```effectivecapabilities
{
  "data": [
    "GetCurrentTime"
  ],
  "event": [
    {
      "id": "event.open.clock.alarm",
      "description": "打开华为时钟应用首页。",
      "call": "clickToDeeplink",
      "args": {
        "abilityName": "com.huawei.hmos.clock.phone",
        "bundleName": "com.huawei.hmos.clock",
        "intentName": "Clock",
        "uri": ""
      }
    }
  ],
  "asset": [
    "asset.emoji_time"
  ]
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
        "/lunarDate"
      ]
    }
  ],
  "candidateEventCandidates": [
    {
      "capabilityId": "event.open.clock.alarm",
      "action": {
        "call": "clickToDeeplink",
        "args": {
          "abilityName": "com.huawei.hmos.clock.phone",
          "bundleName": "com.huawei.hmos.clock",
          "intentName": "Clock",
          "uri": ""
        }
      }
    }
  ],
  "candidateAssetIds": [
    "asset.emoji_time"
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
  "artifactId": "6c04b045-a422-4fce-a7b2-e0772f1be254",
  "createdAt": 1793952175050
}
```
```designcompactdsl
["root","Layout",{"layout":"S-title-content-action"},["title","content","action"]]
["title","SingleLineTitle",{"title":"时钟","fontSize":12}]
["content","Group",{"variant":"hero-support"},["content_primary","content_support"]]
["content_primary","EmphasisText",{"mainText":"当前时间","fontSize":18}]
["content_support","SecondaryBody",{"items":[{"label":"日期 ","value":{"path":"/data/time/currentDate"}},{"label":"星期 ","value":{"path":"/data/time/dayOfWeek"}},{"label":"农历 ","value":{"path":"/data/time/lunarDate"}}],"columns":1,"fontSize":12}]
["action","PillButton",{"label":"打开时钟","icon":"resources/base/media/emoji_time.png","onClick":[{"call":"clickToDeeplink","args":{"abilityName":"com.huawei.hmos.clock.phone","bundleName":"com.huawei.hmos.clock","intentName":"Clock","uri":""}}]}]
["/data/time/currentDate","示例"]
["/data/time/dayOfWeek","示例"]
["/data/time/lunarDate","示例"]
["/state/ready",true]
```
```request
{
  "content": {
    "size": "2x2",
    "functionName": "generateWidgetCardCompactDsl",
    "romVersion": "CMU-AL10 7.0.0.111",
    "candidateAssetIds": [
      "asset.emoji_time"
    ],
    "candidateEventCandidates": [
      {
        "capabilityId": "event.open.clock.alarm",
        "action": {
          "call": "clickToDeeplink",
          "args": {
            "abilityName": "com.huawei.hmos.clock.phone",
            "bundleName": "com.huawei.hmos.clock",
            "intentName": "Clock",
            "uri": ""
          }
        }
      }
    ],
    "bundleName": "com.huawei.genui",
    "description": "实时时钟卡片",
    "userQuery": "创建一张桌面时钟卡片，显示当前时间、日期、星期和农历信息。",
    "title": "时钟",
    "candidateDataBindings": [
      {
        "capabilityId": "GetCurrentTime",
        "arguments": {},
        "writeResultTo": "/data/time",
        "candidateOutputFields": [
          "/currentDate",
          "/dayOfWeek",
          "/lunarDate"
        ]
      }
    ]
  },
  "deviceInfo": {
    "countryCode": "CN",
    "deviceFormation": "HDSpeaker",
    "deviceType": 0,
    "locale": "zh-CN",
    "phoneType": "CMU-AL10",
    "prdVer": "11.7.8.342",
    "sysVer": "EmotionUI_9.0.0",
    "time": "20261102131225391"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q442-000",
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
  "romVersion": "CMU-AL10 7.0.0.111",
  "candidateAssetIds": [
    "asset.emoji_time"
  ],
  "candidateEventCandidates": [
    {
      "capabilityId": "event.open.clock.alarm",
      "action": {
        "call": "clickToDeeplink",
        "args": {
          "abilityName": "com.huawei.hmos.clock.phone",
          "bundleName": "com.huawei.hmos.clock",
          "intentName": "Clock",
          "uri": ""
        }
      }
    }
  ],
  "bundleName": "com.huawei.genui",
  "description": "实时时钟卡片",
  "userQuery": "创建一张桌面时钟卡片，显示当前时间、日期、星期和农历信息。",
  "title": "时钟",
  "candidateDataBindings": [
    {
      "capabilityId": "GetCurrentTime",
      "arguments": {},
      "writeResultTo": "/data/time",
      "candidateOutputFields": [
        "/currentDate",
        "/dayOfWeek",
        "/lunarDate"
      ]
    }
  ]
}
```
