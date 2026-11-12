```cardspec
{
  "title": "今日天气",
  "description": "杭州天气速览",
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
        "districtName": "滨江区",
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
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Column","children":["content"],"styles":{"width":"matchParent","height":"matchParent","borderRadius":20,"clip":true,"alignItems":"center","justifyContent":"center","padding":12,"linearGradient":{"direction":"RightBottom","colors":[["#FFCBDDFE",0],["#FFF1F6FE",1]]}},"itemMargin":0},{"id":"content","component":"Column","children":["content_label","content_value_area","content_supporting"],"itemMargin":8,"styles":{"width":"matchParent","height":122,"alignItems":"center","justifyContent":"center","flexShrink":1}},{"id":"content_label","component":"Text","content":"杭州今日天气","styles":{"width":"matchParent","height":18,"fontSize":12,"fontWeight":500,"textAlign":"center","maxLines":1,"fontColor":"#991F4799","textOverflow":"clip"}},{"id":"content_value_area","component":"Column","children":["content_value"],"styles":{"width":"matchParent","height":60,"alignItems":"center","justifyContent":"center","flexShrink":0},"itemMargin":0},{"id":"content_value","component":"Text","content":"{{ ${/data/weather/current/temperatureText} }}","styles":{"fontSize":21,"fontWeight":700,"textAlign":"center","maxLines":2,"width":"matchParent","lineHeight":1.25,"fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"content_supporting","component":"Text","content":"{{ ${/data/weather/current/condition} }}","styles":{"height":20,"fontSize":14,"fontWeight":400,"textAlign":"center","maxLines":1,"width":"matchParent","margin":{"top":8,"right":0,"bottom":0,"left":0},"flexShrink":0,"fontColor":"#FF1F4799","textOverflow":"clip"}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"weather":{"current":{"temperatureText":"29℃","condition":"多云"}}}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "做一张杭州今日天气卡片，显示当前温度和天气现象。",
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
        "districtName": "滨江区",
        "forecastDays": 1,
        "prefectureName": "杭州市"
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
  "artifactId": "10194c5f-2163-4faa-95a7-02cd05ad31c5",
  "createdAt": 1793934625309
}
```
```designcompactdsl
["root","Layout",{"layout":"S-center"},["content"]]
["content","DataDisplay",{"label":"杭州今日天气","value":{"path":"/data/weather/current/temperatureText"},"supportingText":{"path":"/data/weather/current/condition"}}]
["/data/weather/current/temperatureText","29℃"]
["/data/weather/current/condition","多云"]
```
```request
{
  "content": {
    "bundleName": "com.huawei.genui",
    "userQuery": "做一张杭州今日天气卡片，显示当前温度和天气现象。",
    "candidateDataBindings": [
      {
        "capabilityId": "ViewWeather",
        "arguments": {
          "districtName": "滨江区",
          "forecastDays": 1,
          "prefectureName": "杭州市"
        },
        "writeResultTo": "/data/weather",
        "candidateOutputFields": [
          "/current/temperatureText",
          "/current/condition"
        ]
      }
    ],
    "title": "今日天气",
    "size": "2x2",
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
    "description": "杭州天气速览",
    "candidateAssetIds": []
  },
  "deviceInfo": {
    "countryCode": "CN",
    "deviceFormation": "HDSpeaker",
    "deviceType": 0,
    "locale": "zh-CN",
    "phoneType": "HLS-AL00",
    "prdVer": "11.7.8.342",
    "sysVer": "EmotionUI_9.0.0",
    "time": "20261031065043729"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q388-000",
    "isNew": true,
    "sessionId": "batch-7664fcb9"
  },
  "userAuth": {
    "user": {}
  },
  "utterance": {
    "original": "做一张杭州今日天气卡片，显示当前温度和天气现象。",
    "type": "text"
  },
  "version": "1.0",
  "functionName": "generateWidgetCardCompactDsl",
  "romVersion": "HLS-AL00 7.0.0.111",
  "bundleName": "com.huawei.genui",
  "userQuery": "做一张杭州今日天气卡片，显示当前温度和天气现象。",
  "candidateDataBindings": [
    {
      "capabilityId": "ViewWeather",
      "arguments": {
        "districtName": "滨江区",
        "forecastDays": 1,
        "prefectureName": "杭州市"
      },
      "writeResultTo": "/data/weather",
      "candidateOutputFields": [
        "/current/temperatureText",
        "/current/condition"
      ]
    }
  ],
  "title": "今日天气",
  "size": "2x2",
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
  "description": "杭州天气速览",
  "candidateAssetIds": []
}
```
