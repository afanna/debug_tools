```cardspec
{
  "title": "时间天气",
  "description": "河间实时天气与预报",
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
        "districtName": "河间市",
        "forecastDays": 3,
        "prefectureName": "沧州市"
      },
      "writeResultTo": "/data/weather"
    }
  ]
}
```
```genui
{"version":"v0.9","createSurface":{"surfaceId":"surface_card","catalogId":"ohos.a2ui.extended.catalog.form"}}
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Column","children":["title","__layout__root__body"],"itemMargin":6,"styles":{"width":"matchParent","height":"matchParent","padding":12,"borderRadius":20,"clip":true,"alignItems":"start","justifyContent":"start","linearGradient":{"direction":"RightBottom","colors":[["#FFCBDDFE",0],["#FFF1F6FE",1]]}}},{"id":"title","component":"Row","children":["title_title"],"styles":{"width":"matchParent","height":12,"flexShrink":0,"justifyContent":"start","alignItems":"center"},"itemMargin":0},{"id":"title_title","component":"Text","content":"河间天气","styles":{"fontSize":12,"fontWeight":400,"lineHeight":1,"textAlign":"start","maxLines":1,"flexShrink":0,"width":"matchParent","fontColor":"#991F4799"}},{"id":"__layout__root__body","component":"Column","children":["__layout__root__primary","__layout__root__details"],"itemMargin":8,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1}},{"id":"__layout__root__primary","component":"Column","children":["primary"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"primary","component":"Column","children":["primary_main","primary_secondary"],"itemMargin":2,"styles":{"alignItems":"start","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent"}},{"id":"primary_main","component":"Text","content":"{{ ${/data/weather/current/temperatureText} }}","styles":{"height":18,"fontSize":18,"fontWeight":700,"lineHeight":1,"maxLines":1,"flexShrink":1,"width":"matchParent","fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"primary_secondary","component":"Text","content":"{{ ${/data/weather/current/condition} }}","styles":{"height":16,"fontSize":12,"fontWeight":400,"lineHeight":1.3333333333333333,"maxLines":1,"flexShrink":1,"width":"matchParent","fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"__layout__root__details","component":"Column","children":["details"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1},"itemMargin":0},{"id":"details","component":"Row","children":["details_item0","details_item1","details_item2"],"itemMargin":8,"styles":{"width":"matchParent","height":"matchParent","alignItems":"top","justifyContent":"start","layoutWeight":1,"flexShrink":1,"constraintSize":{"minHeight":48}}},{"id":"details_item0","component":"Column","children":["details_item0_label_slot","details_item0_value_slot"],"itemMargin":2,"styles":{"height":"matchParent","backgroundColor":"#99FFFFFF","padding":{"left":8,"right":8},"borderRadius":16,"alignItems":"start","justifyContent":"center","layoutWeight":1,"flexShrink":1,"constraintSize":{"minWidth":0,"minHeight":0}}},{"id":"details_item0_label_slot","component":"Row","children":["details_item0_label"],"styles":{"width":"matchParent","height":18,"alignItems":"center","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"details_item0_label","component":"Text","content":"{{ ${/data/time/currentDate} }}","styles":{"width":"matchParent","fontSize":12,"fontWeight":700,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","fontColor":"#991F4799"}},{"id":"details_item0_value_slot","component":"Row","children":["details_item0_value"],"styles":{"width":"matchParent","height":16,"alignItems":"center","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"details_item0_value","component":"Text","content":"{{ ${/data/time/dayOfWeek} }}","styles":{"width":"matchParent","fontSize":10,"fontWeight":500,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","fontColor":"#FF1F4799"}},{"id":"details_item1","component":"Column","children":["details_item1_label_slot","details_item1_value_slot"],"itemMargin":2,"styles":{"height":"matchParent","backgroundColor":"#99FFFFFF","padding":{"left":8,"right":8},"borderRadius":16,"alignItems":"start","justifyContent":"center","layoutWeight":1,"flexShrink":1,"constraintSize":{"minWidth":0,"minHeight":0}}},{"id":"details_item1_label_slot","component":"Row","children":["details_item1_label"],"styles":{"width":"matchParent","height":18,"alignItems":"center","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"details_item1_label","component":"Text","content":"{{ ${/data/weather/current/alertLevel} }}","styles":{"width":"matchParent","fontSize":12,"fontWeight":700,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","fontColor":"#991F4799"}},{"id":"details_item1_value_slot","component":"Row","children":["details_item1_value"],"styles":{"width":"matchParent","height":16,"alignItems":"center","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"details_item1_value","component":"Text","content":"{{ ${/data/weather/daily/0/temperatureRangeText} }}","styles":{"width":"matchParent","fontSize":10,"fontWeight":500,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","fontColor":"#FF1F4799"}},{"id":"details_item2","component":"Column","children":["details_item2_label_slot","details_item2_value_slot"],"itemMargin":2,"styles":{"height":"matchParent","backgroundColor":"#99FFFFFF","padding":{"left":8,"right":8},"borderRadius":16,"alignItems":"start","justifyContent":"center","layoutWeight":1,"flexShrink":1,"constraintSize":{"minWidth":0,"minHeight":0}}},{"id":"details_item2_label_slot","component":"Row","children":["details_item2_label"],"styles":{"width":"matchParent","height":18,"alignItems":"center","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"details_item2_label","component":"Text","content":"{{ ${/data/weather/daily/1/weekday} }}","styles":{"width":"matchParent","fontSize":12,"fontWeight":700,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","fontColor":"#991F4799"}},{"id":"details_item2_value_slot","component":"Row","children":["details_item2_value"],"styles":{"width":"matchParent","height":16,"alignItems":"center","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"details_item2_value","component":"Text","content":"{{ ${/data/weather/daily/2/temperatureRangeText} }}","styles":{"width":"matchParent","fontSize":10,"fontWeight":500,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","fontColor":"#FF1F4799"}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"time":{"currentDate":"示例","dayOfWeek":"示例"},"weather":{"current":{"temperatureText":"29℃","condition":"多云","alertLevel":"大风蓝色预警"},"daily":[{"weekday":"星期四","condition":"多云","temperatureRangeText":"25℃ / 32℃"},{"weekday":"星期四","condition":"多云","temperatureRangeText":"25℃ / 32℃"},{"weekday":"星期四","condition":"多云","temperatureRangeText":"25℃ / 32℃"}],"location":{"cityCode":"60814"}}}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "创建一张桌面卡片，显示当前时间、日期、星期，以及河间当前温度、天气现象、大风预警，并显示未来3天的天气预报。",
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
          },
          "alertLevel": {
            "type": "string",
            "description": "预警信息。当前气象预警信息，例如'暴雨橙色预警'、'高温黄色预警'、'台风蓝色预警'。无预警时为空字符串。",
            "sampleValue": "大风蓝色预警"
          }
        },
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
        "abilityName": "",
        "bundleName": "",
        "intentName": "Weather_CityCode",
        "uri": "{{ 'hww://www.huawei.com/totemweather?enterType=share&cityCode=' + ${/data/weather/location/cityCode} }}"
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
        "districtName": "河间市",
        "forecastDays": 3,
        "prefectureName": "沧州市"
      },
      "writeResultTo": "/data/weather",
      "candidateOutputFields": [
        "/current/temperatureText",
        "/current/condition",
        "/current/alertLevel",
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
  "artifactId": "0ea1c605-54ab-40d4-884a-8e96653f8c58",
  "createdAt": 1793934605084
}
```
```designcompactdsl
["root","Layout",{"layout":"W-top-bottom","variant":"continuous"},["title","primary","details"]]
["title","SingleLineTitle",{"title":"河间天气","fontSize":12}]
["primary","EmphasisText",{"mainText":{"path":"/data/weather/current/temperatureText"},"secondaryText":{"path":"/data/weather/current/condition"},"fontSize":18}]
["details","TextBlock",{"items":[{"label":{"path":"/data/time/currentDate"},"value":{"path":"/data/time/dayOfWeek"}},{"label":{"path":"/data/weather/current/alertLevel"},"value":{"path":"/data/weather/daily/0/temperatureRangeText"}},{"label":{"path":"/data/weather/daily/1/weekday"},"value":{"path":"/data/weather/daily/2/temperatureRangeText"}}]}]
["/data/time/currentDate","示例"]
["/data/time/dayOfWeek","示例"]
["/data/weather/current/temperatureText","29℃"]
["/data/weather/current/condition","多云"]
["/data/weather/current/alertLevel","大风蓝色预警"]
["/data/weather/daily/0/weekday","星期四"]
["/data/weather/daily/0/condition","多云"]
["/data/weather/daily/0/temperatureRangeText","25℃ / 32℃"]
["/data/weather/daily/1/weekday","星期四"]
["/data/weather/daily/1/condition","多云"]
["/data/weather/daily/1/temperatureRangeText","25℃ / 32℃"]
["/data/weather/daily/2/weekday","星期四"]
["/data/weather/daily/2/condition","多云"]
["/data/weather/daily/2/temperatureRangeText","25℃ / 32℃"]
["/data/weather/location/cityCode","60814"]
```
```request
{
  "content": {
    "bundleName": "com.huawei.genui",
    "userQuery": "创建一张桌面卡片，显示当前时间、日期、星期，以及河间当前温度、天气现象、大风预警，并显示未来3天的天气预报。",
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
          "districtName": "河间市",
          "forecastDays": 3,
          "prefectureName": "沧州市"
        },
        "writeResultTo": "/data/weather",
        "candidateOutputFields": [
          "/current/temperatureText",
          "/current/condition",
          "/current/alertLevel",
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
      }
    ],
    "title": "时间天气",
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
      }
    ],
    "description": "河间实时天气与预报",
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
    "time": "20261030142920787"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q362-000",
    "isNew": true,
    "sessionId": "batch-7664fcb9"
  },
  "userAuth": {
    "user": {}
  },
  "utterance": {
    "original": "创建一张桌面卡片，显示当前时间、日期、星期，以及河间当前温度、天气现象、大风预警，并显示未来3天的天气预报。",
    "type": "text"
  },
  "version": "1.0",
  "functionName": "generateWidgetCardCompactDsl",
  "romVersion": "CMS-AL20 7.0.0.111",
  "bundleName": "com.huawei.genui",
  "userQuery": "创建一张桌面卡片，显示当前时间、日期、星期，以及河间当前温度、天气现象、大风预警，并显示未来3天的天气预报。",
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
        "districtName": "河间市",
        "forecastDays": 3,
        "prefectureName": "沧州市"
      },
      "writeResultTo": "/data/weather",
      "candidateOutputFields": [
        "/current/temperatureText",
        "/current/condition",
        "/current/alertLevel",
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
    }
  ],
  "title": "时间天气",
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
    }
  ],
  "description": "河间实时天气与预报",
  "candidateAssetIds": []
}
```
```repair-1
{
  "modelGeneratedCompactDsl": "[\"root\",\"Layout\",{\"layout\":\"W-top-bottom\",\"variant\":\"continuous\"},[\"title\",\"primary\",\"details\"]]\n[\"title\",\"SingleLineTitle\",{\"title\":\"河间天气\",\"fontSize\":12}]\n[\"primary\",\"Group\",{\"variant\":\"hero-support\"},[\"primary_hero\",\"primary_support\"]]\n[\"primary_hero\",\"EmphasisText\",{\"mainText\":{\"path\":\"/data/weather/current/temperatureText\"},\"secondaryText\":{\"path\":\"/data/weather/current/condition\"},\"fontSize\":18}]\n[\"primary_support\",\"SecondaryBody\",{\"items\":[{\"label\":\"日期 \",\"value\":{\"path\":\"/data/time/currentDate\"}},{\"label\":\"星期 \",\"value\":{\"path\":\"/data/time/dayOfWeek\"}},{\"value\":{\"path\":\"/data/weather/current/alertLevel\"}}],\"columns\":1,\"fontSize\":12}]\n[\"details\",\"TextBlock\",{\"items\":[{\"label\":{\"path\":\"/data/weather/daily/0/weekday\"},\"value\":\"{{ ${/data/weather/daily/0/condition} + ' ' + ${/data/weather/daily/0/temperatureRangeText} }}\"},{\"label\":{\"path\":\"/data/weather/daily/1/weekday\"},\"value\":\"{{ ${/data/weather/daily/1/condition} + ' ' + ${/data/weather/daily/1/temperatureRangeText} }}\"},{\"label\":{\"path\":\"/data/weather/daily/2/weekday\"},\"value\":\"{{ ${/data/weather/daily/2/condition} + ' ' + ${/data/weather/daily/2/temperatureRangeText} }}\"}]}]\n[\"/data/time/currentDate\",\"示例\"]\n[\"/data/time/dayOfWeek\",\"示例\"]\n[\"/data/weather/current/temperatureText\",\"29℃\"]\n[\"/data/weather/current/condition\",\"多云\"]\n[\"/data/weather/current/alertLevel\",\"大风蓝色预警\"]\n[\"/data/weather/daily/0/weekday\",\"星期四\"]\n[\"/data/weather/daily/0/condition\",\"多云\"]\n[\"/data/weather/daily/0/temperatureRangeText\",\"25℃ / 32℃\"]\n[\"/data/weather/daily/1/weekday\",\"星期四\"]\n[\"/data/weather/daily/1/condition\",\"多云\"]\n[\"/data/weather/daily/1/temperatureRangeText\",\"25℃ / 32℃\"]\n[\"/data/weather/daily/2/weekday\",\"星期四\"]\n[\"/data/weather/daily/2/condition\",\"多云\"]\n[\"/data/weather/daily/2/temperatureRangeText\",\"25℃ / 32℃\"]\n[\"/data/weather/location/cityCode\",\"60814\"]",
  "generatedDsl": "",
  "validationErrors": [
    {
      "stage": "validation",
      "code": "COMPACT_DSL_VALIDATION_FAILED",
      "message": "component root: vertical layout requires at least 144vp within 126vp; it overflows by 18vp. Regroup facts or choose a layout with enough body space; preserve required text, actions, font sizes and fixed design heights. Weight, clipping, flex shrink and distributed alignment cannot eliminate content height. Occupancy: title=12vp+margin(0vp), __layout__root__body=126vp+margin(0vp), gaps=6vp.",
      "compactDiagnostics": [
        {
          "code": "COMPACT_LAYOUT_HEIGHT_OVERFLOW",
          "validationClass": "semantic",
          "category": "layout",
          "severity": "error",
          "message": "component root: vertical layout requires at least 144vp within 126vp; it overflows by 18vp. Occupancy: title=12vp+margin(0vp), __layout__root__body=126vp+margin(0vp), gaps=6vp.",
          "legacyMessage": "component root: vertical layout requires at least 144vp within 126vp; it overflows by 18vp. Regroup facts or choose a layout with enough body space; preserve required text, actions, font sizes and fixed design heights. Weight, clipping, flex shrink and distributed alignment cannot eliminate content height. Occupancy: title=12vp+margin(0vp), __layout__root__body=126vp+margin(0vp), gaps=6vp.",
          "expected": {
            "maximumHeight": 126.0,
            "heightTolerance": 2.0,
            "preserveFixedDesignSizes": true,
            "preserveRequiredTextAndActions": true,
            "overflowConstraint": "不能依靠权重、裁剪、flex shrink 或分布式对齐消除内容高度超限。"
          },
          "actual": {
            "minimumRequiredHeight": 144.0,
            "overflow": 18.0,
            "occupancy": "title=12vp+margin(0vp), __layout__root__body=126vp+margin(0vp), gaps=6vp",
            "secondaryBodyFits": [
              {
                "componentId": "primary_support",
                "parentId": "root",
                "actualRowCount": 3,
                "maxRetainedRowCount": 1,
                "effectiveColumnCount": 1,
                "rowHeights": [
                  12.0,
                  12.0,
                  12.0
                ],
                "rowSpacing": 2.0,
                "directlyFitsItemIndexes": [
                  0
                ],
                "doesNotFitItemIndexes": [
                  1,
                  2
                ],
                "parentAvailableHeight": 126.0
              }
            ]
          },
          "evidenceSource": "expanded",
          "componentId": "root",
          "sourceLine": 1,
          "fixHint": "根据占用明细重新组合完整信息或选择合法布局，保留必要事实、动作、字号和固定设计高度；不能靠裁剪、收缩或调整权重消除负预算。"
        }
      ],
      "capacityFits": [
        {
          "componentId": "primary_support",
          "componentType": "SecondaryBody",
          "actualItemCount": 3,
          "actualRowCount": 3,
          "maxRetainedRowCount": 1,
          "effectiveColumnCount": 1,
          "rowHeights": [
            12.0,
            12.0,
            12.0
          ],
          "rowSpacing": 2.0,
          "parentId": "root",
          "parentAvailableHeight": 126.0,
          "directlyFits": [
            {
              "itemIndex": 0,
              "value": {
                "label": "日期 ",
                "value": {
                  "path": "/data/time/currentDate"
                }
              },
              "planFacts": [
                {
                  "factIndex": 0,
                  "requirement": "当前日期",
                  "priority": "must"
                }
              ]
            }
          ],
          "doesNotFit": [
            {
              "itemIndex": 1,
              "value": {
                "label": "星期 ",
                "value": {
                  "path": "/data/time/dayOfWeek"
                }
              },
              "planFacts": [
                {
                  "factIndex": 1,
                  "requirement": "当前星期",
                  "priority": "must"
                },
                {
                  "factIndex": 5,
                  "requirement": "未来第1天星期",
                  "priority": "must"
                },
                {
                  "factIndex": 8,
                  "requirement": "未来第2天星期",
                  "priority": "must"
                },
                {
                  "factIndex": 11,
                  "requirement": "未来第3天星期",
                  "priority": "must"
                }
              ]
            },
            {
              "itemIndex": 2,
              "value": {
                "value": {
                  "path": "/data/weather/current/alertLevel"
                }
              },
              "planFacts": [
                {
                  "factIndex": 4,
                  "requirement": "大风预警",
                  "priority": "must"
                }
              ]
            }
          ],
          "overflowItemCount": 2,
          "overflowFactCount": 5,
          "scope": "currentComponentItemsOnly",
          "instruction": "父区域剩余高度结合当前列分组、展开后行高和行间距，只能保留 maxRetainedRowCount 行；doesNotFit 是当前组件中无法容纳的条目。该切分不是省略授权；只有 repairStrategy.optionalDrop 或 approvedOmissions 明确列出的非 Action 事实才允许删除。"
        }
      ]
    },
    {
      "stage": "validation",
      "code": "COMPACT_DSL_VALIDATION_FAILED",
      "message": "component __layout__root__body: vertical layout requires at least 126vp within 108vp; it overflows by 18vp. Regroup facts or choose a layout with enough body space; preserve required text, actions, font sizes and fixed design heights. Weight, clipping, flex shrink and distributed alignment cannot eliminate content height. Occupancy: __layout__root__primary=78vp+margin(0vp), __layout__root__details=48vp+margin(0vp), gaps=0vp.",
      "compactDiagnostics": [
        {
          "code": "COMPACT_LAYOUT_HEIGHT_OVERFLOW",
          "validationClass": "semantic",
          "category": "layout",
          "severity": "error",
          "message": "component __layout__root__body: vertical layout requires at least 126vp within 108vp; it overflows by 18vp. Occupancy: __layout__root__primary=78vp+margin(0vp), __layout__root__details=48vp+margin(0vp), gaps=0vp.",
          "legacyMessage": "component __layout__root__body: vertical layout requires at least 126vp within 108vp; it overflows by 18vp. Regroup facts or choose a layout with enough body space; preserve required text, actions, font sizes and fixed design heights. Weight, clipping, flex shrink and distributed alignment cannot eliminate content height. Occupancy: __layout__root__primary=78vp+margin(0vp), __layout__root__details=48vp+margin(0vp), gaps=0vp.",
          "expected": {
            "maximumHeight": 108.0,
            "heightTolerance": 2.0,
            "preserveFixedDesignSizes": true,
            "preserveRequiredTextAndActions": true,
            "overflowConstraint": "不能依靠权重、裁剪、flex shrink 或分布式对齐消除内容高度超限。"
          },
          "actual": {
            "minimumRequiredHeight": 126.0,
            "overflow": 18.0,
            "occupancy": "__layout__root__primary=78vp+margin(0vp), __layout__root__details=48vp+margin(0vp), gaps=0vp",
            "secondaryBodyFits": [
              {
                "componentId": "primary_support",
                "parentId": "__layout__root__body",
                "actualRowCount": 3,
                "maxRetainedRowCount": 1,
                "effectiveColumnCount": 1,
                "rowHeights": [
                  12.0,
                  12.0,
                  12.0
                ],
                "rowSpacing": 2.0,
                "directlyFitsItemIndexes": [
                  0
                ],
                "doesNotFitItemIndexes": [
                  1,
                  2
                ],
                "parentAvailableHeight": 108.0
              }
            ]
          },
          "evidenceSource": "expanded",
          "componentId": "root",
          "sourceLine": 1,
          "fixHint": "根据占用明细重新组合完整信息或选择合法布局，保留必要事实、动作、字号和固定设计高度；不能靠裁剪、收缩或调整权重消除负预算。"
        }
      ]
    },
    {
      "stage": "validation",
      "code": "COMPACT_DSL_VALIDATION_FAILED",
      "message": "component __layout__root__details: vertical layout requires at least 48vp within 30vp; it overflows by 18vp. Regroup facts or choose a layout with enough body space; preserve required text, actions, font sizes and fixed design heights. Weight, clipping, flex shrink and distributed alignment cannot eliminate content height. Occupancy: details=48vp+margin(0vp), gaps=0vp.",
      "compactDiagnostics": [
        {
          "code": "COMPACT_LAYOUT_HEIGHT_OVERFLOW",
          "validationClass": "semantic",
          "category": "layout",
          "severity": "error",
          "message": "component __layout__root__details: vertical layout requires at least 48vp within 30vp; it overflows by 18vp. Occupancy: details=48vp+margin(0vp), gaps=0vp.",
          "legacyMessage": "component __layout__root__details: vertical layout requires at least 48vp within 30vp; it overflows by 18vp. Regroup facts or choose a layout with enough body space; preserve required text, actions, font sizes and fixed design heights. Weight, clipping, flex shrink and distributed alignment cannot eliminate content height. Occupancy: details=48vp+margin(0vp), gaps=0vp.",
          "expected": {
            "maximumHeight": 30.0,
            "heightTolerance": 2.0,
            "preserveFixedDesignSizes": true,
            "preserveRequiredTextAndActions": true,
            "overflowConstraint": "不能依靠权重、裁剪、flex shrink 或分布式对齐消除内容高度超限。"
          },
          "actual": {
            "minimumRequiredHeight": 48.0,
            "overflow": 18.0,
            "occupancy": "details=48vp+margin(0vp), gaps=0vp"
          },
          "evidenceSource": "expanded",
          "componentId": "root",
          "sourceLine": 1,
          "fixHint": "根据占用明细重新组合完整信息或选择合法布局，保留必要事实、动作、字号和固定设计高度；不能靠裁剪、收缩或调整权重消除负预算。"
        }
      ]
    },
    {
      "stage": "validation",
      "code": "COMPACT_DSL_VALIDATION_FAILED",
      "message": "component details_item0: vertical layout requires at least 36vp within 30vp; it overflows by 6vp. Regroup facts or choose a layout with enough body space; preserve required text, actions, font sizes and fixed design heights. Weight, clipping, flex shrink and distributed alignment cannot eliminate content height. Occupancy: details_item0_label_slot=18vp+margin(0vp), details_item0_value_slot=16vp+margin(0vp), gaps=2vp.",
      "compactDiagnostics": [
        {
          "code": "COMPACT_LAYOUT_HEIGHT_OVERFLOW",
          "validationClass": "semantic",
          "category": "layout",
          "severity": "error",
          "message": "component details_item0: vertical layout requires at least 36vp within 30vp; it overflows by 6vp. Occupancy: details_item0_label_slot=18vp+margin(0vp), details_item0_value_slot=16vp+margin(0vp), gaps=2vp.",
          "legacyMessage": "component details_item0: vertical layout requires at least 36vp within 30vp; it overflows by 6vp. Regroup facts or choose a layout with enough body space; preserve required text, actions, font sizes and fixed design heights. Weight, clipping, flex shrink and distributed alignment cannot eliminate content height. Occupancy: details_item0_label_slot=18vp+margin(0vp), details_item0_value_slot=16vp+margin(0vp), gaps=2vp.",
          "expected": {
            "maximumHeight": 30.0,
            "heightTolerance": 2.0,
            "preserveFixedDesignSizes": true,
            "preserveRequiredTextAndActions": true,
            "overflowConstraint": "不能依靠权重、裁剪、flex shrink 或分布式对齐消除内容高度超限。"
          },
          "actual": {
            "minimumRequiredHeight": 36.0,
            "overflow": 6.0,
            "occupancy": "details_item0_label_slot=18vp+margin(0vp), details_item0_value_slot=16vp+margin(0vp), gaps=2vp"
          },
          "evidenceSource": "expanded",
          "fixHint": "根据占用明细重新组合完整信息或选择合法布局，保留必要事实、动作、字号和固定设计高度；不能靠裁剪、收缩或调整权重消除负预算。"
        }
      ]
    },
    {
      "stage": "validation",
      "code": "COMPACT_DSL_VALIDATION_FAILED",
      "message": "component details_item1: vertical layout requires at least 36vp within 30vp; it overflows by 6vp. Regroup facts or choose a layout with enough body space; preserve required text, actions, font sizes and fixed design heights. Weight, clipping, flex shrink and distributed alignment cannot eliminate content height. Occupancy: details_item1_label_slot=18vp+margin(0vp), details_item1_value_slot=16vp+margin(0vp), gaps=2vp.",
      "compactDiagnostics": [
        {
          "code": "COMPACT_LAYOUT_HEIGHT_OVERFLOW",
          "validationClass": "semantic",
          "category": "layout",
          "severity": "error",
          "message": "component details_item1: vertical layout requires at least 36vp within 30vp; it overflows by 6vp. Occupancy: details_item1_label_slot=18vp+margin(0vp), details_item1_value_slot=16vp+margin(0vp), gaps=2vp.",
          "legacyMessage": "component details_item1: vertical layout requires at least 36vp within 30vp; it overflows by 6vp. Regroup facts or choose a layout with enough body space; preserve required text, actions, font sizes and fixed design heights. Weight, clipping, flex shrink and distributed alignment cannot eliminate content height. Occupancy: details_item1_label_slot=18vp+margin(0vp), details_item1_value_slot=16vp+margin(0vp), gaps=2vp.",
          "expected": {
            "maximumHeight": 30.0,
            "heightTolerance": 2.0,
            "preserveFixedDesignSizes": true,
            "preserveRequiredTextAndActions": true,
            "overflowConstraint": "不能依靠权重、裁剪、flex shrink 或分布式对齐消除内容高度超限。"
          },
          "actual": {
            "minimumRequiredHeight": 36.0,
            "overflow": 6.0,
            "occupancy": "details_item1_label_slot=18vp+margin(0vp), details_item1_value_slot=16vp+margin(0vp), gaps=2vp"
          },
          "evidenceSource": "expanded",
          "fixHint": "根据占用明细重新组合完整信息或选择合法布局，保留必要事实、动作、字号和固定设计高度；不能靠裁剪、收缩或调整权重消除负预算。"
        }
      ]
    },
    {
      "stage": "validation",
      "code": "COMPACT_DSL_VALIDATION_FAILED",
      "message": "component details_item2: vertical layout requires at least 36vp within 30vp; it overflows by 6vp. Regroup facts or choose a layout with enough body space; preserve required text, actions, font sizes and fixed design heights. Weight, clipping, flex shrink and distributed alignment cannot eliminate content height. Occupancy: details_item2_label_slot=18vp+margin(0vp), details_item2_value_slot=16vp+margin(0vp), gaps=2vp.",
      "compactDiagnostics": [
        {
          "code": "COMPACT_LAYOUT_HEIGHT_OVERFLOW",
          "validationClass": "semantic",
          "category": "layout",
          "severity": "error",
          "message": "component details_item2: vertical layout requires at least 36vp within 30vp; it overflows by 6vp. Occupancy: details_item2_label_slot=18vp+margin(0vp), details_item2_value_slot=16vp+margin(0vp), gaps=2vp.",
          "legacyMessage": "component details_item2: vertical layout requires at least 36vp within 30vp; it overflows by 6vp. Regroup facts or choose a layout with enough body space; preserve required text, actions, font sizes and fixed design heights. Weight, clipping, flex shrink and distributed alignment cannot eliminate content height. Occupancy: details_item2_label_slot=18vp+margin(0vp), details_item2_value_slot=16vp+margin(0vp), gaps=2vp.",
          "expected": {
            "maximumHeight": 30.0,
            "heightTolerance": 2.0,
            "preserveFixedDesignSizes": true,
            "preserveRequiredTextAndActions": true,
            "overflowConstraint": "不能依靠权重、裁剪、flex shrink 或分布式对齐消除内容高度超限。"
          },
          "actual": {
            "minimumRequiredHeight": 36.0,
            "overflow": 6.0,
            "occupancy": "details_item2_label_slot=18vp+margin(0vp), details_item2_value_slot=16vp+margin(0vp), gaps=2vp"
          },
          "evidenceSource": "expanded",
          "fixHint": "根据占用明细重新组合完整信息或选择合法布局，保留必要事实、动作、字号和固定设计高度；不能靠裁剪、收缩或调整权重消除负预算。"
        }
      ]
    }
  ]
}
```
```repair-2
{
  "modelGeneratedCompactDsl": "[\"root\",\"Layout\",{\"layout\":\"W-top-bottom\",\"variant\":\"continuous\"},[\"title\",\"primary\",\"details\"]]\n[\"title\",\"SingleLineTitle\",{\"title\":\"河间天气\",\"fontSize\":12}]\n[\"primary\",\"EmphasisText\",{\"mainText\":{\"path\":\"/data/weather/current/temperatureText\"},\"secondaryText\":{\"path\":\"/data/weather/current/condition\"},\"fontSize\":18}]\n[\"details\",\"TextBlock\",{\"items\":[{\"label\":{\"path\":\"/data/time/currentDate\"},\"value\":{\"path\":\"/data/time/dayOfWeek\"}},{\"label\":{\"path\":\"/data/weather/current/alertLevel\"},\"value\":{\"path\":\"/data/weather/daily/0/temperatureRangeText\"}},{\"label\":{\"path\":\"/data/weather/daily/1/weekday\"},\"value\":{\"path\":\"/data/weather/daily/2/temperatureRangeText\"}}]}]\n[\"/data/time/currentDate\",\"示例\"]\n[\"/data/time/dayOfWeek\",\"示例\"]\n[\"/data/weather/current/temperatureText\",\"29℃\"]\n[\"/data/weather/current/condition\",\"多云\"]\n[\"/data/weather/current/alertLevel\",\"大风蓝色预警\"]\n[\"/data/weather/daily/0/weekday\",\"星期四\"]\n[\"/data/weather/daily/0/condition\",\"多云\"]\n[\"/data/weather/daily/0/temperatureRangeText\",\"25℃ / 32℃\"]\n[\"/data/weather/daily/1/weekday\",\"星期四\"]\n[\"/data/weather/daily/1/condition\",\"多云\"]\n[\"/data/weather/daily/1/temperatureRangeText\",\"25℃ / 32℃\"]\n[\"/data/weather/daily/2/weekday\",\"星期四\"]\n[\"/data/weather/daily/2/condition\",\"多云\"]\n[\"/data/weather/daily/2/temperatureRangeText\",\"25℃ / 32℃\"]\n[\"/data/weather/location/cityCode\",\"60814\"]",
  "generatedDsl": "{\"version\":\"v0.9\",\"createSurface\":{\"surfaceId\":\"surface_card\",\"catalogId\":\"ohos.a2ui.extended.catalog.form\"}}\n{\"version\":\"v0.9\",\"updateComponents\":{\"surfaceId\":\"surface_card\",\"root\":\"root\",\"components\":[{\"id\":\"root\",\"component\":\"Column\",\"children\":[\"title\",\"__layout__root__body\"],\"itemMargin\":6,\"styles\":{\"width\":\"matchParent\",\"height\":\"matchParent\",\"padding\":12,\"borderRadius\":20,\"clip\":true,\"alignItems\":\"start\",\"justifyContent\":\"start\"}},{\"id\":\"title\",\"component\":\"Row\",\"children\":[\"title_title\"],\"styles\":{\"width\":\"matchParent\",\"height\":12,\"flexShrink\":0,\"justifyContent\":\"start\",\"alignItems\":\"center\"},\"itemMargin\":0},{\"id\":\"title_title\",\"component\":\"Text\",\"content\":\"河间天气\",\"styles\":{\"fontSize\":12,\"fontWeight\":400,\"lineHeight\":1,\"textAlign\":\"start\",\"maxLines\":1,\"flexShrink\":0,\"width\":\"matchParent\",\"fontColor\":\"@theme:secondary/1\"}},{\"id\":\"__layout__root__body\",\"component\":\"Column\",\"children\":[\"__layout__root__primary\",\"__layout__root__details\"],\"itemMargin\":8,\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"layoutWeight\":1}},{\"id\":\"__layout__root__primary\",\"component\":\"Column\",\"children\":[\"primary\"],\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"primary\",\"component\":\"Column\",\"children\":[\"primary_main\",\"primary_secondary\"],\"itemMargin\":2,\"styles\":{\"alignItems\":\"start\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"width\":\"matchParent\"}},{\"id\":\"primary_main\",\"component\":\"Text\",\"content\":\"{{ ${/data/weather/current/temperatureText} }}\",\"styles\":{\"height\":18,\"fontSize\":18,\"fontWeight\":700,\"lineHeight\":1,\"maxLines\":1,\"flexShrink\":1,\"width\":\"matchParent\",\"fontColor\":\"@theme:primary/1\",\"textOverflow\":\"clip\"}},{\"id\":\"primary_secondary\",\"component\":\"Text\",\"content\":\"{{ ${/data/weather/current/condition} }}\",\"styles\":{\"height\":16,\"fontSize\":12,\"fontWeight\":400,\"lineHeight\":1.3333333333333333,\"maxLines\":1,\"flexShrink\":1,\"width\":\"matchParent\",\"fontColor\":\"@theme:primary/1\",\"textOverflow\":\"clip\"}},{\"id\":\"__layout__root__details\",\"component\":\"Column\",\"children\":[\"details\"],\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"layoutWeight\":1},\"itemMargin\":0},{\"id\":\"details\",\"component\":\"Row\",\"children\":[\"details_item0\",\"details_item1\",\"details_item2\"],\"itemMargin\":8,\"styles\":{\"width\":\"matchParent\",\"height\":\"matchParent\",\"alignItems\":\"top\",\"justifyContent\":\"start\",\"layoutWeight\":1,\"flexShrink\":1,\"constraintSize\":{\"minHeight\":48}}},{\"id\":\"details_item0\",\"component\":\"Column\",\"children\":[\"details_item0_label_slot\",\"details_item0_value_slot\"],\"itemMargin\":2,\"styles\":{\"height\":\"matchParent\",\"backgroundColor\":\"@theme:panel/1\",\"padding\":{\"left\":8,\"right\":8},\"borderRadius\":16,\"alignItems\":\"start\",\"justifyContent\":\"center\",\"layoutWeight\":1,\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0,\"minHeight\":0}}},{\"id\":\"details_item0_label_slot\",\"component\":\"Row\",\"children\":[\"details_item0_label\"],\"styles\":{\"width\":\"matchParent\",\"height\":18,\"alignItems\":\"center\",\"justifyContent\":\"start\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"details_item0_label\",\"component\":\"Text\",\"content\":\"{{ ${/data/time/currentDate} }}\",\"styles\":{\"width\":\"matchParent\",\"fontSize\":12,\"fontWeight\":700,\"textAlign\":\"start\",\"maxLines\":1,\"textOverflow\":\"ellipsis\",\"fontColor\":\"@theme:primary/0.6\"}},{\"id\":\"details_item0_value_slot\",\"component\":\"Row\",\"children\":[\"details_item0_value\"],\"styles\":{\"width\":\"matchParent\",\"height\":16,\"alignItems\":\"center\",\"justifyContent\":\"start\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"details_item0_value\",\"component\":\"Text\",\"content\":\"{{ ${/data/time/dayOfWeek} }}\",\"styles\":{\"width\":\"matchParent\",\"fontSize\":10,\"fontWeight\":500,\"textAlign\":\"start\",\"maxLines\":1,\"textOverflow\":\"ellipsis\",\"fontColor\":\"@theme:primary/1\"}},{\"id\":\"details_item1\",\"component\":\"Column\",\"children\":[\"details_item1_label_slot\",\"details_item1_value_slot\"],\"itemMargin\":2,\"styles\":{\"height\":\"matchParent\",\"backgroundColor\":\"@theme:panel/1\",\"padding\":{\"left\":8,\"right\":8},\"borderRadius\":16,\"alignItems\":\"start\",\"justifyContent\":\"center\",\"layoutWeight\":1,\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0,\"minHeight\":0}}},{\"id\":\"details_item1_label_slot\",\"component\":\"Row\",\"children\":[\"details_item1_label\"],\"styles\":{\"width\":\"matchParent\",\"height\":18,\"alignItems\":\"center\",\"justifyContent\":\"start\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"details_item1_label\",\"component\":\"Text\",\"content\":\"{{ ${/data/weather/current/alertLevel} }}\",\"styles\":{\"width\":\"matchParent\",\"fontSize\":12,\"fontWeight\":700,\"textAlign\":\"start\",\"maxLines\":1,\"textOverflow\":\"ellipsis\",\"fontColor\":\"@theme:primary/0.6\"}},{\"id\":\"details_item1_value_slot\",\"component\":\"Row\",\"children\":[\"details_item1_value\"],\"styles\":{\"width\":\"matchParent\",\"height\":16,\"alignItems\":\"center\",\"justifyContent\":\"start\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"details_item1_value\",\"component\":\"Text\",\"content\":\"{{ ${/data/weather/daily/0/temperatureRangeText} }}\",\"styles\":{\"width\":\"matchParent\",\"fontSize\":10,\"fontWeight\":500,\"textAlign\":\"start\",\"maxLines\":1,\"textOverflow\":\"ellipsis\",\"fontColor\":\"@theme:primary/1\"}},{\"id\":\"details_item2\",\"component\":\"Column\",\"children\":[\"details_item2_label_slot\",\"details_item2_value_slot\"],\"itemMargin\":2,\"styles\":{\"height\":\"matchParent\",\"backgroundColor\":\"@theme:panel/1\",\"padding\":{\"left\":8,\"right\":8},\"borderRadius\":16,\"alignItems\":\"start\",\"justifyContent\":\"center\",\"layoutWeight\":1,\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0,\"minHeight\":0}}},{\"id\":\"details_item2_label_slot\",\"component\":\"Row\",\"children\":[\"details_item2_label\"],\"styles\":{\"width\":\"matchParent\",\"height\":18,\"alignItems\":\"center\",\"justifyContent\":\"start\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"details_item2_label\",\"component\":\"Text\",\"content\":\"{{ ${/data/weather/daily/1/weekday} }}\",\"styles\":{\"width\":\"matchParent\",\"fontSize\":12,\"fontWeight\":700,\"textAlign\":\"start\",\"maxLines\":1,\"textOverflow\":\"ellipsis\",\"fontColor\":\"@theme:primary/0.6\"}},{\"id\":\"details_item2_value_slot\",\"component\":\"Row\",\"children\":[\"details_item2_value\"],\"styles\":{\"width\":\"matchParent\",\"height\":16,\"alignItems\":\"center\",\"justifyContent\":\"start\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"details_item2_value\",\"component\":\"Text\",\"content\":\"{{ ${/data/weather/daily/2/temperatureRangeText} }}\",\"styles\":{\"width\":\"matchParent\",\"fontSize\":10,\"fontWeight\":500,\"textAlign\":\"start\",\"maxLines\":1,\"textOverflow\":\"ellipsis\",\"fontColor\":\"@theme:primary/1\"}}]}}\n{\"version\":\"v0.9\",\"updateDataModel\":{\"surfaceId\":\"surface_card\",\"path\":\"/\",\"value\":{\"data\":{\"time\":{\"currentDate\":\"示例\",\"dayOfWeek\":\"示例\"},\"weather\":{\"current\":{\"temperatureText\":\"29℃\",\"condition\":\"多云\",\"alertLevel\":\"大风蓝色预警\"},\"daily\":[{\"weekday\":\"星期四\",\"condition\":\"多云\",\"temperatureRangeText\":\"25℃ / 32℃\"},{\"weekday\":\"星期四\",\"condition\":\"多云\",\"temperatureRangeText\":\"25℃ / 32℃\"},{\"weekday\":\"星期四\",\"condition\":\"多云\",\"temperatureRangeText\":\"25℃ / 32℃\"}],\"location\":{\"cityCode\":\"60814\"}}}}}}",
  "validationErrors": []
}
```
