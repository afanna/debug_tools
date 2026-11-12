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
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Stack","children":["__post_theme_background","__genui_render_component__root"],"styles":{"width":"matchParent","height":"matchParent","padding":0,"alignContent":"topStart","clip":true,"borderRadius":20,"backgroundColor":"#FF1F1F99"}},{"id":"__post_theme_background","component":"Stack","children":["fusionBallBackground","__post_theme_base"],"styles":{"width":"matchParent","height":"matchParent","alignContent":"topStart"}},{"id":"__post_theme_base","component":"Image","src":"https://lfcontentcenterdev.hwcloudtest.cn/pub_5/FaStore_fa_900_9/bb/v3/fa/osms/1/1/027921810f48447db821c68f8f6abe8b/1da1cac0fa514a86b93c07f72c057723.jpg","styles":{"width":"matchParent","height":"matchParent","objectFit":"fill"}},{"id":"fusionBallBackground","component":"Stack","children":["fusionBallLargeSlot","fusionBallMediumSlot","fusionBallSmallSlot","fusionBallGlassLayer"],"styles":{"width":"100%","height":"100%","borderRadius":20,"alignContent":"topStart","clip":true}},{"id":"fusionBallLargeSlot","component":"Stack","children":["fusionBallLarge"],"styles":{"width":"112.5%","height":"58.75%","alignContent":"bottom"}},{"id":"fusionBallLarge","component":"Divider","styles":{"width":"116.666667%","height":"446.808511%","strokeWidth":0,"color":"#00000000","borderRadius":210,"backgroundColor":"#FF1F1F99","clip":true}},{"id":"fusionBallMediumSlot","component":"Stack","children":["fusionBallMedium"],"styles":{"width":"50%","height":"175%","alignContent":"bottom"}},{"id":"fusionBallMedium","component":"Divider","styles":{"width":"200%","height":"114.285714%","strokeWidth":0,"color":"#00000000","borderRadius":160,"backgroundColor":"#FF2B65D9","clip":true}},{"id":"fusionBallSmallSlot","component":"Stack","children":["fusionBallSmall"],"styles":{"width":"121.875%","height":"137.5%","alignContent":"bottomEnd"}},{"id":"fusionBallSmall","component":"Divider","styles":{"width":"51.282051%","height":"90.909091%","strokeWidth":0,"color":"#00000000","borderRadius":100,"backgroundColor":"#FF57AED9","clip":true}},{"id":"fusionBallGlassLayer","component":"Divider","styles":{"width":"100%","height":"100%","strokeWidth":0,"color":"#00000000","backgroundColor":"#0DFFFFFF","backdropBlur":{"radius":210}}},{"id":"__genui_render_component__root","component":"Stack","children":["foreground"],"styles":{"width":"matchParent","height":"matchParent","borderRadius":20,"clip":true}},{"id":"foreground","component":"Column","children":["title"],"styles":{"width":"matchParent","height":"matchParent","padding":12,"alignItems":"start","justifyContent":"start"},"itemMargin":0},{"id":"title","component":"Column","children":["title_main"],"itemMargin":2,"styles":{"alignItems":"start","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent"}},{"id":"title_main","component":"Text","content":"Design Compact Mock","styles":{"height":18,"fontSize":18,"fontWeight":700,"lineHeight":1,"maxLines":1,"flexShrink":1,"width":"matchParent","fontColor":"#FFFFFFFF","textOverflow":"clip"}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"ui":{"state":"ready"}}}}
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
  "assetCandidates": [
    {
      "id": "photo-ux-texture-orange-diagonal-wide",
      "src": "https://lfcontentcenterdev.hwcloudtest.cn/pub_5/FaStore_fa_900_9/bb/v3/fa/osms/1/1/027921810f48447db821c68f8f6abe8b/1da1cac0fa514a86b93c07f72c057723.jpg",
      "description": "主题背景"
    }
  ]
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
  "asset": [
    "photo-ux-texture-orange-diagonal-wide"
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
  "artifactId": "d4db96d3-dc71-4b42-96ed-ac635d40fc8a",
  "createdAt": 1793932878316
}
```
```designcompactdsl
["root","Stack",{"width":"matchParent","height":"matchParent","borderRadius":20,"clip":true},["foreground"]]
["foreground","Column",{"width":"matchParent","height":"matchParent","padding":12,"alignItems":"start","justifyContent":"start"},["title"]]
["title","EmphasisText",{"mainText":"Design Compact Mock"}]
["/ui/state","ready"]
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
    "sessionId": "batch-baaba440"
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
