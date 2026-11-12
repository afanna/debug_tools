```cardspec
{
  "title": "今日天气",
  "description": "天气速览",
  "suggestSize": "2x2",
  "imageDomainWhitelist": [
    "hag-ability-test.obs.cn-north-1.myhuaweicloud.com",
    "lfcontentcenterdev.hwcloudtest.cn",
    "hagres-drcn.dbankcdn.com"
  ],
  "dataBindings": [
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
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Column","children":["first","second"],"itemMargin":8,"styles":{"width":"matchParent","height":"matchParent","borderRadius":20,"clip":true,"alignItems":"start","justifyContent":"start","padding":8,"linearGradient":{"direction":"RightBottom","colors":[["#FFCBDDFE",0],["#FFF1F6FE",1]]}}},{"id":"first","component":"Column","children":["first_text"],"itemMargin":0,"styles":{"padding":{"left":8,"right":8},"borderRadius":16,"alignItems":"start","justifyContent":"center","clip":true,"flexShrink":0,"width":"matchParent","height":63,"backgroundColor":"#CCFFFFFF","layoutWeight":1}},{"id":"first_text","component":"Column","children":["first_primary","first_secondary"],"itemMargin":0,"styles":{"alignItems":"start","justifyContent":"center","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent"}},{"id":"first_primary","component":"Text","content":"{{ ${/data/weather/current/temperatureText} }}","styles":{"height":22,"fontSize":16,"fontWeight":700,"maxLines":1,"flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent","fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"first_secondary","component":"Text","content":"当前温度","styles":{"height":16,"fontSize":12,"fontWeight":500,"maxLines":1,"textOverflow":"ellipsis","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent","fontColor":"#991F4799"}},{"id":"second","component":"Column","children":["second_text"],"itemMargin":0,"styles":{"padding":{"left":8,"right":8},"borderRadius":16,"alignItems":"start","justifyContent":"center","clip":true,"flexShrink":0,"width":"matchParent","height":63,"backgroundColor":"#CCFFFFFF","layoutWeight":1}},{"id":"second_text","component":"Column","children":["second_primary","second_secondary"],"itemMargin":0,"styles":{"alignItems":"start","justifyContent":"center","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent"}},{"id":"second_primary","component":"Text","content":"{{ ${/data/weather/current/condition} }}","styles":{"height":22,"fontSize":16,"fontWeight":700,"maxLines":1,"flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent","fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"second_secondary","component":"Text","content":"天气现象","styles":{"height":16,"fontSize":12,"fontWeight":500,"maxLines":1,"textOverflow":"ellipsis","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent","fontColor":"#991F4799"}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"weather":{"current":{"temperatureText":"29℃","condition":"多云"}}}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "做一张今日天气卡片，显示当前温度和天气现象。",
  "size": "2x2",
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
      "capabilityId": "ViewWeather",
      "arguments": {
        "forecastDays": 1
      },
      "writeResultTo": "/data/weather",
      "candidateOutputFields": [
        "/current/temperatureText",
        "/current/condition"
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
  "artifactId": "34c1da3b-3f14-4f36-9918-4bc556a7e3e4",
  "createdAt": 1793951200575
}
```
```designcompactdsl
["root","Layout",{"layout":"S-dual-info"},["first","second"]]
["first","InfoBlock",{"surfaceRole":"panel","primaryText":{"path":"/data/weather/current/temperatureText"},"secondaryText":"当前温度"}]
["second","InfoBlock",{"surfaceRole":"panel","primaryText":{"path":"/data/weather/current/condition"},"secondaryText":"天气现象"}]
["/data/weather/current/temperatureText","29℃"]
["/data/weather/current/condition","多云"]
```
```request
{
  "content": {
    "size": "2x2",
    "functionName": "generateWidgetCardCompactDsl",
    "romVersion": "CMS-AL20 7.0.0.111",
    "candidateAssetIds": [],
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
    "bundleName": "com.huawei.genui",
    "description": "天气速览",
    "userQuery": "做一张今日天气卡片，显示当前温度和天气现象。",
    "title": "今日天气",
    "candidateDataBindings": [
      {
        "capabilityId": "ViewWeather",
        "arguments": {
          "forecastDays": 1
        },
        "writeResultTo": "/data/weather",
        "candidateOutputFields": [
          "/current/temperatureText",
          "/current/condition"
        ]
      }
    ]
  },
  "deviceInfo": {
    "countryCode": "CN",
    "deviceFormation": "HDSpeaker",
    "deviceType": 0,
    "locale": "zh-CN",
    "phoneType": "CMS-AL20",
    "prdVer": "11.7.8.342",
    "sysVer": "EmotionUI_9.0.0",
    "time": "20261103032900481"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q416-000",
    "isNew": true,
    "sessionId": "batch-19bdad45"
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
  "romVersion": "CMS-AL20 7.0.0.111",
  "candidateAssetIds": [],
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
  "bundleName": "com.huawei.genui",
  "description": "天气速览",
  "userQuery": "做一张今日天气卡片，显示当前温度和天气现象。",
  "title": "今日天气",
  "candidateDataBindings": [
    {
      "capabilityId": "ViewWeather",
      "arguments": {
        "forecastDays": 1
      },
      "writeResultTo": "/data/weather",
      "candidateOutputFields": [
        "/current/temperatureText",
        "/current/condition"
      ]
    }
  ]
}
```
