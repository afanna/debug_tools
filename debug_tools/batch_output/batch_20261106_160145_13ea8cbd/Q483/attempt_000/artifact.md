```cardspec
{
  "title": "锁屏风格卡片",
  "description": "时间天气锁屏卡片",
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
      "capabilityId": "ViewWeather",
      "arguments": {
        "forecastDays": 1
      },
      "writeResultTo": "/data/weather"
    }
  ]
}
```
```genui
{"version":"v0.9","createSurface":{"surfaceId":"surface_card","catalogId":"ohos.a2ui.extended.catalog.form"}}
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Row","children":["left","right"],"itemMargin":12,"styles":{"width":"matchParent","height":"matchParent","padding":12,"borderRadius":20,"clip":true,"alignItems":"center","justifyContent":"start","linearGradient":{"direction":"RightBottom","colors":[["#FFCBDDFE",0],["#FFF1F6FE",1]]}}},{"id":"left","component":"Column","children":["__layout__left__sub"],"styles":{"height":"matchParent","layoutWeight":1,"padding":8,"borderRadius":16,"clip":true,"backgroundColor":"#99FFFFFF"},"itemMargin":0},{"id":"__layout__left__sub","component":"Column","children":["left_title","__layout__left__body"],"itemMargin":6,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":110.0}},{"id":"left_title","component":"Row","children":["left_title_title"],"styles":{"width":"matchParent","height":12,"flexShrink":0,"justifyContent":"start","alignItems":"center"},"itemMargin":0},{"id":"left_title_title","component":"Text","content":"当前时间","styles":{"fontSize":12,"fontWeight":400,"lineHeight":1,"textAlign":"start","maxLines":1,"flexShrink":0,"width":"matchParent","fontColor":"#991F4799"}},{"id":"__layout__left__body","component":"Column","children":["left_body"],"itemMargin":0,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"end","layoutWeight":1}},{"id":"left_body","component":"Column","children":["left_body_main"],"itemMargin":2,"styles":{"alignItems":"start","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent"}},{"id":"left_body_main","component":"Text","content":"{{ ${/data/time/currentDate} }}","styles":{"height":18,"fontSize":18,"fontWeight":700,"lineHeight":1,"maxLines":1,"flexShrink":1,"width":"matchParent","fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"right","component":"Column","children":["__layout__right__sub"],"styles":{"height":"matchParent","layoutWeight":1,"padding":8,"borderRadius":16,"clip":true,"backgroundColor":"#99FFFFFF"},"itemMargin":0},{"id":"__layout__right__sub","component":"Column","children":["right_title","__layout__right__body"],"itemMargin":6,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":110.0}},{"id":"right_title","component":"Row","children":["right_title_title"],"styles":{"width":"matchParent","height":12,"flexShrink":0,"justifyContent":"start","alignItems":"center"},"itemMargin":0},{"id":"right_title_title","component":"Text","content":"天气","styles":{"fontSize":12,"fontWeight":400,"lineHeight":1,"textAlign":"start","maxLines":1,"flexShrink":0,"width":"matchParent","fontColor":"#991F4799"}},{"id":"__layout__right__body","component":"Column","children":["__layout__right__primary","__layout__right__details"],"itemMargin":6,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1}},{"id":"__layout__right__primary","component":"Column","children":["right_primary"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1},"itemMargin":0},{"id":"right_primary","component":"Column","children":["right_primary_main","right_primary_secondary"],"itemMargin":2,"styles":{"alignItems":"start","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent"}},{"id":"right_primary_main","component":"Text","content":"{{ ${/data/weather/current/temperatureText} }}","styles":{"height":18,"fontSize":18,"fontWeight":700,"lineHeight":1,"maxLines":1,"flexShrink":1,"width":"matchParent","fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"right_primary_secondary","component":"Text","content":"{{ ${/data/weather/current/condition} }}","styles":{"height":16,"fontSize":12,"fontWeight":400,"lineHeight":1.3333333333333333,"maxLines":1,"flexShrink":1,"width":"matchParent","fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"__layout__right__details","component":"Column","children":["right_support"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"right_support","component":"Column","children":["right_support_row0","right_support_row1"],"itemMargin":2,"styles":{"width":"matchParent","alignItems":"start","flexShrink":1}},{"id":"right_support_item0_label","component":"Text","content":"星期","styles":{"height":12,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":0,"lineHeight":1,"fontColor":"#991F4799","textOverflow":"clip"}},{"id":"right_support_item0_value","component":"Text","content":"{{ ${/data/time/dayOfWeek} }}","styles":{"height":12.0,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":1,"lineHeight":1,"fontColor":"#FF1F4799","layoutWeight":1,"textOverflow":"clip"}},{"id":"right_support_item0","component":"Row","children":["right_support_item0_label","right_support_item0_value"],"itemMargin":4,"styles":{"height":12.0,"alignItems":"start","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"right_support_row0","component":"Row","children":["right_support_item0"],"itemMargin":0,"styles":{"width":"matchParent","height":12.0,"alignItems":"start","flexShrink":0}},{"id":"right_support_item1_label","component":"Text","content":"农历","styles":{"height":12,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":0,"lineHeight":1,"fontColor":"#991F4799","textOverflow":"clip"}},{"id":"right_support_item1_value","component":"Text","content":"{{ ${/data/time/lunarDate} }}","styles":{"height":12.0,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":1,"lineHeight":1,"fontColor":"#FF1F4799","layoutWeight":1,"textOverflow":"clip"}},{"id":"right_support_item1","component":"Row","children":["right_support_item1_label","right_support_item1_value"],"itemMargin":4,"styles":{"height":12.0,"alignItems":"start","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"right_support_row1","component":"Row","children":["right_support_item1"],"itemMargin":0,"styles":{"width":"matchParent","height":12.0,"alignItems":"start","flexShrink":0}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"time":{"currentDate":"示例","dayOfWeek":"示例","lunarDate":"示例"},"weather":{"current":{"temperatureText":"29℃","condition":"多云"}}}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "创建一张类似锁屏界面的桌面卡片，显示当前时间、日期、星期、农历以及当前天气温度和天气现象。",
  "size": "2x4",
  "appVersion": "11.7.8.342",
  "eventCandidates": [
    {
      "id": "event.open.weather",
      "description": "打开华为天气应用某城市页，uri为固定值勿更改。cityCode来自于数据能力中ViewWeather出参cityCode字段，进行动态拼接，表示跳转到指定城市天气页。",
      "call": "clickToDeeplink",
      "args": {
        "intentName": "Weather_CityCode",
        "bundleName": "",
        "abilityName": "",
        "uri": "{{ 'hww://www.huawei.com/totemweather?enterType=share&cityCode=' + ${/data/weather/location/cityCode} }}"
      }
    },
    {
      "id": "event.open.clock.alarm",
      "description": "打开华为时钟应用首页。",
      "call": "clickToDeeplink",
      "args": {
        "intentName": "Clock",
        "bundleName": "com.huawei.hmos.clock",
        "abilityName": "com.huawei.hmos.clock.phone",
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
      },
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
        "location": {
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
    "ViewWeather"
  ],
  "event": [
    {
      "id": "event.open.weather",
      "description": "打开华为天气应用某城市页，uri为固定值勿更改。cityCode来自于数据能力中ViewWeather出参cityCode字段，进行动态拼接，表示跳转到指定城市天气页。",
      "call": "clickToDeeplink",
      "args": {
        "intentName": "Weather_CityCode",
        "bundleName": "",
        "abilityName": "",
        "uri": "{{ 'hww://www.huawei.com/totemweather?enterType=share&cityCode=' + ${/data/weather/location/cityCode} }}"
      }
    },
    {
      "id": "event.open.clock.alarm",
      "description": "打开华为时钟应用首页。",
      "call": "clickToDeeplink",
      "args": {
        "intentName": "Clock",
        "bundleName": "com.huawei.hmos.clock",
        "abilityName": "com.huawei.hmos.clock.phone",
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
    },
    {
      "capabilityId": "ViewWeather",
      "arguments": {
        "forecastDays": 1
      },
      "writeResultTo": "/data/weather",
      "candidateOutputFields": [
        "/current/temperatureText",
        "/current/condition",
        "/location/districtName"
      ]
    }
  ],
  "candidateEventCandidates": [
    {
      "capabilityId": "event.open.weather",
      "action": {
        "call": "clickToDeeplink",
        "args": {
          "intentName": "Weather_CityCode",
          "bundleName": "",
          "abilityName": "",
          "uri": "{{ 'hww://www.huawei.com/totemweather?enterType=share&cityCode=' + ${/data/weather/location/cityCode} }}"
        }
      }
    },
    {
      "capabilityId": "event.open.clock.alarm",
      "action": {
        "call": "clickToDeeplink",
        "args": {
          "intentName": "Clock",
          "bundleName": "com.huawei.hmos.clock",
          "abilityName": "com.huawei.hmos.clock.phone",
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
  "artifactId": "dc961c1a-5b0d-4fb1-a442-17f2d1002bf3",
  "createdAt": 1793952268215
}
```
```designcompactdsl
["root","Layout",{"layout":"W-split-panels"},["left","right"]]
["left","Region",{"variant":"title-content"},["left_title","left_body"]]
["left_title","SingleLineTitle",{"title":"当前时间","fontSize":12}]
["left_body","EmphasisText",{"mainText":{"path":"/data/time/currentDate"},"fontSize":18}]
["right","Region",{"variant":"title-hero-support"},["right_title","right_primary","right_support"]]
["right_title","SingleLineTitle",{"title":"天气","fontSize":12}]
["right_primary","EmphasisText",{"mainText":{"path":"/data/weather/current/temperatureText"},"secondaryText":{"path":"/data/weather/current/condition"},"fontSize":18}]
["right_support","SecondaryBody",{"items":[{"label":"星期 ","value":{"path":"/data/time/dayOfWeek"}},{"label":"农历 ","value":{"path":"/data/time/lunarDate"}}],"columns":1,"fontSize":12}]
["/data/time/currentDate","示例"]
["/data/time/dayOfWeek","示例"]
["/data/time/lunarDate","示例"]
["/data/weather/current/temperatureText","29℃"]
["/data/weather/current/condition","多云"]
```
```request
{
  "content": {
    "size": "2x4",
    "functionName": "generateWidgetCardCompactDsl",
    "romVersion": "CMM-AL10P 7.0.0.111",
    "candidateAssetIds": [],
    "candidateEventCandidates": [
      {
        "capabilityId": "event.open.weather",
        "action": {
          "call": "clickToDeeplink",
          "args": {
            "intentName": "Weather_CityCode",
            "bundleName": "",
            "abilityName": "",
            "uri": "{{ 'hww://www.huawei.com/totemweather?enterType=share&cityCode=' + ${/data/weather/location/cityCode} }}"
          }
        }
      },
      {
        "capabilityId": "event.open.clock.alarm",
        "action": {
          "call": "clickToDeeplink",
          "args": {
            "intentName": "Clock",
            "bundleName": "com.huawei.hmos.clock",
            "abilityName": "com.huawei.hmos.clock.phone",
            "uri": ""
          }
        }
      }
    ],
    "bundleName": "com.huawei.genui",
    "description": "时间天气锁屏卡片",
    "userQuery": "创建一张类似锁屏界面的桌面卡片，显示当前时间、日期、星期、农历以及当前天气温度和天气现象。",
    "title": "锁屏风格卡片",
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
        "capabilityId": "ViewWeather",
        "arguments": {
          "forecastDays": 1
        },
        "writeResultTo": "/data/weather",
        "candidateOutputFields": [
          "/current/temperatureText",
          "/current/condition",
          "/location/districtName"
        ]
      }
    ]
  },
  "deviceInfo": {
    "countryCode": "CN",
    "deviceFormation": "HDSpeaker",
    "deviceType": 0,
    "locale": "zh-CN",
    "phoneType": "CMM-AL10",
    "prdVer": "11.7.8.342",
    "sysVer": "EmotionUI_9.0.0",
    "time": "20261101163713172"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q483-000",
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
  "size": "2x4",
  "functionName": "generateWidgetCardCompactDsl",
  "romVersion": "CMM-AL10P 7.0.0.111",
  "candidateAssetIds": [],
  "candidateEventCandidates": [
    {
      "capabilityId": "event.open.weather",
      "action": {
        "call": "clickToDeeplink",
        "args": {
          "intentName": "Weather_CityCode",
          "bundleName": "",
          "abilityName": "",
          "uri": "{{ 'hww://www.huawei.com/totemweather?enterType=share&cityCode=' + ${/data/weather/location/cityCode} }}"
        }
      }
    },
    {
      "capabilityId": "event.open.clock.alarm",
      "action": {
        "call": "clickToDeeplink",
        "args": {
          "intentName": "Clock",
          "bundleName": "com.huawei.hmos.clock",
          "abilityName": "com.huawei.hmos.clock.phone",
          "uri": ""
        }
      }
    }
  ],
  "bundleName": "com.huawei.genui",
  "description": "时间天气锁屏卡片",
  "userQuery": "创建一张类似锁屏界面的桌面卡片，显示当前时间、日期、星期、农历以及当前天气温度和天气现象。",
  "title": "锁屏风格卡片",
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
      "capabilityId": "ViewWeather",
      "arguments": {
        "forecastDays": 1
      },
      "writeResultTo": "/data/weather",
      "candidateOutputFields": [
        "/current/temperatureText",
        "/current/condition",
        "/location/districtName"
      ]
    }
  ]
}
```
