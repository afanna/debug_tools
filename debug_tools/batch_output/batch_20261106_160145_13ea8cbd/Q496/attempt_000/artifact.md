```cardspec
{
  "title": "时钟",
  "description": "当前时间",
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
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Column","children":["title","__layout__root__body"],"itemMargin":6,"styles":{"width":"matchParent","height":"matchParent","borderRadius":20,"clip":true,"alignItems":"start","justifyContent":"start","padding":12,"linearGradient":{"direction":"RightBottom","colors":[["#FFCBDDFE",0],["#FFF1F6FE",1]]}}},{"id":"title","component":"Row","children":["title_title"],"styles":{"width":"matchParent","height":12,"flexShrink":0,"justifyContent":"start","alignItems":"center"},"itemMargin":0},{"id":"title_title","component":"Text","content":"时钟","styles":{"fontSize":12,"fontWeight":400,"lineHeight":1,"textAlign":"start","maxLines":1,"flexShrink":0,"width":"matchParent","fontColor":"#991F4799"}},{"id":"__layout__root__body","component":"Column","children":["__layout__root__content","__layout__root__action"],"itemMargin":8,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1}},{"id":"__layout__root__content","component":"Column","children":["content"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1},"itemMargin":0},{"id":"content","component":"Column","children":["content_row0","content_row1"],"itemMargin":2,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"center","flexShrink":1}},{"id":"content_row0","component":"Row","children":["content_row0_label","content_row0_value"],"itemMargin":8,"styles":{"width":"matchParent","height":18,"alignItems":"bottom","justifyContent":"spaceBetween","flexShrink":0}},{"id":"content_row0_label","component":"Text","content":"日期","styles":{"height":18,"fontSize":12,"fontWeight":500,"maxLines":1,"flexShrink":0,"fontColor":"#991F4799","textOverflow":"clip"}},{"id":"content_row0_value","component":"Text","content":"{{ ${/data/time/currentDate} }}","styles":{"height":18,"fontSize":12,"fontWeight":500,"textAlign":"end","maxLines":1,"flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1,"fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"content_row1","component":"Row","children":["content_row1_label","content_row1_value"],"itemMargin":8,"styles":{"width":"matchParent","height":18,"alignItems":"bottom","justifyContent":"spaceBetween","flexShrink":0}},{"id":"content_row1_label","component":"Text","content":"星期","styles":{"height":18,"fontSize":12,"fontWeight":500,"maxLines":1,"flexShrink":0,"fontColor":"#991F4799","textOverflow":"clip"}},{"id":"content_row1_value","component":"Text","content":"{{ ${/data/time/dayOfWeek} }}","styles":{"height":18,"fontSize":12,"fontWeight":500,"textAlign":"end","maxLines":1,"flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1,"fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"__layout__root__action","component":"Column","children":["action"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","height":36,"flexShrink":0},"itemMargin":0},{"id":"action","component":"Button","onClick":[{"call":"clickToDeeplink","args":{"abilityName":"com.huawei.hmos.clock.phone","bundleName":"com.huawei.hmos.clock","intentName":"Clock","uri":""}}],"label":"打开闹钟","styles":{"height":36,"borderRadius":30,"padding":0,"flexShrink":0,"width":"matchParent","backgroundColor":"#331F4799","fontColor":"#FF1F4799","fontSize":14,"fontWeight":500,"textAlign":"center"}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"time":{"currentDate":"示例","dayOfWeek":"示例"}}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "添加时钟挂件到桌面，显示当前时间、日期、星期，点击可打开闹钟应用。",
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
  "assetCandidates": []
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
  "artifactId": "7287cc20-e155-4f8b-8684-436618239b37",
  "createdAt": 1793952318850
}
```
```designcompactdsl
["root","Layout",{"layout":"S-title-content-action"},["title","content","action"]]
["title","SingleLineTitle",{"title":"时钟","fontSize":12}]
["content","TableText",{"items":[{"label":"日期","value":{"path":"/data/time/currentDate"}},{"label":"星期","value":{"path":"/data/time/dayOfWeek"}}],"fontSize":12}]
["action","PillButton",{"label":"打开闹钟","onClick":[{"call":"clickToDeeplink","args":{"abilityName":"com.huawei.hmos.clock.phone","bundleName":"com.huawei.hmos.clock","intentName":"Clock","uri":""}}]}]
["/data/time/currentDate","示例"]
["/data/time/dayOfWeek","示例"]
```
```request
{
  "content": {
    "size": "2x2",
    "functionName": "generateWidgetCardCompactDsl",
    "romVersion": "HLS-AL00 7.0.0.111",
    "candidateAssetIds": [],
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
    "description": "当前时间",
    "userQuery": "添加时钟挂件到桌面，显示当前时间、日期、星期，点击可打开闹钟应用。",
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
    "phoneType": "HLS-AL00",
    "prdVer": "11.7.8.342",
    "sysVer": "EmotionUI_9.0.0",
    "time": "20261101231704805"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q496-000",
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
  "description": "当前时间",
  "userQuery": "添加时钟挂件到桌面，显示当前时间、日期、星期，点击可打开闹钟应用。",
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
```repair-1
{
  "modelGeneratedCompactDsl": "[\"root\",\"Layout\",{\"layout\":\"S-title-content-action\"},[\"title\",\"content\",\"action\"]]\n[\"title\",\"SingleLineTitle\",{\"title\":\"时钟\",\"fontSize\":12}]\n[\"content\",\"TableText\",{\"items\":[{\"label\":\"日期\",\"value\":{\"path\":\"/data/time/currentDate\"}},{\"label\":\"星期\",\"value\":{\"path\":\"/data/time/dayOfWeek\"}}],\"fontSize\":12}]\n[\"action\",\"PillButton\",{\"label\":\"打开闹钟\",\"onClick\":[{\"call\":\"clickToDeeplink\",\"args\":{\"abilityName\":\"com.huawei.hmos.clock.phone\",\"bundleName\":\"com.huawei.hmos.clock\",\"intentName\":\"Clock\",\"uri\":\"\"}}]}]\n[\"/data/time/currentDate\",\"示例\"]\n[\"/data/time/dayOfWeek\",\"示例\"]",
  "generatedDsl": "{\"version\":\"v0.9\",\"createSurface\":{\"surfaceId\":\"surface_card\",\"catalogId\":\"ohos.a2ui.extended.catalog.form\"}}\n{\"version\":\"v0.9\",\"updateComponents\":{\"surfaceId\":\"surface_card\",\"root\":\"root\",\"components\":[{\"id\":\"root\",\"component\":\"Column\",\"children\":[\"title\",\"__layout__root__body\"],\"itemMargin\":6,\"styles\":{\"width\":\"matchParent\",\"height\":\"matchParent\",\"borderRadius\":20,\"clip\":true,\"alignItems\":\"start\",\"justifyContent\":\"start\",\"padding\":12}},{\"id\":\"title\",\"component\":\"Row\",\"children\":[\"title_title\"],\"styles\":{\"width\":\"matchParent\",\"height\":12,\"flexShrink\":0,\"justifyContent\":\"start\",\"alignItems\":\"center\"},\"itemMargin\":0},{\"id\":\"title_title\",\"component\":\"Text\",\"content\":\"时钟\",\"styles\":{\"fontSize\":12,\"fontWeight\":400,\"lineHeight\":1,\"textAlign\":\"start\",\"maxLines\":1,\"flexShrink\":0,\"width\":\"matchParent\",\"fontColor\":\"@theme:secondary/1\"}},{\"id\":\"__layout__root__body\",\"component\":\"Column\",\"children\":[\"__layout__root__content\",\"__layout__root__action\"],\"itemMargin\":8,\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"layoutWeight\":1}},{\"id\":\"__layout__root__content\",\"component\":\"Column\",\"children\":[\"content\"],\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"layoutWeight\":1},\"itemMargin\":0},{\"id\":\"content\",\"component\":\"Column\",\"children\":[\"content_row0\",\"content_row1\"],\"itemMargin\":2,\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"center\",\"flexShrink\":1}},{\"id\":\"content_row0\",\"component\":\"Row\",\"children\":[\"content_row0_label\",\"content_row0_value\"],\"itemMargin\":8,\"styles\":{\"width\":\"matchParent\",\"height\":18,\"alignItems\":\"bottom\",\"justifyContent\":\"spaceBetween\",\"flexShrink\":0}},{\"id\":\"content_row0_label\",\"component\":\"Text\",\"content\":\"日期\",\"styles\":{\"height\":18,\"fontSize\":12,\"fontWeight\":500,\"maxLines\":1,\"flexShrink\":0,\"fontColor\":\"@theme:primary/0.6\",\"textOverflow\":\"clip\"}},{\"id\":\"content_row0_value\",\"component\":\"Text\",\"content\":\"{{ ${/data/time/currentDate} }}\",\"styles\":{\"height\":18,\"fontSize\":12,\"fontWeight\":500,\"textAlign\":\"end\",\"maxLines\":1,\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"layoutWeight\":1,\"fontColor\":\"@theme:primary/1\",\"textOverflow\":\"clip\"}},{\"id\":\"content_row1\",\"component\":\"Row\",\"children\":[\"content_row1_label\",\"content_row1_value\"],\"itemMargin\":8,\"styles\":{\"width\":\"matchParent\",\"height\":18,\"alignItems\":\"bottom\",\"justifyContent\":\"spaceBetween\",\"flexShrink\":0}},{\"id\":\"content_row1_label\",\"component\":\"Text\",\"content\":\"星期\",\"styles\":{\"height\":18,\"fontSize\":12,\"fontWeight\":500,\"maxLines\":1,\"flexShrink\":0,\"fontColor\":\"@theme:primary/0.6\",\"textOverflow\":\"clip\"}},{\"id\":\"content_row1_value\",\"component\":\"Text\",\"content\":\"{{ ${/data/time/dayOfWeek} }}\",\"styles\":{\"height\":18,\"fontSize\":12,\"fontWeight\":500,\"textAlign\":\"end\",\"maxLines\":1,\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"layoutWeight\":1,\"fontColor\":\"@theme:primary/1\",\"textOverflow\":\"clip\"}},{\"id\":\"__layout__root__action\",\"component\":\"Column\",\"children\":[\"action\"],\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"height\":36,\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"action\",\"component\":\"Button\",\"onClick\":[{\"call\":\"clickToDeeplink\",\"args\":{\"abilityName\":\"com.huawei.hmos.clock.phone\",\"bundleName\":\"com.huawei.hmos.clock\",\"intentName\":\"Clock\",\"uri\":\"\"}}],\"label\":\"打开闹钟\",\"styles\":{\"height\":36,\"borderRadius\":30,\"padding\":0,\"flexShrink\":0,\"width\":\"matchParent\",\"backgroundColor\":\"@theme:componentSecondary/1\",\"fontColor\":\"@theme:primary/1\",\"fontSize\":14,\"fontWeight\":500,\"textAlign\":\"center\"}}]}}\n{\"version\":\"v0.9\",\"updateDataModel\":{\"surfaceId\":\"surface_card\",\"path\":\"/\",\"value\":{\"data\":{\"time\":{\"currentDate\":\"示例\",\"dayOfWeek\":\"示例\"}}}}}",
  "validationErrors": []
}
```
