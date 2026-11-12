```cardspec
{
  "title": "时间卡片",
  "description": "展示当前时间、日期、星期和农历的桌面时间卡片",
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
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Column","children":["time_group","date_group"],"itemMargin":8,"onClick":[{"call":"clickToDeeplink","args":{"abilityName":"com.huawei.hmos.clock.phone","bundleName":"com.huawei.hmos.clock","intentName":"Clock","uri":""}}],"styles":{"width":"matchParent","height":"matchParent","padding":12,"borderRadius":20,"clip":true,"alignItems":"center","justifyContent":"center","linearGradient":{"direction":"RightBottom","colors":[["#FFCBDDFE",0],["#FFF1F6FE",1]]}}},{"id":"time_group","component":"Text","content":"18:30","styles":{"width":126,"fontSize":18,"fontWeight":700,"fontColor":"#FF1F4799","textAlign":"center","maxLines":1,"textOverflow":"clip"}},{"id":"date_group","component":"Text","content":"2025年3月15日 周六 · 农历正月十六","styles":{"width":126,"fontSize":12,"fontWeight":400,"fontColor":"#991F4799","textAlign":"center","maxLines":1,"textOverflow":"clip"}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"state":{"ready":true}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "生成一个漂亮的桌面时间卡片，显示当前时间、日期、星期和农历，点击打开闹钟",
  "size": "2x2",
  "appVersion": "11.7.8.342",
  "eventCandidates": [
    {
      "id": "event.open.clock.alarm",
      "description": "打开闹钟应用首页",
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
    "data": {}
  },
  "assetCandidates": []
}
```
```effectivecapabilities
{
  "data": [],
  "event": [
    {
      "id": "event.open.clock.alarm",
      "description": "打开闹钟应用首页",
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
  "candidateDataBindings": [],
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
  "artifactId": "bcf5dedf-3f0b-47d1-ad88-ada12cb21d7d",
  "createdAt": 1793693182939
}
```
```designcompactdsl
["root","Column",{"width":"matchParent","height":"matchParent","padding":12,"borderRadius":20,"clip":true,"alignItems":"center","justifyContent":"center","itemMargin":8,"linearGradient":{"direction":"RightBottom","colors":[["#FFCBDDFE",0],["#FFF1F6FE",1]]},"onClick":[{"call":"clickToDeeplink","args":{"abilityName":"com.huawei.hmos.clock.phone","bundleName":"com.huawei.hmos.clock","intentName":"Clock","uri":""}}]},["time_group","date_group"]]
["time_group","Text",{"content":{"path":"/data/time"},"width":126,"fontSize":18,"fontWeight":700,"fontColor":"#FF1F4799","textAlign":"center","maxLines":1}]
["date_group","Text",{"content":{"path":"/data/date"},"width":126,"fontSize":12,"fontWeight":400,"fontColor":"#991F4799","textAlign":"center","maxLines":1}]
["/state/ready",true]
["/data/time","18:30"]
["/data/date","2025年3月15日 周六 · 农历正月十六"]
```
```request
{
  "content": {
    "dataCapabilities": [
      {
        "dataModelSkeleton": {},
        "dependencies": {
          "requiredPackages": []
        },
        "description": "获取设备当前的实时时间、日期、星期以及对应的农历信息。",
        "id": "GetCurrentTime",
        "inputSchema": {
          "properties": {},
          "required": [],
          "type": "object"
        },
        "outputSchema": {
          "description": "经过端侧格式化的当前系统时间实体，包含公历、农历和星期等信息，适合直接用于桌面卡片的时钟或日历组件渲染。",
          "properties": {
            "currentDate": {
              "description": "格式化的当前公历日期（年-月-日），例如 '2026-07-09'。",
              "type": "string"
            },
            "dayOfWeek": {
              "description": "中文的星期描述，例如 '星期四'。",
              "type": "string"
            },
            "lunarDate": {
              "description": "格式化的中国传统农历日期，例如 '五月廿六'。若系统获取失败则可能为空字符串。",
              "type": "string"
            },
            "updatedAt": {
              "description": "端侧完成该时间数据组装的时间戳字符串，格式如 '2026-07-09 15:30:00'。",
              "type": "string"
            }
          },
          "type": "object"
        },
        "type": "data"
      }
    ],
    "functionName": "generateWidgetCardCompactDsl",
    "romVersion": "CMM-AL10P 7.0.0.111",
    "candidateEventCandidates": [
      {
        "action": {
          "args": {
            "abilityName": "com.huawei.hmos.clock.phone",
            "bundleName": "com.huawei.hmos.clock",
            "intentName": "Clock",
            "uri": ""
          },
          "call": "clickToDeeplink"
        },
        "capabilityId": "event.open.clock.alarm"
      }
    ],
    "description": "展示当前时间、日期、星期和农历的桌面时间卡片",
    "userQuery": "生成一个漂亮的桌面时间卡片，显示当前时间、日期、星期和农历，点击打开闹钟",
    "title": "时间卡片",
    "cardStyle": "modern"
  },
  "deviceInfo": {
    "countryCode": "CN",
    "deviceFormation": "HDSpeaker",
    "deviceType": 0,
    "locale": "zh-CN",
    "phoneType": "CMM-AL10",
    "prdVer": "11.7.8.342",
    "sysVer": "EmotionUI_9.0.0",
    "time": "20261103080603314"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "1",
    "isNew": false,
    "sessionId": "37501657-c145-469b-bb53-d8475669b3e6"
  },
  "userAuth": {
    "user": {}
  },
  "utterance": {
    "original": "",
    "type": "text"
  },
  "version": "1.0",
  "dataCapabilities": [
    {
      "dataModelSkeleton": {},
      "dependencies": {
        "requiredPackages": []
      },
      "description": "获取设备当前的实时时间、日期、星期以及对应的农历信息。",
      "id": "GetCurrentTime",
      "inputSchema": {
        "properties": {},
        "required": [],
        "type": "object"
      },
      "outputSchema": {
        "description": "经过端侧格式化的当前系统时间实体，包含公历、农历和星期等信息，适合直接用于桌面卡片的时钟或日历组件渲染。",
        "properties": {
          "currentDate": {
            "description": "格式化的当前公历日期（年-月-日），例如 '2026-07-09'。",
            "type": "string"
          },
          "dayOfWeek": {
            "description": "中文的星期描述，例如 '星期四'。",
            "type": "string"
          },
          "lunarDate": {
            "description": "格式化的中国传统农历日期，例如 '五月廿六'。若系统获取失败则可能为空字符串。",
            "type": "string"
          },
          "updatedAt": {
            "description": "端侧完成该时间数据组装的时间戳字符串，格式如 '2026-07-09 15:30:00'。",
            "type": "string"
          }
        },
        "type": "object"
      },
      "type": "data"
    }
  ],
  "functionName": "generateWidgetCardCompactDsl",
  "romVersion": "CMM-AL10P 7.0.0.111",
  "candidateEventCandidates": [
    {
      "action": {
        "args": {
          "abilityName": "com.huawei.hmos.clock.phone",
          "bundleName": "com.huawei.hmos.clock",
          "intentName": "Clock",
          "uri": ""
        },
        "call": "clickToDeeplink"
      },
      "capabilityId": "event.open.clock.alarm"
    }
  ],
  "description": "展示当前时间、日期、星期和农历的桌面时间卡片",
  "userQuery": "生成一个漂亮的桌面时间卡片，显示当前时间、日期、星期和农历，点击打开闹钟",
  "title": "时间卡片",
  "cardStyle": "modern"
}
```
```repair-1
{
  "modelGeneratedCompactDsl": "[\"root\",\"Column\",{\"width\":\"matchParent\",\"height\":\"matchParent\",\"padding\":12,\"borderRadius\":20,\"clip\":true,\"alignItems\":\"center\",\"justifyContent\":\"center\",\"itemMargin\":8,\"linearGradient\":{\"direction\":\"RightBottom\",\"colors\":[[\"#FFCBDDFE\",0],[\"#FFF1F6FE\",1]]},\"onClick\":[{\"call\":\"clickToDeeplink\",\"args\":{\"abilityName\":\"com.huawei.hmos.clock.phone\",\"bundleName\":\"com.huawei.hmos.clock\",\"intentName\":\"Clock\",\"uri\":\"\"}}]},[\"time_group\",\"date_group\",\"lunar_group\"]]\n[\"time_group\",\"Row\",{\"itemMargin\":2,\"alignItems\":\"bottom\",\"justifyContent\":\"center\"},[\"time_value\",\"time_suffix\"]]\n[\"time_value\",\"Text\",{\"content\":{\"path\":\"/data/time\"},\"fontSize\":38,\"fontWeight\":700,\"fontColor\":\"#FF1F4799\",\"maxLines\":1}]\n[\"time_suffix\",\"Text\",{\"content\":\"时\",\"fontSize\":16,\"fontWeight\":400,\"fontColor\":\"#FF1F4799\",\"maxLines\":1,\"padding\":{\"bottom\":6}}]\n[\"date_group\",\"Text\",{\"content\":{\"path\":\"/data/date\"},\"width\":126,\"fontSize\":16,\"fontWeight\":600,\"fontColor\":\"#FF1F4799\",\"textAlign\":\"center\",\"maxLines\":1}]\n[\"lunar_group\",\"Text\",{\"content\":{\"path\":\"/data/lunar\"},\"width\":126,\"fontSize\":12,\"fontWeight\":400,\"fontColor\":\"#991F4799\",\"textAlign\":\"center\",\"maxLines\":1}]\n[\"/state/ready\",true]\n[\"/data/time\",\"18:30\"]\n[\"/data/date\",\"2025年3月15日 周六\"]\n[\"/data/lunar\",\"农历正月十六\"]",
  "generatedDsl": "",
  "validationErrors": [
    {
      "stage": "validation",
      "code": "COMPACT_DSL_VALIDATION_FAILED",
      "message": "component time_value: fontSize 38 requires a pure number/integer or a supported primary value. A directly bound measurement with a declared unit may use 20/24fp in a full-width area or 2x4 large panel when its text budget fits; ordinary names, dates, times, and statuses remain at most 18fp."
    },
    {
      "stage": "validation",
      "code": "COMPACT_DSL_VALIDATION_FAILED",
      "message": "component time_group: Text time_suffix after the large numeric value must contain only a real unit for the preceding value. Move labels or descriptions to a separate line."
    },
    {
      "stage": "validation",
      "code": "COMPACT_DSL_VALIDATION_FAILED",
      "message": "2x2 150vp single-business content with a 30fp/38fp numeric hero may contain only the value/unit line and one 12fp/400 auxiliary line. Merge auxiliary fields into that line with ' | '."
    }
  ]
}
```
```repair-2
{
  "modelGeneratedCompactDsl": "[\"root\",\"Column\",{\"width\":\"matchParent\",\"height\":\"matchParent\",\"padding\":12,\"borderRadius\":20,\"clip\":true,\"alignItems\":\"center\",\"justifyContent\":\"center\",\"itemMargin\":8,\"linearGradient\":{\"direction\":\"RightBottom\",\"colors\":[[\"#FFCBDDFE\",0],[\"#FFF1F6FE\",1]]},\"onClick\":[{\"call\":\"clickToDeeplink\",\"args\":{\"abilityName\":\"com.huawei.hmos.clock.phone\",\"bundleName\":\"com.huawei.hmos.clock\",\"intentName\":\"Clock\",\"uri\":\"\"}}]},[\"time_group\",\"date_group\"]]\n[\"time_group\",\"Text\",{\"content\":{\"path\":\"/data/time\"},\"width\":126,\"fontSize\":20,\"fontWeight\":700,\"fontColor\":\"#FF1F4799\",\"textAlign\":\"center\",\"maxLines\":1}]\n[\"date_group\",\"Text\",{\"content\":{\"path\":\"/data/date\"},\"width\":126,\"fontSize\":12,\"fontWeight\":400,\"fontColor\":\"#991F4799\",\"textAlign\":\"center\",\"maxLines\":1}]\n[\"/state/ready\",true]\n[\"/data/time\",\"18:30\"]\n[\"/data/date\",\"2025年3月15日 周六 · 农历正月十六\"]",
  "generatedDsl": "",
  "validationErrors": [
    {
      "stage": "validation",
      "code": "COMPACT_DSL_VALIDATION_FAILED",
      "message": "component time_group: fontSize 20 requires a pure number/integer or a supported primary value. A directly bound measurement with a declared unit may use 20/24fp in a full-width area or 2x4 large panel when its text budget fits; ordinary names, dates, times, and statuses remain at most 18fp."
    }
  ]
}
```
```repair-3
{
  "modelGeneratedCompactDsl": "[\"root\",\"Column\",{\"width\":\"matchParent\",\"height\":\"matchParent\",\"padding\":12,\"borderRadius\":20,\"clip\":true,\"alignItems\":\"center\",\"justifyContent\":\"center\",\"itemMargin\":8,\"linearGradient\":{\"direction\":\"RightBottom\",\"colors\":[[\"#FFCBDDFE\",0],[\"#FFF1F6FE\",1]]},\"onClick\":[{\"call\":\"clickToDeeplink\",\"args\":{\"abilityName\":\"com.huawei.hmos.clock.phone\",\"bundleName\":\"com.huawei.hmos.clock\",\"intentName\":\"Clock\",\"uri\":\"\"}}]},[\"time_group\",\"date_group\"]]\n[\"time_group\",\"Text\",{\"content\":{\"path\":\"/data/time\"},\"width\":126,\"fontSize\":18,\"fontWeight\":700,\"fontColor\":\"#FF1F4799\",\"textAlign\":\"center\",\"maxLines\":1}]\n[\"date_group\",\"Text\",{\"content\":{\"path\":\"/data/date\"},\"width\":126,\"fontSize\":12,\"fontWeight\":400,\"fontColor\":\"#991F4799\",\"textAlign\":\"center\",\"maxLines\":1}]\n[\"/state/ready\",true]\n[\"/data/time\",\"18:30\"]\n[\"/data/date\",\"2025年3月15日 周六 · 农历正月十六\"]",
  "generatedDsl": "{\"version\":\"v0.9\",\"createSurface\":{\"surfaceId\":\"surface_card\",\"catalogId\":\"ohos.a2ui.extended.catalog.form\"}}\n{\"version\":\"v0.9\",\"updateComponents\":{\"surfaceId\":\"surface_card\",\"root\":\"root\",\"components\":[{\"id\":\"root\",\"component\":\"Column\",\"children\":[\"time_group\",\"date_group\"],\"itemMargin\":8,\"onClick\":[{\"call\":\"clickToDeeplink\",\"args\":{\"abilityName\":\"com.huawei.hmos.clock.phone\",\"bundleName\":\"com.huawei.hmos.clock\",\"intentName\":\"Clock\",\"uri\":\"\"}}],\"styles\":{\"width\":\"matchParent\",\"height\":\"matchParent\",\"padding\":12,\"borderRadius\":20,\"clip\":true,\"alignItems\":\"center\",\"justifyContent\":\"center\",\"linearGradient\":{\"direction\":\"RightBottom\",\"colors\":[[\"#FFCBDDFE\",0],[\"#FFF1F6FE\",1]]}}},{\"id\":\"time_group\",\"component\":\"Text\",\"content\":\"18:30\",\"styles\":{\"width\":126,\"fontSize\":18,\"fontWeight\":700,\"fontColor\":\"#FF1F4799\",\"textAlign\":\"center\",\"maxLines\":1,\"textOverflow\":\"clip\"}},{\"id\":\"date_group\",\"component\":\"Text\",\"content\":\"2025年3月15日 周六 · 农历正月十六\",\"styles\":{\"width\":126,\"fontSize\":12,\"fontWeight\":400,\"fontColor\":\"#991F4799\",\"textAlign\":\"center\",\"maxLines\":1,\"textOverflow\":\"clip\"}}]}}\n{\"version\":\"v0.9\",\"updateDataModel\":{\"surfaceId\":\"surface_card\",\"path\":\"/\",\"value\":{\"state\":{\"ready\":true}}}}",
  "validationErrors": []
}
```
