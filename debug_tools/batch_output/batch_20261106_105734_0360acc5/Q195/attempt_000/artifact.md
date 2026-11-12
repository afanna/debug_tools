```cardspec
{
  "title": "天气和日程",
  "description": "天气与日程速览",
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
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Row","children":["left","right"],"itemMargin":12,"styles":{"width":"matchParent","height":"matchParent","padding":12,"borderRadius":20,"clip":true,"alignItems":"center","justifyContent":"start","linearGradient":{"direction":"RightBottom","colors":[["#FFCBDDFE",0],["#FFF1F6FE",1]]}}},{"id":"left","component":"Column","children":["__layout__left__sub"],"styles":{"height":"matchParent","layoutWeight":1,"padding":8,"borderRadius":16,"clip":true,"backgroundColor":"#99FFFFFF"},"itemMargin":0},{"id":"__layout__left__sub","component":"Column","children":["left_title","__layout__left__body"],"itemMargin":6,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":110.0}},{"id":"left_title","component":"Row","children":["left_title_title"],"styles":{"width":"matchParent","height":12,"flexShrink":0,"justifyContent":"start","alignItems":"center"},"itemMargin":0},{"id":"left_title_title","component":"Text","content":"{{ ${/data/weather/location/prefectureName} }}","styles":{"fontSize":12,"fontWeight":400,"lineHeight":1,"textAlign":"start","maxLines":1,"flexShrink":0,"width":"matchParent","fontColor":"#991F4799"}},{"id":"__layout__left__body","component":"Column","children":["__layout__left__primary","__layout__left__details"],"itemMargin":6,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1}},{"id":"__layout__left__primary","component":"Column","children":["left_primary"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1},"itemMargin":0},{"id":"left_primary","component":"Row","children":["left_primary_value"],"itemMargin":0,"styles":{"justifyContent":"start","alignItems":"bottom","flexShrink":0,"width":"matchParent"}},{"id":"left_primary_value","component":"Text","content":"{{ ${/data/weather/current/temperatureText} }}","styles":{"height":30,"fontSize":30,"fontWeight":700,"lineHeight":1,"maxLines":1,"flexShrink":0,"fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"__layout__left__details","component":"Column","children":["left_support"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"left_support","component":"Column","children":["left_support_row0","left_support_row1"],"itemMargin":2,"styles":{"width":"matchParent","alignItems":"start","flexShrink":1}},{"id":"left_support_item0_value","component":"Text","content":"{{ ${/data/weather/current/condition} }}","styles":{"height":12.0,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":1,"lineHeight":1,"fontColor":"#FF1F4799","layoutWeight":1,"textOverflow":"clip"}},{"id":"left_support_item0","component":"Row","children":["left_support_item0_value"],"itemMargin":0,"styles":{"height":12.0,"alignItems":"start","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"left_support_row0","component":"Row","children":["left_support_item0"],"itemMargin":0,"styles":{"width":"matchParent","height":12.0,"alignItems":"start","flexShrink":0}},{"id":"left_support_item1_label","component":"Text","content":"明天","styles":{"height":12,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":0,"lineHeight":1,"fontColor":"#991F4799","textOverflow":"clip"}},{"id":"left_support_item1_value","component":"Text","content":"{{ ${/data/weather/daily/0/weekday} + ' ' + ${/data/weather/daily/0/condition} + ' ' + ${/data/weather/daily/0/temperatureRangeText} }}","styles":{"fontSize":12,"fontWeight":400,"maxLines":2,"flexShrink":1,"lineHeight":1,"fontColor":"#FF1F4799","layoutWeight":1,"textOverflow":"clip"}},{"id":"left_support_item1","component":"Row","children":["left_support_item1_label","left_support_item1_value"],"itemMargin":4,"styles":{"height":24.0,"alignItems":"start","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"left_support_row1","component":"Row","children":["left_support_item1"],"itemMargin":0,"styles":{"width":"matchParent","height":24.0,"alignItems":"start","flexShrink":0}},{"id":"right","component":"Column","children":["__layout__right__sub"],"styles":{"height":"matchParent","layoutWeight":1,"padding":8,"borderRadius":16,"clip":true,"backgroundColor":"#99FFFFFF"},"itemMargin":0},{"id":"__layout__right__sub","component":"Column","children":["right_title","__layout__right__body"],"itemMargin":6,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":110.0}},{"id":"right_title","component":"Row","children":["right_title_title"],"styles":{"width":"matchParent","height":12,"flexShrink":0,"justifyContent":"start","alignItems":"center"},"itemMargin":0},{"id":"right_title_title","component":"Text","content":"日程","styles":{"fontSize":12,"fontWeight":400,"lineHeight":1,"textAlign":"start","maxLines":1,"flexShrink":0,"width":"matchParent","fontColor":"#991F4799"}},{"id":"__layout__right__body","component":"Column","children":["right_body"],"itemMargin":0,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"end","layoutWeight":1}},{"id":"right_body","component":"Row","children":["right_body_rail","right_body_texts"],"itemMargin":7,"styles":{"width":"matchParent","alignItems":"top","flexShrink":1,"clip":true,"height":50}},{"id":"right_body_rail","component":"Column","children":["right_body_rail_dot","right_body_rail_line"],"itemMargin":5,"styles":{"width":8,"padding":{"top":5,"bottom":0},"alignItems":"center","justifyContent":"start","flexShrink":0,"height":50,"clip":true}},{"id":"right_body_rail_dot","component":"Divider","styles":{"width":8,"height":8,"borderRadius":4,"borderWidth":1.5,"strokeWidth":0,"color":"#00000000","flexShrink":0,"borderColor":"#FF1F4799","backgroundColor":"#00000000"}},{"id":"right_body_rail_line","component":"Divider","styles":{"width":1,"strokeWidth":1,"vertical":true,"flexShrink":0,"height":32,"color":"#991F4799"}},{"id":"right_body_texts","component":"Column","children":["right_body_title","right_body_time","right_body_location"],"itemMargin":0,"styles":{"alignItems":"start","justifyContent":"start","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1,"height":50}},{"id":"right_body_title","component":"Text","content":"{{ ${/data/calendar/events/0/title} }}","styles":{"width":"matchParent","fontSize":14,"fontWeight":700,"maxLines":2,"flexShrink":0,"constraintSize":{"minWidth":0,"minHeight":18},"fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"right_body_time","component":"Text","content":"{{ ${/data/calendar/events/0/startDate} + ' ' + ${/data/calendar/events/0/dtStart} }}","styles":{"width":"matchParent","height":16,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":0,"constraintSize":{"minWidth":0},"fontColor":"#991F4799","textOverflow":"clip"}},{"id":"right_body_location","component":"Text","content":"{{ ${/data/calendar/events/0/eventLocation} }}","styles":{"width":"matchParent","height":16,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":0,"constraintSize":{"minWidth":0},"fontColor":"#991F4799","textOverflow":"clip"}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"weather":{"location":{"prefectureName":"上海市"},"current":{"temperatureText":"29℃","condition":"多云"},"daily":[{"weekday":"星期四","condition":"多云","temperatureRangeText":"25℃ / 32℃"}]},"calendar":{"events":[{"title":"项目例会","startDate":"08-06","dtStart":"14:00","eventLocation":"会议室"}]}}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "生成天气和日程卡片",
  "size": "2x4",
  "appVersion": "11.7.8.343",
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
        "current": {
          "temperatureText": {
            "type": "string",
            "description": "可直接显示的当前温度文本，已包含“℃”单位；展示时不得再次追加温度单位。例如“29℃”。",
            "sampleValue": "29℃"
          },
          "condition": {
            "type": "string",
            "description": "当前天气现象，例如“阴”“多云”“小雨”。",
            "sampleValue": "多云"
          }
        },
        "daily": [
          {
            "date": {
              "type": "string",
              "description": "预报日期，来源于 day_time。以端侧本次刷新日期为基准，daily[0]为明天日期，daily[1]为后天日期，不包含今天。",
              "sampleValue": "2026-08-06"
            },
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
            "date": {
              "type": "string",
              "description": "预报日期，来源于 day_time。以端侧本次刷新日期为基准，daily[0]为明天日期，daily[1]为后天日期，不包含今天。",
              "sampleValue": "2026-08-06"
            },
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
            "date": {
              "type": "string",
              "description": "预报日期，来源于 day_time。以端侧本次刷新日期为基准，daily[0]为明天日期，daily[1]为后天日期，不包含今天。",
              "sampleValue": "2026-08-06"
            },
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
          "prefectureName": {
            "type": "string",
            "description": "城市名称",
            "sampleValue": "上海市"
          },
          "districtName": {
            "type": "string",
            "description": "区或县名称",
            "sampleValue": "青浦区"
          },
          "cityCode": {
            "type": "string",
            "description": "城市代码，如60814代表青浦区",
            "sampleValue": "60814"
          }
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
            "eventLocation": {
              "type": "string",
              "description": "日程的具体地点描述，若未填写则为空字符串。",
              "sampleValue": "会议室"
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
          },
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
            "eventLocation": {
              "type": "string",
              "description": "日程的具体地点描述，若未填写则为空字符串。",
              "sampleValue": "会议室"
            },
            "countdownDays": {
              "type": "integer",
              "description": "距离日程开始的自然日天数纯整数，返回值不包含“天”。0 表示今天发生或已经发生，正整数表示距离开始还有多少天；若直接用于文本展示，必须在数值后追加“天”。",
              "sampleValue": 0
            }
          },
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
            "eventLocation": {
              "type": "string",
              "description": "日程的具体地点描述，若未填写则为空字符串。",
              "sampleValue": "会议室"
            },
            "countdownDays": {
              "type": "integer",
              "description": "距离日程开始的自然日天数纯整数，返回值不包含“天”。0 表示今天发生或已经发生，正整数表示距离开始还有多少天；若直接用于文本展示，必须在数值后追加“天”。",
              "sampleValue": 0
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
        "/current/temperatureText",
        "/current/condition",
        "/daily/0/date",
        "/daily/0/weekday",
        "/daily/0/condition",
        "/daily/0/temperatureRangeText",
        "/daily/1/date",
        "/daily/1/weekday",
        "/daily/1/condition",
        "/daily/1/temperatureRangeText",
        "/daily/2/date",
        "/daily/2/weekday",
        "/daily/2/condition",
        "/daily/2/temperatureRangeText",
        "/location/prefectureName",
        "/location/districtName"
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
        "/events/0/eventLocation",
        "/events/0/countdownDays",
        "/events/1/title",
        "/events/1/startDate",
        "/events/1/dtStart",
        "/events/1/eventLocation",
        "/events/1/countdownDays",
        "/events/2/title",
        "/events/2/startDate",
        "/events/2/dtStart",
        "/events/2/eventLocation",
        "/events/2/countdownDays"
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
  "artifactId": "b2a67314-4c6b-4f64-8a47-cae390286f52",
  "createdAt": 1793933872910
}
```
```designcompactdsl
["root","Layout",{"layout":"W-split-panels"},["left","right"]]
["left","Region",{"variant":"title-hero-support"},["left_title","left_primary","left_support"]]
["left_title","SingleLineTitle",{"title":{"path":"/data/weather/location/prefectureName"},"fontSize":12}]
["left_primary","EmphasizedData",{"value":{"path":"/data/weather/current/temperatureText"},"fontSize":30}]
["left_support","SecondaryBody",{"items":[{"value":{"path":"/data/weather/current/condition"}},{"label":"明天 ","value":"{{ ${/data/weather/daily/0/weekday} + ' ' + ${/data/weather/daily/0/condition} + ' ' + ${/data/weather/daily/0/temperatureRangeText} }}","maxLines":2}],"columns":1,"fontSize":12}]
["right","Region",{"variant":"title-content"},["right_title","right_body"]]
["right_title","SingleLineTitle",{"title":"日程","fontSize":12}]
["right_body","EventCard",{"items":[{"title":{"path":"/data/calendar/events/0/title"},"time":"{{ ${/data/calendar/events/0/startDate} + ' ' + ${/data/calendar/events/0/dtStart} }}","location":{"path":"/data/calendar/events/0/eventLocation"}}]}]
["/data/weather/location/prefectureName","上海市"]
["/data/weather/current/temperatureText","29℃"]
["/data/weather/current/condition","多云"]
["/data/weather/daily/0/weekday","星期四"]
["/data/weather/daily/0/condition","多云"]
["/data/weather/daily/0/temperatureRangeText","25℃ / 32℃"]
["/data/calendar/events/0/title","项目例会"]
["/data/calendar/events/0/startDate","08-06"]
["/data/calendar/events/0/dtStart","14:00"]
["/data/calendar/events/0/eventLocation","会议室"]
```
```request
{
  "content": {
    "title": "天气和日程",
    "description": "天气与日程速览",
    "userQuery": "生成天气和日程卡片",
    "size": "2x4",
    "bundleName": "com.huawei.genui",
    "functionName": "generateWidgetCardCompactDsl",
    "romVersion": "CMM-AL10 7.0.0.115",
    "candidateDataBindings": [
      {
        "arguments": {
          "forecastDays": 3
        },
        "candidateOutputFields": [
          "/current/temperatureText",
          "/current/condition",
          "/daily/0/date",
          "/daily/0/weekday",
          "/daily/0/condition",
          "/daily/0/temperatureRangeText",
          "/daily/1/date",
          "/daily/1/weekday",
          "/daily/1/condition",
          "/daily/1/temperatureRangeText",
          "/daily/2/date",
          "/daily/2/weekday",
          "/daily/2/condition",
          "/daily/2/temperatureRangeText",
          "/location/prefectureName",
          "/location/districtName"
        ],
        "capabilityId": "ViewWeather",
        "writeResultTo": "/data/weather"
      },
      {
        "arguments": {
          "futureDays": 7
        },
        "candidateOutputFields": [
          "/eventCount",
          "/events/0/title",
          "/events/0/startDate",
          "/events/0/dtStart",
          "/events/0/eventLocation",
          "/events/0/countdownDays",
          "/events/1/title",
          "/events/1/startDate",
          "/events/1/dtStart",
          "/events/1/eventLocation",
          "/events/1/countdownDays",
          "/events/2/title",
          "/events/2/startDate",
          "/events/2/dtStart",
          "/events/2/eventLocation",
          "/events/2/countdownDays"
        ],
        "capabilityId": "GetCalendarEvents",
        "writeResultTo": "/data/calendar"
      }
    ],
    "candidateEventCandidates": [
      {
        "action": {
          "args": {
            "abilityName": "",
            "bundleName": "",
            "intentName": "Weather_CityCode",
            "uri": "{{ 'hww://www.huawei.com/totemweather?enterType=share&cityCode=' + ${/data/weather/location/cityCode} }}"
          },
          "call": "clickToDeeplink"
        },
        "capabilityId": "event.open.weather"
      },
      {
        "action": {
          "args": {
            "intentName": "ViewCalendarEvent",
            "params": {
              "entityId": "{{ ${/data/calendar/events/0/entityId} }}"
            }
          },
          "call": "clickToIntent"
        },
        "capabilityId": "event.viewCalendarEvent"
      }
    ],
    "candidateAssetIds": []
  },
  "deviceInfo": {
    "countryCode": "CN",
    "deviceFormation": "HDSpeaker",
    "deviceType": 0,
    "locale": "zh-CN",
    "phoneType": "CMM-AL10",
    "prdVer": "11.7.8.343",
    "sysVer": "EmotionUI_9.0.0",
    "time": "20261027033028304"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q195-000",
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
  "size": "2x4",
  "functionName": "generateWidgetCardCompactDsl",
  "romVersion": "CMM-AL10 7.0.0.115",
  "candidateAssetIds": [],
  "candidateEventCandidates": [
    {
      "action": {
        "args": {
          "abilityName": "",
          "bundleName": "",
          "intentName": "Weather_CityCode",
          "uri": "{{ 'hww://www.huawei.com/totemweather?enterType=share&cityCode=' + ${/data/weather/location/cityCode} }}"
        },
        "call": "clickToDeeplink"
      },
      "capabilityId": "event.open.weather"
    },
    {
      "action": {
        "args": {
          "intentName": "ViewCalendarEvent",
          "params": {
            "entityId": "{{ ${/data/calendar/events/0/entityId} }}"
          }
        },
        "call": "clickToIntent"
      },
      "capabilityId": "event.viewCalendarEvent"
    }
  ],
  "bundleName": "com.huawei.genui",
  "description": "天气与日程速览",
  "userQuery": "生成天气和日程卡片",
  "title": "天气和日程",
  "candidateDataBindings": [
    {
      "arguments": {
        "forecastDays": 3
      },
      "candidateOutputFields": [
        "/current/temperatureText",
        "/current/condition",
        "/daily/0/date",
        "/daily/0/weekday",
        "/daily/0/condition",
        "/daily/0/temperatureRangeText",
        "/daily/1/date",
        "/daily/1/weekday",
        "/daily/1/condition",
        "/daily/1/temperatureRangeText",
        "/daily/2/date",
        "/daily/2/weekday",
        "/daily/2/condition",
        "/daily/2/temperatureRangeText",
        "/location/prefectureName",
        "/location/districtName"
      ],
      "capabilityId": "ViewWeather",
      "writeResultTo": "/data/weather"
    },
    {
      "arguments": {
        "futureDays": 7
      },
      "candidateOutputFields": [
        "/eventCount",
        "/events/0/title",
        "/events/0/startDate",
        "/events/0/dtStart",
        "/events/0/eventLocation",
        "/events/0/countdownDays",
        "/events/1/title",
        "/events/1/startDate",
        "/events/1/dtStart",
        "/events/1/eventLocation",
        "/events/1/countdownDays",
        "/events/2/title",
        "/events/2/startDate",
        "/events/2/dtStart",
        "/events/2/eventLocation",
        "/events/2/countdownDays"
      ],
      "capabilityId": "GetCalendarEvents",
      "writeResultTo": "/data/calendar"
    }
  ]
}
```
