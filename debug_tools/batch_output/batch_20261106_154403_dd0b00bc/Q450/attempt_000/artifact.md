```cardspec
{
  "title": "时钟",
  "description": "实时时钟卡片",
  "suggestSize": "2x4",
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
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Column","children":["title","__layout__root__body"],"itemMargin":6,"styles":{"width":"matchParent","height":"matchParent","padding":12,"borderRadius":20,"clip":true,"alignItems":"start","justifyContent":"start","linearGradient":{"direction":"RightBottom","colors":[["#FFCBDDFE",0],["#FFF1F6FE",1]]}}},{"id":"title","component":"Row","children":["title_title","title_icon"],"styles":{"width":"matchParent","height":20,"flexShrink":0,"justifyContent":"spaceBetween","alignItems":"center"},"itemMargin":0},{"id":"title_title","component":"Text","content":"当前时间","styles":{"fontSize":12,"fontWeight":400,"lineHeight":1,"textAlign":"start","maxLines":1,"flexShrink":1,"width":"wrapContent","layoutWeight":1,"constraintSize":{"minWidth":0},"fontColor":"#991F4799"}},{"id":"title_icon","component":"Image","src":"resources/base/media/emoji_time.png","styles":{"width":20,"height":20,"objectFit":"contain","flexShrink":0}},{"id":"__layout__root__body","component":"Column","children":["__layout__root__primary","__layout__root__details"],"itemMargin":8,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1}},{"id":"__layout__root__primary","component":"Column","children":["primary"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"primary","component":"Column","children":["primary_main"],"itemMargin":2,"styles":{"alignItems":"start","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent"}},{"id":"primary_main","component":"Text","content":"当前时间","styles":{"height":18,"fontSize":18,"fontWeight":700,"lineHeight":1,"maxLines":1,"flexShrink":1,"width":"matchParent","fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"__layout__root__details","component":"Column","children":["details"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1},"itemMargin":0},{"id":"details","component":"Row","children":["details_item0","details_item1","details_item2"],"itemMargin":8,"styles":{"width":"matchParent","height":"matchParent","alignItems":"top","justifyContent":"start","layoutWeight":1,"flexShrink":1,"constraintSize":{"minHeight":48}}},{"id":"details_item0","component":"Column","children":["details_item0_label_slot","details_item0_value_slot"],"itemMargin":2,"styles":{"height":"matchParent","backgroundColor":"#99FFFFFF","padding":{"left":8,"right":8},"borderRadius":16,"alignItems":"start","justifyContent":"center","layoutWeight":1,"flexShrink":1,"constraintSize":{"minWidth":0,"minHeight":0}}},{"id":"details_item0_label_slot","component":"Row","children":["details_item0_label"],"styles":{"width":"matchParent","height":18,"alignItems":"center","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"details_item0_label","component":"Text","content":"日期","styles":{"width":"matchParent","fontSize":12,"fontWeight":700,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","fontColor":"#991F4799"}},{"id":"details_item0_value_slot","component":"Row","children":["details_item0_value"],"styles":{"width":"matchParent","height":16,"alignItems":"center","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"details_item0_value","component":"Text","content":"{{ ${/data/time/currentDate} }}","styles":{"width":"matchParent","fontSize":10,"fontWeight":500,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","fontColor":"#FF1F4799"}},{"id":"details_item1","component":"Column","children":["details_item1_label_slot","details_item1_value_slot"],"itemMargin":2,"styles":{"height":"matchParent","backgroundColor":"#99FFFFFF","padding":{"left":8,"right":8},"borderRadius":16,"alignItems":"start","justifyContent":"center","layoutWeight":1,"flexShrink":1,"constraintSize":{"minWidth":0,"minHeight":0}}},{"id":"details_item1_label_slot","component":"Row","children":["details_item1_label"],"styles":{"width":"matchParent","height":18,"alignItems":"center","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"details_item1_label","component":"Text","content":"星期","styles":{"width":"matchParent","fontSize":12,"fontWeight":700,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","fontColor":"#991F4799"}},{"id":"details_item1_value_slot","component":"Row","children":["details_item1_value"],"styles":{"width":"matchParent","height":16,"alignItems":"center","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"details_item1_value","component":"Text","content":"{{ ${/data/time/dayOfWeek} }}","styles":{"width":"matchParent","fontSize":10,"fontWeight":500,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","fontColor":"#FF1F4799"}},{"id":"details_item2","component":"Column","children":["details_item2_label_slot","details_item2_value_slot"],"itemMargin":2,"styles":{"height":"matchParent","backgroundColor":"#99FFFFFF","padding":{"left":8,"right":8},"borderRadius":16,"alignItems":"start","justifyContent":"center","layoutWeight":1,"flexShrink":1,"constraintSize":{"minWidth":0,"minHeight":0}}},{"id":"details_item2_label_slot","component":"Row","children":["details_item2_label"],"styles":{"width":"matchParent","height":18,"alignItems":"center","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"details_item2_label","component":"Text","content":"农历","styles":{"width":"matchParent","fontSize":12,"fontWeight":700,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","fontColor":"#991F4799"}},{"id":"details_item2_value_slot","component":"Row","children":["details_item2_value"],"styles":{"width":"matchParent","height":16,"alignItems":"center","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"details_item2_value","component":"Text","content":"{{ ${/data/time/lunarDate} }}","styles":{"width":"matchParent","fontSize":10,"fontWeight":500,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","fontColor":"#FF1F4799"}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"time":{"currentDate":"示例","dayOfWeek":"示例","lunarDate":"示例"}},"state":{"ready":true}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "创建一张横版2x4尺寸的桌面时钟卡片，重点突出显示当前时间，同时展示日期、星期和农历信息。",
  "size": "2x4",
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
  "artifactId": "0862bece-f179-4a28-8bc7-fa29ebccef25",
  "createdAt": 1793951115697
}
```
```designcompactdsl
["root","Layout",{"layout":"W-top-bottom","variant":"continuous"},["title","primary","details"]]
["title","SingleLineTitle",{"title":"当前时间","icon":"resources/base/media/emoji_time.png","fontSize":12}]
["primary","EmphasisText",{"mainText":"当前时间","fontSize":18}]
["details","TextBlock",{"items":[{"label":"日期","value":{"path":"/data/time/currentDate"}},{"label":"星期","value":{"path":"/data/time/dayOfWeek"}},{"label":"农历","value":{"path":"/data/time/lunarDate"}}]}]
["/data/time/currentDate","示例"]
["/data/time/dayOfWeek","示例"]
["/data/time/lunarDate","示例"]
["/state/ready",true]
```
```request
{
  "content": {
    "size": "2x4",
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
    "userQuery": "创建一张横版2x4尺寸的桌面时钟卡片，重点突出显示当前时间，同时展示日期、星期和农历信息。",
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
    "time": "20261102131342789"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q450-000",
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
  "userQuery": "创建一张横版2x4尺寸的桌面时钟卡片，重点突出显示当前时间，同时展示日期、星期和农历信息。",
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
