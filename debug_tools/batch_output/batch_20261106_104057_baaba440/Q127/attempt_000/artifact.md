```cardspec
{
  "title": "杭州西湖区天气",
  "description": "查看杭州市西湖区当前天气，点击查看杭州天气详情",
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
        "districtName": "西湖区",
        "forecastDays": 1,
        "prefectureName": "杭州市"
      },
      "writeResultTo": "/data/weather"
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
  "userQuery": "帮我做个卡片，看杭州市西湖区现在是什么天气，点一下查看杭州天气详情。",
  "size": "2x4",
  "appVersion": "11.9.9.300",
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
      "weather": {
        "location": {
          "cityCode": {
            "type": "string",
            "description": "城市代码，如60814代表青浦区",
            "sampleValue": "60814"
          },
          "districtName": {
            "type": "string",
            "description": "区或县名称",
            "sampleValue": "青浦区"
          },
          "prefectureName": {
            "type": "string",
            "description": "城市名称",
            "sampleValue": "上海市"
          }
        },
        "current": {
          "temperatureC": {
            "type": "number",
            "description": "当前温度的纯数值，单位为摄氏度，返回值不包含单位。若直接用于文本展示，必须在数值后追加“℃”；优先使用 temperatureText。",
            "sampleValue": 29
          },
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
          "feelsLikeC": {
            "type": "number",
            "description": "当前体感温度的纯数值，单位为摄氏度，返回值不包含单位。若直接用于文本展示，必须在数值后追加“℃”。",
            "sampleValue": 31
          },
          "humidityPercent": {
            "type": "number",
            "description": "当前相对湿度的纯数值百分比，取值范围为 0 到 100，返回值不包含“%”。若直接用于文本展示，必须在数值后追加“%”。",
            "sampleValue": 68
          },
          "airQuality": {
            "type": "string",
            "description": "当前空气质量等级，例如“优”“良”。",
            "sampleValue": "良"
          },
          "windDirection": {
            "type": "string",
            "description": "当前风向。",
            "sampleValue": "东南风"
          },
          "windLevel": {
            "type": "integer",
            "description": "当前风力等级的纯整数，返回值不包含“级”。若直接用于文本展示，必须在数值后追加“级”。",
            "sampleValue": 2
          },
          "uvIndex": {
            "type": "string",
            "description": "当前紫外线等级，例如“弱”“中等”“强”。",
            "sampleValue": "中等"
          },
          "coldLevel": {
            "type": "string",
            "description": "感冒指数。",
            "sampleValue": "低"
          },
          "alertLevel": {
            "type": "string",
            "description": "预警信息。当前气象预警信息，例如'暴雨橙色预警'、'高温黄色预警'、'台风蓝色预警'。无预警时为空字符串。",
            "sampleValue": "大风蓝色预警"
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
            },
            "rainProbabilityPercent": {
              "type": "number",
              "description": "白天降雨概率的百分数数值，返回值不包含单位，例如 20 表示 20%；文本展示必须追加一个“%”，进度组件直接使用数值。",
              "sampleValue": 20
            },
            "airQuality": {
              "type": "string",
              "description": "当天空气质量等级。",
              "sampleValue": "良"
            },
            "uvIndex": {
              "type": "string",
              "description": "当天紫外线等级。",
              "sampleValue": "中等"
            },
            "coldLevel": {
              "type": "string",
              "description": "感冒指数。",
              "sampleValue": "低"
            }
          }
        ],
        "updatedAt": {
          "type": "string",
          "description": "端侧完成天气查询和归一化的时间。如：2026-06-14 15:30",
          "sampleValue": "2026-08-06 09:00"
        }
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
        "districtName": "西湖区",
        "forecastDays": 1,
        "prefectureName": "杭州市"
      },
      "writeResultTo": "/data/weather",
      "candidateOutputFields": []
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
  "artifactId": "eb68557d-ffce-48a4-8e54-27693b881b06",
  "createdAt": 1793932858446
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
    "title": "杭州西湖区天气",
    "description": "查看杭州市西湖区当前天气，点击查看杭州天气详情",
    "userQuery": "帮我做个卡片，看杭州市西湖区现在是什么天气，点一下查看杭州天气详情。",
    "size": "2x4",
    "bundleName": "com.huawei.genui",
    "functionName": "generateWidgetCardCompactDsl",
    "romVersion": "SGT-AL10 7.0.0.111",
    "candidateDataBindings": [
      {
        "capabilityId": "ViewWeather",
        "arguments": {
          "districtName": "西湖区",
          "forecastDays": 1,
          "prefectureName": "杭州市"
        },
        "writeResultTo": "/data/weather"
      }
    ],
    "candidateEventCandidates": [
      {
        "capabilityId": "event.open.weather",
        "action": {
          "args": {
            "abilityName": "",
            "bundleName": "",
            "intentName": "Weather_CityCode",
            "uri": "{{ 'hww://www.huawei.com/totemweather?enterType=share&cityCode=' + ${/data/weather/location/cityCode} }}"
          },
          "call": "clickToDeeplink"
        }
      }
    ],
    "candidateAssetIds": []
  },
  "deviceInfo": {
    "countryCode": "CN",
    "deviceFormation": "HDSpeaker",
    "deviceType": 0,
    "locale": "zh-CN",
    "phoneType": "SGT-AL10",
    "prdVer": "11.9.9.300",
    "sysVer": "EmotionUI_9.0.0",
    "time": "20261020114814782"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q127-000",
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
  "cardSize": "2x4",
  "dataCapabilities": [
    {
      "id": "ViewWeather",
      "inputParams": {
        "districtName": "西湖区",
        "forecastDays": 1,
        "prefectureName": "杭州市"
      }
    }
  ],
  "functionName": "generateWidgetCardCompactDsl",
  "romVersion": "SGT-AL10 7.0.0.111",
  "bundleName": "com.huawei.genui",
  "description": "查看杭州市西湖区当前天气，点击查看杭州天气详情",
  "userQuery": "帮我做个卡片，看杭州市西湖区现在是什么天气，点一下查看杭州天气详情。",
  "title": "杭州西湖区天气",
  "eventCapabilities": [
    {
      "actionTemplate": {
        "args": {
          "abilityName": "",
          "bundleName": "",
          "intentName": "Weather_CityCode",
          "uri": "{{ 'hww://www.huawei.com/totemweather?enterType=share&cityCode=' + ${/data/weather/location/cityCode} }}"
        },
        "call": "clickToDeeplink"
      },
      "id": "event.open.weather"
    }
  ]
}
```
