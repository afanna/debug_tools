```cardspec
{
  "title": "时间",
  "description": "当前时间日期",
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
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Column","children":["title","__layout__root__content"],"itemMargin":6,"styles":{"width":"matchParent","height":"matchParent","borderRadius":20,"clip":true,"alignItems":"start","justifyContent":"start","padding":12,"linearGradient":{"direction":"RightBottom","colors":[["#FFCBDDFE",0],["#FFF1F6FE",1]]}}},{"id":"title","component":"Row","children":["title_title"],"styles":{"width":"matchParent","height":12,"flexShrink":0,"justifyContent":"start","alignItems":"center"},"itemMargin":0},{"id":"title_title","component":"Text","content":"时间","styles":{"fontSize":12,"fontWeight":400,"lineHeight":1,"textAlign":"start","maxLines":1,"flexShrink":0,"width":"matchParent","fontColor":"#991F4799"}},{"id":"__layout__root__content","component":"Column","children":["content"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"end","layoutWeight":1},"itemMargin":0},{"id":"content","component":"Column","children":["content_row0","content_row1","content_row2"],"itemMargin":2,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"center","flexShrink":1}},{"id":"content_row0","component":"Row","children":["content_row0_label","content_row0_value"],"itemMargin":8,"styles":{"width":"matchParent","height":16,"alignItems":"top","justifyContent":"spaceBetween","flexShrink":0}},{"id":"content_row0_label","component":"Text","content":"日期","styles":{"height":16,"fontSize":10,"fontWeight":500,"maxLines":1,"flexShrink":0,"fontColor":"#991F4799","textOverflow":"clip"}},{"id":"content_row0_value","component":"Text","content":"{{ ${/data/time/currentDate} }}","styles":{"height":16,"fontSize":10,"fontWeight":500,"textAlign":"end","maxLines":1,"flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1,"fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"content_row1","component":"Row","children":["content_row1_label","content_row1_value"],"itemMargin":8,"styles":{"width":"matchParent","height":16,"alignItems":"top","justifyContent":"spaceBetween","flexShrink":0}},{"id":"content_row1_label","component":"Text","content":"星期","styles":{"height":16,"fontSize":10,"fontWeight":500,"maxLines":1,"flexShrink":0,"fontColor":"#991F4799","textOverflow":"clip"}},{"id":"content_row1_value","component":"Text","content":"{{ ${/data/time/dayOfWeek} }}","styles":{"height":16,"fontSize":10,"fontWeight":500,"textAlign":"end","maxLines":1,"flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1,"fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"content_row2","component":"Row","children":["content_row2_label","content_row2_value"],"itemMargin":8,"styles":{"width":"matchParent","height":16,"alignItems":"top","justifyContent":"spaceBetween","flexShrink":0}},{"id":"content_row2_label","component":"Text","content":"农历","styles":{"height":16,"fontSize":10,"fontWeight":500,"maxLines":1,"flexShrink":0,"fontColor":"#991F4799","textOverflow":"clip"}},{"id":"content_row2_value","component":"Text","content":"{{ ${/data/time/lunarDate} }}","styles":{"height":16,"fontSize":10,"fontWeight":500,"textAlign":"end","maxLines":1,"flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1,"fontColor":"#FF1F4799","textOverflow":"clip"}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"time":{"currentDate":"示例","dayOfWeek":"示例","lunarDate":"示例"}}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "添加时间组件，在桌面卡片上显示当前时间、日期、星期和农历信息。",
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
        "/lunarDate"
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
  "artifactId": "027cef90-38b5-45b3-8620-68de94ddb7bd",
  "createdAt": 1793934612091
}
```
```designcompactdsl
["root","Layout",{"layout":"S-title-content"},["title","content"]]
["title","SingleLineTitle",{"title":"时间","fontSize":12}]
["content","TableText",{"items":[{"label":"日期","value":{"path":"/data/time/currentDate"}},{"label":"星期","value":{"path":"/data/time/dayOfWeek"}},{"label":"农历","value":{"path":"/data/time/lunarDate"}}],"fontSize":10}]
["/data/time/currentDate","示例"]
["/data/time/dayOfWeek","示例"]
["/data/time/lunarDate","示例"]
```
```request
{
  "content": {
    "bundleName": "com.huawei.genui",
    "userQuery": "添加时间组件，在桌面卡片上显示当前时间、日期、星期和农历信息。",
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
    "title": "时间",
    "size": "2x2",
    "candidateEventCandidates": [],
    "description": "当前时间日期",
    "candidateAssetIds": []
  },
  "deviceInfo": {
    "countryCode": "CN",
    "deviceFormation": "HDSpeaker",
    "deviceType": 0,
    "locale": "zh-CN",
    "phoneType": "CMU-AL10",
    "prdVer": "11.7.8.342",
    "sysVer": "EmotionUI_9.0.0",
    "time": "20261031005852928"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q375-000",
    "isNew": true,
    "sessionId": "batch-7664fcb9"
  },
  "userAuth": {
    "user": {}
  },
  "utterance": {
    "original": "添加时间组件，在桌面卡片上显示当前时间、日期、星期和农历信息。",
    "type": "text"
  },
  "version": "1.0",
  "functionName": "generateWidgetCardCompactDsl",
  "romVersion": "CMU-AL10 7.0.0.111",
  "bundleName": "com.huawei.genui",
  "userQuery": "添加时间组件，在桌面卡片上显示当前时间、日期、星期和农历信息。",
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
  "title": "时间",
  "size": "2x2",
  "candidateEventCandidates": [],
  "description": "当前时间日期",
  "candidateAssetIds": []
}
```
