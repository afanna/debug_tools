```cardspec
{
  "title": "天气",
  "description": "天气卡片",
  "suggestSize": "2x2",
  "imageDomainWhitelist": [
    "hag-ability-test.obs.cn-north-1.myhuaweicloud.com",
    "lfcontentcenterdev.hwcloudtest.cn",
    "hagres-drcn.dbankcdn.com"
  ],
  "dataBindings": [
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
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Column","children":["title","__layout__root__body"],"itemMargin":6,"styles":{"width":"matchParent","height":"matchParent","borderRadius":20,"clip":true,"alignItems":"start","justifyContent":"start","padding":12,"linearGradient":{"direction":"RightBottom","colors":[["#FFCBDDFE",0],["#FFF1F6FE",1]]}}},{"id":"title","component":"Row","children":["title_title","title_icon"],"styles":{"width":"matchParent","height":20,"flexShrink":0,"justifyContent":"spaceBetween","alignItems":"center"},"itemMargin":0},{"id":"title_title","component":"Text","content":"{{ ${/data/weather/location/prefectureName} }}","styles":{"fontSize":12,"fontWeight":400,"lineHeight":1,"textAlign":"start","maxLines":1,"flexShrink":1,"width":"wrapContent","layoutWeight":1,"constraintSize":{"minWidth":0},"fontColor":"#991F4799"}},{"id":"title_icon","component":"Image","src":"resources/base/media/ic_weather_monochrome.svg","styles":{"width":20,"height":20,"objectFit":"contain","flexShrink":0,"fillColor":"#FF1F4799"}},{"id":"__layout__root__body","component":"Column","children":["__layout__root__primary","__layout__root__support"],"itemMargin":8,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1}},{"id":"__layout__root__primary","component":"Column","children":["current"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1,"flexShrink":0},"itemMargin":0},{"id":"current","component":"Column","children":["current_main","current_secondary"],"itemMargin":2,"styles":{"alignItems":"start","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent"}},{"id":"current_main","component":"Text","content":"{{ ${/data/weather/current/temperatureText} }}","styles":{"height":18,"fontSize":18,"fontWeight":700,"lineHeight":1,"maxLines":1,"flexShrink":1,"width":"matchParent","fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"current_secondary","component":"Text","content":"{{ ${/data/weather/current/condition} }}","styles":{"height":16,"fontSize":12,"fontWeight":400,"lineHeight":1.3333333333333333,"maxLines":1,"flexShrink":1,"width":"matchParent","fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"__layout__root__support","component":"Column","children":["forecast"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"forecast","component":"Column","children":["forecast_row0","forecast_row1"],"itemMargin":2,"styles":{"width":"matchParent","alignItems":"start","flexShrink":1}},{"id":"forecast_item0_value","component":"Text","content":"{{ ${/data/weather/daily/0/weekday} + ' ' + ${/data/weather/daily/0/condition} + ' ' + ${/data/weather/daily/0/temperatureRangeText} }}","styles":{"height":24.0,"fontSize":12,"fontWeight":400,"maxLines":2,"flexShrink":1,"lineHeight":1,"fontColor":"#FF1F4799","layoutWeight":1,"textOverflow":"clip"}},{"id":"forecast_item0","component":"Row","children":["forecast_item0_value"],"itemMargin":0,"styles":{"height":24.0,"alignItems":"top","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"forecast_row0","component":"Row","children":["forecast_item0"],"itemMargin":0,"styles":{"width":"matchParent","height":24.0,"alignItems":"top","flexShrink":0}},{"id":"forecast_item1_value","component":"Text","content":"{{ ${/data/weather/daily/1/weekday} + ' ' + ${/data/weather/daily/1/condition} + ' ' + ${/data/weather/daily/1/temperatureRangeText} }}","styles":{"height":24.0,"fontSize":12,"fontWeight":400,"maxLines":2,"flexShrink":1,"lineHeight":1,"fontColor":"#FF1F4799","layoutWeight":1,"textOverflow":"clip"}},{"id":"forecast_item1","component":"Row","children":["forecast_item1_value"],"itemMargin":0,"styles":{"height":24.0,"alignItems":"top","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"forecast_row1","component":"Row","children":["forecast_item1"],"itemMargin":0,"styles":{"width":"matchParent","height":24.0,"alignItems":"top","flexShrink":0}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"weather":{"location":{"prefectureName":"上海市"},"current":{"temperatureText":"29℃","condition":"多云"},"daily":[{"weekday":"星期四","condition":"多云","temperatureRangeText":"25℃ / 32℃"},{"weekday":"星期四","condition":"多云","temperatureRangeText":"25℃ / 32℃"}]}}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "在桌面添加一个天气小部件，展示当前天气和未来天气预报",
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
        },
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
          "humidityPercent": {
            "type": "number",
            "description": "当前相对湿度的纯数值百分比，取值范围为 0 到 100，返回值不包含“%”。若直接用于文本展示，必须在数值后追加“%”。",
            "sampleValue": 68
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
          }
        ]
      }
    }
  },
  "assetCandidates": [
    {
      "id": "asset.ic_weather_monochrome",
      "src": "resources/base/media/ic_weather_monochrome.svg",
      "description": "样式：黑色单色云朵图标，原始尺寸为 24×24，可随主题染成白色或黑色；选择：普通天气或天气详情需求的首选云朵图标。适用：天气卡片中配合 ViewWeather 的 current.condition 或 daily.condition 展示天气现象，也可与 event.open.weather 组成天气详情入口。图标仅表示天气主题，不代表晴、阴、雨等具体天气状态。"
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
    "asset.ic_weather_monochrome"
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
      "arguments": {},
      "writeResultTo": "/data/weather",
      "candidateOutputFields": [
        "/location/prefectureName",
        "/location/districtName",
        "/current/temperatureText",
        "/current/condition",
        "/current/humidityPercent",
        "/daily/0/weekday",
        "/daily/0/condition",
        "/daily/0/temperatureRangeText",
        "/daily/1/weekday",
        "/daily/1/condition",
        "/daily/1/temperatureRangeText"
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
  "candidateAssetIds": [
    "asset.ic_weather_monochrome"
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
  "artifactId": "f1616e94-d3cd-46d2-948b-ba13e09e5051",
  "createdAt": 1793934611855
}
```
```designcompactdsl
["root","Layout",{"layout":"S-title-dual-content"},["title","current","forecast"]]
["title","SingleLineTitle",{"title":{"path":"/data/weather/location/prefectureName"},"icon":"resources/base/media/ic_weather_monochrome.svg","fontSize":12}]
["current","EmphasisText",{"mainText":{"path":"/data/weather/current/temperatureText"},"secondaryText":{"path":"/data/weather/current/condition"},"fontSize":18}]
["forecast","SecondaryBody",{"items":[{"value":"{{ ${/data/weather/daily/0/weekday} + ' ' + ${/data/weather/daily/0/condition} + ' ' + ${/data/weather/daily/0/temperatureRangeText} }}"},{"value":"{{ ${/data/weather/daily/1/weekday} + ' ' + ${/data/weather/daily/1/condition} + ' ' + ${/data/weather/daily/1/temperatureRangeText} }}"}],"columns":1,"fontSize":12}]
["/data/weather/location/prefectureName","上海市"]
["/data/weather/current/temperatureText","29℃"]
["/data/weather/current/condition","多云"]
["/data/weather/daily/0/weekday","星期四"]
["/data/weather/daily/0/condition","多云"]
["/data/weather/daily/0/temperatureRangeText","25℃ / 32℃"]
["/data/weather/daily/1/weekday","星期四"]
["/data/weather/daily/1/condition","多云"]
["/data/weather/daily/1/temperatureRangeText","25℃ / 32℃"]
```
```request
{
  "content": {
    "bundleName": "com.huawei.genui",
    "userQuery": "在桌面添加一个天气小部件，展示当前天气和未来天气预报",
    "candidateDataBindings": [
      {
        "capabilityId": "ViewWeather",
        "arguments": {},
        "writeResultTo": "/data/weather",
        "candidateOutputFields": [
          "/location/prefectureName",
          "/location/districtName",
          "/current/temperatureText",
          "/current/condition",
          "/current/humidityPercent",
          "/daily/0/weekday",
          "/daily/0/condition",
          "/daily/0/temperatureRangeText",
          "/daily/1/weekday",
          "/daily/1/condition",
          "/daily/1/temperatureRangeText"
        ]
      }
    ],
    "title": "天气",
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
    "description": "天气卡片",
    "candidateAssetIds": [
      "asset.ic_weather_monochrome"
    ]
  },
  "deviceInfo": {
    "countryCode": "CN",
    "deviceFormation": "HDSpeaker",
    "deviceType": 0,
    "locale": "zh-CN",
    "phoneType": "HLS-AL00",
    "prdVer": "11.7.8.342",
    "sysVer": "EmotionUI_9.0.0",
    "time": "20261030231427755"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q371-000",
    "isNew": true,
    "sessionId": "batch-7664fcb9"
  },
  "userAuth": {
    "user": {}
  },
  "utterance": {
    "original": "在桌面添加一个天气小部件，展示当前天气和未来天气预报",
    "type": "text"
  },
  "version": "1.0",
  "functionName": "generateWidgetCardCompactDsl",
  "romVersion": "HLS-AL00 7.0.0.111",
  "bundleName": "com.huawei.genui",
  "userQuery": "在桌面添加一个天气小部件，展示当前天气和未来天气预报",
  "candidateDataBindings": [
    {
      "capabilityId": "ViewWeather",
      "arguments": {},
      "writeResultTo": "/data/weather",
      "candidateOutputFields": [
        "/location/prefectureName",
        "/location/districtName",
        "/current/temperatureText",
        "/current/condition",
        "/current/humidityPercent",
        "/daily/0/weekday",
        "/daily/0/condition",
        "/daily/0/temperatureRangeText",
        "/daily/1/weekday",
        "/daily/1/condition",
        "/daily/1/temperatureRangeText"
      ]
    }
  ],
  "title": "天气",
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
  "description": "天气卡片",
  "candidateAssetIds": [
    "asset.ic_weather_monochrome"
  ]
}
```
```repair-1
{
  "modelGeneratedCompactDsl": "[\"root\",\"Layout\",{\"layout\":\"S-title-dual-content\"},[\"title\",\"current\",\"forecast\"]]\n[\"title\",\"SingleLineTitle\",{\"title\":{\"path\":\"/data/weather/location/prefectureName\"},\"icon\":\"resources/base/media/ic_weather_monochrome.svg\",\"fontSize\":12}]\n[\"current\",\"EmphasisText\",{\"mainText\":{\"path\":\"/data/weather/current/temperatureText\"},\"secondaryText\":{\"path\":\"/data/weather/current/condition\"},\"fontSize\":18}]\n[\"forecast\",\"SecondaryBody\",{\"items\":[{\"value\":\"{{ ${/data/weather/daily/0/weekday} + ' ' + ${/data/weather/daily/0/condition} + ' ' + ${/data/weather/daily/0/temperatureRangeText} }}\"},{\"value\":\"{{ ${/data/weather/daily/1/weekday} + ' ' + ${/data/weather/daily/1/condition} + ' ' + ${/data/weather/daily/1/temperatureRangeText} }}\"}],\"columns\":1,\"fontSize\":12}]\n[\"/data/weather/location/prefectureName\",\"上海市\"]\n[\"/data/weather/current/temperatureText\",\"29℃\"]\n[\"/data/weather/current/condition\",\"多云\"]\n[\"/data/weather/daily/0/weekday\",\"星期四\"]\n[\"/data/weather/daily/0/condition\",\"多云\"]\n[\"/data/weather/daily/0/temperatureRangeText\",\"25℃ / 32℃\"]\n[\"/data/weather/daily/1/weekday\",\"星期四\"]\n[\"/data/weather/daily/1/condition\",\"多云\"]\n[\"/data/weather/daily/1/temperatureRangeText\",\"25℃ / 32℃\"]",
  "generatedDsl": "{\"version\":\"v0.9\",\"createSurface\":{\"surfaceId\":\"surface_card\",\"catalogId\":\"ohos.a2ui.extended.catalog.form\"}}\n{\"version\":\"v0.9\",\"updateComponents\":{\"surfaceId\":\"surface_card\",\"root\":\"root\",\"components\":[{\"id\":\"root\",\"component\":\"Column\",\"children\":[\"title\",\"__layout__root__body\"],\"itemMargin\":6,\"styles\":{\"width\":\"matchParent\",\"height\":\"matchParent\",\"borderRadius\":20,\"clip\":true,\"alignItems\":\"start\",\"justifyContent\":\"start\",\"padding\":12}},{\"id\":\"title\",\"component\":\"Row\",\"children\":[\"title_title\",\"title_icon\"],\"styles\":{\"width\":\"matchParent\",\"height\":20,\"flexShrink\":0,\"justifyContent\":\"spaceBetween\",\"alignItems\":\"center\"},\"itemMargin\":0},{\"id\":\"title_title\",\"component\":\"Text\",\"content\":\"{{ ${/data/weather/location/prefectureName} }}\",\"styles\":{\"fontSize\":12,\"fontWeight\":400,\"lineHeight\":1,\"textAlign\":\"start\",\"maxLines\":1,\"flexShrink\":1,\"width\":\"wrapContent\",\"layoutWeight\":1,\"constraintSize\":{\"minWidth\":0},\"fontColor\":\"@theme:secondary/1\"}},{\"id\":\"title_icon\",\"component\":\"Image\",\"src\":\"resources/base/media/ic_weather_monochrome.svg\",\"styles\":{\"width\":20,\"height\":20,\"objectFit\":\"contain\",\"flexShrink\":0,\"fillColor\":\"@theme:graphicPrimary/1\"}},{\"id\":\"__layout__root__body\",\"component\":\"Column\",\"children\":[\"__layout__root__primary\",\"__layout__root__support\"],\"itemMargin\":8,\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"layoutWeight\":1}},{\"id\":\"__layout__root__primary\",\"component\":\"Column\",\"children\":[\"current\"],\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"layoutWeight\":1,\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"current\",\"component\":\"Column\",\"children\":[\"current_main\",\"current_secondary\"],\"itemMargin\":2,\"styles\":{\"alignItems\":\"start\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"width\":\"matchParent\"}},{\"id\":\"current_main\",\"component\":\"Text\",\"content\":\"{{ ${/data/weather/current/temperatureText} }}\",\"styles\":{\"height\":18,\"fontSize\":18,\"fontWeight\":700,\"lineHeight\":1,\"maxLines\":1,\"flexShrink\":1,\"width\":\"matchParent\",\"fontColor\":\"@theme:primary/1\",\"textOverflow\":\"clip\"}},{\"id\":\"current_secondary\",\"component\":\"Text\",\"content\":\"{{ ${/data/weather/current/condition} }}\",\"styles\":{\"height\":16,\"fontSize\":12,\"fontWeight\":400,\"lineHeight\":1.3333333333333333,\"maxLines\":1,\"flexShrink\":1,\"width\":\"matchParent\",\"fontColor\":\"@theme:primary/1\",\"textOverflow\":\"clip\"}},{\"id\":\"__layout__root__support\",\"component\":\"Column\",\"children\":[\"forecast\"],\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"forecast\",\"component\":\"Column\",\"children\":[\"forecast_row0\",\"forecast_row1\"],\"itemMargin\":2,\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"flexShrink\":1}},{\"id\":\"forecast_item0_value\",\"component\":\"Text\",\"content\":\"{{ ${/data/weather/daily/0/weekday} + ' ' + ${/data/weather/daily/0/condition} + ' ' + ${/data/weather/daily/0/temperatureRangeText} }}\",\"styles\":{\"height\":24.0,\"fontSize\":12,\"fontWeight\":400,\"maxLines\":2,\"flexShrink\":1,\"lineHeight\":1,\"fontColor\":\"@theme:primary/1\",\"layoutWeight\":1,\"textOverflow\":\"clip\"}},{\"id\":\"forecast_item0\",\"component\":\"Row\",\"children\":[\"forecast_item0_value\"],\"itemMargin\":0,\"styles\":{\"height\":24.0,\"alignItems\":\"top\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"layoutWeight\":1}},{\"id\":\"forecast_row0\",\"component\":\"Row\",\"children\":[\"forecast_item0\"],\"itemMargin\":0,\"styles\":{\"width\":\"matchParent\",\"height\":24.0,\"alignItems\":\"top\",\"flexShrink\":0}},{\"id\":\"forecast_item1_value\",\"component\":\"Text\",\"content\":\"{{ ${/data/weather/daily/1/weekday} + ' ' + ${/data/weather/daily/1/condition} + ' ' + ${/data/weather/daily/1/temperatureRangeText} }}\",\"styles\":{\"height\":24.0,\"fontSize\":12,\"fontWeight\":400,\"maxLines\":2,\"flexShrink\":1,\"lineHeight\":1,\"fontColor\":\"@theme:primary/1\",\"layoutWeight\":1,\"textOverflow\":\"clip\"}},{\"id\":\"forecast_item1\",\"component\":\"Row\",\"children\":[\"forecast_item1_value\"],\"itemMargin\":0,\"styles\":{\"height\":24.0,\"alignItems\":\"top\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"layoutWeight\":1}},{\"id\":\"forecast_row1\",\"component\":\"Row\",\"children\":[\"forecast_item1\"],\"itemMargin\":0,\"styles\":{\"width\":\"matchParent\",\"height\":24.0,\"alignItems\":\"top\",\"flexShrink\":0}}]}}\n{\"version\":\"v0.9\",\"updateDataModel\":{\"surfaceId\":\"surface_card\",\"path\":\"/\",\"value\":{\"data\":{\"weather\":{\"location\":{\"prefectureName\":\"上海市\"},\"current\":{\"temperatureText\":\"29℃\",\"condition\":\"多云\"},\"daily\":[{\"weekday\":\"星期四\",\"condition\":\"多云\",\"temperatureRangeText\":\"25℃ / 32℃\"},{\"weekday\":\"星期四\",\"condition\":\"多云\",\"temperatureRangeText\":\"25℃ / 32℃\"}]}}}}}",
  "validationErrors": []
}
```
