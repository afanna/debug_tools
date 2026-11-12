```cardspec
{
  "title": "时间天气",
  "description": "展示当前时间和北京天气的小组件",
  "suggestSize": "2x2",
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
      "capabilityId": "ViewWeather",
      "arguments": {},
      "writeResultTo": "/data/weather"
    }
  ]
}
```
```genui
{"version":"v0.9","createSurface":{"surfaceId":"surface_card","catalogId":"ohos.a2ui.extended.catalog.form"}}
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Column","children":["title","__layout__root__body"],"itemMargin":6,"styles":{"width":"matchParent","height":"matchParent","borderRadius":20,"clip":true,"alignItems":"start","justifyContent":"start","padding":12,"linearGradient":{"direction":"RightBottom","colors":[["#FFCBDDFE",0],["#FFF1F6FE",1]]}}},{"id":"title","component":"Row","children":["title_title"],"styles":{"width":"matchParent","height":12,"flexShrink":0,"justifyContent":"start","alignItems":"center"},"itemMargin":0},{"id":"title_title","component":"Text","content":"北京天气","styles":{"fontSize":12,"fontWeight":400,"lineHeight":1,"textAlign":"start","maxLines":1,"flexShrink":0,"width":"matchParent","fontColor":"#991F4799"}},{"id":"__layout__root__body","component":"Column","children":["__layout__root__primary","__layout__root__support"],"itemMargin":8,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1}},{"id":"__layout__root__primary","component":"Column","children":["temperature"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1,"flexShrink":0},"itemMargin":0},{"id":"temperature","component":"Row","children":["temperature_value"],"itemMargin":0,"styles":{"justifyContent":"start","alignItems":"bottom","flexShrink":0,"width":"matchParent"}},{"id":"temperature_value","component":"Text","content":"{{ ${/data/weather/current/temperatureText} }}","styles":{"height":30,"fontSize":30,"fontWeight":700,"lineHeight":1,"maxLines":1,"flexShrink":0,"fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"__layout__root__support","component":"Column","children":["details"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"details","component":"Column","children":["details_row0","details_row1","details_row2","details_row3"],"itemMargin":2,"styles":{"width":"matchParent","alignItems":"start","flexShrink":1}},{"id":"details_item0_label","component":"Text","content":"天气","styles":{"height":12,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":0,"lineHeight":1,"fontColor":"#991F4799","textOverflow":"clip"}},{"id":"details_item0_value","component":"Text","content":"{{ ${/data/weather/current/condition} }}","styles":{"height":12.0,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":1,"lineHeight":1,"fontColor":"#FF1F4799","layoutWeight":1,"textOverflow":"clip"}},{"id":"details_item0","component":"Row","children":["details_item0_label","details_item0_value"],"itemMargin":4,"styles":{"height":12.0,"alignItems":"top","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"details_row0","component":"Row","children":["details_item0"],"itemMargin":0,"styles":{"width":"matchParent","height":12.0,"alignItems":"top","flexShrink":0}},{"id":"details_item1_label","component":"Text","content":"日期","styles":{"height":12,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":0,"lineHeight":1,"fontColor":"#991F4799","textOverflow":"clip"}},{"id":"details_item1_value","component":"Text","content":"{{ ${/data/currentTime/currentDate} }}","styles":{"height":12.0,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":1,"lineHeight":1,"fontColor":"#FF1F4799","layoutWeight":1,"textOverflow":"clip"}},{"id":"details_item1","component":"Row","children":["details_item1_label","details_item1_value"],"itemMargin":4,"styles":{"height":12.0,"alignItems":"top","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"details_row1","component":"Row","children":["details_item1"],"itemMargin":0,"styles":{"width":"matchParent","height":12.0,"alignItems":"top","flexShrink":0}},{"id":"details_item2_label","component":"Text","content":"星期","styles":{"height":12,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":0,"lineHeight":1,"fontColor":"#991F4799","textOverflow":"clip"}},{"id":"details_item2_value","component":"Text","content":"{{ ${/data/currentTime/dayOfWeek} }}","styles":{"height":12.0,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":1,"lineHeight":1,"fontColor":"#FF1F4799","layoutWeight":1,"textOverflow":"clip"}},{"id":"details_item2","component":"Row","children":["details_item2_label","details_item2_value"],"itemMargin":4,"styles":{"height":12.0,"alignItems":"top","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"details_row2","component":"Row","children":["details_item2"],"itemMargin":0,"styles":{"width":"matchParent","height":12.0,"alignItems":"top","flexShrink":0}},{"id":"details_item3_label","component":"Text","content":"农历","styles":{"height":12,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":0,"lineHeight":1,"fontColor":"#991F4799","textOverflow":"clip"}},{"id":"details_item3_value","component":"Text","content":"{{ ${/data/currentTime/lunarDate} }}","styles":{"height":12.0,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":1,"lineHeight":1,"fontColor":"#FF1F4799","layoutWeight":1,"textOverflow":"clip"}},{"id":"details_item3","component":"Row","children":["details_item3_label","details_item3_value"],"itemMargin":4,"styles":{"height":12.0,"alignItems":"top","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"details_row3","component":"Row","children":["details_item3"],"itemMargin":0,"styles":{"width":"matchParent","height":12.0,"alignItems":"top","flexShrink":0}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"weather":{"current":{"temperatureText":"29℃","condition":"多云"}},"currentTime":{"currentDate":"示例","dayOfWeek":"示例","lunarDate":"示例"}}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "添加小组件，展示当前时间和北京天气。\n本轮卡片静态内容（用作展示的外部事实）：\n- 当前时间、日期、星期及农历信息\n- 北京市朝阳区当前天气及未来天气预报",
  "size": "2x2",
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
    }
  ],
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
        },
        "lunarDate": {
          "type": "string",
          "description": "格式化的中国传统农历日期，例如 '五月廿六'。若系统获取失败则可能为空字符串。",
          "sampleValue": "示例"
        }
      },
      "weather": {
        "current": {
          "condition": {
            "type": "string",
            "description": "当前天气现象，例如“阴”“多云”“小雨”。",
            "sampleValue": "多云"
          },
          "temperatureText": {
            "type": "string",
            "description": "可直接显示的当前温度文本，已包含“℃”单位；展示时不得再次追加温度单位。例如“29℃”。",
            "sampleValue": "29℃"
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
      "writeResultTo": "/data/currentTime",
      "candidateOutputFields": [
        "/currentDate",
        "/dayOfWeek",
        "/lunarDate"
      ]
    },
    {
      "capabilityId": "ViewWeather",
      "arguments": {},
      "writeResultTo": "/data/weather",
      "candidateOutputFields": [
        "/current/condition",
        "/current/temperatureText",
        "/location/cityCode"
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
  "artifactId": "09e115a8-0aca-41dc-8830-80341818e34c",
  "createdAt": 1793933875604
}
```
```designcompactdsl
["root","Layout",{"layout":"S-title-dual-content"},["title","temperature","details"]]
["title","SingleLineTitle",{"title":"北京天气","fontSize":12}]
["temperature","EmphasizedData",{"value":{"path":"/data/weather/current/temperatureText"},"fontSize":30}]
["details","SecondaryBody",{"items":[{"label":"天气","value":{"path":"/data/weather/current/condition"}},{"label":"日期","value":{"path":"/data/currentTime/currentDate"}},{"label":"星期","value":{"path":"/data/currentTime/dayOfWeek"}},{"label":"农历","value":{"path":"/data/currentTime/lunarDate"}}],"columns":1,"fontSize":12}]
["/data/weather/current/temperatureText","29℃"]
["/data/weather/current/condition","多云"]
["/data/currentTime/currentDate","示例"]
["/data/currentTime/dayOfWeek","示例"]
["/data/currentTime/lunarDate","示例"]
```
```request
{
  "content": {
    "title": "时间天气",
    "description": "展示当前时间和北京天气的小组件",
    "userQuery": "添加小组件，展示当前时间和北京天气。\n本轮卡片静态内容（用作展示的外部事实）：\n- 当前时间、日期、星期及农历信息\n- 北京市朝阳区当前天气及未来天气预报",
    "size": "2x2",
    "bundleName": "com.huawei.genui",
    "functionName": "generateWidgetCardCompactDsl",
    "romVersion": "CMM-AL10P 7.0.0.111",
    "candidateDataBindings": [
      {
        "capabilityId": "GetCurrentTime",
        "writeResultTo": "/data/currentTime",
        "candidateOutputFields": [
          "/currentDate",
          "/dayOfWeek",
          "/lunarDate"
        ]
      },
      {
        "capabilityId": "ViewWeather",
        "writeResultTo": "/data/weather",
        "candidateOutputFields": [
          "/current/condition",
          "/current/temperatureText",
          "/location/cityCode"
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
    "prdVer": "11.7.8.342",
    "sysVer": "EmotionUI_9.0.0",
    "time": "20261026035501595"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q271-000",
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
  "previewSize": "2x2",
  "assetCandidateIds": [],
  "functionName": "generateWidgetCardCompactDsl",
  "romVersion": "CMM-AL10P 7.0.0.111",
  "eventCapabilityIds": [
    "event.open.weather"
  ],
  "bundleName": "com.huawei.genui",
  "description": "展示当前时间和北京天气的小组件",
  "userQuery": "添加小组件，展示当前时间和北京天气。\n本轮卡片静态内容（用作展示的外部事实）：\n- 当前时间、日期、星期及农历信息\n- 北京市朝阳区当前天气及未来天气预报",
  "title": "时间天气",
  "dataCapabilityIds": [
    "GetCurrentTime",
    "ViewWeather"
  ]
}
```
