```cardspec
{
  "title": "日历卡片",
  "description": "日期与日程速览",
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
    },
    {
      "capabilityId": "GetCalendarEvents",
      "arguments": {
        "futureDays": 7
      },
      "writeResultTo": "/data/calendar"
    }
  ]
}
```
```genui
{"version":"v0.9","createSurface":{"surfaceId":"surface_card","catalogId":"ohos.a2ui.extended.catalog.form"}}
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Column","children":["title","__layout__root__body"],"itemMargin":6,"styles":{"width":"matchParent","height":"matchParent","padding":12,"borderRadius":20,"clip":true,"alignItems":"start","justifyContent":"start","linearGradient":{"direction":"RightBottom","colors":[["#FFFFE0CC",0],["#FFFFF7F2",1]]}}},{"id":"title","component":"Row","children":["title_title"],"styles":{"width":"matchParent","height":12,"flexShrink":0,"justifyContent":"start","alignItems":"center"},"itemMargin":0},{"id":"title_title","component":"Text","content":"{{ ${/data/time/currentDate} + ' ' + ${/data/time/dayOfWeek} }}","styles":{"fontSize":12,"fontWeight":400,"lineHeight":1,"textAlign":"start","maxLines":1,"flexShrink":0,"width":"matchParent","fontColor":"#998C4B1C"}},{"id":"__layout__root__body","component":"Column","children":["__layout__root__primary","__layout__root__details"],"itemMargin":8,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1}},{"id":"__layout__root__primary","component":"Column","children":["primary"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"primary","component":"Column","children":["primary_main","primary_secondary"],"itemMargin":2,"styles":{"alignItems":"start","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent"}},{"id":"primary_main","component":"Text","content":"{{ '距离开始还有 ' + ${/data/calendar/events/0/countdownDays} + ' 天' }}","styles":{"height":18,"fontSize":18,"fontWeight":700,"lineHeight":1,"maxLines":1,"flexShrink":1,"width":"matchParent","fontColor":"#FF8C4B1C","textOverflow":"clip"}},{"id":"primary_secondary","component":"Text","content":"{{ ${/data/time/lunarDate} }}","styles":{"height":16,"fontSize":12,"fontWeight":400,"lineHeight":1.3333333333333333,"maxLines":1,"flexShrink":1,"width":"matchParent","fontColor":"#FF8C4B1C","textOverflow":"clip"}},{"id":"__layout__root__details","component":"Column","children":["details"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1},"itemMargin":0},{"id":"details","component":"Row","children":["details_rail","details_texts"],"itemMargin":7,"onClick":[{"call":"clickToIntent","args":{"intentName":"ViewCalendarEvent","params":{"entityId":"{{ ${/data/calendar/events/0/entityId} }}"}}}],"styles":{"width":"matchParent","alignItems":"top","flexShrink":1,"clip":true,"height":34}},{"id":"details_rail","component":"Column","children":["details_rail_dot","details_rail_line"],"itemMargin":5,"styles":{"width":8,"padding":{"top":5,"bottom":0},"alignItems":"center","justifyContent":"start","flexShrink":0,"height":34,"clip":true}},{"id":"details_rail_dot","component":"Divider","styles":{"width":8,"height":8,"borderRadius":4,"borderWidth":1.5,"strokeWidth":0,"color":"#00000000","flexShrink":0,"borderColor":"#FF8C4B1C","backgroundColor":"#00000000"}},{"id":"details_rail_line","component":"Divider","styles":{"width":1,"strokeWidth":1,"vertical":true,"flexShrink":0,"height":16,"color":"#998C4B1C"}},{"id":"details_texts","component":"Column","children":["details_title","details_time"],"itemMargin":0,"styles":{"alignItems":"start","justifyContent":"start","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1,"height":34}},{"id":"details_title","component":"Text","content":"{{ ${/data/calendar/events/0/title} }}","styles":{"width":"matchParent","fontSize":14,"fontWeight":700,"maxLines":2,"flexShrink":0,"constraintSize":{"minWidth":0,"minHeight":18},"fontColor":"#FF8C4B1C","textOverflow":"clip"}},{"id":"details_time","component":"Text","content":"{{ ${/data/calendar/events/0/startDate} + ' ' + ${/data/calendar/events/0/dtStart} }}","styles":{"width":"matchParent","height":16,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":0,"constraintSize":{"minWidth":0},"fontColor":"#998C4B1C","textOverflow":"clip"}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"time":{"currentDate":"示例","dayOfWeek":"示例","lunarDate":"示例"},"calendar":{"events":[{"title":"项目例会","startDate":"08-06","dtStart":"14:00","countdownDays":0,"entityId":"example-event-001"}]}}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "生成一张日历卡片，显示当前日期、星期、农历信息，以及最近的日程安排和倒计时。",
  "size": "2x4",
  "appVersion": "11.7.8.343",
  "eventCandidates": [
    {
      "id": "event.viewCalendarEvent",
      "description": "点击日程卡片 or 日程按钮，跳转到华为日历应用 查看该日程的详情。",
      "call": "clickToIntent",
      "args": {
        "intentName": "ViewCalendarEvent",
        "params": {
          "entityId": "{{ ${/data/calendar/events/0/entityId} }}"
        }
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
      },
      "calendar": {
        "eventCount": {
          "type": "integer",
          "description": "查询到的日程记录总数量。",
          "sampleValue": 1
        },
        "events": [
          {
            "title": {
              "type": "string",
              "description": "日程标题，例如“咪咕视频《西班牙 VS 奥地利》”或“项目进展会”。",
              "sampleValue": "项目例会"
            },
            "startDate": {
              "type": "string",
              "description": "日程开始日期格式化文本，例如 '07-03'。",
              "sampleValue": "08-06"
            },
            "dtStart": {
              "type": "string",
              "description": "格式化后的日程开始时间短文本，如 '03:00'，若为全天日程可能为特殊标记。",
              "sampleValue": "14:00"
            },
            "countdownDays": {
              "type": "integer",
              "description": "距离日程开始的自然日天数纯整数，返回值不包含“天”。0 表示今天发生或已经发生，正整数表示距离开始还有多少天；若直接用于文本展示，必须在数值后追加“天”。",
              "sampleValue": 0
            },
            "entityId": {
              "type": "string",
              "description": "系统日程的全局唯一实体ID。",
              "sampleValue": "example-event-001"
            }
          }
        ]
      }
    }
  },
  "assetCandidates": [
    {
      "id": "asset.calendar_fill",
      "src": "resources/base/media/calendar_fill.svg",
      "description": "样式：日历实心图标，默认黑色，图形为带格线的日历本造型；适用：日程管理、日历事件查看、当日安排。"
    }
  ]
}
```
```effectivecapabilities
{
  "data": [
    "GetCurrentTime",
    "GetCalendarEvents"
  ],
  "event": [
    {
      "id": "event.viewCalendarEvent",
      "description": "点击日程卡片 or 日程按钮，跳转到华为日历应用 查看该日程的详情。",
      "call": "clickToIntent",
      "args": {
        "intentName": "ViewCalendarEvent",
        "params": {
          "entityId": "{{ ${/data/calendar/events/0/entityId} }}"
        }
      }
    }
  ],
  "asset": [
    "asset.calendar_fill"
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
    },
    {
      "capabilityId": "GetCalendarEvents",
      "arguments": {
        "futureDays": 7
      },
      "writeResultTo": "/data/calendar",
      "candidateOutputFields": [
        "/eventCount",
        "/events/0/title",
        "/events/0/startDate",
        "/events/0/dtStart",
        "/events/0/countdownDays"
      ]
    }
  ],
  "candidateEventCandidates": [
    {
      "capabilityId": "event.viewCalendarEvent",
      "action": {
        "call": "clickToIntent",
        "args": {
          "intentName": "ViewCalendarEvent",
          "params": {
            "entityId": "{{ ${/data/calendar/events/0/entityId} }}"
          }
        }
      }
    }
  ],
  "candidateAssetIds": [
    "asset.calendar_fill"
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
  "artifactId": "f524e7a7-f26b-4358-b10c-b1a42df08e59",
  "createdAt": 1793934622456
}
```
```designcompactdsl
["root","Layout",{"layout":"W-top-bottom","variant":"continuous"},["title","primary","details"]]
["title","SingleLineTitle",{"title":"{{ ${/data/time/currentDate} + ' ' + ${/data/time/dayOfWeek} }}","fontSize":12}]
["primary","EmphasisText",{"mainText":"{{ '距离开始还有 ' + ${/data/calendar/events/0/countdownDays} + ' 天' }}","secondaryText":{"path":"/data/time/lunarDate"},"fontSize":18}]
["details","EventCard",{"items":[{"title":{"path":"/data/calendar/events/0/title"},"time":"{{ ${/data/calendar/events/0/startDate} + ' ' + ${/data/calendar/events/0/dtStart} }}","onClick":[{"call":"clickToIntent","args":{"intentName":"ViewCalendarEvent","params":{"entityId":"{{ ${/data/calendar/events/0/entityId} }}"}}}]}]}]
["/data/time/currentDate","示例"]
["/data/time/dayOfWeek","示例"]
["/data/time/lunarDate","示例"]
["/data/calendar/events/0/title","项目例会"]
["/data/calendar/events/0/startDate","08-06"]
["/data/calendar/events/0/dtStart","14:00"]
["/data/calendar/events/0/countdownDays",0]
["/data/calendar/events/0/entityId","example-event-001"]
```
```request
{
  "content": {
    "bundleName": "com.huawei.genui",
    "userQuery": "生成一张日历卡片，显示当前日期、星期、农历信息，以及最近的日程安排和倒计时。",
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
        "capabilityId": "GetCalendarEvents",
        "arguments": {
          "futureDays": 7
        },
        "writeResultTo": "/data/calendar",
        "candidateOutputFields": [
          "/eventCount",
          "/events/0/title",
          "/events/0/startDate",
          "/events/0/dtStart",
          "/events/0/countdownDays"
        ]
      }
    ],
    "title": "日历卡片",
    "size": "2x4",
    "candidateEventCandidates": [
      {
        "capabilityId": "event.viewCalendarEvent",
        "action": {
          "call": "clickToIntent",
          "args": {
            "intentName": "ViewCalendarEvent",
            "params": {
              "entityId": "{{ ${/data/calendar/events/0/entityId} }}"
            }
          }
        }
      }
    ],
    "description": "日期与日程速览",
    "candidateAssetIds": [
      "asset.calendar_fill"
    ]
  },
  "deviceInfo": {
    "countryCode": "CN",
    "deviceFormation": "HDSpeaker",
    "deviceType": 0,
    "locale": "zh-CN",
    "phoneType": "CMS-AL20",
    "prdVer": "11.7.8.343",
    "sysVer": "EmotionUI_9.0.0",
    "time": "20261031014910839"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q380-000",
    "isNew": true,
    "sessionId": "batch-7664fcb9"
  },
  "userAuth": {
    "user": {}
  },
  "utterance": {
    "original": "生成一张日历卡片，显示当前日期、星期、农历信息，以及最近的日程安排和倒计时。",
    "type": "text"
  },
  "version": "1.0",
  "functionName": "generateWidgetCardCompactDsl",
  "romVersion": "CMS-AL20 7.0.0.115",
  "bundleName": "com.huawei.genui",
  "userQuery": "生成一张日历卡片，显示当前日期、星期、农历信息，以及最近的日程安排和倒计时。",
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
      "capabilityId": "GetCalendarEvents",
      "arguments": {
        "futureDays": 7
      },
      "writeResultTo": "/data/calendar",
      "candidateOutputFields": [
        "/eventCount",
        "/events/0/title",
        "/events/0/startDate",
        "/events/0/dtStart",
        "/events/0/countdownDays"
      ]
    }
  ],
  "title": "日历卡片",
  "size": "2x4",
  "candidateEventCandidates": [
    {
      "capabilityId": "event.viewCalendarEvent",
      "action": {
        "call": "clickToIntent",
        "args": {
          "intentName": "ViewCalendarEvent",
          "params": {
            "entityId": "{{ ${/data/calendar/events/0/entityId} }}"
          }
        }
      }
    }
  ],
  "description": "日期与日程速览",
  "candidateAssetIds": [
    "asset.calendar_fill"
  ]
}
```
```repair-1
{
  "modelGeneratedCompactDsl": "[\"root\",\"Layout\",{\"layout\":\"W-top-bottom\",\"variant\":\"continuous\"},[\"title\",\"primary\",\"details\"]]\n[\"title\",\"SingleLineTitle\",{\"title\":\"{{ ${/data/time/currentDate} + ' ' + ${/data/time/dayOfWeek} }}\",\"fontSize\":12}]\n[\"primary\",\"EmphasisText\",{\"mainText\":\"{{ '距离开始还有 ' + ${/data/calendar/events/0/countdownDays} + ' 天' }}\",\"secondaryText\":{\"path\":\"/data/time/lunarDate\"},\"fontSize\":18}]\n[\"details\",\"EventCard\",{\"items\":[{\"title\":{\"path\":\"/data/calendar/events/0/title\"},\"time\":\"{{ ${/data/calendar/events/0/startDate} + ' ' + ${/data/calendar/events/0/dtStart} }}\",\"onClick\":[{\"call\":\"clickToIntent\",\"args\":{\"intentName\":\"ViewCalendarEvent\",\"params\":{\"entityId\":\"{{ ${/data/calendar/events/0/entityId} }}\"}}}]}]}]\n[\"/data/time/currentDate\",\"示例\"]\n[\"/data/time/dayOfWeek\",\"示例\"]\n[\"/data/time/lunarDate\",\"示例\"]\n[\"/data/calendar/events/0/title\",\"项目例会\"]\n[\"/data/calendar/events/0/startDate\",\"08-06\"]\n[\"/data/calendar/events/0/dtStart\",\"14:00\"]\n[\"/data/calendar/events/0/countdownDays\",0]\n[\"/data/calendar/events/0/entityId\",\"example-event-001\"]",
  "generatedDsl": "{\"version\":\"v0.9\",\"createSurface\":{\"surfaceId\":\"surface_card\",\"catalogId\":\"ohos.a2ui.extended.catalog.form\"}}\n{\"version\":\"v0.9\",\"updateComponents\":{\"surfaceId\":\"surface_card\",\"root\":\"root\",\"components\":[{\"id\":\"root\",\"component\":\"Column\",\"children\":[\"title\",\"__layout__root__body\"],\"itemMargin\":6,\"styles\":{\"width\":\"matchParent\",\"height\":\"matchParent\",\"padding\":12,\"borderRadius\":20,\"clip\":true,\"alignItems\":\"start\",\"justifyContent\":\"start\"}},{\"id\":\"title\",\"component\":\"Row\",\"children\":[\"title_title\"],\"styles\":{\"width\":\"matchParent\",\"height\":12,\"flexShrink\":0,\"justifyContent\":\"start\",\"alignItems\":\"center\"},\"itemMargin\":0},{\"id\":\"title_title\",\"component\":\"Text\",\"content\":\"{{ ${/data/time/currentDate} + ' ' + ${/data/time/dayOfWeek} }}\",\"styles\":{\"fontSize\":12,\"fontWeight\":400,\"lineHeight\":1,\"textAlign\":\"start\",\"maxLines\":1,\"flexShrink\":0,\"width\":\"matchParent\",\"fontColor\":\"@theme:secondary/1\"}},{\"id\":\"__layout__root__body\",\"component\":\"Column\",\"children\":[\"__layout__root__primary\",\"__layout__root__details\"],\"itemMargin\":8,\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"layoutWeight\":1}},{\"id\":\"__layout__root__primary\",\"component\":\"Column\",\"children\":[\"primary\"],\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"primary\",\"component\":\"Column\",\"children\":[\"primary_main\",\"primary_secondary\"],\"itemMargin\":2,\"styles\":{\"alignItems\":\"start\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"width\":\"matchParent\"}},{\"id\":\"primary_main\",\"component\":\"Text\",\"content\":\"{{ '距离开始还有 ' + ${/data/calendar/events/0/countdownDays} + ' 天' }}\",\"styles\":{\"height\":18,\"fontSize\":18,\"fontWeight\":700,\"lineHeight\":1,\"maxLines\":1,\"flexShrink\":1,\"width\":\"matchParent\",\"fontColor\":\"@theme:primary/1\",\"textOverflow\":\"clip\"}},{\"id\":\"primary_secondary\",\"component\":\"Text\",\"content\":\"{{ ${/data/time/lunarDate} }}\",\"styles\":{\"height\":16,\"fontSize\":12,\"fontWeight\":400,\"lineHeight\":1.3333333333333333,\"maxLines\":1,\"flexShrink\":1,\"width\":\"matchParent\",\"fontColor\":\"@theme:primary/1\",\"textOverflow\":\"clip\"}},{\"id\":\"__layout__root__details\",\"component\":\"Column\",\"children\":[\"details\"],\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"layoutWeight\":1},\"itemMargin\":0},{\"id\":\"details\",\"component\":\"Row\",\"children\":[\"details_rail\",\"details_texts\"],\"itemMargin\":7,\"onClick\":[{\"call\":\"clickToIntent\",\"args\":{\"intentName\":\"ViewCalendarEvent\",\"params\":{\"entityId\":\"{{ ${/data/calendar/events/0/entityId} }}\"}}}],\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"top\",\"flexShrink\":1,\"clip\":true,\"height\":34}},{\"id\":\"details_rail\",\"component\":\"Column\",\"children\":[\"details_rail_dot\",\"details_rail_line\"],\"itemMargin\":5,\"styles\":{\"width\":8,\"padding\":{\"top\":5,\"bottom\":0},\"alignItems\":\"center\",\"justifyContent\":\"start\",\"flexShrink\":0,\"height\":34,\"clip\":true}},{\"id\":\"details_rail_dot\",\"component\":\"Divider\",\"styles\":{\"width\":8,\"height\":8,\"borderRadius\":4,\"borderWidth\":1.5,\"strokeWidth\":0,\"color\":\"@theme:transparent/1\",\"flexShrink\":0,\"borderColor\":\"@theme:primary/1\",\"backgroundColor\":\"@theme:transparent/1\"}},{\"id\":\"details_rail_line\",\"component\":\"Divider\",\"styles\":{\"width\":1,\"strokeWidth\":1,\"vertical\":true,\"flexShrink\":0,\"height\":16,\"color\":\"@theme:primary/0.6\"}},{\"id\":\"details_texts\",\"component\":\"Column\",\"children\":[\"details_title\",\"details_time\"],\"itemMargin\":0,\"styles\":{\"alignItems\":\"start\",\"justifyContent\":\"start\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"layoutWeight\":1,\"height\":34}},{\"id\":\"details_title\",\"component\":\"Text\",\"content\":\"{{ ${/data/calendar/events/0/title} }}\",\"styles\":{\"width\":\"matchParent\",\"fontSize\":14,\"fontWeight\":700,\"maxLines\":2,\"flexShrink\":0,\"constraintSize\":{\"minWidth\":0,\"minHeight\":18},\"fontColor\":\"@theme:primary/1\",\"textOverflow\":\"clip\"}},{\"id\":\"details_time\",\"component\":\"Text\",\"content\":\"{{ ${/data/calendar/events/0/startDate} + ' ' + ${/data/calendar/events/0/dtStart} }}\",\"styles\":{\"width\":\"matchParent\",\"height\":16,\"fontSize\":12,\"fontWeight\":400,\"maxLines\":1,\"flexShrink\":0,\"constraintSize\":{\"minWidth\":0},\"fontColor\":\"@theme:primary/0.6\",\"textOverflow\":\"clip\"}}]}}\n{\"version\":\"v0.9\",\"updateDataModel\":{\"surfaceId\":\"surface_card\",\"path\":\"/\",\"value\":{\"data\":{\"time\":{\"currentDate\":\"示例\",\"dayOfWeek\":\"示例\",\"lunarDate\":\"示例\"},\"calendar\":{\"events\":[{\"title\":\"项目例会\",\"startDate\":\"08-06\",\"dtStart\":\"14:00\",\"countdownDays\":0,\"entityId\":\"example-event-001\"}]}}}}}",
  "validationErrors": []
}
```
