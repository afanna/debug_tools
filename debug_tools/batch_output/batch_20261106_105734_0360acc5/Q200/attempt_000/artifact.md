```cardspec
{
  "title": "家庭简报",
  "description": "展示当前时间、手机电量、近期日程和备忘录待办的家庭简报卡片",
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
      "writeResultTo": "/data/currentTime"
    },
    {
      "capabilityId": "GetPhoneBatteryInfo",
      "arguments": {},
      "writeResultTo": "/data/phoneBattery"
    },
    {
      "capabilityId": "GetCalendarEvents",
      "arguments": {},
      "writeResultTo": "/data/calendar"
    },
    {
      "capabilityId": "GetMemoData",
      "arguments": {},
      "writeResultTo": "/data/memo"
    }
  ]
}
```
```genui
{"version":"v0.9","createSurface":{"surfaceId":"surface_card","catalogId":"ohos.a2ui.extended.catalog.form"}}
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Row","children":["content","__layout__root__slots"],"itemMargin":12,"styles":{"width":"matchParent","height":"matchParent","padding":12,"borderRadius":20,"clip":true,"alignItems":"center","justifyContent":"start","linearGradient":{"direction":"RightBottom","colors":[["#FFFFE0CC",0],["#FFFFF7F2",1]]}}},{"id":"content","component":"Column","children":["__layout__content__sub"],"styles":{"height":"matchParent","layoutWeight":1},"itemMargin":0},{"id":"__layout__content__sub","component":"Column","children":["content_title","__layout__content__body"],"itemMargin":8,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":126.0}},{"id":"content_title","component":"Row","children":["content_title_title"],"styles":{"width":"matchParent","height":12,"flexShrink":0,"justifyContent":"start","alignItems":"center"},"itemMargin":0},{"id":"content_title_title","component":"Text","content":"家庭简报","styles":{"fontSize":12,"fontWeight":400,"lineHeight":1,"textAlign":"start","maxLines":1,"flexShrink":0,"width":"matchParent","fontColor":"#998C4B1C"}},{"id":"__layout__content__body","component":"Column","children":["__layout__content__primary","__layout__content__details"],"itemMargin":8,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1}},{"id":"__layout__content__primary","component":"Column","children":["content_primary"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1},"itemMargin":0},{"id":"content_primary","component":"Column","children":["content_primary_main","content_primary_secondary"],"itemMargin":2,"styles":{"alignItems":"start","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent"}},{"id":"content_primary_main","component":"Text","content":"{{ ${/data/currentTime/currentDate} }}","styles":{"height":18,"fontSize":18,"fontWeight":700,"lineHeight":1,"maxLines":1,"flexShrink":1,"width":"matchParent","fontColor":"#FF8C4B1C","textOverflow":"clip"}},{"id":"content_primary_secondary","component":"Text","content":"{{ ${/data/currentTime/dayOfWeek} }}","styles":{"height":16,"fontSize":12,"fontWeight":400,"lineHeight":1.3333333333333333,"maxLines":1,"flexShrink":1,"width":"matchParent","fontColor":"#FF8C4B1C","textOverflow":"clip"}},{"id":"__layout__content__details","component":"Column","children":["content_support"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"content_support","component":"Row","children":["content_support_rail","content_support_texts"],"itemMargin":7,"styles":{"width":"matchParent","alignItems":"top","flexShrink":1,"clip":true,"height":50}},{"id":"content_support_rail","component":"Column","children":["content_support_rail_dot","content_support_rail_line"],"itemMargin":5,"styles":{"width":8,"padding":{"top":5,"bottom":0},"alignItems":"center","justifyContent":"start","flexShrink":0,"height":50,"clip":true}},{"id":"content_support_rail_dot","component":"Divider","styles":{"width":8,"height":8,"borderRadius":4,"borderWidth":1.5,"strokeWidth":0,"color":"#00000000","flexShrink":0,"borderColor":"#FF8C4B1C","backgroundColor":"#00000000"}},{"id":"content_support_rail_line","component":"Divider","styles":{"width":1,"strokeWidth":1,"vertical":true,"flexShrink":0,"height":32,"color":"#998C4B1C"}},{"id":"content_support_texts","component":"Column","children":["content_support_title","content_support_time","content_support_location"],"itemMargin":0,"styles":{"alignItems":"start","justifyContent":"start","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1,"height":50}},{"id":"content_support_title","component":"Text","content":"{{ ${/data/calendar/events/0/title} }}","styles":{"width":"matchParent","fontSize":14,"fontWeight":700,"maxLines":2,"flexShrink":0,"constraintSize":{"minWidth":0,"minHeight":18},"fontColor":"#FF8C4B1C","textOverflow":"clip"}},{"id":"content_support_time","component":"Text","content":"{{ ${/data/calendar/events/0/dtStart} }}","styles":{"width":"matchParent","height":16,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":0,"constraintSize":{"minWidth":0},"fontColor":"#998C4B1C","textOverflow":"clip"}},{"id":"content_support_location","component":"Text","content":"{{ ${/data/calendar/events/0/eventLocation} }}","styles":{"width":"matchParent","height":16,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":0,"constraintSize":{"minWidth":0},"fontColor":"#998C4B1C","textOverflow":"clip"}},{"id":"__layout__root__slots","component":"Column","children":["upper","lower"],"itemMargin":12,"styles":{"height":"matchParent","layoutWeight":1}},{"id":"upper","component":"Column","children":["upper_text"],"itemMargin":0,"styles":{"padding":{"left":8,"right":8},"borderRadius":16,"alignItems":"start","justifyContent":"center","clip":true,"flexShrink":0,"width":"matchParent","backgroundColor":"#99FFFFFF","layoutWeight":57.0}},{"id":"upper_text","component":"Column","children":["upper_primary","upper_secondary"],"itemMargin":2,"styles":{"alignItems":"start","justifyContent":"start","flexShrink":1,"constraintSize":{"minWidth":0},"height":"matchParent","padding":{"top":8},"width":"matchParent"}},{"id":"upper_primary","component":"Text","content":"{{ ${/data/phoneBattery/batterySOCText} }}","styles":{"height":19,"fontSize":14,"fontWeight":700,"maxLines":1,"flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent","lineHeight":1.3571428571428572,"fontColor":"#FF8C4B1C","textOverflow":"clip"}},{"id":"upper_secondary","component":"Text","content":"{{ ${/data/phoneBattery/chargingStatusDesc} }}","styles":{"height":16,"fontSize":12,"fontWeight":500,"maxLines":1,"textOverflow":"ellipsis","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent","lineHeight":1.3333333333333333,"fontColor":"#FF8C4B1C"}},{"id":"lower","component":"Column","children":["lower_text"],"itemMargin":0,"styles":{"padding":{"left":8,"right":8},"borderRadius":16,"alignItems":"start","justifyContent":"center","clip":true,"flexShrink":0,"width":"matchParent","backgroundColor":"#99FFFFFF","layoutWeight":57.0}},{"id":"lower_text","component":"Column","children":["lower_primary","lower_secondary"],"itemMargin":2,"styles":{"alignItems":"start","justifyContent":"start","flexShrink":1,"constraintSize":{"minWidth":0},"height":"matchParent","padding":{"top":8},"width":"matchParent"}},{"id":"lower_primary","component":"Text","content":"{{ ${/data/memo/todoPendingCount} + '/' + ${/data/memo/todoTotalCount} }}","styles":{"height":19,"fontSize":14,"fontWeight":700,"maxLines":1,"flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent","lineHeight":1.3571428571428572,"fontColor":"#FF8C4B1C","textOverflow":"clip"}},{"id":"lower_secondary","component":"Text","content":"待办 未完成/总数","styles":{"height":16,"fontSize":12,"fontWeight":500,"maxLines":1,"textOverflow":"ellipsis","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent","lineHeight":1.3333333333333333,"fontColor":"#998C4B1C"}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"currentTime":{"currentDate":"2026-07-09","dayOfWeek":"星期四"},"phoneBattery":{"batterySOCText":"68%","chargingStatusDesc":"未充电","batterySOC":68},"calendar":{"events":[{"dtStart":"14:00","eventLocation":"会议室","title":"项目例会"}]},"memo":{"todoPendingCount":0,"todoTotalCount":0}}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "家庭简报卡片，展示当前时间、手机电量、近期日程和备忘录待办信息",
  "size": "2x4",
  "appVersion": "11.7.8.342",
  "eventCandidates": [],
  "dataModelSchema": {
    "data": {
      "currentTime": {
        "currentDate": {
          "type": "string",
          "description": "格式化的当前公历日期（年-月-日），例如 '2026-07-09'。",
          "sampleValue": "示例"
        },
        "dayOfWeek": {
          "type": "string",
          "description": "中文的星期描述，例如 '星期四'。",
          "sampleValue": "示例"
        }
      },
      "phoneBattery": {
        "batterySOCText": {
          "type": "string",
          "description": "可直接显示的当前手机设备剩余电量文本，已包含“%”单位；展示时不得再次追加“%”。",
          "sampleValue": "68%",
          "numericSource": "/data/phoneBattery/batterySOC"
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
      },
      "calendar": {
        "events": [
          {
            "dtStart": {
              "type": "string",
              "description": "格式化后的日程开始时间短文本，如 '03:00'，若为全天日程可能为特殊标记。",
              "sampleValue": "14:00"
            },
            "eventLocation": {
              "type": "string",
              "description": "日程的具体地点描述，若未填写则为空字符串。",
              "sampleValue": "会议室"
            },
            "title": {
              "type": "string",
              "description": "日程标题，例如“咪咕视频《西班牙 VS 奥地利》”或“项目进展会”。",
              "sampleValue": "项目例会"
            }
          }
        ]
      },
      "memo": {
        "todoPendingCount": {
          "type": "integer",
          "description": "未完成的待办记录数。",
          "sampleValue": 0
        },
        "todoTotalCount": {
          "type": "integer",
          "description": "查询到的待办总数量（已过滤已删除待办）。",
          "sampleValue": 0
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
    "GetPhoneBatteryInfo",
    "GetCalendarEvents",
    "GetMemoData"
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
      "writeResultTo": "/data/currentTime",
      "candidateOutputFields": [
        "/currentDate",
        "/dayOfWeek"
      ]
    },
    {
      "capabilityId": "GetPhoneBatteryInfo",
      "arguments": {},
      "writeResultTo": "/data/phoneBattery",
      "candidateOutputFields": [
        "/batterySOCText",
        "/chargingStatusDesc",
        "/batterySOC"
      ]
    },
    {
      "capabilityId": "GetCalendarEvents",
      "arguments": {},
      "writeResultTo": "/data/calendar",
      "candidateOutputFields": [
        "/events/0/dtStart",
        "/events/0/eventLocation",
        "/events/0/title"
      ]
    },
    {
      "capabilityId": "GetMemoData",
      "arguments": {},
      "writeResultTo": "/data/memo",
      "candidateOutputFields": [
        "/todoPendingCount",
        "/todoTotalCount"
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
  "artifactId": "003ca5dd-39b2-46ba-a9c1-fb6827b2e293",
  "createdAt": 1793933877459
}
```
```designcompactdsl
["root","Layout",{"layout":"W-content-side-slots","orientation":"content-left"},["content","upper","lower"]]
["content","Region",{"variant":"title-hero-support"},["content_title","content_primary","content_support"]]
["content_title","SingleLineTitle",{"title":"家庭简报","fontSize":12}]
["content_primary","EmphasisText",{"mainText":{"path":"/data/currentTime/currentDate"},"secondaryText":{"path":"/data/currentTime/dayOfWeek"},"fontSize":18}]
["content_support","EventCard",{"items":[{"title":{"path":"/data/calendar/events/0/title"},"time":{"path":"/data/calendar/events/0/dtStart"},"location":{"path":"/data/calendar/events/0/eventLocation"}}]}]
["upper","InfoBlock",{"variant":"slot","primaryText":{"path":"/data/phoneBattery/batterySOCText"},"secondaryText":{"path":"/data/phoneBattery/chargingStatusDesc"}}]
["lower","InfoBlock",{"variant":"slot","primaryText":"{{ ${/data/memo/todoPendingCount} + '/' + ${/data/memo/todoTotalCount} }}","secondaryText":"待办 未完成/总数"}]
["/data/currentTime/currentDate","2026-07-09"]
["/data/currentTime/dayOfWeek","星期四"]
["/data/phoneBattery/batterySOCText","68%"]
["/data/phoneBattery/chargingStatusDesc","未充电"]
["/data/phoneBattery/batterySOC",68]
["/data/calendar/events/0/dtStart","14:00"]
["/data/calendar/events/0/eventLocation","会议室"]
["/data/calendar/events/0/title","项目例会"]
["/data/memo/todoPendingCount",0]
["/data/memo/todoTotalCount",0]
```
```request
{
  "content": {
    "title": "家庭简报",
    "description": "展示当前时间、手机电量、近期日程和备忘录待办的家庭简报卡片",
    "userQuery": "家庭简报卡片，展示当前时间、手机电量、近期日程和备忘录待办信息",
    "size": "2x4",
    "bundleName": "com.huawei.genui",
    "functionName": "generateWidgetCardCompactDsl",
    "romVersion": "CMS-AL20 7.0.0.111",
    "candidateDataBindings": [
      {
        "capabilityId": "GetCurrentTime",
        "writeResultTo": "/data/currentTime",
        "candidateOutputFields": [
          "/currentDate",
          "/dayOfWeek"
        ]
      },
      {
        "capabilityId": "GetPhoneBatteryInfo",
        "writeResultTo": "/data/phoneBattery",
        "candidateOutputFields": [
          "/batterySOCText",
          "/chargingStatusDesc"
        ]
      },
      {
        "capabilityId": "GetCalendarEvents",
        "writeResultTo": "/data/calendar",
        "candidateOutputFields": [
          "/events/0/dtStart",
          "/events/0/eventLocation",
          "/events/0/title"
        ]
      },
      {
        "capabilityId": "GetMemoData",
        "writeResultTo": "/data/memo",
        "candidateOutputFields": [
          "/todoPendingCount",
          "/todoTotalCount"
        ]
      }
    ],
    "candidateEventCandidates": [],
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
    "time": "20261027091150629"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q200-000",
    "isNew": true,
    "sessionId": "batch-0360acc5"
  },
  "userAuth": {
    "user": {}
  },
  "utterance": {
    "original": "",
    "type": "text"
  },
  "version": "1.0",
  "cardSize": "2x4",
  "assets": [],
  "dataCapabilities": [
    {
      "data": {
        "writeResultTo": "/data/currentTime"
      },
      "id": "GetCurrentTime"
    },
    {
      "data": {
        "writeResultTo": "/data/phoneBattery"
      },
      "id": "GetPhoneBatteryInfo"
    },
    {
      "data": {
        "futureDays": 7,
        "writeResultTo": "/data/calendar"
      },
      "id": "GetCalendarEvents"
    },
    {
      "data": {
        "writeResultTo": "/data/memo"
      },
      "id": "GetMemoData"
    }
  ],
  "functionName": "generateWidgetCardCompactDsl",
  "romVersion": "CMS-AL20 7.0.0.111",
  "bundleName": "com.huawei.genui",
  "description": "展示当前时间、手机电量、近期日程和备忘录待办的家庭简报卡片",
  "userQuery": "家庭简报卡片，展示当前时间、手机电量、近期日程和备忘录待办信息",
  "title": "家庭简报",
  "events": [
    {
      "id": "event.open.clock.alarm"
    },
    {
      "id": "event.viewNote"
    }
  ]
}
```
```repair-1
{
  "modelGeneratedCompactDsl": "[\"root\",\"Layout\",{\"layout\":\"W-content-side-slots\",\"orientation\":\"content-left\"},[\"content\",\"upper\",\"lower\"]]\n[\"content_title\",\"SingleLineTitle\",{\"title\":\"家庭简报\",\"fontSize\":12}]\n[\"content_primary\",\"EmphasisText\",{\"mainText\":{\"path\":\"/data/currentTime/currentDate\"},\"secondaryText\":{\"path\":\"/data/currentTime/dayOfWeek\"},\"fontSize\":18}]\n[\"content_support\",\"EventCard\",{\"items\":[{\"title\":{\"path\":\"/data/calendar/events/0/title\"},\"time\":{\"path\":\"/data/calendar/events/0/dtStart\"},\"location\":{\"path\":\"/data/calendar/events/0/eventLocation\"}}]}]\n[\"content\",\"Region\",{\"variant\":\"title-hero-support\"},[\"content_title\",\"content_primary\",\"content_support\"]]\n[\"upper\",\"InfoBlock\",{\"variant\":\"slot\",\"primaryText\":{\"path\":\"/data/phoneBattery/batterySOCText\"},\"secondaryText\":{\"path\":\"/data/phoneBattery/chargingStatusDesc\"}}]\n[\"lower\",\"InfoBlock\",{\"variant\":\"slot\",\"primaryText\":\"{{ ${/data/memo/todoPendingCount} + '/' + ${/data/memo/todoTotalCount} }}\",\"secondaryText\":\"待办 未完成/总数\"}]\n[\"/data/currentTime/currentDate\",\"2026-07-09\"]\n[\"/data/currentTime/dayOfWeek\",\"星期四\"]\n[\"/data/phoneBattery/batterySOCText\",\"68%\"]\n[\"/data/phoneBattery/chargingStatusDesc\",\"未充电\"]\n[\"/data/phoneBattery/batterySOC\",68]\n[\"/data/calendar/events/0/dtStart\",\"14:00\"]\n[\"/data/calendar/events/0/eventLocation\",\"会议室\"]\n[\"/data/calendar/events/0/title\",\"项目例会\"]\n[\"/data/memo/todoPendingCount\",0]\n[\"/data/memo/todoTotalCount\",0]",
  "generatedDsl": "{\"version\":\"v0.9\",\"createSurface\":{\"surfaceId\":\"surface_card\",\"catalogId\":\"ohos.a2ui.extended.catalog.form\"}}\n{\"version\":\"v0.9\",\"updateComponents\":{\"surfaceId\":\"surface_card\",\"root\":\"root\",\"components\":[{\"id\":\"root\",\"component\":\"Row\",\"children\":[\"content\",\"__layout__root__slots\"],\"itemMargin\":12,\"styles\":{\"width\":\"matchParent\",\"height\":\"matchParent\",\"padding\":12,\"borderRadius\":20,\"clip\":true,\"alignItems\":\"center\",\"justifyContent\":\"start\"}},{\"id\":\"content\",\"component\":\"Column\",\"children\":[\"__layout__content__sub\"],\"styles\":{\"height\":\"matchParent\",\"layoutWeight\":1},\"itemMargin\":0},{\"id\":\"__layout__content__sub\",\"component\":\"Column\",\"children\":[\"content_title\",\"__layout__content__body\"],\"itemMargin\":8,\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"layoutWeight\":126.0}},{\"id\":\"content_title\",\"component\":\"Row\",\"children\":[\"content_title_title\"],\"styles\":{\"width\":\"matchParent\",\"height\":12,\"flexShrink\":0,\"justifyContent\":\"start\",\"alignItems\":\"center\"},\"itemMargin\":0},{\"id\":\"content_title_title\",\"component\":\"Text\",\"content\":\"家庭简报\",\"styles\":{\"fontSize\":12,\"fontWeight\":400,\"lineHeight\":1,\"textAlign\":\"start\",\"maxLines\":1,\"flexShrink\":0,\"width\":\"matchParent\",\"fontColor\":\"@theme:secondary/1\"}},{\"id\":\"__layout__content__body\",\"component\":\"Column\",\"children\":[\"__layout__content__primary\",\"__layout__content__details\"],\"itemMargin\":8,\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"layoutWeight\":1}},{\"id\":\"__layout__content__primary\",\"component\":\"Column\",\"children\":[\"content_primary\"],\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"layoutWeight\":1},\"itemMargin\":0},{\"id\":\"content_primary\",\"component\":\"Column\",\"children\":[\"content_primary_main\",\"content_primary_secondary\"],\"itemMargin\":2,\"styles\":{\"alignItems\":\"start\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"width\":\"matchParent\"}},{\"id\":\"content_primary_main\",\"component\":\"Text\",\"content\":\"{{ ${/data/currentTime/currentDate} }}\",\"styles\":{\"height\":18,\"fontSize\":18,\"fontWeight\":700,\"lineHeight\":1,\"maxLines\":1,\"flexShrink\":1,\"width\":\"matchParent\",\"fontColor\":\"@theme:primary/1\",\"textOverflow\":\"clip\"}},{\"id\":\"content_primary_secondary\",\"component\":\"Text\",\"content\":\"{{ ${/data/currentTime/dayOfWeek} }}\",\"styles\":{\"height\":16,\"fontSize\":12,\"fontWeight\":400,\"lineHeight\":1.3333333333333333,\"maxLines\":1,\"flexShrink\":1,\"width\":\"matchParent\",\"fontColor\":\"@theme:primary/1\",\"textOverflow\":\"clip\"}},{\"id\":\"__layout__content__details\",\"component\":\"Column\",\"children\":[\"content_support\"],\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"content_support\",\"component\":\"Row\",\"children\":[\"content_support_rail\",\"content_support_texts\"],\"itemMargin\":7,\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"top\",\"flexShrink\":1,\"clip\":true,\"height\":50}},{\"id\":\"content_support_rail\",\"component\":\"Column\",\"children\":[\"content_support_rail_dot\",\"content_support_rail_line\"],\"itemMargin\":5,\"styles\":{\"width\":8,\"padding\":{\"top\":5,\"bottom\":0},\"alignItems\":\"center\",\"justifyContent\":\"start\",\"flexShrink\":0,\"height\":50,\"clip\":true}},{\"id\":\"content_support_rail_dot\",\"component\":\"Divider\",\"styles\":{\"width\":8,\"height\":8,\"borderRadius\":4,\"borderWidth\":1.5,\"strokeWidth\":0,\"color\":\"@theme:transparent/1\",\"flexShrink\":0,\"borderColor\":\"@theme:primary/1\",\"backgroundColor\":\"@theme:transparent/1\"}},{\"id\":\"content_support_rail_line\",\"component\":\"Divider\",\"styles\":{\"width\":1,\"strokeWidth\":1,\"vertical\":true,\"flexShrink\":0,\"height\":32,\"color\":\"@theme:primary/0.6\"}},{\"id\":\"content_support_texts\",\"component\":\"Column\",\"children\":[\"content_support_title\",\"content_support_time\",\"content_support_location\"],\"itemMargin\":0,\"styles\":{\"alignItems\":\"start\",\"justifyContent\":\"start\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"layoutWeight\":1,\"height\":50}},{\"id\":\"content_support_title\",\"component\":\"Text\",\"content\":\"{{ ${/data/calendar/events/0/title} }}\",\"styles\":{\"width\":\"matchParent\",\"fontSize\":14,\"fontWeight\":700,\"maxLines\":2,\"flexShrink\":0,\"constraintSize\":{\"minWidth\":0,\"minHeight\":18},\"fontColor\":\"@theme:primary/1\",\"textOverflow\":\"clip\"}},{\"id\":\"content_support_time\",\"component\":\"Text\",\"content\":\"{{ ${/data/calendar/events/0/dtStart} }}\",\"styles\":{\"width\":\"matchParent\",\"height\":16,\"fontSize\":12,\"fontWeight\":400,\"maxLines\":1,\"flexShrink\":0,\"constraintSize\":{\"minWidth\":0},\"fontColor\":\"@theme:primary/0.6\",\"textOverflow\":\"clip\"}},{\"id\":\"content_support_location\",\"component\":\"Text\",\"content\":\"{{ ${/data/calendar/events/0/eventLocation} }}\",\"styles\":{\"width\":\"matchParent\",\"height\":16,\"fontSize\":12,\"fontWeight\":400,\"maxLines\":1,\"flexShrink\":0,\"constraintSize\":{\"minWidth\":0},\"fontColor\":\"@theme:primary/0.6\",\"textOverflow\":\"clip\"}},{\"id\":\"__layout__root__slots\",\"component\":\"Column\",\"children\":[\"upper\",\"lower\"],\"itemMargin\":12,\"styles\":{\"height\":\"matchParent\",\"layoutWeight\":1}},{\"id\":\"upper\",\"component\":\"Column\",\"children\":[\"upper_text\"],\"itemMargin\":0,\"styles\":{\"padding\":{\"left\":8,\"right\":8},\"borderRadius\":16,\"alignItems\":\"start\",\"justifyContent\":\"center\",\"clip\":true,\"flexShrink\":0,\"width\":\"matchParent\",\"backgroundColor\":\"@theme:panel/1\",\"layoutWeight\":57.0}},{\"id\":\"upper_text\",\"component\":\"Column\",\"children\":[\"upper_primary\",\"upper_secondary\"],\"itemMargin\":2,\"styles\":{\"alignItems\":\"start\",\"justifyContent\":\"start\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"height\":\"matchParent\",\"padding\":{\"top\":8},\"width\":\"matchParent\"}},{\"id\":\"upper_primary\",\"component\":\"Text\",\"content\":\"{{ ${/data/phoneBattery/batterySOCText} }}\",\"styles\":{\"height\":19,\"fontSize\":14,\"fontWeight\":700,\"maxLines\":1,\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"width\":\"matchParent\",\"lineHeight\":1.3571428571428572,\"fontColor\":\"@theme:primary/1\",\"textOverflow\":\"clip\"}},{\"id\":\"upper_secondary\",\"component\":\"Text\",\"content\":\"{{ ${/data/phoneBattery/chargingStatusDesc} }}\",\"styles\":{\"height\":16,\"fontSize\":12,\"fontWeight\":500,\"maxLines\":1,\"textOverflow\":\"ellipsis\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"width\":\"matchParent\",\"lineHeight\":1.3333333333333333,\"fontColor\":\"@theme:primary/1\"}},{\"id\":\"lower\",\"component\":\"Column\",\"children\":[\"lower_text\"],\"itemMargin\":0,\"styles\":{\"padding\":{\"left\":8,\"right\":8},\"borderRadius\":16,\"alignItems\":\"start\",\"justifyContent\":\"center\",\"clip\":true,\"flexShrink\":0,\"width\":\"matchParent\",\"backgroundColor\":\"@theme:panel/1\",\"layoutWeight\":57.0}},{\"id\":\"lower_text\",\"component\":\"Column\",\"children\":[\"lower_primary\",\"lower_secondary\"],\"itemMargin\":2,\"styles\":{\"alignItems\":\"start\",\"justifyContent\":\"start\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"height\":\"matchParent\",\"padding\":{\"top\":8},\"width\":\"matchParent\"}},{\"id\":\"lower_primary\",\"component\":\"Text\",\"content\":\"{{ ${/data/memo/todoPendingCount} + '/' + ${/data/memo/todoTotalCount} }}\",\"styles\":{\"height\":19,\"fontSize\":14,\"fontWeight\":700,\"maxLines\":1,\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"width\":\"matchParent\",\"lineHeight\":1.3571428571428572,\"fontColor\":\"@theme:primary/1\",\"textOverflow\":\"clip\"}},{\"id\":\"lower_secondary\",\"component\":\"Text\",\"content\":\"待办 未完成/总数\",\"styles\":{\"height\":16,\"fontSize\":12,\"fontWeight\":500,\"maxLines\":1,\"textOverflow\":\"ellipsis\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"width\":\"matchParent\",\"lineHeight\":1.3333333333333333,\"fontColor\":\"@theme:primary/0.6\"}}]}}\n{\"version\":\"v0.9\",\"updateDataModel\":{\"surfaceId\":\"surface_card\",\"path\":\"/\",\"value\":{\"data\":{\"currentTime\":{\"currentDate\":\"2026-07-09\",\"dayOfWeek\":\"星期四\"},\"phoneBattery\":{\"batterySOCText\":\"68%\",\"chargingStatusDesc\":\"未充电\",\"batterySOC\":68},\"calendar\":{\"events\":[{\"dtStart\":\"14:00\",\"eventLocation\":\"会议室\",\"title\":\"项目例会\"}]},\"memo\":{\"todoPendingCount\":0,\"todoTotalCount\":0}}}}}",
  "validationErrors": []
}
```
