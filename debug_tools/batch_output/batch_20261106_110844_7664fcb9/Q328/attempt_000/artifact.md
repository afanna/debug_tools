```cardspec
{
  "title": "日历黄历",
  "description": "农历日期速览",
  "suggestSize": "2x2",
  "imageDomainWhitelist": [
    "hag-ability-test.obs.cn-north-1.myhuaweicloud.com",
    "lfcontentcenterdev.hwcloudtest.cn",
    "hagres-drcn.dbankcdn.com"
  ],
  "dataBindings": [
    {
      "capabilityId": "GetCalendarEvents",
      "arguments": {},
      "writeResultTo": "/data/calendar"
    },
    {
      "capabilityId": "GetCurrentTime",
      "arguments": {},
      "writeResultTo": "/data/time"
    }
  ]
}
```
```genui
{"version":"v0.9","createSurface":{"surfaceId":"surface_card","catalogId":"ohos.a2ui.extended.catalog.form"}}
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Column","children":["content"],"styles":{"width":"matchParent","height":"matchParent","borderRadius":20,"clip":true,"alignItems":"center","justifyContent":"center","padding":12,"linearGradient":{"direction":"RightBottom","colors":[["#FFFFE0CC",0],["#FFFFF7F2",1]]}},"itemMargin":0},{"id":"content","component":"Column","children":["content_icon","content_value_area","content_supporting"],"itemMargin":8,"styles":{"width":"matchParent","height":122,"alignItems":"center","justifyContent":"center","flexShrink":1}},{"id":"content_icon","component":"Image","src":"resources/base/media/calendar_fill.svg","styles":{"width":18,"height":18,"objectFit":"contain","flexShrink":0,"fillColor":"#FF8C4B1C"}},{"id":"content_value_area","component":"Column","children":["content_value"],"styles":{"width":"matchParent","height":60,"alignItems":"center","justifyContent":"center","flexShrink":0},"itemMargin":0},{"id":"content_value","component":"Text","content":"{{ ${/data/time/lunarDate} }}","styles":{"fontSize":21,"fontWeight":700,"textAlign":"center","maxLines":2,"width":"matchParent","lineHeight":1.25,"fontColor":"#FF8C4B1C","textOverflow":"clip"}},{"id":"content_supporting","component":"Text","content":"农历日期","styles":{"height":20,"fontSize":14,"fontWeight":400,"textAlign":"center","maxLines":1,"width":"matchParent","margin":{"top":8,"right":0,"bottom":0,"left":0},"flexShrink":0,"fontColor":"#998C4B1C","textOverflow":"clip"}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"time":{"lunarDate":"示例"}}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "在日历中添加黄历信息，显示农历日期。",
  "size": "2x2",
  "appVersion": "11.7.8.342",
  "eventCandidates": [],
  "dataModelSchema": {
    "data": {
      "calendar": {
        "events": [
          {
            "title": {
              "type": "string",
              "description": "日程标题，例如“咪咕视频《西班牙 VS 奥地利》”或“项目进展会”。",
              "sampleValue": "项目例会"
            },
            "dtStart": {
              "type": "string",
              "description": "格式化后的日程开始时间短文本，如 '03:00'，若为全天日程可能为特殊标记。",
              "sampleValue": "14:00"
            }
          }
        ]
      },
      "time": {
        "lunarDate": {
          "type": "string",
          "description": "格式化的中国传统农历日期，例如 '五月廿六'。若系统获取失败则可能为空字符串。",
          "sampleValue": "示例"
        }
      }
    }
  },
  "assetCandidates": [
    {
      "id": "asset.calendar_fill",
      "src": "resources/base/media/calendar_fill.svg",
      "description": "样式：日历实心图标，默认黑色，图形为带格线的日历本造型；适用：日程管理、日历事件查看、当日安排。"
    }
  ]
}
```
```effectivecapabilities
{
  "data": [
    "GetCalendarEvents",
    "GetCurrentTime"
  ],
  "event": [],
  "asset": [
    "asset.calendar_fill"
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
      "capabilityId": "GetCalendarEvents",
      "arguments": {},
      "writeResultTo": "/data/calendar",
      "candidateOutputFields": [
        "/events/0/title",
        "/events/0/dtStart"
      ]
    },
    {
      "capabilityId": "GetCurrentTime",
      "arguments": {},
      "writeResultTo": "/data/time",
      "candidateOutputFields": [
        "/lunarDate"
      ]
    }
  ],
  "candidateEventCandidates": [],
  "candidateAssetIds": [
    "asset.calendar_fill"
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
  "artifactId": "3200944e-7a7c-4989-b25e-c6dc3aa2b8ba",
  "createdAt": 1793934565664
}
```
```designcompactdsl
["root","Layout",{"layout":"S-center"},["content"]]
["content","DataDisplay",{"icon":"resources/base/media/calendar_fill.svg","value":{"path":"/data/time/lunarDate"},"supportingText":"农历日期"}]
["/data/time/lunarDate","示例"]
```
```request
{
  "content": {
    "bundleName": "com.huawei.genui",
    "userQuery": "在日历中添加黄历信息，显示农历日期。",
    "candidateDataBindings": [
      {
        "capabilityId": "GetCalendarEvents",
        "arguments": {},
        "writeResultTo": "/data/calendar",
        "candidateOutputFields": [
          "/events/0/title",
          "/events/0/dtStart"
        ]
      },
      {
        "capabilityId": "GetCurrentTime",
        "arguments": {},
        "writeResultTo": "/data/time",
        "candidateOutputFields": [
          "/lunarDate"
        ]
      }
    ],
    "title": "日历黄历",
    "size": "2x2",
    "candidateEventCandidates": [],
    "description": "农历日期速览",
    "candidateAssetIds": [
      "asset.calendar_fill"
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
    "time": "20261029224452654"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q328-000",
    "isNew": true,
    "sessionId": "batch-7664fcb9"
  },
  "userAuth": {
    "user": {}
  },
  "utterance": {
    "original": "在日历中添加黄历信息，显示农历日期。",
    "type": "text"
  },
  "version": "1.0",
  "functionName": "generateWidgetCardCompactDsl",
  "romVersion": "HLS-AL00 7.0.0.111",
  "bundleName": "com.huawei.genui",
  "userQuery": "在日历中添加黄历信息，显示农历日期。",
  "candidateDataBindings": [
    {
      "capabilityId": "GetCalendarEvents",
      "arguments": {},
      "writeResultTo": "/data/calendar",
      "candidateOutputFields": [
        "/events/0/title",
        "/events/0/dtStart"
      ]
    },
    {
      "capabilityId": "GetCurrentTime",
      "arguments": {},
      "writeResultTo": "/data/time",
      "candidateOutputFields": [
        "/lunarDate"
      ]
    }
  ],
  "title": "日历黄历",
  "size": "2x2",
  "candidateEventCandidates": [],
  "description": "农历日期速览",
  "candidateAssetIds": [
    "asset.calendar_fill"
  ]
}
```
