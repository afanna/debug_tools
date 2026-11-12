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
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Stack","children":["__post_theme_background","__genui_render_component__root"],"styles":{"width":"matchParent","height":"matchParent","padding":0,"alignContent":"topStart","clip":true,"borderRadius":20,"backgroundColor":"#FF1F1F99"}},{"id":"__post_theme_background","component":"Stack","children":["fusionBallBackground","__post_theme_base"],"styles":{"width":"matchParent","height":"matchParent","alignContent":"topStart"}},{"id":"__post_theme_base","component":"Image","src":"https://lfcontentcenterdev.hwcloudtest.cn/pub_5/FaStore_fa_900_9/bb/v3/fa/osms/1/1/7016f2bb9242499a99b3439c2fb2ed26/fe04c25a2ecd41ea94617315efd39925.jpg","styles":{"width":"matchParent","height":"matchParent","objectFit":"fill"}},{"id":"fusionBallBackground","component":"Stack","children":["fusionBallLargeSlot","fusionBallMediumSlot","fusionBallSmallSlot","fusionBallGlassLayer"],"styles":{"width":"100%","height":"100%","borderRadius":20,"alignContent":"topStart","clip":true}},{"id":"fusionBallLargeSlot","component":"Stack","children":["fusionBallLarge"],"styles":{"width":"112.5%","height":"27.5%","alignContent":"center"}},{"id":"fusionBallLarge","component":"Divider","styles":{"width":"116.666667%","height":"477.272727%","strokeWidth":0,"color":"#00000000","borderRadius":105,"backgroundColor":"#FF1F1F99","clip":true}},{"id":"fusionBallMediumSlot","component":"Stack","children":["fusionBallMedium"],"styles":{"width":"50%","height":"137.5%","alignContent":"bottom"}},{"id":"fusionBallMedium","component":"Divider","styles":{"width":"200%","height":"72.727273%","strokeWidth":0,"color":"#00000000","borderRadius":80,"backgroundColor":"#FF2B65D9","clip":true}},{"id":"fusionBallSmallSlot","component":"Stack","children":["fusionBallSmall"],"styles":{"width":"121.875%","height":"118.75%","alignContent":"bottomEnd"}},{"id":"fusionBallSmall","component":"Divider","styles":{"width":"51.282051%","height":"52.631579%","strokeWidth":0,"color":"#00000000","borderRadius":50,"backgroundColor":"#FF57AED9","clip":true}},{"id":"fusionBallGlassLayer","component":"Divider","styles":{"width":"100%","height":"100%","strokeWidth":0,"color":"#00000000","backgroundColor":"#0DFFFFFF","backdropBlur":{"radius":210}}},{"id":"__genui_render_component__root","component":"Column","children":["title","body"],"itemMargin":6,"styles":{"width":"matchParent","height":"matchParent","padding":12,"borderRadius":20,"clip":true,"alignItems":"start","justifyContent":"start"}},{"id":"title","component":"Row","children":["title_title"],"styles":{"width":"matchParent","height":12,"flexShrink":0,"justifyContent":"start","alignItems":"center"},"itemMargin":0},{"id":"title_title","component":"Text","content":"Design Compact Mock","styles":{"fontSize":12,"fontWeight":400,"lineHeight":1,"textAlign":"start","maxLines":1,"flexShrink":0,"width":"matchParent","fontColor":"#CCFFFFFF"}},{"id":"body","component":"Column","children":["content"],"styles":{"width":"matchParent","layoutWeight":1},"itemMargin":0},{"id":"content","component":"Column","children":["content_main"],"itemMargin":2,"styles":{"alignItems":"start","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent"}},{"id":"content_main","component":"Text","content":"Mock ready","styles":{"height":18,"fontSize":18,"fontWeight":700,"lineHeight":1,"maxLines":1,"flexShrink":1,"width":"matchParent","fontColor":"#FFFFFFFF","textOverflow":"clip"}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"ui":{"state":"ready"}}}}
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
  "assetCandidates": [
    {
      "id": "photo-ux-texture-purple-diamond-square",
      "src": "https://lfcontentcenterdev.hwcloudtest.cn/pub_5/FaStore_fa_900_9/bb/v3/fa/osms/1/1/7016f2bb9242499a99b3439c2fb2ed26/fe04c25a2ecd41ea94617315efd39925.jpg",
      "description": "主题背景"
    }
  ]
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
  "asset": [
    "photo-ux-texture-purple-diamond-square"
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
  "artifactId": "b12830b3-1a60-4f82-9ae0-bbe9d26d738f",
  "createdAt": 1793932871500
}
```
```designcompactdsl
["root","Column",{"width":"matchParent","height":"matchParent","padding":12,"borderRadius":20,"clip":true,"itemMargin":6,"alignItems":"start","justifyContent":"start"},["title","body"]]
["title","SingleLineTitle",{"title":"Design Compact Mock"}]
["body","Column",{"width":"matchParent","layoutWeight":1},["content"]]
["content","EmphasisText",{"mainText":"Mock ready"}]
["/ui/state","ready"]
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
