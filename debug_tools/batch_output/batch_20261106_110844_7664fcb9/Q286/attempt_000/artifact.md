```cardspec
{
  "title": "小艺卡片",
  "description": "时间电量速览",
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
    },
    {
      "capabilityId": "GetPhoneBatteryInfo",
      "arguments": {},
      "writeResultTo": "/data/battery"
    }
  ]
}
```
```genui
{"version":"v0.9","createSurface":{"surfaceId":"surface_card","catalogId":"ohos.a2ui.extended.catalog.form"}}
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Column","children":["first","second"],"itemMargin":8,"styles":{"width":"matchParent","height":"matchParent","borderRadius":20,"clip":true,"alignItems":"start","justifyContent":"start","padding":8,"linearGradient":{"direction":"RightBottom","colors":[["#FFCBDDFE",0],["#FFF1F6FE",1]]}}},{"id":"first","component":"Column","children":["first_text"],"itemMargin":0,"styles":{"padding":{"left":8,"right":8},"borderRadius":16,"alignItems":"start","justifyContent":"center","clip":true,"flexShrink":0,"width":"matchParent","height":63,"backgroundColor":"#CCFFFFFF","layoutWeight":1}},{"id":"first_text","component":"Column","children":["first_primary","first_secondary"],"itemMargin":0,"styles":{"alignItems":"start","justifyContent":"center","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent"}},{"id":"first_primary","component":"Text","content":"{{ ${/data/time/currentDate} }}","styles":{"height":22,"fontSize":16,"fontWeight":700,"maxLines":1,"flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent","fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"first_secondary","component":"Text","content":"{{ ${/data/time/dayOfWeek} }}","styles":{"height":16,"fontSize":12,"fontWeight":500,"maxLines":1,"textOverflow":"ellipsis","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent","fontColor":"#FF1F4799"}},{"id":"second","component":"Column","children":["second_text"],"itemMargin":0,"styles":{"padding":{"left":8,"right":8},"borderRadius":16,"alignItems":"start","justifyContent":"center","clip":true,"flexShrink":0,"width":"matchParent","height":63,"backgroundColor":"#CCFFFFFF","layoutWeight":1}},{"id":"second_text","component":"Column","children":["second_primary","second_secondary"],"itemMargin":0,"styles":{"alignItems":"start","justifyContent":"center","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent"}},{"id":"second_primary","component":"Text","content":"{{ ${/data/battery/batterySOCText} }}","styles":{"height":22,"fontSize":16,"fontWeight":700,"maxLines":1,"flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent","fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"second_secondary","component":"Text","content":"{{ ${/data/battery/chargingStatusDesc} }}","styles":{"height":16,"fontSize":12,"fontWeight":500,"maxLines":1,"textOverflow":"ellipsis","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent","fontColor":"#FF1F4799"}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"time":{"currentDate":"示例","dayOfWeek":"示例"},"battery":{"batterySOCText":"68%","chargingStatusDesc":"未充电"}}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "创建一张小艺卡片，展示当前时间、日期和星期，以及手机当前电量信息。",
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
        "lunarDate": {
          "type": "string",
          "description": "格式化的中国传统农历日期，例如 '五月廿六'。若系统获取失败则可能为空字符串。",
          "sampleValue": "示例"
        }
      },
      "battery": {
        "batterySOCText": {
          "type": "string",
          "description": "可直接显示的当前手机设备剩余电量文本，已包含“%”单位；展示时不得再次追加“%”。",
          "sampleValue": "68%",
          "numericSource": "/data/battery/batterySOC"
        },
        "chargingStatusDesc": {
          "type": "string",
          "description": "当前设备电池的充电状态文本描述。",
          "sampleValue": "未充电"
        },
        "batterySOC": {
          "type": "integer",
          "description": "当前手机设备剩余电量的纯整数百分比，取值范围为 0 到 100，返回值不包含“%”。若直接用于文本展示，必须在数值后追加“%”；优先使用 batterySOCText。",
          "sampleValue": 68
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
    "GetCurrentTime",
    "GetPhoneBatteryInfo"
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
        "/lunarDate"
      ]
    },
    {
      "capabilityId": "GetPhoneBatteryInfo",
      "arguments": {},
      "writeResultTo": "/data/battery",
      "candidateOutputFields": [
        "/batterySOCText",
        "/chargingStatusDesc",
        "/batterySOC"
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
  "artifactId": "b61cb85d-0f66-487f-9f32-e3f8fa954405",
  "createdAt": 1793934532315
}
```
```designcompactdsl
["root","Layout",{"layout":"S-dual-info"},["first","second"]]
["first","InfoBlock",{"surfaceRole":"panel","primaryText":{"path":"/data/time/currentDate"},"secondaryText":{"path":"/data/time/dayOfWeek"}}]
["second","InfoBlock",{"surfaceRole":"panel","primaryText":{"path":"/data/battery/batterySOCText"},"secondaryText":{"path":"/data/battery/chargingStatusDesc"}}]
["/data/time/currentDate","示例"]
["/data/time/dayOfWeek","示例"]
["/data/battery/batterySOCText","68%"]
["/data/battery/chargingStatusDesc","未充电"]
```
```request
{
  "content": {
    "bundleName": "com.huawei.genui",
    "userQuery": "创建一张小艺卡片，展示当前时间、日期和星期，以及手机当前电量信息。",
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
      },
      {
        "capabilityId": "GetPhoneBatteryInfo",
        "arguments": {},
        "writeResultTo": "/data/battery",
        "candidateOutputFields": [
          "/batterySOCText",
          "/chargingStatusDesc",
          "/batterySOC"
        ]
      }
    ],
    "title": "小艺卡片",
    "size": "2x2",
    "candidateEventCandidates": [],
    "description": "时间电量速览",
    "candidateAssetIds": []
  },
  "deviceInfo": {
    "countryCode": "CN",
    "deviceFormation": "HDSpeaker",
    "deviceType": 0,
    "locale": "zh-CN",
    "phoneType": "CMM-AL10",
    "prdVer": "11.7.8.342",
    "sysVer": "EmotionUI_9.0.0",
    "time": "20261028155507251"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q286-000",
    "isNew": true,
    "sessionId": "batch-7664fcb9"
  },
  "userAuth": {
    "user": {}
  },
  "utterance": {
    "original": "创建一张小艺卡片，展示当前时间、日期和星期，以及手机当前电量信息。",
    "type": "text"
  },
  "version": "1.0",
  "functionName": "generateWidgetCardCompactDsl",
  "romVersion": "CMM-AL10 7.0.0.111",
  "bundleName": "com.huawei.genui",
  "userQuery": "创建一张小艺卡片，展示当前时间、日期和星期，以及手机当前电量信息。",
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
    },
    {
      "capabilityId": "GetPhoneBatteryInfo",
      "arguments": {},
      "writeResultTo": "/data/battery",
      "candidateOutputFields": [
        "/batterySOCText",
        "/chargingStatusDesc",
        "/batterySOC"
      ]
    }
  ],
  "title": "小艺卡片",
  "size": "2x2",
  "candidateEventCandidates": [],
  "description": "时间电量速览",
  "candidateAssetIds": []
}
```
