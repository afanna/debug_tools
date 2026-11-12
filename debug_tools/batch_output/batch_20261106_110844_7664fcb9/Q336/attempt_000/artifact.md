```cardspec
{
  "title": "天气日程",
  "description": "天气与日程叠加卡片",
  "suggestSize": "2x4",
  "imageDomainWhitelist": [
    "hag-ability-test.obs.cn-north-1.myhuaweicloud.com",
    "lfcontentcenterdev.hwcloudtest.cn",
    "hagres-drcn.dbankcdn.com"
  ],
  "dataBindings": [
    {
      "capabilityId": "ViewWeather",
      "arguments": {
        "forecastDays": 3
      },
      "writeResultTo": "/data/weather"
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
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Column","children":["title","__layout__root__body"],"itemMargin":6,"styles":{"width":"matchParent","height":"matchParent","padding":12,"borderRadius":20,"clip":true,"alignItems":"start","justifyContent":"start","linearGradient":{"direction":"RightBottom","colors":[["#FFCBDDFE",0],["#FFF1F6FE",1]]}}},{"id":"title","component":"Row","children":["title_title"],"styles":{"width":"matchParent","height":12,"flexShrink":0,"justifyContent":"start","alignItems":"center"},"itemMargin":0},{"id":"title_title","component":"Text","content":"天气与日程","styles":{"fontSize":12,"fontWeight":400,"lineHeight":1,"textAlign":"start","maxLines":1,"flexShrink":0,"width":"matchParent","fontColor":"#991F4799"}},{"id":"__layout__root__body","component":"Column","children":["__layout__root__primary","__layout__root__details"],"itemMargin":8,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1}},{"id":"__layout__root__primary","component":"Column","children":["primary"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1},"itemMargin":0},{"id":"primary","component":"Row","children":["primary_item0","primary_item1","primary_item2"],"itemMargin":8,"styles":{"width":"matchParent","height":"matchParent","alignItems":"top","justifyContent":"start","layoutWeight":1,"flexShrink":1,"constraintSize":{"minHeight":48}}},{"id":"primary_item0","component":"Column","children":["primary_item0_label_slot","primary_item0_value_slot"],"itemMargin":2,"styles":{"height":"matchParent","backgroundColor":"#99FFFFFF","padding":{"left":8,"right":8},"borderRadius":16,"alignItems":"start","justifyContent":"center","layoutWeight":1,"flexShrink":1,"constraintSize":{"minWidth":0,"minHeight":0}}},{"id":"primary_item0_label_slot","component":"Row","children":["primary_item0_label"],"styles":{"width":"matchParent","height":18,"alignItems":"center","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"primary_item0_label","component":"Text","content":"{{ ${/data/weather/daily/0/weekday} + ' ' + ${/data/weather/daily/0/condition} }}","styles":{"width":"matchParent","fontSize":12,"fontWeight":700,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","fontColor":"#991F4799"}},{"id":"primary_item0_value_slot","component":"Row","children":["primary_item0_value"],"styles":{"width":"matchParent","height":16,"alignItems":"center","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"primary_item0_value","component":"Text","content":"{{ ${/data/weather/daily/0/temperatureRangeText} }}","styles":{"width":"matchParent","fontSize":10,"fontWeight":500,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","fontColor":"#FF1F4799"}},{"id":"primary_item1","component":"Column","children":["primary_item1_label_slot","primary_item1_value_slot"],"itemMargin":2,"styles":{"height":"matchParent","backgroundColor":"#99FFFFFF","padding":{"left":8,"right":8},"borderRadius":16,"alignItems":"start","justifyContent":"center","layoutWeight":1,"flexShrink":1,"constraintSize":{"minWidth":0,"minHeight":0}}},{"id":"primary_item1_label_slot","component":"Row","children":["primary_item1_label"],"styles":{"width":"matchParent","height":18,"alignItems":"center","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"primary_item1_label","component":"Text","content":"{{ ${/data/weather/daily/1/weekday} + ' ' + ${/data/weather/daily/1/condition} }}","styles":{"width":"matchParent","fontSize":12,"fontWeight":700,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","fontColor":"#991F4799"}},{"id":"primary_item1_value_slot","component":"Row","children":["primary_item1_value"],"styles":{"width":"matchParent","height":16,"alignItems":"center","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"primary_item1_value","component":"Text","content":"{{ ${/data/weather/daily/1/temperatureRangeText} }}","styles":{"width":"matchParent","fontSize":10,"fontWeight":500,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","fontColor":"#FF1F4799"}},{"id":"primary_item2","component":"Column","children":["primary_item2_label_slot","primary_item2_value_slot"],"itemMargin":2,"styles":{"height":"matchParent","backgroundColor":"#99FFFFFF","padding":{"left":8,"right":8},"borderRadius":16,"alignItems":"start","justifyContent":"center","layoutWeight":1,"flexShrink":1,"constraintSize":{"minWidth":0,"minHeight":0}}},{"id":"primary_item2_label_slot","component":"Row","children":["primary_item2_label"],"styles":{"width":"matchParent","height":18,"alignItems":"center","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"primary_item2_label","component":"Text","content":"{{ ${/data/weather/daily/2/weekday} + ' ' + ${/data/weather/daily/2/condition} }}","styles":{"width":"matchParent","fontSize":12,"fontWeight":700,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","fontColor":"#991F4799"}},{"id":"primary_item2_value_slot","component":"Row","children":["primary_item2_value"],"styles":{"width":"matchParent","height":16,"alignItems":"center","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"primary_item2_value","component":"Text","content":"{{ ${/data/weather/daily/2/temperatureRangeText} }}","styles":{"width":"matchParent","fontSize":10,"fontWeight":500,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","fontColor":"#FF1F4799"}},{"id":"__layout__root__details","component":"Column","children":["details"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"details","component":"Row","children":["details_rail","details_texts"],"itemMargin":7,"styles":{"width":"matchParent","alignItems":"top","flexShrink":1,"clip":true,"height":34}},{"id":"details_rail","component":"Column","children":["details_rail_dot","details_rail_line"],"itemMargin":5,"styles":{"width":8,"padding":{"top":5,"bottom":0},"alignItems":"center","justifyContent":"start","flexShrink":0,"height":34,"clip":true}},{"id":"details_rail_dot","component":"Divider","styles":{"width":8,"height":8,"borderRadius":4,"borderWidth":1.5,"strokeWidth":0,"color":"#00000000","flexShrink":0,"borderColor":"#FF1F4799","backgroundColor":"#00000000"}},{"id":"details_rail_line","component":"Divider","styles":{"width":1,"strokeWidth":1,"vertical":true,"flexShrink":0,"height":16,"color":"#991F4799"}},{"id":"details_texts","component":"Column","children":["details_title","details_time"],"itemMargin":0,"styles":{"alignItems":"start","justifyContent":"start","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1,"height":34}},{"id":"details_title","component":"Text","content":"{{ ${/data/calendar/events/0/title} }}","styles":{"width":"matchParent","fontSize":14,"fontWeight":700,"maxLines":2,"flexShrink":0,"constraintSize":{"minWidth":0,"minHeight":18},"fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"details_time","component":"Text","content":"{{ ${/data/calendar/events/0/startDate} + ' ' + ${/data/calendar/events/0/dtStart} }}","styles":{"width":"matchParent","height":16,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":0,"constraintSize":{"minWidth":0},"fontColor":"#991F4799","textOverflow":"clip"}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"weather":{"daily":[{"weekday":"星期四","condition":"多云","temperatureRangeText":"25℃ / 32℃"},{"weekday":"星期四","condition":"多云","temperatureRangeText":"25℃ / 32℃"},{"weekday":"星期四","condition":"多云","temperatureRangeText":"25℃ / 32℃"}]},"calendar":{"events":[{"title":"项目例会","dtStart":"14:00","startDate":"08-06","entityId":"example-event-001"}]}}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "将天气和日历叠加在一张卡片上，上半部分展示当前位置未来3天的天气预报（星期、天气现象、温度范围），下半部分展示最近的日程安排（日程标题、开始时间），逐条叠加展示。",
  "size": "2x4",
  "appVersion": "11.7.8.342",
  "eventCandidates": [
    {
      "id": "event.open.weather",
      "description": "打开华为天气应用某城市页，uri为固定值勿更改。cityCode来自于数据能力中ViewWeather出参cityCode字段，进行动态拼接，表示跳转到指定城市天气页。",
      "call": "clickToDeeplink",
      "args": {
        "abilityName": "",
        "bundleName": "",
        "intentName": "Weather_CityCode",
        "uri": "{{ 'hww://www.huawei.com/totemweather?enterType=share&cityCode=' + ${/data/weather/location/cityCode} }}"
      }
    },
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
      "weather": {
        "daily": [
          {
            "weekday": {
              "type": "string",
              "description": "星期文本，例如“星期日”。",
              "sampleValue": "星期四"
            },
            "condition": {
              "type": "string",
              "description": "白天天气现象，来源于weather_icon。",
              "sampleValue": "多云"
            },
            "temperatureRangeText": {
              "type": "string",
              "description": "可直接显示的最低温与最高温范围文本，每个温度值均已包含“℃”单位；展示时不得再次追加温度单位。例如“25℃ / 32℃”。",
              "sampleValue": "25℃ / 32℃"
            }
          },
          {
            "weekday": {
              "type": "string",
              "description": "星期文本，例如“星期日”。",
              "sampleValue": "星期四"
            },
            "condition": {
              "type": "string",
              "description": "白天天气现象，来源于weather_icon。",
              "sampleValue": "多云"
            },
            "temperatureRangeText": {
              "type": "string",
              "description": "可直接显示的最低温与最高温范围文本，每个温度值均已包含“℃”单位；展示时不得再次追加温度单位。例如“25℃ / 32℃”。",
              "sampleValue": "25℃ / 32℃"
            }
          },
          {
            "weekday": {
              "type": "string",
              "description": "星期文本，例如“星期日”。",
              "sampleValue": "星期四"
            },
            "condition": {
              "type": "string",
              "description": "白天天气现象，来源于weather_icon。",
              "sampleValue": "多云"
            },
            "temperatureRangeText": {
              "type": "string",
              "description": "可直接显示的最低温与最高温范围文本，每个温度值均已包含“℃”单位；展示时不得再次追加温度单位。例如“25℃ / 32℃”。",
              "sampleValue": "25℃ / 32℃"
            }
          }
        ],
        "location": {
          "cityCode": {
            "type": "string",
            "description": "城市代码，如60814代表青浦区",
            "sampleValue": "60814"
          }
        }
      },
      "calendar": {
        "events": [
          {
            "title": {
              "type": "string",
              "description": "日程标题，例如“咪咕视频《西班牙 VS 奥地利》”或“项目进展会”。",
              "sampleValue": "项目例会"
            },
            "dtStart": {
              "type": "string",
              "description": "格式化后的日程开始时间短文本，如 '03:00'，若为全天日程可能为特殊标记。",
              "sampleValue": "14:00"
            },
            "startDate": {
              "type": "string",
              "description": "日程开始日期格式化文本，例如 '07-03'。",
              "sampleValue": "08-06"
            },
            "entityId": {
              "type": "string",
              "description": "系统日程的全局唯一实体ID。",
              "sampleValue": "example-event-001"
            }
          },
          {
            "title": {
              "type": "string",
              "description": "日程标题，例如“咪咕视频《西班牙 VS 奥地利》”或“项目进展会”。",
              "sampleValue": "项目例会"
            },
            "dtStart": {
              "type": "string",
              "description": "格式化后的日程开始时间短文本，如 '03:00'，若为全天日程可能为特殊标记。",
              "sampleValue": "14:00"
            },
            "startDate": {
              "type": "string",
              "description": "日程开始日期格式化文本，例如 '07-03'。",
              "sampleValue": "08-06"
            }
          },
          {
            "title": {
              "type": "string",
              "description": "日程标题，例如“咪咕视频《西班牙 VS 奥地利》”或“项目进展会”。",
              "sampleValue": "项目例会"
            },
            "dtStart": {
              "type": "string",
              "description": "格式化后的日程开始时间短文本，如 '03:00'，若为全天日程可能为特殊标记。",
              "sampleValue": "14:00"
            },
            "startDate": {
              "type": "string",
              "description": "日程开始日期格式化文本，例如 '07-03'。",
              "sampleValue": "08-06"
            }
          }
        ]
      }
    }
  },
  "assetCandidates": []
}
```
```effectivecapabilities
{
  "data": [
    "ViewWeather",
    "GetCalendarEvents"
  ],
  "event": [
    {
      "id": "event.open.weather",
      "description": "打开华为天气应用某城市页，uri为固定值勿更改。cityCode来自于数据能力中ViewWeather出参cityCode字段，进行动态拼接，表示跳转到指定城市天气页。",
      "call": "clickToDeeplink",
      "args": {
        "abilityName": "",
        "bundleName": "",
        "intentName": "Weather_CityCode",
        "uri": "{{ 'hww://www.huawei.com/totemweather?enterType=share&cityCode=' + ${/data/weather/location/cityCode} }}"
      }
    },
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
      "capabilityId": "ViewWeather",
      "arguments": {
        "forecastDays": 3
      },
      "writeResultTo": "/data/weather",
      "candidateOutputFields": [
        "/daily/0/weekday",
        "/daily/0/condition",
        "/daily/0/temperatureRangeText",
        "/daily/1/weekday",
        "/daily/1/condition",
        "/daily/1/temperatureRangeText",
        "/daily/2/weekday",
        "/daily/2/condition",
        "/daily/2/temperatureRangeText"
      ]
    },
    {
      "capabilityId": "GetCalendarEvents",
      "arguments": {
        "futureDays": 7
      },
      "writeResultTo": "/data/calendar",
      "candidateOutputFields": [
        "/events/0/title",
        "/events/0/dtStart",
        "/events/0/startDate",
        "/events/1/title",
        "/events/1/dtStart",
        "/events/1/startDate",
        "/events/2/title",
        "/events/2/dtStart",
        "/events/2/startDate"
      ]
    }
  ],
  "candidateEventCandidates": [
    {
      "capabilityId": "event.open.weather",
      "action": {
        "call": "clickToDeeplink",
        "args": {
          "abilityName": "",
          "bundleName": "",
          "intentName": "Weather_CityCode",
          "uri": "{{ 'hww://www.huawei.com/totemweather?enterType=share&cityCode=' + ${/data/weather/location/cityCode} }}"
        }
      }
    },
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
  "artifactId": "19f9ce76-f19c-4c5b-8de3-c0776b39afed",
  "createdAt": 1793934574806
}
```
```designcompactdsl
["root","Layout",{"layout":"W-top-bottom","variant":"bottom-details"},["title","primary","details"]]
["title","SingleLineTitle",{"title":"天气与日程","fontSize":12}]
["primary","TextBlock",{"items":[{"label":"{{ ${/data/weather/daily/0/weekday} + ' ' + ${/data/weather/daily/0/condition} }}","value":{"path":"/data/weather/daily/0/temperatureRangeText"}},{"label":"{{ ${/data/weather/daily/1/weekday} + ' ' + ${/data/weather/daily/1/condition} }}","value":{"path":"/data/weather/daily/1/temperatureRangeText"}},{"label":"{{ ${/data/weather/daily/2/weekday} + ' ' + ${/data/weather/daily/2/condition} }}","value":{"path":"/data/weather/daily/2/temperatureRangeText"}}]}]
["details","EventCard",{"items":[{"title":{"path":"/data/calendar/events/0/title"},"time":"{{ ${/data/calendar/events/0/startDate} + ' ' + ${/data/calendar/events/0/dtStart} }}"}]}]
["/data/weather/daily/0/weekday","星期四"]
["/data/weather/daily/0/condition","多云"]
["/data/weather/daily/0/temperatureRangeText","25℃ / 32℃"]
["/data/weather/daily/1/weekday","星期四"]
["/data/weather/daily/1/condition","多云"]
["/data/weather/daily/1/temperatureRangeText","25℃ / 32℃"]
["/data/weather/daily/2/weekday","星期四"]
["/data/weather/daily/2/condition","多云"]
["/data/weather/daily/2/temperatureRangeText","25℃ / 32℃"]
["/data/calendar/events/0/title","项目例会"]
["/data/calendar/events/0/dtStart","14:00"]
["/data/calendar/events/0/startDate","08-06"]
["/data/calendar/events/0/entityId","example-event-001"]
```
```request
{
  "content": {
    "bundleName": "com.huawei.genui",
    "userQuery": "将天气和日历叠加在一张卡片上，上半部分展示当前位置未来3天的天气预报（星期、天气现象、温度范围），下半部分展示最近的日程安排（日程标题、开始时间），逐条叠加展示。",
    "candidateDataBindings": [
      {
        "capabilityId": "ViewWeather",
        "arguments": {
          "forecastDays": 3
        },
        "writeResultTo": "/data/weather",
        "candidateOutputFields": [
          "/daily/0/weekday",
          "/daily/0/condition",
          "/daily/0/temperatureRangeText",
          "/daily/1/weekday",
          "/daily/1/condition",
          "/daily/1/temperatureRangeText",
          "/daily/2/weekday",
          "/daily/2/condition",
          "/daily/2/temperatureRangeText"
        ]
      },
      {
        "capabilityId": "GetCalendarEvents",
        "arguments": {
          "futureDays": 7
        },
        "writeResultTo": "/data/calendar",
        "candidateOutputFields": [
          "/events/0/title",
          "/events/0/dtStart",
          "/events/0/startDate",
          "/events/1/title",
          "/events/1/dtStart",
          "/events/1/startDate",
          "/events/2/title",
          "/events/2/dtStart",
          "/events/2/startDate"
        ]
      }
    ],
    "title": "天气日程",
    "size": "2x4",
    "candidateEventCandidates": [
      {
        "capabilityId": "event.open.weather",
        "action": {
          "call": "clickToDeeplink",
          "args": {
            "abilityName": "",
            "bundleName": "",
            "intentName": "Weather_CityCode",
            "uri": "{{ 'hww://www.huawei.com/totemweather?enterType=share&cityCode=' + ${/data/weather/location/cityCode} }}"
          }
        }
      },
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
    "description": "天气与日程叠加卡片",
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
    "time": "20261030030748428"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q336-000",
    "isNew": true,
    "sessionId": "batch-7664fcb9"
  },
  "userAuth": {
    "user": {}
  },
  "utterance": {
    "original": "将天气和日历叠加在一张卡片上，上半部分展示当前位置未来3天的天气预报（星期、天气现象、温度范围），下半部分展示最近的日程安排（日程标题、开始时间），逐条叠加展示。",
    "type": "text"
  },
  "version": "1.0",
  "functionName": "generateWidgetCardCompactDsl",
  "romVersion": "CMS-AL20 7.0.0.111",
  "bundleName": "com.huawei.genui",
  "userQuery": "将天气和日历叠加在一张卡片上，上半部分展示当前位置未来3天的天气预报（星期、天气现象、温度范围），下半部分展示最近的日程安排（日程标题、开始时间），逐条叠加展示。",
  "candidateDataBindings": [
    {
      "capabilityId": "ViewWeather",
      "arguments": {
        "forecastDays": 3
      },
      "writeResultTo": "/data/weather",
      "candidateOutputFields": [
        "/daily/0/weekday",
        "/daily/0/condition",
        "/daily/0/temperatureRangeText",
        "/daily/1/weekday",
        "/daily/1/condition",
        "/daily/1/temperatureRangeText",
        "/daily/2/weekday",
        "/daily/2/condition",
        "/daily/2/temperatureRangeText"
      ]
    },
    {
      "capabilityId": "GetCalendarEvents",
      "arguments": {
        "futureDays": 7
      },
      "writeResultTo": "/data/calendar",
      "candidateOutputFields": [
        "/events/0/title",
        "/events/0/dtStart",
        "/events/0/startDate",
        "/events/1/title",
        "/events/1/dtStart",
        "/events/1/startDate",
        "/events/2/title",
        "/events/2/dtStart",
        "/events/2/startDate"
      ]
    }
  ],
  "title": "天气日程",
  "size": "2x4",
  "candidateEventCandidates": [
    {
      "capabilityId": "event.open.weather",
      "action": {
        "call": "clickToDeeplink",
        "args": {
          "abilityName": "",
          "bundleName": "",
          "intentName": "Weather_CityCode",
          "uri": "{{ 'hww://www.huawei.com/totemweather?enterType=share&cityCode=' + ${/data/weather/location/cityCode} }}"
        }
      }
    },
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
  "description": "天气与日程叠加卡片",
  "candidateAssetIds": []
}
```
